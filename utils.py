import base64
import sys

def str_to_hex(str_in):
    hex_out = ""
    for chr_in in str_in:
        hex_out += hex(ord(chr_in))[2:]
    return hex_out

def hex_to_str(in_hex):
    str_out = ""
    for byt in bytearray.fromhex(in_hex):
        str_out += chr(byt)
    return str_out

def str_to_bits(str_in):
    hex_str = str_to_hex(str_in)
    hex_arr = bytearray.fromhex(hex_str)
    bits_out = ""
    for byt in hex_arr:
        byt_out = bin(byt)[2:]
        while len(byt_out) % 8 > 0:
            byt_out = "0" + byt_out
        bits_out += byt_out
    return bits_out

def hex_to_bits(in_hex):
    return str_to_bits(hex_to_str(in_hex))
def hex_to_bin(hex_string):
    hex_val = int("0x" + hex_string, 16)
    return bin(hex_val)[2:]

# wrapper-functions for the base64 module
def base64Encode(msg):
    return base64.b64encode(msg)

def base64Decode(base64_string):
    return base64.b64decode(base64_string)

# computes the bitwise XOR of msg and key
def xor(msg,key):
    msg_int = int.from_bytes(msg, byteorder = sys.byteorder)
    key_int = int.from_bytes(key, byteorder = sys.byteorder)
    #for byt in range(len(msg)):
    #    output.append(msg[byt] ^ key[byt % 16])
    #return bytes(output)
    output = msg_int ^ key_int
    return output.to_bytes(len(msg), byteorder = sys.byteorder)
