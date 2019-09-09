import utils
import sys

#import padding
import gf256
import s_box
import key_schedule

def encrypt(file,key):
    file = open(file)
    msg = file.read()
    msg_bytes = bytes(msg,encoding='utf-8')
    while (len(msg_bytes) % 16 != 0):
        msg_bytes += b'\x00'
    blocks = build_blocks(msg_bytes)
    print(blocks)
    for block in blocks:
        block = cipher(block,key)
    print(blocks)

def cipher(state, key):
    keys = key_schedule.generate(key)
    sub_box = s_box.create()
    for key in keys:
        sub_bytes(state,sub_box)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state,key)

def sub_bytes(state,sub_box):
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
    #for row in state:
        #print(row)
    return state

def mix_columns(state):
    state = state_to_columns(state)
    result = state
    factor = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    for column in range(4):
        for element in range(4):
            result[column][element] = multiply_vectors(state[column],factor[element])
    return state_to_rows(result)

def multiply_vectors(column,factor):
    out = 0
    for x in range(4):
        y = int.from_bytes(column[x], byteorder = sys.byteorder)
        out ^= gf256.mul_bytes(y,factor[x])
    return bytes([out])

def add_round_key(state,key):
    state = state_to_columns(state)
    result = state
    for column in range(4):
        col = state[column]
        for element in range(4):
            #print(key,key[element])
            result[column][element] = utils.xor(col[element],key)#[element])
    return state_to_rows(result)

###############################################################################

def build_blocks(msg_bytes):
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
                word.append(bytes(chr(blocks[w][x][y]),"utf-8"))
            b.append(word)
        result.append(b)
    return result

# transforms the state from rows to columns
def state_to_columns(state):
    new_state = [[],[],[],[]]
    for column in range(4):
        for row in state:
            new_state[column].append(row[column])
    return new_state

# transforms the state from columns to rows
def state_to_rows(state):
    return state_to_columns(state)

if __name__ == "__main__":
    state = [[b'\x01',b'\x01',b'\x01',b'\x01'],
             [b'\x01',b'\x01',b'\x01',b'\x01'],
             [b'\x01',b'\x01',b'\x01',b'\x01'],
             [b'\x01',b'\x01',b'\x01',b'\x01']]
    state2 = mix_columns(state)
    state3 = add_round_key(state,[b'\x02',b'\x02',b'\x02',b'\x02'])
    sub_box = s_box.create()
    state4 = sub_bytes(state,sub_box)
    print(state4)