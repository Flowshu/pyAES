import s_box

# performs key expansion and generates key schedule
# param: key -- a 128-bit, 192-bit or 256-bit key as bytes-object (b'...')
# return: key_schedule -- a list of keys as bytes-object ([b'...',...,b'...'])
def generate(key: bytes) -> list:
    words,rounds = check_and_transform_key(key)
    rcon = [[0x01,0,0,0],[0x02,0,0,0],[0x04,0,0,0],[0x08,0,0,0],
            [0x10,0,0,0],[0x20,0,0,0],[0x40,0,0,0],[0x80,0,0,0],
            [0x1B,0,0,0],[0x36,0,0,0]]
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
    key_schedule = build_schedule_from_words(expanded)
    return key_schedule

# converts the list of words generated through key expansion into a list of keys
# param: word_list -- a list of words(list of 4 integers)
# return: key_schedule -- a list of keys as bytes-object ([b'...',...,b'...'])
def build_schedule_from_words(schedule: list) -> list:
    keys = []
    for round in range(int(len(schedule)/4)):
        key = b''
        for word in range(4):
            for byt in range(4):
                key += bytes([schedule[round*4 + word][byt]])
        keys.append(key)
    return keys

# validates the key length to be 16, 24 or 32 byte
def check_and_transform_key(key: bytes):
    if len(key) == 16:
        words, rounds = transform_key(key), 11
    elif len(key) == 24:
        words, rounds = transform_key(key), 13
    elif len(key) == 32:
        words, rounds = transform_key(key), 15
    else:
        words, rounds = [], -1
    return words, rounds

# transforms a key into an array of 32-bit/4-byte words
def transform_key(key: bytes) -> list:
    key_bytes = list(key)
    words = []
    for word_in_key in range(int(len(key) / 4)):
        word = []
        for byte_in_word in range(4):
            word.append(key_bytes.pop(0))
        words.append(word)
    return words

# rotates a 32-bit/4-byte word by one byte to the left
# param: word -- a list of 4 integers i with 0 <= i <= 255
# return: word -- a list of 4 integers i with 0 <= i <= 255
def rot_word(word: list) -> list:
    return word[1:] + word[:1]

# substitutes each byte in a 32-bit/4-byte word according to the S-box
# param: word -- a list of 4 integers i with 0 <= i <= 255
# return: word -- a list of 4 integers i with 0 <= i <= 255
def sub_word(word: list) -> list:
    word_out = [0,0,0,0]
    sub_box = s_box.create()
    for byt in range(4):
        word_out[byt] = sub_box[int(word[byt] / 16)][word[byt] % 16]       
    return word_out

# performs the XOR-operation on two 32-bit/4-byte words
# params: word -- a list of 4 integers i with 0 <= i <= 255
# return: word -- a list of 4 integers i with 0 <= i <= 255
def xor_words(word1: list, word2: list) -> list:
    xored_word = [0,0,0,0]
    for byt in range(4):
        xored_word[byt] = word1[byt] ^ word2[byt]
    return xored_word
