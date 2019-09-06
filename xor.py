#! /usr/bin/env python3

def crypt(msg,key):

    keybyts = []
    for character in key:
        byt = int(str.encode(character).hex(),16)
        keybyts.append(byt)
    out = ""
    for x in range(len(msg)):
        byt = int(str.encode(msg[x]).hex(),16)
        q =  bin(byt ^ keybyts[x % len(key)])[2:]
        while len(q) < 8:
            q = "0" + q
        out = out + q
    return out
