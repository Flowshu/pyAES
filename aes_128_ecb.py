import converter
import xor
import gf256
import s_box
import key_schedule

def encrypt(state):
    keys = key_schedule.generate()
    sub_box = s_box.create()
    
    for q in range(9):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state,key)

def build_block(word):
    bits = list(converter.str_to_bits(word))
    #print(bits)
    grid = {}
    for row in range(4):
        vector = []
        for byt in range(4):
            bytval = ""
            for bit in range(8):
                bytval += bits.pop(0)
            vector.append(bytval)
        grid[row] = vector
    #for r in range(4):
    #    print(grid[r])
    return grid

def shift_rows(word):
    block = build_block(word)
    for q in range(4):
        row = block[q]
        for w in range(q):
            row.append(row.pop(0))
    for e in range(4):
        print(block[e])
    #return block

def add_round_key(state,key):
    state_block = build_block(state)
    key_block = build_block(key)
    out = ""
    for q in range(4):
        state_row = state_block[q]
        key_row = key_block[q]
        for w in range(4):
            print(state_row[w])
            print(key_row[w])
            xored = xor.crypt(chr(int(state_row[w],2)),chr(int(key_row[w],2)))
            print(xored)
            out += xored
    return out

def mix_columns(word):
    word_list = list(word)
    byts = []
    for byt in range(4):
        octet = ""
        for bit in range(8):
            octet += word_list.pop(0)
        byts.append(octet)
    factor = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    for q in range(4):
        out = 0
        for e in range(4):
            out ^= gf256.mul_bytes(int(byts[e],2),factor[q][e])
        print(hex(out))
#######################
#######################
#######################
def gal_mul(byt1,byt2):
    prod = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for q in range(8):
        for w in range(8):
            q2 = 7-q
            w2 = 7-w
            if int(byt1[q2]) == 1 and int(byt2[w2]) == 1:
                prod[q2+w2] += 1
    for e in range(len(prod)):
        prod[e] = str(prod[e] % 2)
    result = "".join(prod)
    print(result)
    return int(result,2) % 0x11B

