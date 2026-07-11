from PIL import Image
import struct


def _bytes_to_bits(data):
    bits = []

    for byte in data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)

    return bits


def _bits_to_bytes(bits):

    output = bytearray()

    for i in range(0, len(bits), 8):

        byte = 0

        for bit in bits[i:i+8]:
            byte = (byte << 1) | bit

        output.append(byte)

    return bytes(output)


def calculate_capacity(image_path):

    image = Image.open(image_path).convert("RGB")

    width, height = image.size

    total_bits = width * height * 3

    # Reserve 4 bytes for the length header
    return (total_bits // 8) - 4


def encode_image(input_image, output_image, secret_text):

    image = Image.open(input_image).convert("RGB")

    pixels = list(image.getdata())

    payload = secret_text.encode("utf-8")

    header = struct.pack(">I", len(payload))

    final_data = header + payload

    bits = _bytes_to_bits(final_data)

    if len(bits) > len(pixels) * 3:
        raise ValueError("Image does not have enough capacity.")

    bit_index = 0

    new_pixels = []

    for pixel in pixels:

        r, g, b = pixel

        rgb = [r, g, b]

        for i in range(3):

            if bit_index < len(bits):

                rgb[i] = (rgb[i] & 0xFE) | bits[bit_index]

                bit_index += 1

        new_pixels.append(tuple(rgb))

    image.putdata(new_pixels)

    image.save(output_image)


def decode_image(image_path):

    image = Image.open(image_path).convert("RGB")

    pixels = list(image.getdata())

    bits = []

    for pixel in pixels:

        bits.append(pixel[0] & 1)
        bits.append(pixel[1] & 1)
        bits.append(pixel[2] & 1)

    header = _bits_to_bytes(bits[:32])

    length = struct.unpack(">I", header)[0]

    payload_bits = bits[32:32 + (length * 8)]

    payload = _bits_to_bytes(payload_bits)

    return payload.decode("utf-8")
