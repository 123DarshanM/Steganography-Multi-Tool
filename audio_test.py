from audio.wav import encode_audio, decode_audio

message = "Hello Darshan! Audio Steganography Works."

encode_audio(
    "examples/input.wav",
    "examples/output.wav",
    message
)

secret = decode_audio("examples/output.wav")

print("\nRecovered Message:")
print(secret)

