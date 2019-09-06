#! /usr/bin/env python3

block = int(input("Block Length: "))
strng = input("Text: ")

to_padd = block - (len(strng) % block)
byt = ""
out = strng + (to_padd * byt)
