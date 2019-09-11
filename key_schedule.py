import s_box

# performs key expansion and generates key schedule
# param: a 128-bit, 192-bit or 256-bit key as bytes
# return: list of keys as bytes
def generate(key: bytes):
    words,rounds = check_and_transform_key(key)
    rcon = [[0x01,0,0,0],[0x02,0,0,0],[0x04,0,0,0],[0x08,0,0,0],
            [0x10,0,0,0],[0x20,0,0,0],[0x40,0,0,0],[0x80,0,0,0],
            [0x1B,0,0,0],[0x36,0,0,0]]
    expanded = [0,0,0,0] * rounds
    num_words = len(words)
    for q in range(rounds*num_words):
        if q < num_words:
            expanded[q] = words[q]
        elif (q >= num_words) and ((q % num_words) == 0):
            expanded[q] = xor_words(xor_words(rot_word(sub_word(expanded[q-1])),rcon[int((q-1)/num_words)]),expanded[q-num_words])
        elif (q >= num_words) and ((q % num_words) == 4) and (num_words > 6):
            expanded[q] = xor_words(expanded[q-num_words],sub_word(expanded[q-1]))
        expanded[q] = xor_words(expanded[q-num_words],expanded[q-1])
    result = []

    for x in range(rounds):
        l = ""
        for y in range(4):
                for v in range(4):
                    l += chr(expanded[x*4 + y][v])
        result.append(bytes(l,"utf-8"))
    return result

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
    for word_in_key in range(len(key) / 4):
        word = []
        for byte_in_word in range(4):
            word.append(key_bytes.pop(0))
        words.append(word)
    return words

# rotates a 32-bit/4-byte word by one byte to the left
def rot_word(word):
    result = []
    result.append(word.pop(0))
    return result

# substitutes each byte in a 32-bit/4-byte word according to the S-box
def sub_word(word):
    word_out = [0,0,0,0]
    sub_box = s_box.create()
    for byt in range(4):
        word_out[byt] = sub_box[int(byt / 16)][byt % 16]       
    return word_out

# performs the XOR-operation on two 32-bit words
def xor_words(word1,word2):
    xored_word = [0,0,0,0]
    for byt in range(4):
        xored_word[byt] = word1[byt] ^ word2[byt]
    return xored_word

def test():
    result = generate('1234567890ABCDEF')
    for w in range(11):
        print(result[w])

if __name__ == "__main__":
    test()
