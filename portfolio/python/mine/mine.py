from math import ceil
from time import sleep

def generate_ground():
    l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    g = "#"
    for i in range(98):
        g = g + " "
    g = g + "\n"
    for i in range(26):
        for j in range(i + 1):
            for k in range(99):
                g = g + l[i]
            g = g + "\n"
    return g
def controls(c, m, g, p):
    if m.isalpha() == True and m.islower() == True:
        if len(m) == 1:
            so = shop(m, c, p)
            c = so[0]
            p = so[1]
        elif m == "save":
            save(g, c, p)
        return g, c, p
    if m == "load save":
            lso = load_save(g, c, p)
            g = lso[0]
            c = lso[1]
            p = lso[2]
            return g, c, p
    s = 0
    sg = ""
    for i in range(len(g)):
            if g[i] == "#":
                s = i
            sg = sg + g[i]
            sg = sg + ","
    ng = sg.split(',')
    if m == "1":
        if ng[s - 101] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s - 101], p)
        ng[s - 101] = " "
    if m == "2":
        if ng[s - 100] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s - 100], p)
        ng[s - 100] = " "
    if m == "3":
        if ng[s - 99] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s - 99], p)
        ng[s - 99] = " "
    if m == "4":
        if ng[s - 1] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s - 1], p)
        ng[s - 1] = " "
    if m == "5":
        if ng[s + 1] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s + 1], p)
        ng[s + 1] = " "
    if m == "6":
        if ng[s + 99] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s + 99], p)
        ng[s + 99] = " "
    if m == "7":
        if ng[s + 100] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s + 100], p)
        ng[s + 100] = " "
    if m == "8":
        if ng[s + 101] == " ":
            return g, c, p
        c = add_money_wait(c, ng[s + 101], p)
        ng[s + 101] = " "
    if m == ";":
        if ng[s - 100] != " ":
            return g, c, p
        ng[s] = " "
        ng[s - 100] = "#"
    if m == ".":
        if ng[s + 100] != " ":
            return g, c, p
        ng[s] = " "
        ng[s + 100] = "#"
    if m == "/":
        if ng[s + 1] != " ":
            return g, c, p
        ng[s] = " "
        ng[s + 1] = "#"
    if m == ",":
        if ng[s - 1] != " ":
            return g, c, p
        ng[s] = " "
        ng[s - 1] = "#"
    g = "".join(ng)
    return g, c, p
def splice(g):
    p = 0
    for i in range(len(g)):
        if g[i] == "#":
            p = i
    p = ((ceil(p / 100) * 100) + 299)
    sg = ""
    for i in range(p):
        sg = sg + g[i]
    return sg
def add_money_wait(c, b, p):
    c = c + (ord(b) - 64)
    st = (ord(b) - 64) - (ord(p) - 96)
    if st > 0:
        sleep(st)
    return c
def shop(m, c, p):
    co = (ord(m) - 96) * 100
    np = chr(ord(p) + 1)
    if c > co and m == np:
        c = c - co
        p = np
    return c, p
def save(g, c, p):
    f = open("mine_save.txt", "w")
    f.write("Pickaxe: ")
    f.write(p)
    f.write("\n")
    f.write(str(c))
    f.write("©\n")
    f.write(g)
    f.close()
def load_save(g, c, p):
    f = open("mine_save.txt", "r")
    l = f.readline()
    p = l[9]
    l = f.readline()
    sc = ""
    for i in range(len(l) - 2):
        sc = sc + l[i]
    c = int(sc)
    g = f.read()
    f.close()
    return g, c, p
g = generate_ground()
c = 0
p = 'a'
while(True):
    sg = splice(g)
    print(c, end = "©\n")
    print(sg)
    m = input("Move: ")
    co = controls(c, m, g, p)
    g = co[0]
    c = co[1]
    p = co[2]