"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    cnt = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                cnt += 1
    if cnt == 0:
        return None
    return 'X' if cnt % 2 == 1 else 'O'


def actions(board):
    action = []
    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == EMPTY:
                action.append((row_index, col_index))
    return action


def result(board, action):
    if 0 <= action[0] <= 2 and 0 <= action[1] <= 2 and board[action[0]][action[1]] == EMPTY:
        board_copy = deepcopy(board)
        board_copy[action[0]][action[1]] = player(board)
        return board_copy
    else:
        raise ValueError('Invalid action')

def winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    if winner(board) != None:
        return True
    
    cnt = sum(row.count(EMPTY) for row in board)
    
    return True if cnt == 0 else False


def utility(board):
    winning_player = winner(board)
    if winning_player == 'X':
        return 1
    elif winning_player == 'O':
        return -1
    return 0

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def minimax(board):
    if terminal(board):
        return None
    
    best_action = None
    alpha, beta = float('-inf'), float('inf')

    if player(board) == 'X': # maximizing player
        best_value = float('-inf')
        for action in actions(board):
            tmp = min_value(result(board, action), alpha, beta)

            if tmp > best_value:
                best_value = tmp
                best_action = action
            
            alpha = max(alpha, best_value)
    else: # minimizing player
        best_value = float('inf')
        for action in actions(board):
            tmp = max_value(result(board, action), alpha, beta)

            if tmp < best_value:
                best_value = tmp
                best_action = action

            beta = min(beta, best_value)

    return best_action
