#!/usr/bin/env python3
from whisper import asr_cli
# import click
import os
import time
from transformers import pipeline
import torch

# Perform ASR on the audio file
res = asr_cli('output.wav')

# Write the result to a text file
with open("asr_output.txt", "w") as file:
    file.write(res)

print("ASR result has been written to asr_output.txt")

