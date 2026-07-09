from core.crypto import encrypt_message, decrypt_message

message = "Hello Darshan! This is a secret."

password = "mypassword123"

print("Original:")
print(message)

encrypted = encrypt_message(message, password)

print("\nEncrypted:")
print(encrypted)

decrypted = decrypt_message(encrypted, "mypassword123")

print("\nDecrypted:")
print(decrypted)
