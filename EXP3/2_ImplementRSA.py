import random
import sympy


class RSAEncryptor:
    def __init__(self, bit_length=1024):
        self.bit_length = bit_length
        self.public_key, self.private_key = self._generate_keypair()

    def _generate_prime(self):
        """生成指定位数的素数"""
        while True:
            num = random.getrandbits(self.bit_length)
            if sympy.isprime(num):
                return num

    def _gcd(self, a, b):
        """计算最大公约数"""
        while b:
            a, b = b, a % b
        return a

    def _mod_inverse(self, a, m):
        """求模逆"""
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def _generate_keypair(self):
        """生成RSA密钥对"""
        p = self._generate_prime()
        q = self._generate_prime()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(1, phi)
        while self._gcd(e, phi) != 1:
            e = random.randint(1, phi)
        d = self._mod_inverse(e, phi)
        return ((n, e), (n, d))

    def _string_to_int(self, s):
        """将字符串转换为整数"""
        return int.from_bytes(s.encode(), 'big')

    def _int_to_string(self, i):
        """将整数转换回字符串"""
        return i.to_bytes((i.bit_length() + 7) // 8, 'big').decode()

    def encrypt(self, plaintext):
        """加密函数，将字符串转换为一个整数，然后加密这个整数"""
        n, e = self.public_key
        plaintext_int = self._string_to_int(plaintext)
        encrypted_int = pow(plaintext_int, e, n)
        return encrypted_int

    def decrypt(self, encrypted_int):
        """解密函数，先解密整数，然后将其转换回字符串"""
        n, d = self.private_key
        decrypted_int = pow(encrypted_int, d, n)
        return self._int_to_string(decrypted_int)


# 主程序
if __name__ == '__main__':
    bits = 1024  # 指定位长度
    rsa = RSAEncryptor(bits)  # 使用指定的位长度初始化RSA加密器
    message = "CryptoExp3_2"
    encrypted_msg = rsa.encrypt(message)
    decrypted_msg = rsa.decrypt(encrypted_msg)
    print(f"原始消息: {message}")
    print(f"加密消息: {encrypted_msg}")
    print(f"解密消息: {decrypted_msg}")
