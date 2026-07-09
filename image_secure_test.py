from image.encoder import encode_secret
from image.decoder import decode_secret

encrypt_password = "cyber123"
decrypt_password = "wrongpassword"

message = "This is my hidden secret."

encode_secret(
    "examples/input.png",
    "examples/secret.png",
    message,
    encrypt_password
)

decode_secret(
    "examples/secret.png",
    decrypt_password
)
