import gf256

def new_box():
    box = []
    for rows in range(16):
        box.append([])
        for columns in range(16):
            box[rows].append([])
    return box

def out():
    box = new_box()
    for byt in range(256):
        row = int(byt/16)
        column = byt % 16
        inverse = gf256.get_inverse(byt)
        box[row][column] = sub(inverse)
    return box

def create():
    out = []
    for q in range(256):
        inverse = gf256.get_inverse(q)
        out.append(sub(inverse))
    return out

def shift(byt):
    if byt & 0x80 == 0x80:
        return (byt << 1) - 255
    else:
        return byt << 1

def sub(byt):
    subst = byt
    out = byt
    for q in range(4):
        subst = shift(subst)
        out ^= subst
    out ^= 0x63
    return out