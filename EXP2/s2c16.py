from secrets import token_bytes
from Crypto.Cipher.AES import block_size as bs
from s2c9 import pkcs7_unpad
from s2c10 import cbc_en, cbc_de, xor


def enc(p):
    p = p.replace(';', '').replace('=', '')
    return cbc_en(pre + p.encode() + suf, k)


def dec(c):
    p = pkcs7_unpad(cbc_de(c, k))
    return False if p.find(b';admin=true;') == -1 else True


if __name__ == '__main__':
    pre = b'comment1=cooking%20MCs;userdata='
    suf = b';comment2=%20like%20a%20pound%20of%20bacon'
    k = token_bytes(bs)
    p = b';admin=true;    '
    c = enc('0' * bs)
    cc = xor(p, suf[:bs])
    print(dec(c))
    print(dec(c[:2 * bs] + xor(c[2 * bs: 3 * bs], cc) + c[3 * bs:]))
