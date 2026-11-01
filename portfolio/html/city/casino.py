from time import sleep
from random import randint
def casino():
    c = 100
    a = input("Welcome to the Casino. You have " + str(c) + " dollars. We have an awesome selection of games for you to play. You can play the slot machine(type sm to play), the lottery(type lotto to play), roulette(type roulette to play), and blackjack(type blackjack to play). If you want to stop playing type end.")
    if a == "sm":
        print("Play for 1 coin and a chance of winning 100 to 300 coins.")
        n = []
        for i in range(3):
            n.append(randint(1, 3))
        for i in range(5):
            print("...")
            sleep(1)
        print("The numbers are", n[0], n[1], str(n[2]) + ".")
        if n[0] == n[1] == n[2]:
            print("You won.")
            w = randint(100, 300)
            c = c + w
            print("You won", w, "dollars.")
        else:
            print("You lose.")
            c = c - 1
    if a == "blackjack":
        print("Play for 5 coins and a chance to win 25 coins.")
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
        ca = d[0]
        d[0] = d[len(d) - 1]
        d[len(d) - 1] = ca
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
                ap = 0
                for i in p1:
                    if i[1:].isalpha() == False:
                        p1ct = p1ct + int(i[1:])
                    else:
                        if i[1:] == 'J' or i[1:] == 'Q' or i[1:] == 'K':
                            p1ct = p1ct + 10
                        elif i[1:] == 'A':
                            if ap == 0: ap = int(input("Ace Point Value(1 or 11)."))
                            p1ct = p1ct + ap
                break
            else:
                [p1, d] = deal(p1, d, 1)
        if p1ct > 21:
            print("You Lose. You got over 21 points.")
            return c - 5
        while True:
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
                c = c + 25
                break
            elif t > p1ct:
                print("You Lose. The dealer got", t, "points.")
                c = c - 5
                break
            elif t == 21 and t == p1ct:
                print("You Tied. The dealer got", t, "points.")
                break
    if a == "lotto":
        q = randint(25000000, 1500000000)
        print("Play for 2 dollars and mabye win", q, "dollars.")
        rn = []
        for i in range(6): rn.append(randint(1, 50))
        rn = sort(rn, [])
        print("Choose six numbers form 1 to 50 in the spaces below.")
        pn = []
        for i in range(6): pn.append(int(input("Number " + str(i + 1) + ": ")))
        pn = sort(pn, [])
        if rn == pn:
            print("You won", q, "dollars.")
            c = c + q
        else:
            print("You lose.")
            c = c - 2
    if a == "roulette":
        #Make lines 32-36 a do while loop.
        d = int(input("How much money do you want to bet?"))
        while d > c:
            print("You don't have that much money.")
            d = int(input("How much money do you want to bet?"))
        n = randint(1, 10)
        if int(input("Pick your number from 1 to 30.")) == n:
            print("You win.")
            c = c + d
        else:
            print("You lose.")
            print("The number was...")
            sleep(1)
            print(n)
            c = c - d
    if a == "end":
        print("Why did you press end. :(")
        print("Ending in:")
        for i in range(3):
            print(3 - i)
            sleep(1)
        print("..... (beeeep)")
    return c
def sort(values, svalues):
    if len(values) == 0: return svalues
    min = 10000000
    ind = 0
    for i in range(len(values)):
        if values[i] < min:
            min = values[i]
            ind = i
    del values[ind]
    svalues.append(min)
    return sort(values, svalues)
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
casino()