from random import randint
from linecache import getline

# vowel means + and consonant means -.
# odd after the + and else -.
alpha = []
for i in range(26): alpha.append([chr(i + 65), i + 1])
alpha.append([" ", 27])
eod = input("Encrypt, Decrypt, or Make Keys: ").lower()
if eod == "encrypt" or eod == "e":
    t = input("Plaintext: ").upper()
    e = ""
    llt = ""
    for c in t:
        lc = 0
        if c.isalpha() == True:
            lc = ord(c) - 65
        elif c == " ": lc = 26
        if llt == "v": e = e + str(alpha[lc][1] + 1)
        elif llt == "c": e = e + str(alpha[lc][1] - 1)
        else:
            kl = getline("Key List.txt", randint(1, 100))
            kn = ""
            k = ""
            for i in range(len(kl)):
                if i > 4 and kl[i].isnumeric() == True:
                    if i > 7: k = k + kl[i]
                    else: kn = kn + kl[i]
            e = e + kn
            e = e + " "
            co = (ord(c) - 65) + int(k)
            if co > 26: co = co - 27
            e = e + str(alpha[co][1] - 1)
        e = e + " "
        if c.isalpha() == True:
            if c == "A" or c == "E" or c == "I" or c == "O" or c == "U": llt = "v"
            else: llt = "c"
    print(e)
if eod == "make keys" or eod == "mk" or eod == "m":
    f = open("Key List.txt", "w")
    for i in range(100): f.write("Key #" + str(i + 1) + ": " + str(randint(1, 26)) + "\n")
    f.close()
if eod == "decrypt" or eod == "d":
    e = input("Encrypted text: ")
    e = e.split(" ")
    for i in range(len(e)): e[i] = int(e[i])
    kl = getline("Key List.txt", e[0])
    k = ""
    for i in range(len(kl)):
        if i > 7 and kl[i].isnumeric() == True: k = k + kl[i]
    t = ""
    t = t + alpha[e[1] - int(k)][0]
    llt = ""
    for i in range(len(e) - 2):
        if t[i].isalpha() == True:
            if t[i] == "A" or t[i] == "E" or t[i] == "I" or t[i] == "O" or t[i] == "U": llt = "v"
            else: llt = "c"
        if llt == "v": t = t + alpha[e[i + 2] - 2][0]
        else: t = t + alpha[e[i + 2]][0]
    print(t)