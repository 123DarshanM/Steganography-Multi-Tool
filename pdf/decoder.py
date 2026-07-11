from pdf.metadata import read_metadata
from core.crypto import decrypt_message


def decode_secret(
    pdf_file,
    password
):
    """
    Extract and decrypt
    hidden PDF message.
    """

    encrypted = read_metadata(
        pdf_file
    )

    if encrypted == "":
        raise ValueError(
            "No hidden message found."
        )

    try:

        return decrypt_message(
            encrypted,
            password
        )

    except Exception:

        raise ValueError(
            "Invalid password or corrupted PDF."
        )
