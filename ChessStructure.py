import chess as ch
import pygame as pg

import Engine as en
import otherFunctions as of
import playFunctions as pf


def playerPlay(board):
    global noPrint, depth

    if not noPrint:
        colour = of.opt("Which colour do you want to play?", "w", "b")
        depth = of.opt("What depth should the computer search to? (rec 4)", "int")

    if colour == "w":
        board = playerMove(board)

    while True:
        board = engineMove(board, colour, depth)

        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        pf.load(dis, board, of.SQ_COLOR_WHITE, of.SQ_COLOR_BLACK)


        board = playerMove(board)

        if pf.isGameEnd(board):
            return pf.isGameEnd(board)

        pf.load(dis, board, of.SQ_COLOR_WHITE, of.SQ_COLOR_BLACK)

def computerPlay(board):
    global noPrint, depth

    if not noPrint:
        depth = of.opt("What depth should the computer search to? (rec 4)", "int")

    while True:
        board = engineMove(board, "w", depth)

        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        pf.load(dis, board, of.SQ_COLOR_WHITE, of.SQ_COLOR_BLACK)

        board = engineMove(board, "b", depth)

        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        pf.load(dis, board, of.SQ_COLOR_WHITE, of.SQ_COLOR_BLACK)


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


dis = pg.display.set_mode((800, 800))
pf.loadImages(100)

gamemode = of.opt("What gamemode do you want to play?", "player", "computer")
autoplay = bool(of.opt("Do you want the games to autoplay?", "yes", "no"))

whiteScore, blackScore, results = 0, 0, [0, 0, 0]
noPrint = False


while True:
    board = ch.Board()
    pf.load(dis, board, of.SQ_COLOR_WHITE, of.SQ_COLOR_BLACK)

    if gamemode == "player":
        val = playerPlay(board)

    elif gamemode == "computer":
        val = computerPlay(board)

    results, whiteScore, blackScore = of.getOutcome(board.outcome(), results, whiteScore, blackScore)
    noPrint = autoplay

    print(str(whiteScore)+" - "+str(blackScore)+" | "+"Draws: "+str(results[0])+", "+"White Wins: "+str(results[1])+", "+"Black Wins: "+str(results[2])+"\n")
