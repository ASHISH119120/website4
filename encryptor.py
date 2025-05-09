# encryptor.py
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    output_file = filename.replace(".enc", ".dec")
    with open(output_file, "wb") as file:
        file.write(decrypted)
