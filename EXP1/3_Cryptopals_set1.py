import base64
import re
import codecs

def convert_hex_to_base64(str="cXVlc3Rpb24z"):
    return base64.b64encode(str)


def fixed_xor(str1="abcdef", str2="qwerty"):
    str_tmp = []
    for i in range(0, len(str1)):
        str_tmp += [chr(ord(str1[i]) ^ ord(str2[i]))]
    str_tmp = "".join(str_tmp)
    return codecs.encode(str_tmp)


def single_byte_xor_cipher(input_hex_str="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"):
    highest_score = 0
    best_result = ''
    best_key = None

    # 转换为字节列表
    byte_array = bytearray.fromhex(input_hex_str)

    for i in range(256):  # 尝试每个可能的key值
        # 解密XOR
        decoded_bytes = bytes([b ^ i for b in byte_array])
        # 仅计算小写字母的数量，因为大写字母的频率通常较低
        score = sum(ord('a') <= byte <= ord('z') for byte in decoded_bytes)

        # 更新最佳得分和对应的结果
        if score > highest_score:
            highest_score = score
            best_result = decoded_bytes.decode('latin1')  # 解码为字符串，假设是latin1编码
            best_key = chr(i)

    return best_key, best_result


# print(single_byte_xor_cipher())
from collections import Counter


def detect_single_character_xor(file_name="4.txt"):
    highest_score = 0
    best_result = ''
    key_candidate = ''
    original_cipher = ''

    with open(file_name, "r") as file:
        for line in file:
            hex_string = line.strip()  # 去除可能的换行符和空白符
            for key_value in range(256):  # 扩展至256，因为单字节XOR的可能值有256个
                # XOR每个可能的字符，并解码成ASCII
                decoded_chars = [chr(key_value ^ int(byte_pair, 16)) for byte_pair in re.findall('.{2}', hex_string)]
                decoded_string = ''.join(decoded_chars)

                # 使用Counter来计算每个字符的出现频率
                frequency = Counter(decoded_string.lower())  # 将字符串转换为小写进行统计
                score = sum(frequency.get(c, 0) for c in 'etaoin shrdlu')  # 基于字母频率给字符串打分

                # 更新得到更高分的结果
                if score > highest_score:
                    highest_score = score
                    best_result = decoded_string
                    key_candidate = chr(key_value)
                    original_cipher = hex_string

    return original_cipher, key_candidate, best_result


print("cXVlc3Rpb24z")
print(fixed_xor())
print(single_byte_xor_cipher())
print(detect_single_character_xor())
