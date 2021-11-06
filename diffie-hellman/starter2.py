p = 28151


def order(g, p): 
    for i in range(2, p): 
        if pow(g, i, p) == g:
            return i
    return p


for g in range(2, p):
    o = order(g, p)
    if o == p:
        print(g)
        break