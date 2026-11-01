"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty = actions(board)
    if len(empty) % 2 == 0: return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY: empty.append((i, j))
    return empty


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    acs = actions(board)
    for i in acs:
        if i == action:
            acs = False
            break
    if acs != False or action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0: raise ValueError("Action cannot be executed on board.")
    cboard = copy.deepcopy(board)
    cboard[action[0]][action[1]] = player(cboard)
    return cboard

def calc_win(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != EMPTY:
                win = False
                if i == 0:
                    if board[i][j] == board[i + 1][j] == board[i + 2][j]: win = True
                if j == 0:
                    if board[i][j] == board[i][j + 1] == board[i][j + 2]: win = True
                if i == 0 and j == 0:
                    if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2]: win = True
                elif i == 2 and j == 0:
                    if board[i][j] == board[i - 1][j + 1] == board[i - 2][j + 2]: win = True
                if win == True:
                    if board[i][j] == X: return X
                    return O
    if len(actions(board)) == 0: return None
    return "Not Ended"

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = calc_win(board)
    if win == "Not Ended": return None
    return win

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if calc_win(board) != "Not Ended": return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X: return 1
    elif win == O: return -1
    else: return 0

def unended_utility(board):
    autility = []
    for action in actions(board):
        nboard = result(board, action)
        if terminal(nboard): autility.append([utility(nboard), action])
        else: autility.append(unended_utility(nboard))
    index = 0
    if player(nboard) == X:
        max = -2
        for i in range(len(autility)):
            if autility[i][0] > max:
                max = autility[i][0]
                index = i
    else:
        min = 2
        for i in range(len(autility)):
            if autility[i][0] < min:
                min = autility[i][0]
                index = i
    return autility[index]

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    _, acn = unended_utility(board)
    return acn