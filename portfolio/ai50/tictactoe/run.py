from tictactoe import *

board = initial_state()
while not terminal(board):
    pboard = []
    for row in board:
        prow = []
        for spot in row:
            if spot == None: prow.append(" ")
            else: prow.append(spot)
        pboard.append(prow)
    for i in range(len(pboard)):
        for j in range(len(pboard[i])):
            print(pboard[i][j], end = "")
            if j != 2: print("|", end = "")
        print()
        if i != 2: print("=====")
    if player(board) == X:
        move = input("Move coordinates: ")
        try: move = move.split(", ")
        except: raise TypeError("Input should be formatted: y, x.")
        board = result(board, (int(move[0]), int(move[1])))
    else: board = result(board, minimax(board))
print(winner(board), "wins.")