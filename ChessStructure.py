import chess as ch
import pygame as pg
pg.font.init()

import Engine as en
import otherFunctions as of
import playFunctions as pf

dis = pg.display.set_mode((900, 600), pg.RESIZABLE)

pg.mouse.set_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)
pg.display.set_caption("Chess Version 4 - by Flynn")

size = pg.display.get_surface()
x, y = size.get_width(), size.get_height()

font = pg.font.Font('Other/coconutFont.ttf', 20)

results = [0, 0, 0]
text = pf.loadScoreText(font, results)


def playervsplayerPlay(board):
    global colour, depth

    colour = "w"#of.opt("Which colour do you want to play?", "w", "b")
    depth = 4#of.opt("What depth should the computer search to? (rec 4)", "int")
    pf.playerData()
    
    ogColour = of.copyVar(colour, "w", "b")

    while True:
        board = playerMove(board)

        if pf.isGameEnd(board):
            return
        
        colour = of.flipColour(colour)

        pf.load(dis, board, size, sideText=text)
        pf.loadEvents()

def playervscomputerPlay(board):
    global colour, depth

    colour = "b"#of.opt("Which colour do you want to play?", "w", "b")
    depth = 4#of.opt("What depth should the computer search to? (rec 4)", "int")
    pf.playerData()
    
    ogColour = of.copyVar(colour, "w", "b")

    while True:
        if ogColour != colour:
            board.push_san(engineMove(board, colour, depth))
        else:
            board = playerMove(board)

        if pf.isGameEnd(board):
            return
        
        colour = of.flipColour(colour)

        pf.load(dis, board, size, sideText=text)
        pf.loadEvents()

def computervscomputerPlay(board):
    global depth
    colour = True

    depth = 4#of.opt("What depth should the computer search to? (rec 4)", "int")
    pf.depthData()

    while True:
        board.push(engineMove(board, colour, depth))

        if pf.isGameEnd(board):
            return
        
        colour = not colour
        
        pf.load(dis, board, size, sideText=text)
        pf.loadEvents()


def gamemodeSelect(gamemode):
    if gamemode == "singleplayer":
        return playervscomputerPlay(board)

    elif gamemode == "multiplayer":
        return playervsplayerPlay(board)

    elif gamemode == "computer":
        return computervscomputerPlay(board)


def playerMove(board):
    atSquare, startHover = None, [-1, -1]
    lastAction, startingBoard = None, board
    coordBoard = of.boardify_fen(board)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

            # If the mouse position is not withing the bounds of the board return.
            if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP:
                if event.pos[0] < x//3:
                    continue

            if event.type == pg.MOUSEBUTTONDOWN:
                lastAction = "DOWN"

                # Get which square the mouse is hovered over
                startHover = pf.getBoardHover(event.pos, (x, y))
                atSquare = pf.pieceAtSquare(coordBoard, startHover)

                if atSquare == ".":
                    continue

            if event.type == pg.MOUSEBUTTONUP:
                lastAction, atSquare = "UP", "."

                # Get which square the mouse is hovered over
                boardHover = pf.getBoardHover(event.pos, (x, y))
                move = of.coordsToString(startHover, boardHover)

                try:
                    board.push_san(move)
                except:
                    continue

                return board

        # If a piece was lifted or the move was denied so the board stayed the same. Don't load a board overlay
        if lastAction == "UP" and startingBoard == board:
            pf.load(dis, board, size, sideText=text)
        else:
            pf.load(dis, board, size, dragItems=(atSquare, startHover), sideText=text)

def engineMove(board, colour, depth):
    if colour == "w":
        colour = True
    elif colour == "b":
        colour = False

    return en.giveBestMove(board, colour)


pf.loadImages(100, size)
gamemode = "singleplayer"#of.opt("What gamemode do you want to play?", "player", "computer")

while True:
    # Reset Variables
    board = ch.Board()

    # Play the game
    gamemodeSelect(gamemode)

    # Update Score Text
    results = of.getOutcome(board.outcome(), results)
    text = pf.loadScoreText(font, results)
