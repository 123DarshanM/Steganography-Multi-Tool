from image.lsb import decode_image
from core.crypto import decrypt_message


def decode_secret(image_path, password):

    encrypted = decode_image(image_path)

    if not encrypted:
        print("No hidden message found.")
        return

    try:
        message = decrypt_message(
            encrypted,
            password
        )

        print("\nRecovered Secret:")
        print(message)

    except Exception:
        print("Wrong password or corrupted data.")
