from minesweeper import Minesweeper, MinesweeperAI

game = Minesweeper(height=10, width=10, mines=10)
ai = MinesweeperAI(height=10, width=10)
board = [[" " for i in range(game.width)] for i in range(game.height)]
while True:
    for i in range(game.height):
        print("--" * game.width + "-")
        for j in range(game.height):
            print(f"|{board[i][j]}", end="")
        print("|")
    print("--" * game.width + "-")
    move = ai.make_safe_move()
    if move == None:
        move = ai.make_random_move()
    if game.is_mine(move):
        print("You Lose.")
        break
    count = game.nearby_mines(move)
    ai.add_knowledge(move, count)
    board[move[0]][move[1]] = str(count)
    for mine in ai.mines:
        board[mine[0]][mine[1]] = "X"
    game.mines_found = ai.mines
    if game.won():
        print("You Win!")
        break