#!/usr/bin/env python3

import click
import os
import time
from transformers import pipeline
import torch

def asr_cli(audio_file, model="openai/whisper-small.en", device='cpu', dtype='float32', batch_size=8, better_transformer=False, chunk_length=30):
    # Initialize the ASR pipeline
    pipe = pipeline("automatic-speech-recognition",
                    model=model,
                    device=device,
                    torch_dtype=torch.float16 if dtype == "float16" else torch.float32)

    if better_transformer:
        pipe.model = pipe.model.to_bettertransformer()

    # Perform ASR
    click.echo("Model loaded.")
    start_time = time.perf_counter()
    outputs = pipe(audio_file, chunk_length_s=chunk_length, batch_size=batch_size, return_timestamps=True)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    click.echo(f"ASR took {elapsed_time:.2f} seconds.")

    # Output transcription text
    transcriptions = []
    for chunk in outputs['chunks']:
        transcriptions.append(chunk['text'].strip())

    # Print or return the transcription text
    transcription_text = "\n".join(transcriptions)
    click.echo("Transcription complete.")
    click.echo("\nTranscription Text:\n")
    click.echo(transcription_text)

    return transcription_text

if __name__ == '__main__':
     asr_cli("test.mp3")
