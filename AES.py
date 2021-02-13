from Crypto.Cipher import AES as aes


def fix_key_length(k: bytes) -> bytes:
    if len(k) < 16:
        temp = bytearray(k)
        while len(temp) < 16:
            temp.append(0x00)
        return bytes(temp)

    elif len(k) == 16:
        return k
    elif len(k) < 24:
        return k[0:16]
    elif len(k) == 24:
        return k
    elif len(k) < 32:
        return k[0:24]
    elif len(k) == 32:
        return k
    else:
        return k[0:32]


class AES:
    cipher_block = None

    def __init__(self, master_key: bytes):
        message = fix_key_length(master_key)
        self.cipher_block = aes.new(bytearray(message), aes.MODE_CFB, bytes("This is an IV456", encoding='utf8'))

    def encrypt(self, cipher_bytes) -> bytes:
        return bytes(self.cipher_block.encrypt(cipher_bytes))

    def decrypt(self, cipher_bytes) -> bytes:
        return bytes(self.cipher_block.decrypt(cipher_bytes))
