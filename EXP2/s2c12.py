from s1c7 import ecb_en
from secrets import token_bytes
from Crypto.Cipher.AES import block_size as bs
from base64 import b64decode
from s2c11 import det_cip
from s2c9 import pkcs7_unpad


def rand_ecb_en(p): return ecb_en(p + c, k)


def det_block_size(en):
    p = b'A'
    while len(en(p)) == len(en(b'A')):
        p += b'A'
    cnt = 0
    n = len(en(p))
    while len(en(p)) == n:
        cnt += 1
        p += b'A'
    return cnt


def dec(en, sz):
    p = b''
    for i in range(20):
        for j in range(sz):
            tmp_p = b'A' * (sz - j - 1)
            tmp_pp = tmp_p + p
            c = en(tmp_p)[:(i + 1) * sz]
            for k in range(256):
                if en(tmp_pp + bytes([k]))[:(i + 1) * sz] == c:
                    p += bytes([k])
    return pkcs7_unpad(p)


if __name__ == '__main__':
    c = b''
    k = token_bytes(bs)
    for line in open('s2c12.in').readlines():
        c += line.encode()[:-1]
    c = b64decode(c)
    sz = det_block_size(rand_ecb_en)
    cip = det_cip(rand_ecb_en(bytes([0] * sz * 2)))
    assert cip == 'ECB'
    p = dec(rand_ecb_en, sz)
    print(p.decode())
