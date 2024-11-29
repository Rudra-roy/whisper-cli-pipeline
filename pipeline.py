#!/usr/bin/env python3
import pyaudio
import wave
import os
import queue
import threading
import time
from transformers import pipeline
import time
import click
import torch
from whisper import asr_cli


# Initialize queues
audio_queue = queue.Queue()
text_queue = queue.Queue()

# ASR CLI function (your custom function, assuming it returns transcription)

# NER function for location filtering
def filter_locations(text):
    ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english" ,grouped_entities=True)
    return [ent['word'] for ent in ner(text) if ent['entity_group'] == 'LOC']

# Recording function
def record_audio():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    seconds = 30
    p = pyaudio.PyAudio()

    while True:
        filename = f"audio_{int(time.time())}.wav"
        print(f"Recording {filename}")
        
        stream = p.open(format=sample_format, channels=channels,
                        rate=fs, frames_per_buffer=chunk, input=True)
        
        frames = []
        for _ in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        audio_queue.put(filename)  # Add file to the queue for processing

# Transcription function
def transcribe_audio():
    while True:
        if not audio_queue.empty():
            audio_file = audio_queue.get()
            print(f"Transcribing {audio_file}")
            
            transcribed_text = asr_cli(audio_file)
            text_filename = audio_file.replace(".wav", ".txt")
            
            with open(text_filename, "w") as text_file:
                text_file.write(transcribed_text)

            text_queue.put(text_filename)
            os.remove(audio_file)  # Delete the audio file after transcription

# NER filtering and saving locations
def filter_and_save_locations():
    location_file = "locations.txt"
    
    while True:
        if not text_queue.empty():
            text_file = text_queue.get()
            print(f"Filtering {text_file}")
            
            with open(text_file, "r") as f:
                text = f.read()
            
            locations = filter_locations(text)
            
            with open(location_file, "a") as loc_file:
                for location in locations:
                    loc_file.write(f"{location}\n")

            os.remove(text_file)  # Delete the text file after NER processing

# Threading to keep everything running concurrently
def run_pipeline():
    threading.Thread(target=record_audio).start()
    threading.Thread(target=transcribe_audio).start()
    threading.Thread(target=filter_and_save_locations).start()

if __name__ == "__main__":
    run_pipeline()
