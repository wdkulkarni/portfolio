import curses
from time import sleep
from sys import exit
from random import randint

def main(screen):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    screen.nodelay(True)
    ds = {curses.KEY_UP: (-1, 0), curses.KEY_DOWN: (1, 0), curses.KEY_LEFT: (0, -1), curses.KEY_RIGHT: (0, 1)}
    d = ds[curses.KEY_RIGHT]
    mn = 1
    s = []
    mco = (randint(0, curses.LINES - 1), (randint(0, curses.COLS - 1)))
    mc = 0
    for i in reversed(range(20 * (int(int(100 * ((curses.LINES * curses.COLS) / 700)) / 100)))):
        s.append((0, i))
    while True:
        screen.erase()
        screen.addstr(*mco, "m")
        if (int(mn * 100) / 100).is_integer():
            for i in range(int(mn)):
                mco = (randint(0, curses.LINES - 1), (randint(0, curses.COLS - 1)))
        mn = mn + ((curses.LINES * curses.COLS) / 500)
        if s[0] == mco:
            mc = mc + 1
            for i in range(int(int(100 * ((curses.LINES * curses.COLS) / 700)) / 100)):
                s.insert(0, tuple(map(sum, zip(s[0], d))))
        for i in range(len(s)):
            if i != 0:
                if s[i] == s[0]:
                    exit("\033[1m" + "Game Over\n" + "\033[0m" + "\033[38;5;34m" + "*********><" + "\033[0m" + "\nYou ate " + "\033[38;5;234m" + str(mc) + " mice." + "\033[0m")
        try:
            screen.addstr(*s[0], "@", curses.color_pair(1))
        except:
            if mc == 1: 
                exit("\033[1m" + "Game Over\n" + "\033[0m" + "\033[38;5;34m" + "*********><" + "\033[0m" + "\nYou ate " + "\033[38;5;234m" + str(mc) + " mouse." + "\033[0m")
            exit("\033[1m" + "Game Over\n" + "\033[0m" + "\033[38;5;34m" + "*********><" + "\033[0m" + "\nYou ate " + "\033[38;5;234m" + str(mc) + " mice." + "\033[0m")
        for segment in s[1:]:
            screen.addstr(*segment, '*', curses.color_pair(1))
        s.pop()
        s.insert(0, tuple(map(sum, zip(s[0], d))))
        d = ds.get(screen.getch(), d)
        screen.refresh()
        sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)