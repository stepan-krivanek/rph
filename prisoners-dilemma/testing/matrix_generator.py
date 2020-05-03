import random

def gen_num():
    return random.randrange(1, 10)

def create_matrix():
    a = gen_num()
    b = gen_num()
    c = gen_num()
    d = gen_num()
    return (((a,a),(c,d)),((d,c),(b,b)))

def check_matrix():
    wantedKey = 2111100
    key = [2,0,0,0,0,0,0]
    m = create_matrix()

    cc = m[0][0][0]
    dd = m[1][1][1]
    cd = m[0][1][0]
    dc = m[0][1][1]

    if cc > dd: key[1] = 1
    if cc > cd: key[2] = 1
    if cc > dc: key[3] = 1
    if dd > cd: key[4] = 1
    if dd > dc: key[5] = 1
    if cd > dc: key[6] = 1

    newKey = int("".join(map(str, key)))

    if newKey != wantedKey:
        check_matrix()
    else:
        print(m)

check_matrix()