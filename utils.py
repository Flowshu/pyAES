import base64
import sys

# wrapper-functions for the base64 module
def base64Encode(msg):
    return base64.b64encode(msg)

def base64Decode(base64_string):
    return base64.b64decode(base64_string)

def hexEncode(msg):
    pass

def hexDecode(hex_string):
    pass

# transforms the state from rows to columns
def state_to_columns(state: list):
    new_state = [[],[],[],[]]
    for column in range(4):
        for row in state:
            new_state[column].append(row[column])
    return new_state

# transforms the state from columns to rows
def state_to_rows(state: list):
    return state_to_columns(state)

# computes the bitwise XOR of msg and key
def xor(msg,key):
    msg_int = int.from_bytes(msg, byteorder = sys.byteorder)
    key_int = int.from_bytes(key, byteorder = sys.byteorder)
    #for byt in range(len(msg)):
    #    output.append(msg[byt] ^ key[byt % 16])
    #return bytes(output)
    output = (msg_int ^ key_int) % 2**32
    return output.to_bytes(32, byteorder = sys.byteorder)
