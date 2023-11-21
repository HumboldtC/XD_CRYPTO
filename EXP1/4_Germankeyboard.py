import hashlib
import itertools
import datetime

starttime = datetime.datetime.now()
hash1 = "67ae1a64661ac8b4494666f58c4822408dd0a3e4"
str1 = "QqWw%58(=0Ii*+nN"
str2 = [['Q', 'q'], ['W', 'w'], ['%', '5'], ['8', '('], ['=', '0'], ['I', 'i'], ['*', '+'], ['n', 'N']]


# SHA加密函数
def sha_encrypt(s):
    sha = hashlib.sha1(s.encode())  # 将字符串转换为字节串
    encrypts = sha.hexdigest()
    return encrypts


str3 = ["0"] * 8

# 生成并测试所有可能的组合
for combination in itertools.product(*str2):  # 使用itertools.product生成笛卡尔积
    test_str = "".join(combination)
    for perm in itertools.permutations(test_str):  # 对生成的组合进行排列
        str4 = sha_encrypt("".join(perm))
        if str4 == hash1:
            print("Found:", "".join(perm))
            endtime = datetime.datetime.now()
            print("Time taken:", (endtime - starttime).total_seconds())
            exit(0)  # 退出程序

