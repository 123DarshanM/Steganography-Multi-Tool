from core.crypto import encrypt_message
from image.lsb import encode_image


def encode_secret(input_image, output_image, message, password):
    encrypted = encrypt_message(message, password)

    encode_image(
        input_image,
        output_image,
        encrypted
    )

    print("✓ Secret encrypted and embedded successfully.")
