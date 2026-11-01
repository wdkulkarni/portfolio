from random import randint
from sys import exit

# A recreation of the common game blackjack.

def deal(pd, d, cn):
    for i in range(cn):
        j = 4 * i
        pd.append(d[j])
    nd = []
    for i in range(len(d)):
        if i > cn:
            nd.append(d[i])
    d = nd
    return [pd, d]
d = ["s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK", "sA", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK", "dA", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", "hA", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK", "cA", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "sJ", "sQ", "sK", "sA", "d2", "d3", "d4", "d5", "d6", "d7", "d8", "d9", "d10", "dJ", "dQ", "dK", "dA", "h2", "h3", "h4", "h5", "h6", "h7", "h8", "h9", "h10", "hJ", "hQ", "hK", "hA", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "cJ", "cQ", "cK", "cA"]
sd = []
for i in range(len(d)):
    ri = 0
    m = 0
    while(m < (len(sd) - 1)):
        m = 0
        ri = randint(0, (len(d) - 1))
        for j in sd:
            if j != d[ri]: m = m + 1
    sd.append(d[ri])
d = sd
c = d[0]
d[0] = d[len(d) - 1]
d[len(d) - 1] = c
p1 = []
p2 = []
[p1, d] = deal(p1, d, 2)
[p2, d] = deal(p2, d, 2)
p1ct = 0
while True:
    print("Your Cards: ", end = "")
    for i in p1:
        print(i, end = " ")
    print("\nDealer's Card:", p2[0])
    if input("Type more for more cards or end to end the game: ") == "end":
        ap = int(input("Ace Point Value (If you have no aces, put a random number): "))
        for i in p1:
            if i[1:].isalpha() == False:
                p1ct = p1ct + int(i[1:])
            else:
                if i[1:] == 'J' or i[1:] == 'Q' or i[1:] == 'K':
                    p1ct = p1ct + 10
                elif i[1:] == 'A':
                    p1ct = p1ct + ap
        break
    else:
        [p1, d] = deal(p1, d, 1)
if p1ct > 21:
    exit("You Lose. You got over 21 points.")
while(True):
    p2p = []
    ac = 0
    for i in p2:
        if i[1:].isalpha() == False:
            p2p.append(int(i[1:]))
        else:
            if i[1:] == 'J' or i[1:] == 'Q' or i[1:] == 'K':
                p2p.append(10)
            elif i[1:] == 'A':
                ac = ac + 1
                p2p.append(111)
    t = 0
    for i in p2p:
        if i != 111:
            t = t + i
    if ac > 0:
        if t + (ac * 11) > 21:
            t = t + ac
        else:
            t = t + (ac * 11)
    if t < p1ct:
        [p2, d] = deal(p2, d, 1)
    elif t > 21:
        print("You Win! The dealer got", t, "points.")
        exit()
    elif t >= p1ct:
        print("You Lose. The dealer got", t, "points.")
        exit()
    elif t == 21 and t == p1ct:
        print("You Tied. The dealer got", t, "points.")
        exit()