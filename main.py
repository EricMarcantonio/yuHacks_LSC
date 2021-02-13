import os
from rsa import Cipher
from file_utils import read_file, write_file, merk, unmerk


class CustomCrypto:
    # isDir: bool
    isFile: bool
    key_name: str
    location: str

    def __init__(self, location: str, key_name: str):
        # self.isDir = os.path.isdir(location)
        self.isFile = os.path.isfile(location)
        self.key_name = key_name
        self.location = location

    def encrypt(self):
        if self.isFile:
            print("It's a file!")
            f = read_file(self.location)
            cipher = Cipher(self.key_name)
            f_enc = cipher.encrypt(f)
            write_file(merk(self.location), f_enc)

    def decrypt(self):
        if self.isFile:
            print("It's a file!")
            f = read_file(self.location)
            cipher = Cipher(self.key_name)
            f_dec = cipher.decrypt(f)
            write_file(unmerk(self.location), f_dec)


if __name__ == "__main__":
    test = CustomCrypto("./test_files/a-pair-of-hands-typing-away.jpg", "mykeyname")
    test.encrypt()

    lol = CustomCrypto("./test_files/a-pair-of-hands-typing-away.jpg.merk", "mykeyname")
    lol.decrypt()
