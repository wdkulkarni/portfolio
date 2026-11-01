import curses
from time import sleep
from random import randint

def lockpick(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    l = ["#" for i in range(8)]
    for i in range(4): l.append(" ")
    for i in range(5): l.append("#")
    l.extend([" ", " ", " ", "#", "#", "#", " ", " "])
    for i in range(4): l.append("#")
    for i in range(6): l.append(" ")
    l.append("#")
    for i in range(5): l.append("#")
    l.extend([" ", " ", " ", "#", "#", "#", " "])
    for i in range(8): l.append("#")
    for i in range(4): l.append(" ")
    pp = 0
    p = False
    lx = 12
    while(True):
        screen.erase()
        ic = 0
        for i in range(5):
            for j in range(lx):
                screen.addstr(*(i, j + 5), l[ic])
                ic = ic + 1
        if p == False:
            screen.addstr(*(pp, 0), "====>")
        elif p == True:
            screen.addstr(*(2, 4), "====>")
            screen.refresh()
            sleep(5)
            return
        ri = randint(1, 3)
        if ri == 1: pp = pp - 1
        elif ri == 3: pp = pp + 1
        if screen.getch() == curses.KEY_UP: pp = pp - 1
        elif screen.getch() == curses.KEY_DOWN: pp = pp + 1
        if pp > 4: pp = 4
        elif pp < 0: pp = 0
        if screen.getch() == curses.KEY_RIGHT and pp == 2:
            p = True
            lx = 17
            for i in range(5): l.insert(5, " ")
            for i in range(5): l.insert(22, " ")
            for i in range(5): l.insert(39, " ")
            for i in range(5): l.insert(56, " ")
            for i in range(5): l.insert(73, "#")
        screen.refresh()
        sleep(.3)