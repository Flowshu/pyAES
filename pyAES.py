import utils
import sys

#import padding
import s_box
import key_schedule

def encrypt(file,key):
    input_file = open(file,'r')
    msg = input_file.read()
    input_file.close()
    msg_bytes = bytes(msg,encoding='utf-8')
    blocks = build_blocks(msg_bytes)
    for block in blocks:
        block = cipher(block,key)
    enc_msg = build_message(blocks)
    output_file = open(file + '.enc','w')
    output_file.write(enc_msg.decode("utf-8"))
    output_file.close

def decrypt(file,key):
    input_file = open(file,'r')
    msg = input_file.read()
    input_file.close()
    msg = utils.base64Decode(bytes(msg, "utf-8"))
    blocks = build_blocks(msg)
    for block in blocks:
        block = inverse_cipher(block,key)
    dec_msg = build_message(blocks)
    output_file = open(file + '.dec','w')
    output_file.write(dec_msg.decode("utf-8"))
    output_file.close

def cipher(state, key):
    keys = key_schedule.generate(key)
    sub_box = s_box.create()
    
    add_round_key(state,keys[0])
    
    for key in keys[1:len(keys)-1]:
        sub_bytes(state,sub_box)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state,key)
    
    sub_bytes(state,sub_box)
    shift_rows(state)
    add_round_key(state,keys[len(keys)-1])
    
    return state

def inverse_cipher(state, key):
    keys = key_schedule.generate(key)#.reverse()
    sub_box = s_box.create()

    add_round_key(state,keys[0])

    for key in keys[1:len(keys)-1]:
        print(state)
        inverse_shift_rows(state)
        inverse_sub_bytes(state,sub_box)
        add_round_key(state,key)
        inverse_mix_columns(state)

    inverse_shift_rows(state)
    inverse_sub_bytes(state,sub_box)
    add_round_key(state,keys[len(keys)-1])

    return state

def sub_bytes(state,sub_box):
    result = state
    for row in range(4):
        for column in range(4):
            value = int.from_bytes(state[row][column], byteorder=sys.byteorder)
            srow = int(value / 16)
            scol = value % 16
            result[row][column] = bytes([sub_box[srow][scol]])
    return result

def inverse_sub_bytes(state,sub_box):
    result = state
    for row in range(4):
        for column in range(4):
            value = int.from_bytes(state[row][column], byteorder=sys.byteorder)
            srow = int(value / 16)
            scol = value % 16
            result[row][column] = bytes([sub_box[srow][scol]])
    return result

def shift_rows(state):
    for row in range(4):
        current_row = state[row]
        for shift in range(row):
            current_row.append(current_row.pop(0))
    return state

def inverse_shift_rows(state):
    for row in range(4):
        current_row = state[row]
        for shift in range(row):
            current_row.insert(0,current_row.pop(3))
    return state

def mix_columns(state):
    state = utils.state_to_columns(state)
    result = state
    factor = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    for column in range(4):
        for element in range(4):
            result[column][element] = utils.multiply_vectors(state[column],factor[element])
    return utils.state_to_rows(result)

def inverse_mix_columns(state):
    state = utils.state_to_columns(state)
    result = state
    factor = [[0x0e,0x0b,0x0d,0x09],[0x09,0x0e,0x0b,0x0d],[0x0d,0x09,0x0e,0x0b],[0x0b,0x0d,0x09,0x0e]]
    for column in range(4):
        for element in range(4):
            result[column][element] = utils.multiply_vectors(state[column],factor[element])
    return utils.state_to_rows(result)

def add_round_key(state,key):
    state = utils.state_to_columns(state)
    result = state
    for column in range(4):
        col = state[column]
        for element in range(4):
            result[column][element] = utils.xor(col[element],key)
    return utils.state_to_rows(result)

###############################################################################

def build_blocks(msg_bytes):
    #TODO: bad padding
    #msg_bytes = padding.pkcs7(msg_bytes)
    while (len(msg_bytes) % 16 != 0):
        msg_bytes += b'\x00'
    msg_bytes = list(msg_bytes)
    num_blocks = int(len(msg_bytes)/16)
    blocks = []
    for a in range(int(len(msg_bytes)/16)):
        block = []
        for b in range(4):
            row = []
            for c in range(4):
                row.append(msg_bytes.pop(0))
            block.append(row)
        blocks.append(block)
    result = []
    for w in range(num_blocks):
        b = []
        for x in range(4):
            word = []
            for y in range(4):
                word.append(bytes([blocks[w][x][y]]))
                #word.append(bytes(chr(blocks[w][x][y]),"utf-8"))
            b.append(word)
        result.append(b)
    return result

def build_message(blocks: list):
    msg_bytes = b''
    for block in blocks:
        for row in block:
            for byt in row:
                msg_bytes += byt
    msg_out = utils.base64Encode(msg_bytes)
    return msg_out

if __name__ == "__main__":
    state = [[b'\x01',b'\x02',b'\x03',b'\x04'],
             [b'\x05',b'\x06',b'\x07',b'\x08'],
             [b'\x09',b'\x0a',b'\x0b',b'\x0c'],
             [b'\x0d',b'\x0e',b'\x0f',b'\x00']]
    sbox = s_box.create()
    inv_sbox = s_box.create_inverse()
    print(state)
    print(shift_rows(state))
    print(inverse_shift_rows(state))
    print()
    print(state)
    print(sub_bytes(state, sbox))
    print(inverse_sub_bytes(state, inv_sbox))
    print()
    print(state)
    print(mix_columns(state))
    print(inverse_mix_columns(state))
