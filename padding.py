'''
This module implements the PKCS#7 padding.
'''

def apply_padding(message: bytes, block=16):
    bytes_in_last_block = len(message) % block
    if bytes_in_last_block != 0:
        missing_bytes = block - bytes_in_last_block
        padding = bytes([missing_bytes]) * missing_bytes
        return message + padding
    else:
        return message

def remove_padding(message: bytes, block=16):
    if message == b'':
        return message
    message_length = len(message)
    padded_bytes = message[message_length-1]
    if 1 <= padded_bytes <= block:
        for padded_byte in range(padded_bytes):
            if padded_bytes != message[message_length-1-padded_byte]:
                return message
            else:
                return message[:message_length-padded_bytes]
    else:
        return message
