from image.lsb import (
    encode_image,
    calculate_capacity
)

from core.crypto import encrypt_message


def encode_secret(
    input_image,
    output_image,
    message,
    password
):
    """
    Encrypts the message and embeds it into the image.
    """

    # Encrypt message using AES
    encrypted_message = encrypt_message(
        message,
        password
    )

    # Calculate image capacity
    max_capacity = calculate_capacity(
        input_image
    )

    required = len(
        encrypted_message.encode("utf-8")
    )

    if required > max_capacity:

        raise ValueError(

            f"""
Message Too Large

Image Capacity : {max_capacity} Bytes
Required       : {required} Bytes

Choose a larger image.
"""

        )

    # Hide encrypted message
    encode_image(
        input_image,
        output_image,
        encrypted_message
    )

    return output_image
