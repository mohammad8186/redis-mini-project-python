import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os



class AESCipher:
    def __init__(self, key_file='./secret/aes.key'):
        self.key_file = key_file
        if not os.path.exists(self.key_file):
            self.key = os.urandom(32) 
            self.save_key()
        else:
            self.load_key()

    def save_key(self):
        with open(self.key_file, 'wb') as key_file:
            key_file.write(self.key)

    def load_key(self):
        with open(self.key_file, 'rb') as key_file:
            self.key = key_file.read()

    def encrypt(self, message):
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(message.encode()) + padder.finalize()

        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_message = encryptor.update(padded_data) + encryptor.finalize()

        return base64.b64encode(iv + encrypted_message).decode('utf-8')
    
