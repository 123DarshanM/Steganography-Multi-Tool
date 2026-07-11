from audio.lsb_audio import (
    encode_audio,
    calculate_capacity
)

from core.crypto import encrypt_message


def encode_secret(
    input_audio,
    output_audio,
    message,
    password
):
    """
    Encrypt and hide a secret message inside a WAV file.
    """

    encrypted = encrypt_message(
        message,
        password
    )

    capacity = calculate_capacity(
        input_audio
    )

    required = len(
        encrypted.encode("utf-8")
    )

    if required > capacity:

        raise ValueError(

f"""
Audio file is too small.

Capacity : {capacity} Bytes

Required : {required} Bytes

Choose a larger WAV file.
"""

        )

    encode_audio(
        input_audio,
        output_audio,
        encrypted
    )

    return output_audio
