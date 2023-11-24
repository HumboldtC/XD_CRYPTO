from secrets import token_bytes
from Crypto.Cipher.AES import block_size as bs
from s1c7 import ecb_en, ecb_de
from s2c10 import pkcs7_unpad


def parse(p):
    dic = dict()
    for now_p in p.split('&'):
        key, value = now_p.split('=')
        dic[key] = value
    return dic


def profile_for(email):
    email = email.replace('&', '').replace('=', '')
    return f'email={email}&uid=10&role=user'


def enc(p):
    p = profile_for(p).encode()
    return ecb_en(p, k)


def dec(c):
    p = ecb_de(c, k)
    return parse(pkcs7_unpad(p).decode())


if __name__ == '__main__':
    k = token_bytes(bs)
    admin_p = '0' * 10 + 'admin' + '\x0b' * 11
    admin_c = enc(admin_p)[bs: 2 * bs]
    p = 'F@outlook.com'
    print(dec(enc(p)))
    print(dec(enc(p)[: 2 * bs] + admin_c))
