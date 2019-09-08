import base64
import sys

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
