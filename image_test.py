from image.lsb import encode_image, decode_image

message = "Hello Darshan! Welcome to Steganography."

encode_image(
    "examples/input.png",
    "examples/output.png",
    message
)

decoded = decode_image("examples/output.png")

print("\nRecovered Message:")
print(decoded)
