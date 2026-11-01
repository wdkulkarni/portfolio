import curses
from time import sleep
from random import randint
from sys import exit

def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    h = [" " for i in range(10)]
    for i in range(curses.COLS - 11):
        if randint(1, 10) == 7: h.append("A")
        else: h.append(" ")
    p = (curses.LINES - 1, 0)
    at = 0
    s = .5
    while(True):
        screen.erase()
        for i in range(curses.COLS - 1): screen.addstr(*(curses.LINES - 1, i), h[i], curses.color_pair(1))
        screen.addstr(*p, " ", curses.color_pair(2))
        if p == (curses.LINES - 1, 0) and h[0] == "A":
            exit("\033[1m" + "You lost.\n" + "\033[0m" + "You got a score of " + str(int((.5 - s) / .0001)) + ".")
        h.pop(0)
        if randint(1, 10) == 7: h.append("A")
        else: h.append(" ")
        if at > 0:
            at = at + 1
            if at == 4:
                at = 0
                p = (curses.LINES - 1, 0)
        if screen.getch() == curses.KEY_UP and at == 0:
            p = tuple(map(sum, zip(p, (-1, 0))))
            at = at + 1
        s = s - .0001
        screen.refresh()
        sleep(s)
if __name__ == "__main__":
    curses.wrapper(main)