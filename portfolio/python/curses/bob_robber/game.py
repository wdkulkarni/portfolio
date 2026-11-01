import curses
from time import sleep
from sys import exit

from init_level import call_level
from lockpick import lockpick

def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    pp = (1, 1)
    ds = {curses.KEY_UP: (-1, 0), curses.KEY_DOWN: (1, 0), curses.KEY_LEFT: (0, -1), curses.KEY_RIGHT: (0, 1)}
    ln = 1
    l = call_level(ln)
    hc = 0
    while(True):
        screen.erase()
        try: screen.addstr(*pp, "b")
        except: ...
        try:
            for i in l:
                if i.type == "hazard" and hc == 3: screen.addstr(*i.coord, i.char, curses.color_pair(1))
                elif i.type == "lock": screen.addstr(*i.coord, i.char, curses.color_pair(2))
                elif i.char == "▯" or i.type == "plock": screen.addstr(*i.coord, i.char, curses.color_pair(3))
                else: screen.addstr(*i.coord, i.char)
        except: exit("\033[1m" + "Make the screen bigger." + "\033[0m")
        mpp = pp
        try: mpp = tuple(map(sum, zip(pp, ds.get(screen.getch()))))
        except: ...
        c = 0
        for i in l:
            if mpp == i.coord:
                if i.type == "hazard":
                    if hc == 3: pp = (1, 1)
                    else: c = c + 1
                elif i.type == "lock":
                    lockpick(screen)
                    for j in range(len(l)):
                        if l[j].coord == i.coord:
                            l.pop(j)
                            break
                elif i.char == "▯":
                    c = c + 1
                elif i.type == "plock":
                    p = ""
                    for j in l:
                        if j.char == "▯": p = j.type
                    screen.erase()
                    screen.addstr(*(0, 0), "Type in a password.\n")
                    screen.refresh()
                    curses.echo()
                    screen.nodelay(False)
                    sleep(1)
                    for j in range(5):
                        if chr(screen.getch()) != p[j]:
                            p = "False"
                            break
                    if p != "False":
                        for j in range(len(l)):
                            if l[j].coord == i.coord:
                                l.pop(j)
                                break
                    curses.noecho()
                    screen.nodelay(True)
                elif i.type == "finish":
                    ln = ln + 1
                    pp = (1, 1)
                    l = call_level(ln)
                    if l == None: exit("\033[1m" + "You Won!" + "\033[0m")
            else: c = c + 1
        if c == len(l): pp = mpp
        for i in l:
            if pp == i.coord and i.char == "▯" and screen.getch() == curses.KEY_DOWN:
                screen.erase()
                screen.addstr(*(0, 0), "The password is " + i.type + ".")
                screen.refresh()
                sleep(1)
        if hc == 3: hc = 0
        else: hc = hc + 1
        screen.refresh()
        sleep(.2)
if __name__ == "__main__":
    curses.wrapper(main)