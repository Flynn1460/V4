import chess as ch
import pygame as pg
import time

import Engine as en
import otherFunctions as of
import playFunctions as pf

SQ_COLOR_WHITE = (237, 214, 176)
SQ_COLOR_BLACK = (184, 135, 98)


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
        
        pf.load(dis, board, SQ_COLOR_WHITE, SQ_COLOR_BLACK)

        board = playerMove(board)
        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        pf.load(dis, board, SQ_COLOR_WHITE, SQ_COLOR_BLACK)

def computerPlay(board):
    global noPrint, depth

    if not noPrint:
        depth = of.opt("What depth should the computer search to? (rec 4)", "int")

    while True:
        board = engineMove(board, "w", depth)
        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        pf.load(dis, board, SQ_COLOR_WHITE, SQ_COLOR_BLACK)

        board = engineMove(board, "b", depth)
        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        pf.load(dis, board, SQ_COLOR_WHITE, SQ_COLOR_BLACK)


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

noPrint = False
whiteScore, blackScore = 0, 0
results = [0, 0, 0]

while True:
    board = ch.Board()

    pf.load(dis, board, SQ_COLOR_WHITE, SQ_COLOR_BLACK)

    while True:
        if gamemode == "player":
            val = playerPlay(board)

        elif gamemode == "computer":
            val = computerPlay(board)

        
        break

    noPrint = autoplay

    outcomeInfo = board.outcome()
    resultCause = str(outcomeInfo.termination)

    if outcomeInfo.result()[0:3] == "1/2":
        whiteScore += 0.5
        blackScore += 0.5
        results[0] += 1

    elif outcomeInfo.result()[0] == "1":
        whiteScore += 1
        results[1] += 1
    
    elif outcomeInfo.result()[2] == "1":
        blackScore += 1
        results[2] += 1


    print(str(whiteScore) + " - " + str(blackScore) + "  |  " + "Draws : "  + str(results[0]) + ", " + "White Wins : " + str(results[1]) + ", " + "Black Wins : " + str(results[2]))
    print("\n")

    continue
