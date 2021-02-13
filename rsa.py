import os
import ast

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from AES import AES


class Cipher:
    rand_bytes = None
    key_name = ""

    def __init__(self, key_name: str):
        self.key_name = key_name

    def encrypt(self, cipher_bytes: bytes) -> bytes:
        self.generate_key_pair(4096)
        self.gen_random_bytes()
        cipher = AES(self.rand_bytes)

        encryptedFile = cipher.encrypt(cipher_bytes)
        tail = self.encryption_tail()
        result = encryptedFile + tail

        return result

    def decrypt(self, cipher_bytes: bytes) -> bytes:
        tail = cipher_bytes[-512:]  # take last 256 char tail
        cipherBytes = cipher_bytes[:-512]  # the actual ciphertext

        key = self.decrypt_tail(tail)

        cipher = AES(key)

        result = cipher.decrypt(cipherBytes)

        return result

    def encryption_tail(self) -> bytes:
        public_key = open(self.key_name + "_pub.pem", "rb")
        pub = RSA.importKey(public_key.read())
        public_key.close()

        encryptor = PKCS1_OAEP.new(pub)
        encrypted = encryptor.encrypt(self.rand_bytes)

        return encrypted

    def decrypt_tail(self, byte_array: bytes) -> bytes:
        private_key = open(self.key_name + ".pem", "rb")
        priv = RSA.importKey(private_key.read())
        private_key.close()
        decryptor = PKCS1_OAEP.new(priv)
        len(byte_array)
        decrypted = decryptor.decrypt(byte_array)

        return decrypted

    def generate_key_pair(self, bit_size: int) -> None:
        key = RSA.generate(bit_size)
        pub = key.publickey()

        f = open(self.key_name + "_pub.pem", "wb")
        f.write(pub.export_key())
        f.close()
        print("GENERATED PUBLIC KEY: ", self.key_name + "_pub.pem")
        f = open(self.key_name + ".pem", "wb")
        f.write(key.export_key())
        f.close()
        print("GENERATED PRIVATE KEY: ", self.key_name + ".pem")

    def gen_random_bytes(self) -> bytes:
        self.rand_bytes = os.urandom(256)
