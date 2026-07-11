import wave
import struct


def calculate_capacity(audio_file):

    audio = wave.open(audio_file, "rb")

    frames = audio.getnframes()
    channels = audio.getnchannels()

    audio.close()

    return (frames * channels) // 8 - 4


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


def encode_audio(input_audio, output_audio, message):

    audio = wave.open(input_audio, "rb")

    params = audio.getparams()

    frames = bytearray(audio.readframes(audio.getnframes()))

    audio.close()

    payload = message.encode("utf-8")

    header = struct.pack(">I", len(payload))

    data = header + payload

    bits = _bytes_to_bits(data)

    if len(bits) > len(frames):

        raise ValueError("Audio file too small.")

    for i in range(len(bits)):

        frames[i] = (frames[i] & 254) | bits[i]

    output = wave.open(output_audio, "wb")

    output.setparams(params)

    output.writeframes(bytes(frames))

    output.close()


def decode_audio(audio_file):

    audio = wave.open(audio_file, "rb")

    frames = bytearray(audio.readframes(audio.getnframes()))

    audio.close()

    bits = []

    for byte in frames:

        bits.append(byte & 1)

    header = _bits_to_bytes(bits[:32])

    length = struct.unpack(">I", header)[0]

    payload = bits[32:32 + length * 8]

    data = _bits_to_bytes(payload)

    return data.decode("utf-8")
