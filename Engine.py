import chess as ch, random, playFunctions as pf, time

pieces = {
    None : "0",
    ch.KING : "0",
    ch.PAWN : "1",
    ch.BISHOP : "3",
    ch.KNIGHT : "3",
    ch.ROOK : "5",
    ch.QUEEN : "9"
}

def changeValueFromPiece(board, square, playerColour):
    pieceColour = str(board.piece_at(square)).isupper()

    pieceRelation = pieceColour ^ playerColour

    if pieceRelation:
        return int(pieces[board.piece_type_at(square)])
    else:
        return int(pieces[board.piece_type_at(square)]) * -1

def cutLegalMoves(legalMoves):
    legalMoves = str(legalMoves)[38:-2]
    legalMoves = legalMoves.split(', ')

    return legalMoves

def evaluatePosition(board, colour):
    pieceValue = 0
    for i in range(64):
        pieceValue += changeValueFromPiece(board, i, True)

    return pieceValue



# Min Max Algorithm      
def engine(board, isComputerWhite):
    # Get a list of the legal moves
    positionMovesList = cutLegalMoves(board.legal_moves)
    bestMoveAmount, bestMoves = -999, []

    # Play the board in that position
    for move in positionMovesList:
        board.push_san(move)

        # Evaluate the new position
        positionEvaluation = evaluatePosition(board, isComputerWhite)

        print(positionEvaluation,"\n", board, "\n")

        if positionEvaluation > bestMoveAmount:
            bestMoves, bestMoveAmount = [move], positionEvaluation
        
        elif positionEvaluation == bestMoveAmount:
            bestMoves.append(move)

        board.pop()


    print(bestMoveAmount, bestMoves)
    
    return random.choice(bestMoves)



def giveBestMove(board, colour):
    return engine(board, colour)


