from pdf.metadata import write_metadata
from core.crypto import encrypt_message


def encode_secret(
    input_pdf,
    output_pdf,
    message,
    password
):
    """
    Encrypt and hide a secret message
    inside PDF metadata.
    """

    encrypted = encrypt_message(
        message,
        password
    )

    write_metadata(
        input_pdf,
        output_pdf,
        encrypted
    )

    return output_pdf
