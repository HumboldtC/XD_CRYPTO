from secrets import token_bytes
from Crypto.Cipher.AES import block_size as bs
from random import randint
from s2c10 import cbc_en
from s1c7 import ecb_en


def rand_en(p):
    p = token_bytes(randint(5, 10)) + p + token_bytes(randint(5, 10))
    k = token_bytes(bs)
    iv = token_bytes(bs)
    if (randint(0, 1)):
        return "ECB", ecb_en(p, k)
    else:
        return "CBC", cbc_en(p, k, iv)


def det_cip(c):
    a = []
    for i in range(0, len(c), bs):
        if c[i: i + bs] in a:
            return "ECB"
        a.append(c[i: i + bs])
    return "CBC"


if __name__ == '__main__':
    p = bytes([0]*43)
    for i in range(1000):
        cry, c = rand_en(p)
        assert cry == det_cip(c)
    print("Successful")
