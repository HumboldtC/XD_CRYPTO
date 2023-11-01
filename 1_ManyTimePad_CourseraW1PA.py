ciphertext = []
for i in range(0, 11): ciphertext += ['0']

ciphertext_target = '32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54' \
                    'fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'
ciphertext[
    1] = '315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468' \
         'aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b8' \
         '3b220809560987815f65286764703de0f3d524400a19b159610b11ef3e'
ciphertext[
    2] = '234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543b' \
         'edb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8' \
         '356f'
ciphertext[
    3] = '32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112b' \
         'acb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb'
ciphertext[
    4] = '32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68' \
         'a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba' \
         '246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa'
ciphertext[
    5] = '3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68' \
         'bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba4' \
         '3722130f042f8ec85b7c2070'
ciphertext[
    6] = '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123' \
         'a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba9' \
         '38220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87' \
         'a59c355d25f8e4'
ciphertext[
    7] = '32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592d' \
         'ed9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a5' \
         '3e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6' \
         'b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce'
ciphertext[
    8] = '315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327' \
         'a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada4' \
         '3d6712150441c2e04f6565517f317da9d3'
ciphertext[
    9] = '271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264' \
         'edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a5' \
         '2222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027'
ciphertext[
    10] = '466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503' \
          'bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83'

dict_hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12,
            "d": 13, "e": 14, "f": 15}


def str2int(strh):
    tmp1 = []
    for i in range(0, len(strh), 2):
        tmp1 += [strh[i:i + 2]]
    tmp2 = []
    for j in tmp1:
        tmp2 += [dict_hex[j[0]] * 16 + dict_hex[j[1]]]
    return tmp2


def xorct(s1, s2):
    d1 = str2int(s1)
    d2 = str2int(s2)
    tmp = ""
    for i in range(0, min(len(d1), len(d2))):
        tmpx = d1[i] ^ d2[i]
        if (97 <= tmpx < 123) or (65 <= tmpx < 91):
            tmp += chr(tmpx)
        else:
            tmp += '?'
    return tmp


tmpchar = []
for i in range(1, 11):
    print(xorct(ciphertext_target, ciphertext[i]))
    tmpchar += [xorct(ciphertext_target, ciphertext[i])]
print('===================================================================================')
plaintext = ''

for j in range(0, len(tmpchar[0])):
    countchar = 0
    tmpdict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
               'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
               'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
               'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
               }
    for k in range(0, 10):
        a = ord(tmpchar[k][j])
        if (97 <= a < 123) or (65 <= a < 91):
            countchar += 1
            tmpdict[tmpchar[k][j]] += 1
            # print(tmpdict[tmpchar[k][j]])
    if countchar >= 6:
        plaintext += ' '
    else:
        if max(tmpdict, key=tmpdict.get).islower():
            plaintext += max(tmpdict, key=tmpdict.get).upper()
        elif max(tmpdict, key=tmpdict.get).isupper():
            plaintext += max(tmpdict, key=tmpdict.get).lower()
    # print(max(tmpdict, key=tmpdict.get))
print(plaintext)
