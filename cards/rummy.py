from random import randint

# A recreation of the common game rummy.

def shuffle(d):
    sd = []
    for i in range(len(d)):
        ri = 0
        m = 0
        ril = []
        while(m < (len(sd) - 1)):
            m = 0
            ri = randint(0, (len(d) - 1))
            for j in sd:
                if j != d[ri]:
                    m = m + 1
        sd.append(d[ri])
    d = sd
    return d
def deal(p1, p2, p3, p4, d):
    for i in range(13):
        j = 4 * i
        p1.append(d[j])
        p2.append(d[j + 1])
        p3.append(d[j + 2])
        p4.append(d[j + 3])
    nd = []
    for i in range(len(d)):
        if i >= 52:
            nd.append(d[i])
    d = nd
    return p1, p2, p3, p4, d
def ai(aid, d):
    dp = []
    tp = []
    tnp = []
    for i in range(len(aid)):
        for j in range(len(aid)):
            if i != j and aid[i] == aid[j]:
                tnpc = 0
                for k in tnp:
                    if k != i:
                        tnpc = tnpc + 1
                if tnpc == len(tnp):
                    tp.append(i)
                    tnp.append(j)
                    dp.append(aid[i])
    pn = 0
    for i in tp:
        aid.pop(i - pn)
        pn = pn + 1
    print(aid[5:])
    return aid, d
d = ["s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK", "sA", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK", "dA", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", "hA", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK", "cA", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK", "sA", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK", "dA", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", "hA", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK", "cA"]
d = shuffle(d)
p1 = []
p2 = []
p3 = []
p4 = []
do = deal(p1, p2, p3, p4, d)
p1 = do[0]
p2 = do[1]
p3 = do[2]
p4 = do[3]
d = do[4]
o = d[0]
d.pop(0)
while(True):
    print("Open Card:", o)
    for i in p1:
        print(i, end = " ")
    print()
    if input("Pick Up Spot: ") == "o":
        p1.append(o)
    dc = int(input("Discard Card #: "))
    dc = dc - 1
    co = controls(l, dc, p1, d, o)
    p1 = co[0]
    d = co[1]
    o = co[2]
    aio = []
    aio = ai(p2, d)
    p2 = aio[0]
    d = aio[1]
    aio = []
    aio = ai(p3, d)
    p3 = aio[0]
    d = aio[1]
    aio = []
    aio = ai(p4, d)
    p4 = aio[0]
    d = aio[1]