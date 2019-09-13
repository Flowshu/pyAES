import s_box

# performs key expansion and generates key schedule
# param: a 128-bit, 192-bit or 256-bit key as bytes
# return: list of words in key schedule
def generate(key: bytes):
    words,rounds = check_and_transform_key(key)
    rcon = [[0x01,0,0,0],[0x02,0,0,0],[0x04,0,0,0],[0x08,0,0,0],
            [0x10,0,0,0],[0x20,0,0,0],[0x40,0,0,0],[0x80,0,0,0],
            [0x1B,0,0,0],[0x36,0,0,0],[0x6C,0,0,0],[0xD8,0,0,0],
            [0xAB,0,0,0],[0x4D,0,0,0],[0x1B,0,0,0],[0x36,0,0,0],
            [0x1B,0,0,0],[0x36,0,0,0],[0x1B,0,0,0],[0x36,0,0,0],
            [0x1B,0,0,0],[0x36,0,0,0],[0x1B,0,0,0],[0x36,0,0,0],
            [0x1B,0,0,0],[0x36,0,0,0],[0x1B,0,0,0],[0x36,0,0,0],
            [0x1B,0,0,0]]
    num_words = len(words)
    expanded = [0] * 4 * rounds
    for word in range(rounds*4):
        if word < num_words:
            expanded[word] = words[word]
        elif (word >= num_words) and ((word % num_words) == 0):
            temp = xor_words(sub_word(rot_word(expanded[word-1])),rcon[int(word/num_words)-1])
            expanded[word] = xor_words(temp,expanded[word-num_words])
        elif (word >= num_words) and ((word % num_words) == 4) and (num_words > 6):
            expanded[word] = xor_words(expanded[word-num_words],sub_word(expanded[word-1]))
        else:
            expanded[word] = xor_words(expanded[word-num_words],expanded[word-1])
    #printSchedule(expanded)
    #print(expanded)
    return expanded
    '''
    result = []
    for x in range(rounds):
        l = ""
        for y in range(4):
                for v in range(4):
                    l += chr(expanded[x*4 + y][v])
        result.append(bytes(l,"utf-8"))
    return result
'''
def printSchedule(expanded):
    for word in expanded:
        print([hex(b) for b in word])

def build_key_schedule():
    pass

# validates the key length to be 16, 24 or 32 byte
def check_and_transform_key(key: bytes):
    if len(key) == 16:
        words = transform_key(key)
        rounds = 11
    elif len(key) == 24:
        words = transform_key(key)
        rounds = 13
    elif len(key) == 32:
        words = transform_key(key)
        rounds = 15
    else:
        words = []        
        rounds = -1
    return words,rounds

# transforms a key into an array of 32-bit/4-byte words
def transform_key(key: bytes):
    key_bytes = list(key)
    words = []
    for word_in_key in range(int(len(key) / 4)):
        word = []
        for byte_in_word in range(4):
            word.append(key_bytes.pop(0))
        words.append(word)
    return words

# rotates a 32-bit/4-byte word by one byte to the left
def rot_word(word):
    return word[1:] + word[:1]

# substitutes each byte in a 32-bit/4-byte word according to the S-box
def sub_word(word):
    word_out = [0,0,0,0]
    sub_box = s_box.create()
    for byt in range(4):
        word_out[byt] = sub_box[int(word[byt] / 16)][word[byt] % 16]       
    return word_out

# performs the XOR-operation on two 32-bit/4-byte words
def xor_words(word1,word2):
    xored_word = [0,0,0,0]
    for byt in range(4):
        xored_word[byt] = word1[byt] ^ word2[byt]
    return xored_word

def test():
    result1 = generate(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c')
    result2 = generate(b'\x8e\x73\xb0\xf7\xda\x0e\x64\x52\xc8\x10\xf3\x2b\x80\x90\x79\xe5\x62\xf8\xea\xd2\x52\x2c\x6b\x7b')
    result3 = generate(b'\x60\x3d\xeb\x10\x15\xca\x71\xbe\x2b\x73\xae\xf0\x85\x7d\x77\x81\x1f\x35\x2c\x07\x3b\x61\x08\xd7\x2d\x98\x10\xa3\x09\x14\xdf\xf4')
    test_case1 = [[43, 126, 21, 22], [40, 174, 210, 166], [171, 247, 21, 136], [9, 207, 79, 60],
                 [160, 250, 254, 23], [136, 84, 44, 177], [35, 163, 57, 57], [42, 108, 118, 5], 
                 [242, 194, 149, 242], [122, 150, 185, 67], [89, 53, 128, 122], [115, 89, 246, 127], 
                 [61, 128, 71, 125], [71, 22, 254, 62], [30, 35, 126, 68], [109, 122, 136, 59],
                 [239, 68, 165, 65], [168, 82, 91, 127], [182, 113, 37, 59], [219, 11, 173, 0],
                 [212, 209, 198, 248], [124, 131, 157, 135], [202, 242, 184, 188], [17, 249, 21, 188],
                 [109, 136, 163, 122], [17, 11, 62, 253], [219, 249, 134, 65], [202, 0, 147, 253],
                 [78, 84, 247, 14], [95, 95, 201, 243], [132, 166, 79, 178], [78, 166, 220, 79],
                 [234, 210, 115, 33], [181, 141, 186, 210], [49, 43, 245, 96], [127, 141, 41, 47],
                 [172, 119, 102, 243], [25, 250, 220, 33], [40, 209, 41, 65], [87, 92, 0, 110], 
                 [208, 20, 249, 168], [201, 238, 37, 137], [225, 63, 12, 200], [182, 99, 12, 166]]
    test_case2 = [[142, 115, 176, 247], [218, 14, 100, 82], [200, 16, 243, 43], [128, 144, 121, 229], [98, 248, 234, 210], [82, 44, 107, 123],
                  [254, 12, 145, 247], [36, 2, 245, 165], [236, 18, 6, 142], [108, 130, 127, 107], [14, 122, 149, 185], [92, 86, 254, 194], 
                  [77, 183, 180, 189], [105, 181, 65, 24], [133, 167, 71, 150], [233, 37, 56, 253], [231, 95, 173, 68], [187, 9, 83, 134], 
                  [72, 90, 240, 87], [33, 239, 177, 79], [164, 72, 246, 217], [77, 109, 206, 36], [170, 50, 99, 96], [17, 59, 48, 230], 
                  [162, 94, 126, 213], [131, 177, 207, 154], [39, 249, 57, 67], [106, 148, 247, 103], [192, 166, 148, 7], [209, 157, 164, 225], 
                  [236, 23, 134, 235], [111, 166, 73, 113], [72, 95, 112, 50], [34, 203, 135, 85], [226, 109, 19, 82], [51, 240, 183, 179], 
                  [64, 190, 235, 40], [47, 24, 162, 89], [103, 71, 210, 107], [69, 140, 85, 62], [167, 225, 70, 108], [148, 17, 241, 223], 
                  [130, 31, 117, 10], [173, 7, 215, 83], [202, 64, 5, 56], [143, 204, 80, 6], [40, 45, 22, 106], [188, 60, 231, 181], 
                  [233, 139, 160, 111], [68, 140, 119, 60], [142, 204, 114, 4], [1, 0, 34, 2]]
    test_case3 = [[96, 61, 235, 16], [21, 202, 113, 190], [43, 115, 174, 240], [133, 125, 119, 129], [31, 53, 44, 7], [59, 97, 8, 215], [45, 152, 16, 163], [9, 20, 223, 244],
                  [155, 163, 84, 17], [142, 105, 37, 175], [165, 26, 139, 95], [32, 103, 252, 222], [168, 176, 156, 26], [147, 209, 148, 205], [190, 73, 132, 110], [183, 93, 91, 154], 
                  [213, 154, 236, 184], [91, 243, 201, 23], [254, 233, 66, 72], [222, 142, 190, 150], [181, 169, 50, 138], [38, 120, 166, 71], [152, 49, 34, 41], [47, 108, 121, 179], 
                  [129, 44, 129, 173], [218, 223, 72, 186], [36, 54, 10, 242], [250, 184, 180, 100], [152, 197, 191, 201], [190, 189, 25, 142], [38, 140, 59, 167], [9, 224, 66, 20], 
                  [104, 0, 123, 172], [178, 223, 51, 22], [150, 233, 57, 228], [108, 81, 141, 128], [200, 20, 226, 4], [118, 169, 251, 138], [80, 37, 192, 45], [89, 197, 130, 57],
                    [222, 19, 105, 103], [108, 204, 90, 113], [250, 37, 99, 149], [150, 116, 238, 21], [88, 134, 202, 93], [46, 47, 49, 215], [126, 10, 241, 250], [39, 207, 115, 195],
                    [116, 156, 71, 171], [24, 80, 29, 218], [226, 117, 126, 79], [116, 1, 144, 90], [202, 250, 170, 227], [228, 213, 155, 52], [154, 223, 106, 206], [189, 16, 25, 13],
                    [254, 72, 144, 209], [230, 24, 141, 11], [4, 109, 243, 68], [112, 108, 99, 30]]
    if result1 == test_case1:
        print('Passed test 1!')
    if result2 == test_case2:
        print('Passed test 2!')
    if result3 == test_case3:
        print('Passed test 3!')

if __name__ == "__main__":
    test()
