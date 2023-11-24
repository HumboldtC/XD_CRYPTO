from s2c9 import pkcs7_unpad

if __name__ == '__main__':
    c1 = b'ICE ICE BABY\x04\x04\x04\x04'
    c2 = b'ICE ICE BABY\x05\x05\x05\x05'
    c3 = b'ICE ICE BABY\x01\x02\x03\x04'
    p1 = pkcs7_unpad(c1)
    print(p1.decode())
try:
    p2 = pkcs7_unpad(c2)
except ValueError as e:
    print(e)
try:
    p3 = pkcs7_unpad(c3)
except ValueError as e:
    print(e)
