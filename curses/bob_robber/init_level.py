from random import randint

class block:
    def __init__(self, char, coord, type):
        self.char = char
        self.coord = coord
        self.type = type
    def __str__(self):
        return f"{self.char} : {self.coord} : {self.type}"
def level1():
    l = []
    for i in range(50): l.extend([block("-", (0, i), "block"), block("-", (2, i), "block")])
    l.extend([block("|", (1, 0), "block"), block("|", (1, 49), "lock")])
    c = 2
    for i in range(10):
        l.append(block(" ", (1, c), "hazard"))
        c = c + 3
    l.append(block("o", (1, 50), "finish"))
    return l
def level2():
    l = []
    for i in range(50): l.append(block("-", (0, i), "block"))
    for i in range(48): l.append(block("-", (2, i), "block"))
    l.extend([block("-", (2, 48), "lock"), block("-", (2, 49), "block")])
    l.extend([block("|", (1, 0), "block"), block("|", (1, 49), "block")])
    l.extend([block("|", (3, 0), "block"), block("|", (3, 49), "block")])
    for i in range(48): l.append(block("-", (4, i + 2), "block"))
    l.extend([block("-", (4, 0), "block"), block("-", (4, 1), "lock")])
    l.extend([block("|", (1, 47), "lock"), block("|", (3, 2), "lock"), block("|", (3, 47), "lock")])
    l.append(block("o", (5, 1), "finish"))
    c = 2
    for i in range(20):
        l.append(block(" ", (1, c), "hazard"))
        c = c + 2
    c = 2
    for i in range(10):
        l.append(block(" ", (3, 48 - c), "hazard"))
        c = c + 3
    return l
def level3():
    l = []
    for i in range(50): l.append(block("-", (0, i), "block"))
    c = 2
    for j in range(2):
        for i in range(48): l.append(block("-", (c, i), "block"))
        l.extend([block("-", (c, 48), "lock"), block("-", (c, 49), "block")])
        c = 6
    c = 4
    for j in range(2):
        for i in range(48): l.append(block("-", (c, i + 2), "block"))
        l.extend([block("-", (c, 0), "block"), block("-", (c, 1), "lock")])
        c = 8
    c = 1
    for i in range(4):
        l.extend([block("|", (c, 0), "block"), block("|", (c, 49), "block")])
        c = c + 2
    c = 1
    for i in range(2):
        l.append(block("|", (c, 47), "lock"))
        c = 5
        l.append(block("|", (3, 2), "lock"))
    c = randint(2, 5)
    while(c < 46):
        l.append(block(" ", (3, 48 - c), "hazard"))
        c = c + randint(2, 5)
    c = randint(2, 5)
    while(c < 46):
        l.append(block(" ", (1, 48 - c), "hazard"))
        c = c + randint(2, 5)
    c = 2
    for i in range(15):
        l.extend([block(" ", (5, c), "hazard"), block(" ", (7, 48 - c), "hazard")])
        c = c + 3
    r = ""
    for i in range(5): r = r + str(randint(1, 9))
    l.append(block("▯", (1, 1), r))
    l.append(block("|", (7, 2), "plock"))
    l.append(block("o", (9, 1), "finish"))
    return l
def level4():
    l = []
    for i in range(50): l.append(block("-", (0, i), "block"))
    c = 2
    for j in range(2):
        for i in range(48): l.append(block("-", (c, i), "block"))
        l.extend([block("-", (c, 48), "lock"), block("-", (c, 49), "block")])
        c = 6
    c = 4
    for j in range(2):
        for i in range(48): l.append(block("-", (c, i + 2), "block"))
        l.extend([block("-", (c, 0), "block"), block("-", (c, 1), "lock")])
        c = 8
    c = 1
    for i in range(4):
        l.extend([block("|", (c, 0), "block"), block("|", (c, 49), "block")])
        c = c + 2
    c = 1
    for i in range(2):
        l.append(block("|", (c, 47), "lock"))
        c = 5
        l.append(block("|", (3, 2), "lock"))
    c = 2
    for i in range(22):
        l.extend([block(" ", (7, 48 - c), "hazard"), block(" ", (1, c), "hazard")])
        c = c + 2
    c = randint(2, 5)
    while(c < 46):
        l.append(block(" ", (5, c), "hazard"))
        c = c + randint(2, 5)
    c = randint(2, 5)
    while(c < 46):
        l.append(block(" ", (3, 48 - c), "hazard"))
        c = c + randint(2, 5)
    r = ""
    for i in range(5): r = r + str(randint(1, 9))
    l.append(block("▯", (1, 1), r))
    l.append(block("|", (7, 2), "plock"))
    l.append(block("o", (9, 1), "finish"))
    return l
def call_level(ln):
    if ln == 1: return level1()
    elif ln == 2: return level2()
    elif ln == 3: return level3()
    elif ln == 4: return level4()