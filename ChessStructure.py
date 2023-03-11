import chess as ch

import Engine as en
import otherFunctions as of
import playFunctions as pf


def playerPlay(board):
    colour = of.opt("Which colour do you want to play?", "w", "b")
    depth = of.opt("What depth should the computer search to? (rec 4)", "int")

    if colour == "w":
        board = playerMove(board)

    while True:
        board = engineMove(board, colour, depth)
        if pf.isGameEnd(board):
            return
        print("\n", board)

        board = playerMove(board)
        if pf.isGameEnd(board):
            return
        print("\n", board)

def computerPlay(board):
    
    depth = of.opt("What depth should the computer search to? (rec 4)", "int")

    while True:
        board = engineMove(board, "w", depth)
        if pf.isGameEnd(board):
            return
        print("\n", board)

        board = engineMove(board, "b", depth)
        if pf.isGameEnd(board):
            return
        print("\n", board)


def playerMove(board):
    while True:
        try:
            print("\nLegal Move List : " + str(board.legal_moves)[37:-1])

            move = input("Your move : ")
            board.push_san(move)
            return board

        except:
            continue

def engineMove(board, colour, depth):
    return en.giveBestMove(board)


board = ch.Board()

while True:
    gamemode = of.opt("What gamemode do you want to play?", "player", "computer")

    if gamemode == "player":
        playerPlay(board)
    elif gamemode == "computer":
        computerPlay(board)

    playAgain = of.opt("Play again?", "yes", "no")

    if playAgain == "yes":
        continue
    elif playAgain == "no":
        quit()