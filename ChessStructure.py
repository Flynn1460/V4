import chess as ch, pygame as pg, time
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
text = pf.loadScoreText(font, [0, 0, 0])

results = [0, 0, 0]

currentMoveList = []

pf.updateVars((x,y))


def playervsplayerPlay(board):
    colour = True
    
    while not pf.isGameEnd(board):
        board = playerMove(board)
        
        colour = not colour
        pf.load(dis, board, size)

def playervscomputerPlay(board):
    colour, ogColour, depth = False, False, 4

    while not pf.isGameEnd(board):
        if ogColour != colour:
            board = engineMove(board, colour, depth)
        else:
            board = playerMove(board)

        colour = not colour

        pf.load(dis, board, size)

def computervscomputerPlay(board):
    colour, depth = True, 4

    while not pf.isGameEnd(board):
        board = engineMove(board, colour, depth)
        
        colour = not colour
        
        pf.loadEvents()
        pf.load(dis, board, size)

def gamemodeSelect(gamemode):
    if gamemode == "singleplayer":
        return playervscomputerPlay(board)

    elif gamemode == "multiplayer":
        return playervsplayerPlay(board)

    elif gamemode == "computer":
        return computervscomputerPlay(board)


def playerMove(board):
    global currentMoveList
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
                startHover = pf.getBoardHover(event.pos)
                atSquare = pf.pieceAtSquare(coordBoard, startHover)


            if event.type == pg.MOUSEBUTTONUP:
                lastAction, atSquare = "UP", "."

                # Get which square the mouse is hovered over
                boardHover = pf.getBoardHover(event.pos)

                # Actions may crash indicating an illegal player move
                try:
                    # Turn the coordinates into a move vector
                    move = of.coordsToString(startHover, boardHover)

                    # Push the move onto the board
                    currentMoveList.append(of.convertUCItoNotation(board, move))
                    board.push_san(move)

                    return board
                except:
                    continue

        # If a piece was lifted or the move was denied so the board stayed the same. Don't load a board overlay
        if lastAction == "UP" and startingBoard == board:
            pf.load(dis, board, size)
        else:
            pf.load(dis, board, size, dragItems=(atSquare, startHover))

def engineMove(board, colour, depth):
    global currentMoveList
    engineMove = en.giveBestMove(board, colour, currentMoveList)

    currentMoveList.append(engineMove)
    board.push_san(engineMove)

    time.sleep(0.3)

    return board


pf.loadImages()
gamemode = "singleplayer"

while True:
    # Reset Variables
    board, currentMoveList = ch.Board(), []
    
    # Refesh Everything
    pf.initScreen(dis, text)

    # Play the game
    gamemodeSelect(gamemode)

    # Update Score Text
    results = of.getOutcome(board.outcome(), results)
    text = pf.loadScoreText(font, results)

