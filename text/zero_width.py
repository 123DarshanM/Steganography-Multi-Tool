ZERO = "\u200B"      # Zero Width Space
ONE = "\u200C"       # Zero Width Non Joiner
END = "\u200D"       # Zero Width Joiner


def _text_to_bits(text):

    bits = ""

    for c in text.encode():

        bits += format(c, "08b")

    return bits


def _bits_to_text(bits):

    output = bytearray()

    for i in range(0, len(bits), 8):

        byte = bits[i:i+8]

        if len(byte) == 8:

            output.append(int(byte, 2))

    return output.decode()


def encode_text(cover_text, secret):

    bits = _text_to_bits(secret)

    hidden = ""

    for bit in bits:

        if bit == "0":

            hidden += ZERO

        else:

            hidden += ONE

    hidden += END

    return cover_text + hidden


def decode_text(stego):

    hidden = ""

    recording = False

    for c in stego:

        if c == ZERO:

            hidden += "0"

            recording = True

        elif c == ONE:

            hidden += "1"

            recording = True

        elif c == END:

            break

        elif recording:

            break

    return _bits_to_text(hidden)
