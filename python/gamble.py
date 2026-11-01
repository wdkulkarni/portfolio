from random import randint
from sys import exit

# A small casino with two games.

def roulette(c):
    b = int(input("Bet in ©s: "))
    while(b > c or b == 0):
        print("Can not bet this amount of money.")
        b = int(input("Bet in ©s: "))
    c = c - b
    n = int(input("Number: "))
    while(n == 0 or n > 30):
        print("Can not bet on this number.")
        n = int(input("Number: "))
    rn = randint(1, 30)
    if n == rn:
        print("You Win!")
        c = c + (b * 2)
    else:
        print("You lost.")
        print("The number was ", end = str(rn))
        print(".")
    return c
def slot_machine(c):
    if c > 10:
        c = c - int(c / 5)
    else:
        if c > 5:
            c = c - 2
        else:
            c = c - 1
    n1 = randint(1, 9)
    n2 = randint(1, 9)
    n3 = randint(1, 9)
    if n1 == n2 and n2 == n3:
        c = c + (n1 * 9)
        print("All three matched!")
        return c
    if n1 == n2 or n1 == n3 or n2 == n3:
        c = c + int((n1 + n2 + n3) / 3)
        print("Two matched!")
    else:
        print("You lost.")
    return c
c = 5
r = 0
while(True):
    print(c, end = "©\n")
    print("What would you like to play?")
    print("They are all fun.")
    print("Roulette? or Slot Machine?")
    g = input("Game choice: ")
    if g == "roulette" or g == "Roulette" or g == "r":
        c = roulette(c)
        r = r + 1
    if g == "Slot Machine" or g == "Slot machine" or g == "slot machine" or g == "sm":
        c = slot_machine(c)
        r = r + 1
    if c <= 0:
        print("No more money. You went for ", end = str(r))
        exit(" rounds.")