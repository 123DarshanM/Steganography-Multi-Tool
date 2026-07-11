from text.zero_width import decode_text
from core.crypto import decrypt_message


def decode_secret(
    stego_text,
    password
):

    encrypted = decode_text(
        stego_text
    )

    return decrypt_message(
        encrypted,
        password
    )
