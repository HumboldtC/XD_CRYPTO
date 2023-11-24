from Crypto.Cipher.AES import block_size as bs

def pkcs7_pad(p, length):
    # 计算需要添加的填充字节长度
    pad_len = length - len(p) % length
    # 返回原数据加上填充字节
    return p + bytes([pad_len] * pad_len)

def pkcs7_unpad(p):
    # 获取填充的长度，即数据的最后一个字节的值
    pad_len = p[-1]
    # 检查填充是否有效
    if pad_len > bs or pad_len == 0 or p[-pad_len:] != bytes([pad_len] * pad_len):
        raise ValueError("Invalid PKCS#7 padding")
    # 返回去除填充后的数据
    return p[:-pad_len]


if __name__ == '__main__':
    p = b'YELLOW SUBMARINE'
    padded = pkcs7_pad(p, 20)
    print("Padded:", padded)
    unpadded = pkcs7_unpad(padded)
    print("Unpadded:", unpadded)