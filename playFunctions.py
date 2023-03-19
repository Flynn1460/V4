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


def loadImages(SQUARE_SIZE):
    global images
    images = []

    for pColor in ["w", "b"]:
        for pType in ["P", "N", "B", "R", "Q", "K"]:
            images.append(pg.image.load("Images/"+pColor+pType+".png"))

def resizeImages(SQUARE_SIZE):
    SQUARE_SIZE = SQUARE_SIZE//8
    global imagesDict
    imagesDict = {}

    i = -1
    for pColor in ["w", "b"]:
        for pType in ["P", "N", "B", "R", "Q", "K"]:
            i += 1

            if pColor == "w":
                imagesDict[pType] = pg.transform.scale(images[i], (SQUARE_SIZE, SQUARE_SIZE))
            elif pColor == "b":
                imagesDict[pType.lower()] = pg.transform.scale(images[i], (SQUARE_SIZE, SQUARE_SIZE))


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
            pg.draw.rect(dis, CURRENT_COLOR, ((SQUARE_SIZE*boardWidth)+400, SQUARE_SIZE*boardHeight, SQUARE_SIZE, SQUARE_SIZE))

            # Flip the square color
            CURRENT_VAL = CURRENT_VAL^1
            CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]

def drawImages(dis, board):
    board = of.make_matrix(board)

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            try:
                dis.blit(imagesDict[piece], pg.Rect((y * 100) + 400, x * 100, 100, 100))
            
            except:
                pass

def load(dis, board, color_white, color_black, height):
    drawBoard(dis, color_white, color_black, height//8)
    drawImages(dis, board)
    pg.display.update()


def startData():
    pass

def playerData():
    pass

def depthData():
    pass
