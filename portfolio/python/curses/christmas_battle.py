import curses
from time import sleep
from random import randint
from sys import exit

class Character:
    def __init__(self, name, power, health, display, attack, coord, gravity):
        self.name, self.power, self.health, self.display, self.attack, self.coord, self.gravity = name, power, health, display, attack, coord, gravity
        self.cooldown = 0
    def __str__(self):
        return f"{self.name}\n{self.name} uses {self.power} to attack enemies."

def load_content(screen, time, coord, str):
    screen.erase()
    screen.addstr(*coord, str)
    screen.refresh()
    sleep(time)

def attack(screen, a, v, r):
    if a.cooldown == 0:
        if a.coord[0] == v.coord[0]: va = [1]
        elif a.coord[1] == v.coord[1]: va = [0]
        else: return v.health
        if abs(a.coord[va[0]] - v.coord[va[0]]) > r: return v.health
        if a.coord[va[0]] - v.coord[va[0]] < 0:
            if va[0] == 1: va.append((0, 1))
            else: va.append((1, 0))
        elif a.coord[va[0]] - v.coord[va[0]] > 0:
            if va[0] == 1: va.append((0, -1))
            else: va.append((-1, 0))
        else: return v.health - 5
        co = tuple(map(sum, zip(a.coord, va[1])))
        for i in range(abs(a.coord[va[0]] - v.coord[va[0]]) - 1):
            screen.addstr(*co, a.attack)
            screen.refresh()
            co = tuple(map(sum, zip(co, va[1])))
            sleep(.2)
        a.cooldown = 100
        return v.health - 5
    return v.health

def gravity(ce):
    if ce.gravity[1] == True:
        if ce.gravity[0] == 0:
            ce.coord, ce.gravity = tuple(map(sum, zip(ce.coord, (2, 0)))), [7, False]
        else: ce.gravity[0] = ce.gravity[0] - 1
    return ce

def controls(screen, i, p, o, r):
    if i == curses.KEY_UP:
        if p.gravity[1] == False: p.coord, p.gravity[1] = tuple(map(sum, zip(p.coord, (-2, 0)))), True
    if i == curses.KEY_LEFT: p.coord = tuple(map(sum, zip(p.coord, (0, -1))))
    if i == curses.KEY_RIGHT: p.coord = tuple(map(sum, zip(p.coord, (0, 1))))
    if i == ord("p"):
        while screen.getch() != ord("u"): load_content(screen, .1, (int(curses.LINES / 2), int(curses.COLS / 2) - 13), "PAUSED (u to unpause)")
    if i == ord("z"): o.health = attack(screen, p, o, r)
    return p, o

def main(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    curses.mousemask(True)
    load_content(screen, 0, (0, 0), '''Christmas Killer\nBy: Vyoma Kulkarni\nArrow Keys to move. "p" to pause. "u" to unpause. "z" to attack. Choose the settings and character that you want and try not to get hit while attacking your opponent. Click anywhere to move on. Good Luck!''')
    while True:
        if screen.getch() == curses.KEY_MOUSE: break
    load_content(screen, 0, (0, 0), "Starting Health:\n150\n100\n50")
    while True:
        if screen.getch() == curses.KEY_MOUSE:
            _, _, y, _, _ = curses.getmouse()
            if y == 1: h = 150
            elif y == 3: h = 50
            else: h = 100
            break
    players = [Character("Santa", "Gift Blast", h, "O", "■", (3, 0), [7, False]), Character("Rudolph", "Nose Ray", h, "K", "→", (3, 0), [7, False]), Character("Elf", "Tool Throw", h, "I", "┌", (3, 0), [7, False]), Character("Mrs. Claus", "Love Shower", h, "P", "♥", (3, 0), [7, False])]
    load_content(screen, 0, (0, 0), "Difficulty Level:\nSuper Easy\nEasy\nMedium\nHard\nSuper Hard")
    while True:
        if screen.getch() == curses.KEY_MOUSE:
            _, _, y, _, _ = curses.getmouse()
            if y == 1: d = 13
            elif y == 2: d = 10
            elif y == 4: d = 5
            elif y == 5: d = 3
            else: d = 7
            break
    load_content(screen, 0, (0, 0), "Attacking Range:\nSmall\nMedium\nLarge")
    while True:
        if screen.getch() == curses.KEY_MOUSE:
            _, _, y, _, _ = curses.getmouse()
            if y == 1: r = 3
            elif y == 3: r = 7
            else: r = 5
            break
    load_content(screen, 0, (0, 0), "Choose Your Character:\nSanta\nRudolph\nElf\nMrs. Claus")
    while True:
        if screen.getch() == curses.KEY_MOUSE:
            _, _, y, _, _ = curses.getmouse()
            p = y - 1
            load_content(screen, 5, (0, 0), "You are " + players[p].__str__())
            o = randint(0, 3)
            while o == p: o = randint(0, 3)
            break
    load_content(screen, 5, (0, 0), "Your opponent is " + players[o].__str__())
    players[o].coord, oc = (3, 10), 0
    while True:
        screen.erase()
        screen.addstr(*players[p].coord, players[p].display)
        screen.addstr(*players[o].coord, players[o].display)
        try: players[p], players[o] = controls(screen, screen.getch(), players[p], players[o], r)
        except: ...
        if oc == d: players[p].health = attack(screen, players[o], players[p], r)
        if oc % 2 == 0:
            ri = randint(1, 3)
            if ri == 1: players[o].coord = tuple(map(sum, zip(players[o].coord, (0, -1))))
            elif ri == 2: players[o].coord = tuple(map(sum, zip(players[o].coord, (0, 1))))
            else:
                if players[o].gravity[1] == False: players[o].coord, players[o].gravity[1] = tuple(map(sum, zip(players[o].coord, (-2, 0)))), True
        c = [players[p].coord, players[o].coord]
        for i in range(2):
            if c[i][0] == -1: c[i] = tuple(map(sum, zip(c[i], (1, 0))))
            elif c[i][0] == curses.LINES: c[i] = tuple(map(sum, zip(c[i], (-1, 0))))
            elif c[i][1] == -1: c[i] = tuple(map(sum, zip(c[i], (0, 1))))
            elif c[i][1] == curses.COLS: c[i] = tuple(map(sum, zip(c[i], (0, -1))))
        players[p].coord, players[o].coord = c[0], c[1]
        if players[p].health <= 0: exit("\033[1;38;5;196m" + "You Lose" + "\033[0m")
        elif players[o].health <= 0: exit("\033[1;38;5;46m" + "You Win" + "\033[0m")
        if oc == d: oc = 0
        else: oc = oc + 1
        players[p], players[o] = gravity(players[p]), gravity(players[o])
        for i in players:
            i.cooldown -= 1
            if i.cooldown < 0:
                i.cooldown = 0
        screen.refresh()
        sleep(.1)

if __name__ == '__main__': curses.wrapper(main)