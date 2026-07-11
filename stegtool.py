import click

from image.encoder import encode_secret
from image.decoder import decode_secret

from audio.wav import encode_audio, decode_audio

from text.zerowidth import encode_text, decode_text

from pdf.metadata import hide_metadata, read_metadata


@click.group()
def cli():
    """Steganography Multi Tool"""
    pass


# ---------------- IMAGE ----------------

@cli.group()
def image():
    """Image Steganography"""
    pass


@image.command()
@click.option("--input", "-i", required=True)
@click.option("--output", "-o", required=True)
@click.option("--message", "-m", required=True)
@click.option("--password", "-p", required=True)
def encode(input, output, message, password):
    encode_secret(input, output, message, password)


@image.command()
@click.option("--input", "-i", required=True)
@click.option("--password", "-p", required=True)
def decode(input, password):
    decode_secret(input, password)


# ---------------- AUDIO ----------------

@cli.group()
def audio():
    pass


@audio.command()
@click.option("--input", "-i", required=True)
@click.option("--output", "-o", required=True)
@click.option("--message", "-m", required=True)
def encode(input, output, message):
    encode_audio(input, output, message)


@audio.command()
@click.option("--input", "-i", required=True)
def decode(input):
    print(decode_audio(input))


# ---------------- TEXT ----------------

@cli.group()
def text():
    pass


@text.command()
@click.option("--visible", "-v", required=True)
@click.option("--secret", "-s", required=True)
def encode(visible, secret):
    print(encode_text(visible, secret))


@text.command()
@click.option("--text", "-t", required=True)
def decode(text):
    print(decode_text(text))


# ---------------- PDF ----------------

@cli.group()
def pdf():
    pass


@pdf.command()
@click.option("--input", "-i", required=True)
@click.option("--output", "-o", required=True)
@click.option("--message", "-m", required=True)
def encode(input, output, message):
    hide_metadata(input, output, message)


@pdf.command()
@click.option("--input", "-i", required=True)
def decode(input):
    print(read_metadata(input))


if __name__ == "__main__":
    cli()
