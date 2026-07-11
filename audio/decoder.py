from audio.lsb_audio import decode_audio
from core.crypto import decrypt_message


def decode_secret(
    audio_file,
    password
):
    """
    Extract and decrypt the hidden message.
    """

    try:

        encrypted = decode_audio(
            audio_file
        )

        if encrypted == "":

            raise ValueError(
                "No hidden message found."
            )

        return decrypt_message(
            encrypted,
            password
        )

    except Exception:

        raise ValueError(
            "Invalid password or corrupted audio."
        )
