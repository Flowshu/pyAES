import s_box

def generate(key):
    rcon = [[0x1,0,0,0],[0x2,0,0,0],[0x4,0,0,0],[0x8,0,0,0],[0x10,0,0,0],[0x20,0,0,0],[0x40,0,0,0],[0x80,0,0,0],[0x1B,0,0,0],[0x36,0,0,0]]
    key_bytes = list(bytes(key,"utf-8"))
    words = []
    for q in range(4):
        word = []
        for e in range(4):
            byt = key_bytes.pop(0)
            word.append(byt)
        words.append(word)
    expanded = [0] * 44
    rounds = 11
    for q in range(rounds*len(words)):
        if q < len(words):
            expanded[q] = words[q]
        elif (q >= len(words)) and ((q % len(words)) == 0):
            expanded[q] = xor_words(xor_words(rot_word(sub_word(expanded[q-1])),rcon[int((q-1)/len(words))]),expanded[q-len(words)])
        #else if (q >= len(words)) and ((q % len(words)) == 4) and (len(words) > 6):
        #    expanded[q] = xor_words(expanded[q-len(words)],sub_word(expanded[q-1])
        else:
            expanded[q] = xor_words(expanded[q-len(words)],expanded[q-1])
    result = []
    for x in range(11):
        l = ""
        for y in range(4):
                for v in range(4):
                    l += chr(expanded[x*4 + y][v])
        result.append(bytes(l,"utf-8"))
    return result

def rot_word(word):
    word_copy = word
    word_copy.append(word_copy.pop(0))
    return word_copy

def sub_word(word):
    word_out = [0] * 4
    sub_box = s_box.create()
    for byt in range(4):
        word_out[byt] = sub_box[int(byt / 16)][byt % 16]       
    return word_out

def xor_words(word1,word2):
    xored_word = [0] * 4
    for byt in range(4):
        xored_word[byt] = word1[byt] ^ word2[byt]
    return xored_word

if __name__ == "__main__":
    result = generate('1234567890ABCDEF')
    for w in range(11):
        print(result[w])