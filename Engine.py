import chess, random

def giveBestMove(board):
    return random.choice(list(board.legal_moves))