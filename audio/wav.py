import wave

END_MARKER = "#####END#####"


def text_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)


def binary_to_text(binary):
    chars = []

    for i in range(0, len(binary), 8):
        byte = binary[i:i + 8]

        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))

    return ''.join(chars)


def encode_audio(input_file, output_file, secret):

    secret += END_MARKER

    binary = text_to_binary(secret)

    audio = wave.open(input_file, 'rb')

    params = audio.getparams()

    frames = bytearray(audio.readframes(audio.getnframes()))

    audio.close()

    if len(binary) > len(frames):
        raise ValueError("Message too large for this audio file.")

    for i in range(len(binary)):
        frames[i] = (frames[i] & 254) | int(binary[i])

    output = wave.open(output_file, 'wb')

    output.setparams(params)

    output.writeframes(frames)

    output.close()

    print("Audio saved:", output_file)


def decode_audio(audio_file):

    audio = wave.open(audio_file, 'rb')

    frames = bytearray(audio.readframes(audio.getnframes()))

    audio.close()

    binary = ""

    for byte in frames:
        binary += str(byte & 1)

    text = binary_to_text(binary)

    end = text.find(END_MARKER)

    if end == -1:
        return ""

    return text[:end]
