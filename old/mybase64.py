#! /usr/bin/env python3

def encode(hex_string):
    bin_string = hex_to_bin(hex_string)
    print(bin_string)

def decode(base64_string):
    pass

def hex_to_bin(hex_string):
    hex_val = int("0x" + hex_string, 16)
    return bin(hex_val)[2:]

hex = input()
hexarr = ""
for b in hex:
    if b == "a":
        hexarr += "1010"
    elif b == "b":
        hexarr += "1011"   
    elif b == "c":
        hexarr += "1100"
    elif b == "d":
        hexarr += "1101"
    elif b == "e":
        hexarr += "1110"
    elif b == "f":
        hexarr += "1111"
    elif b == "0":
        hexarr += "0000"
    elif b == "1":
        hexarr += "0001"
    elif b == "2":
        hexarr += "0010"
    elif b == "3":
        hexarr += "0011"
    elif b == "4":
        hexarr += "0100"
    elif b == "5":
        hexarr += "0101"
    elif b == "6":
        hexarr += "0110"
    elif b == "7":
        hexarr += "0111"
    elif b == "8":
        hexarr += "1000"
    elif b == "9":
        hexarr += "1001"
count = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet += alphabet.lower()
alphabet += "0123456789+/"
basestring = ""
while len(hexarr) % 6 > 0:
    for bit in range(int(len(hexarr) / 6)):
        base64val = hexarr[count:count+6]
        spot = int(base64val,2)
        basestring += alphabet[spot]
        count += 6

print (basestring)
