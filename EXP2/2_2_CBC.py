from Crypto.Cipher.AES import block_size as bs
from Crypto.Cipher import AES
from base64 import b64decode


# 使用ECB模式解密
def decrypt_ecb(ciphertext, key):
    ciphertext = pkcs7_pad(ciphertext, AES.block_size)
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(ciphertext)


# 使用ECB模式加密
def encrypt_ecb(plaintext, key):
    plaintext = pkcs7_pad(plaintext, AES.block_size)
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(plaintext)


# PKCS#7填充
def pkcs7_pad(data, block_length):
    padding_length = block_length - (len(data) - 1) % block_length - 1
    return data + bytes([padding_length] * padding_length)


# PKCS#7去除填充
def pkcs7_unpad(data):
    padding_length = data[-1]
    if padding_length > bs or padding_length == 0 or data[-padding_length:] != bytes(
            [padding_length] * padding_length):
        raise ValueError("无效的PKCS#7填充")
    return data[:-padding_length]


# 异或操作
def xor_bytes(byte_array1, byte_array2):
    return bytes([byte1 ^ byte2 for byte1, byte2 in zip(byte_array1, byte_array2)])


# 使用CBC模式解密
def decrypt_cbc(ciphertext, key, iv=b'\x00' * bs):
    ciphertext = pkcs7_pad(ciphertext, bs)
    plaintext = b''
    previous_block = iv
    for i in range(0, len(ciphertext), bs):
        current_block = ciphertext[i: i + bs]
        decrypted_block = xor_bytes(decrypt_ecb(current_block, key), previous_block)
        plaintext += decrypted_block
        previous_block = current_block
    return plaintext


# 使用CBC模式加密
def encrypt_cbc(plaintext, key, iv=b'\x00' * bs):
    plaintext = pkcs7_pad(plaintext, bs)
    ciphertext = b''
    previous_block = iv
    for i in range(0, len(plaintext), bs):
        current_block = plaintext[i: i + bs]
        encrypted_block = encrypt_ecb(xor_bytes(current_block, previous_block), key)
        previous_block = encrypted_block
        ciphertext += encrypted_block
    return ciphertext


if __name__ == '__main__':
    encrypted_data = b''
    key = b'YELLOW SUBMARINE'
    with open('2_2_CBC.in', 'r') as file:
        for line in file.readlines():
            encrypted_data += line.encode()[:-1]
    encrypted_data += b'=' * (len(encrypted_data) % 4)
    encrypted_data = b64decode(encrypted_data)
    print(pkcs7_unpad(decrypt_cbc(encrypted_data, key)).decode())
