from image.lsb import decode_image
from core.crypto import decrypt_message


def decode_secret(image_path, password):
    """
    Extracts and decrypts the hidden message from an image.

    Args:
        image_path (str): Path to the encoded image.
        password (str): Password used during encryption.

    Returns:
        str: Original hidden message.

    Raises:
        ValueError: If decoding or decryption fails.
    """

    try:
        # Extract encrypted payload from image
        encrypted_message = decode_image(image_path)

        if not encrypted_message:
            raise ValueError("No hidden message found.")

        # Decrypt payload
        secret = decrypt_message(
            encrypted_message,
            password
        )

        return secret

    except Exception:
        raise ValueError(
            "Invalid password or corrupted image."
        )
