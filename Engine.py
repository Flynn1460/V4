import chess, random

def giveBestMove(board):
    board.push(random.choice(list(board.legal_moves)))
    return board