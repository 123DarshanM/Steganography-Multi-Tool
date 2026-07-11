import os
import wave
from PIL import Image


def image_capacity(image_path):
    image = Image.open(image_path)

    width, height = image.size

    bits = width * height * 3

    bytes_available = bits // 8

    return bytes_available


def audio_capacity(audio_path):
    audio = wave.open(audio_path, 'rb')

    frames = audio.getnframes()

    channels = audio.getnchannels()

    capacity = (frames * channels) // 8

    audio.close()

    return capacity


def pdf_capacity(pdf_path):
    return os.path.getsize(pdf_path) // 20


def human(size):

    if size < 1024:
        return f"{size} Bytes"

    elif size < 1024 * 1024:
        return f"{size/1024:.2f} KB"

    return f"{size/(1024*1024):.2f} MB"
