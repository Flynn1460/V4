import chess as ch
import pygame as pg
import otherFunctions as of

def isGameEnd(board):
    if board.is_checkmate():
        return True, "Mate"
    
    elif board.is_fivefold_repetition():
        return True, "Mate"
    
    elif board.is_stalemate():
        return True, "Stalemate"
    
    elif board.is_insufficient_material():
        return True, "Insufficient Material"
    
    else:
        return False

def drawBoard(dis, SQ_COLOR_WHITE, SQ_COLOR_BLACK,  SQUARE_SIZE):

    # Board Color (0 = White, 1 = Black)
    CURRENT_VAL = 1

    # Colors for computer to refer to
    SQUARE_COLOR_LIST = [SQ_COLOR_WHITE, SQ_COLOR_BLACK]

    # The color of the board square
    CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]

    for boardWidth in range(8):

        # Set the starting row color
        CURRENT_VAL = CURRENT_VAL^1
        CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]


        for boardHeight in range(8):

            # Draw the square
            pg.draw.rect(dis, CURRENT_COLOR, (SQUARE_SIZE*boardWidth, SQUARE_SIZE*boardHeight, SQUARE_SIZE, SQUARE_SIZE))

            # Flip the square color
            CURRENT_VAL = CURRENT_VAL^1
            CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]

def loadImages(SQUARE_SIZE):
    global imagesDict
    imagesDict = {}

    for pColor in ["w", "b"]:
        for pType in ["P", "N", "B", "R", "Q", "K"]:

            if pColor == "w":
                imagesDict[pType] = pg.transform.scale(pg.image.load("Images/"+pColor+pType+".png"), (SQUARE_SIZE, SQUARE_SIZE))
            elif pColor == "b":
                imagesDict[pType.lower()] = pg.transform.scale(pg.image.load("Images/"+pColor+pType+".png"), (SQUARE_SIZE, SQUARE_SIZE))

def drawImages(dis, board):
    board = of.make_matrix(board)

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            try:
                dis.blit(imagesDict[piece], pg.Rect(y * 100, x * 100, 100, 100))
            
            except:
                pass

def load(dis, board, color_white, color_black):
    drawBoard(dis, color_white, color_black, 100)
    drawImages(dis, board)
    pg.display.update()
