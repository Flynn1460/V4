import chess as ch
import pygame as pg

import Engine as en
import otherFunctions as of
import playFunctions as pf

dis = pg.display.set_mode((900, 600), pg.RESIZABLE)
board = ch.Board()

size = pg.display.get_surface()
x, y = size.get_width(), size.get_height()

whiteScore, blackScore, results = 0, 0, [0, 0, 0]
noPrint = False

def playerPlay(board):
    global noPrint, colour, depth
    if not noPrint:
        colour = "w"#of.opt("Which colour do you want to play?", "w", "b")
        depth = 4#of.opt("What depth should the computer search to? (rec 4)", "int")
        pf.playerData()
    
    ogColour = of.copyVar(colour, "w", "b")

    while True:
        if ogColour != colour:
            board.push(engineMove(board, colour, depth))
        else:
            board = playerMove(board)

        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        colour = of.flipColour(colour)

        pf.load(dis, board, size)
        pf.loadEvents()

def computerPlay(board):
    global noPrint, depth
    colour = "w"
    if not noPrint:
        depth = 4#of.opt("What depth should the computer search to? (rec 4)", "int")
        pf.depthData()

    while True:
        board.push(engineMove(board, colour, depth))

        if pf.isGameEnd(board):
            return pf.isGameEnd(board)
        
        colour = of.flipColour(colour)
        
        pf.load(dis, board, size)
        pf.loadEvents()


def playerMove(board):
    atSquare, startCoords, boardHover = ".", [-1, -1], False
    lastAction = None

    startingBoard = board


    while True:
        try:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    lastAction = "DOWN"
                    if event.pos[0] < x//3:
                        continue

                    boardHover = pf.getBoardHover(event.pos, (x, y))
                    coordBoard = of.make_matrix(board)
                    atSquare = coordBoard[boardHover[1]][boardHover[0]]

                    if atSquare == ".":
                        continue

                    startCoords = boardHover


                if event.type == pg.MOUSEBUTTONUP:
                    lastAction = "UP"
                    atSquare = "."
                    if event.pos[0] < x//3:
                        continue

                    boardHover = pf.getBoardHover(event.pos, (x, y))
                    coordBoard = of.make_matrix(board)

                    move = of.coordsToString((startCoords[0], startCoords[1]), (boardHover[0], boardHover[1]))
                    board.push_san(move)

                    return board

            # If a piece was lifted or the move was denied so the board stayed the same. Don't load a board overlay
            if lastAction == "UP" and startingBoard == board:
                pf.load(dis, board, size)

            else:
                pf.load(dis, board, size, atSquare=atSquare, pieceEraseCoords=startCoords)

           


        except ValueError:
            continue

def engineMove(board, colour, depth):
    return en.giveBestMove(board)


pf.loadImages(100)
pf.resizeImages(y)
pf.load(dis, board, size)

gamemode = "player"#of.opt("What gamemode do you want to play?", "player", "computer")
autoplay = True#bool(of.opt("Do you want the games to autoplay?", "yes", "no"))
pf.startData()


while True:
    board = ch.Board()

    size = pg.display.get_surface()
    x, y = size.get_width(), size.get_height()

    pf.resizeImages(y)
    pf.load(dis, board, size)


    if gamemode == "player":
        val = playerPlay(board)

    elif gamemode == "computer":
        val = computerPlay(board)

    results, whiteScore, blackScore = of.getOutcome(board.outcome(), results, whiteScore, blackScore)
    noPrint = autoplay

    print(str(whiteScore)+" - "+str(blackScore)+" | "+"Draws: "+str(results[0])+", "+"White Wins: "+str(results[1])+", "+"Black Wins: "+str(results[2])+"\n")
