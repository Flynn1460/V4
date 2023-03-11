import chess as ch

def isGameEnd(board):
    if board.is_checkmate():
        return True
    
    elif board.is_fivefold_repetition():
        return True
    
    else:
        return False
