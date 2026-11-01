#Go here for more information. https://docs.python.org/3/howto/curses.html
#Go here for the key codes like curses.KEY_UP and other attributes: https://pubs.opengroup.org/onlinepubs/7908799/xcurses/curses.h.html

import time, curses

def main(screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) #Initializes a color pair with argument 2 as text color and argument 3 as background color.
    curses.curs_set(0) #Gets rid of the cursor.
    screen.nodelay(True) #So that the window does not stop after you call getch().
    directions = {
        curses.KEY_UP: (-1, 0),
        curses.KEY_DOWN: (1, 0),
        curses.KEY_LEFT: (0, -1),
        curses.KEY_RIGHT: (0, 1),
    } #Dict with the moving values in it.
    direction = directions[curses.KEY_RIGHT] #Sets the starting direction to right.
    snake = [(0, i) for i in reversed(range(20))] #Creates a list with coordinates with y as 0 and x as values decreasing from 20, which is the length of the snake.
    while(True):
        screen.erase() #Clears screen.
        screen.addstr(*snake[0], '@', curses.color_pair(1)) #Adds snake's head at coordinate (0, 20) with the color pair that was initialized at line 6.
        for segment in snake[1:]: #For each next coordinate in snake.
            screen.addstr(*segment, '*', curses.color_pair(1)) #Add snake body piece.
        snake.pop() #takes out the last segment in snake.
        snake.insert(0, tuple(map(sum, zip(snake[0], direction)))) #Adds the coordinates the snake's head will be at to the beggining of snake.
        direction = directions.get(screen.getch(), direction) #Changes the direction of movement to the direction that the user inputted.
        screen.refresh() #Refreshes the screen.
        time.sleep(0.1) #Sleeps for a while so that the snake does not move too fast.
if __name__ == '__main__':
    curses.wrapper(main)