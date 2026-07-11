ZERO = "\u200b"   # Zero Width Space
ONE = "\u200c"    # Zero Width Non-Joiner
END = "\u200d"    # Zero Width Joiner


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def encode_text(visible_text, secret):

    binary = text_to_binary(secret)

    hidden = ""

    for bit in binary:
        if bit == "0":
            hidden += ZERO
        else:
            hidden += ONE

    hidden += END

    return visible_text + hidden


def decode_text(encoded):

    binary = ""

    for ch in encoded:

        if ch == ZERO:
            binary += "0"

        elif ch == ONE:
            binary += "1"

        elif ch == END:
            break

    return binary_to_text(binary)
