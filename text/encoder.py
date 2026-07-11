from core.crypto import encrypt_message
from text.zero_width import encode_text


def encode_secret(
    cover_text,
    message,
    password
):

    encrypted = encrypt_message(
        message,
        password
    )

    return encode_text(
        cover_text,
        encrypted
    )
