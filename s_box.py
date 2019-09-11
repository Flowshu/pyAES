import gf256

def create():
    box = [[0 for x in range(16)] for y in range(16)] 
    for i in range(256):
        row = int(i / 16)
        column = i % 16
        inverse = gf256.get_inverse(i)
        box[row][column] = sub(inverse)
    return box

def create_inverse():
    pass

def sub(inverse):
    result = inverse
    for k in range(4):
        inverse = shift(inverse)
        result ^= inverse
    result ^= 0x63
    return result

def shift(byt):
    if byt & 0x80 == 0x80:
        return (byt << 1) - 255
    else:
        return byt << 1
