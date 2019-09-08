#this module implements mathematical operations in the Galois-Filed 2^8 (GF256)

import converter

def add(byte1,byte2):
    if len(byte1) != 8 or len(byte2) != 8 or type(byte1) != str or type(byte2) != str:
        print("error in gf256.add()")
        print("please enter 8-bit strings")
        return
    int1 = converter.byte_to_int(byte1)
    int2 = converter.byte_to_int(byte2)
    xored = int1 ^ int2
    return converter.int_to_byte(xored)

def mul_word(word1,word2):
    if len(byte1) != 8 or len(byte2) != 8 or type(byte1) != str or type(byte2) != str:
        print("error in gf256.mul_word()")
        print("please enter words (4-byte array)")
        return
    mod_red = 0b10001
    #...
    out = "" 
    return out % mod_red

def mul_bytes(q,w):
    e = 0
    for x in range(8):
        if ((w & 1) != 0):
            e ^= q
        bit_set = ((q & 0x80) != 0)
        q <<= 1
        if bit_set:
            q ^= 0x1B
        w >>= 1
    return e % 256

def get_inverse(byt):
    if byt == 0:
        return 0    
    for q in range(256):
        if mul_bytes(byt,q) == 1:
            byt_inverse = q
    return byt_inverse
#############################
#############################
#############################
def pol_mod(pol,mod):
    to_divide = pol
    while to_divide >= mod:
    #for q in range(int(to_divide/mod)):
        sub_to_divide = ""
        pol_str = bin(to_divide)[2:]
        for bit in range(len(pol_str)):
            sub_to_divide += pol_str[bit]
            divide = int(sub_to_divide,2)
            if divide > mod:
                to_divide = bin(divide ^ mod)[2:]
                print(to_divide)
                if bit < len(pol_str):
                    to_divide += pol_str[bit+1:]
                print(to_divide)
                to_divide = int(to_divide,2)
                break
    return to_divide

def pol_mod_copy(pol,mod):
    to_divide = pol
    while to_divide > mod:
        sub_to_divide = ""
        pol_str = bin(to_divide)[2:]
        for bit in range(len(pol_str)):
            sub_to_divide += pol_str[bit]
            divide = int(sub_to_divide,2)
            if divide > mod:
                to_divide = bin(divide ^ mod)[2:]
                print(to_divide)
                if bit < len(pol_str):
                    to_divide += pol_str[bit+1:]
                print(to_divide)
                to_divide = int(to_divide,2)
                break
    return divide

def mul_byte(byte1,byte2):
    if len(byte1) != 8 or len(byte2) != 8 or type(byte1) != str or type(byte2) != str:
        print("error in gf256.mul_byte()")
        print("please enter 8-bit strings")
        return
    mod_red = 0b100011011
    out = 0
    factor = converter.byte_to_int(byte1)
    for q in range(8):
        if byte2[q] == "1":
            shifted = factor << 7-q
            out ^= shifted
    #...shift and add(xor)
    return pol_mod(out,mod_red)