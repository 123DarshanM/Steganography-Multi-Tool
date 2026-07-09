from PIL import Image


END_MARKER = "#####END#####"


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]

        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def encode_image(input_image, output_image, secret_text):

    image = Image.open(input_image)

    image = image.convert("RGB")

    pixels = list(image.getdata())

    secret_text += END_MARKER

    binary = text_to_binary(secret_text)

    if len(binary) > len(pixels) * 3:
        raise ValueError("Message is too large for this image.")

    new_pixels = []

    bit_index = 0

    for pixel in pixels:

        r, g, b = pixel

        if bit_index < len(binary):
            r = (r & ~1) | int(binary[bit_index])
            bit_index += 1

        if bit_index < len(binary):
            g = (g & ~1) | int(binary[bit_index])
            bit_index += 1

        if bit_index < len(binary):
            b = (b & ~1) | int(binary[bit_index])
            bit_index += 1

        new_pixels.append((r, g, b))

    image.putdata(new_pixels)

    image.save(output_image)

    print("Image saved:", output_image)


def decode_image(image_path):

    image = Image.open(image_path)

    image = image.convert("RGB")

    pixels = list(image.getdata())

    binary = ""

    for pixel in pixels:

        binary += str(pixel[0] & 1)
        binary += str(pixel[1] & 1)
        binary += str(pixel[2] & 1)

    text = binary_to_text(binary)

    end = text.find(END_MARKER)

    if end == -1:
        return ""

    return text[:end]
