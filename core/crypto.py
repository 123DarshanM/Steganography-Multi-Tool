import os
import base64

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def derive_key(password: str, salt: bytes):
    """
    Derive a 256-bit AES key from a password using PBKDF2.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return kdf.derive(password.encode())


def encrypt_message(message: str, password: str):
    """
    Encrypt a string using AES-GCM.

    Returns:
        Base64 encoded string containing:
        salt + nonce + ciphertext
    """

    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)

    aes = AESGCM(key)

    ciphertext = aes.encrypt(
        nonce,
        message.encode(),
        None
    )

    data = salt + nonce + ciphertext

    return base64.b64encode(data).decode()


def decrypt_message(token: str, password: str):
    """
    Decrypt a Base64 encoded AES-GCM message.
    """

    data = base64.b64decode(token)

    salt = data[:16]
    nonce = data[16:28]
    ciphertext = data[28:]

    key = derive_key(password, salt)

    aes = AESGCM(key)

    plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode()
