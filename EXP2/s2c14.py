from base64 import b64decode
from Crypto.Cipher.AES import block_size as bs
from secrets import token_bytes
from random import randint
from s1c7 import ecb_en
from s2c12 import dec


def rand_ecb_en(p): return ecb_en(rand_pre + p + c, k)


def det_pre_len(en):
    p = b'\x00' * bs * 2
    for i in range(bs):
        p = b'\x01' + p
        c = en(p)
        a = []
        for j in range(0, len(c), bs):
            if c[j: j + bs] in a:
                return j - bs - i - 1
            a.append(c[j: j + bs])


def new_en(p):
    p = (bs - n % bs) * b'0' + p
    return rand_ecb_en(p)[n // bs * bs + bs:]


if __name__ == '__main__':
    k = token_bytes(bs)
    rand_pre = token_bytes(randint(5, 100))
    c = b''
    for line in open('s2c12.in').readlines():
        c += line.encode()[:-1]
    c = b64decode(c)
    n = det_pre_len(rand_ecb_en)
    p = dec(new_en, bs)
    print(p.decode())
