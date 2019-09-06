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
