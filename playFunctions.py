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


def drawBoard(dis, coords):
    smCoord = of.smOf(coords[0], coords[1])

    SQ_SZ = smCoord//8
    # Board Color (0 = White, 1 = Black)
    CURRENT_VAL = 1

    # Colors for computer to refer to
    SQUARE_COLOR_LIST = [of.SQ_COLOR_WHITE, of.SQ_COLOR_BLACK]
    # The color of the board square
    CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]

    for x in range(8):

        # Set the starting row color
        CURRENT_VAL = CURRENT_VAL ^ 1
        CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]

        for y in range(8):

            # Draw the square
            pg.draw.rect(dis, CURRENT_COLOR, ((y * SQ_SZ) + (coords[0]//3), x * SQ_SZ, SQ_SZ, SQ_SZ))

            # Flip the square color
            CURRENT_VAL = CURRENT_VAL^1
            CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]

def redoSquare(dis, dims, startCoords):
    smCoord = of.smOf(dims[0], dims[1])
    SQ_SZ = smCoord//8

    squareFill = of.colourBin(startCoords)
    pg.draw.rect(dis, squareFill, ((startCoords[0] * SQ_SZ) + (dims[0]//3), startCoords[1] * SQ_SZ, SQ_SZ, SQ_SZ))


def drawImages(dis, board, coords):
    smCoord = of.smOf(coords[0], coords[1])
    
    SQ_SZ = smCoord//8
    board = of.make_matrix(board)

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            try:
                dis.blit(imagesDict[piece], ((y * SQ_SZ) + (coords[0]//3), x * SQ_SZ, SQ_SZ, SQ_SZ))
            
            except:
                pass

def load(dis, board, size, atSquare=False, pieceEraseCoords=False):
    x, y = size.get_width(), size.get_height()

    drawBoard(dis, (x, y))

    drawImages(dis, board, (x, y))

    if atSquare:
        redoSquare(dis, (x, y), pieceEraseCoords)
        carryPiece(dis, atSquare, 75)
    
    pg.display.update()


def startData():
    pass

def playerData():
    pass

def depthData():
    pass

def loadEvents():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()


def getBoardHover(mousePos, size):
    sq_sz = ((2*size[0]) // 3) // 8
    mousePosition = [  (mousePos[0] - size[0]//3) // sq_sz  ,  (mousePos[1]) // sq_sz  ]

    return mousePosition

def carryPiece(dis, piece, SQUARE_SIZE):
    if piece != ".":
        mouseLocation = pg.mouse.get_pos()

        square_image = imagesDict[piece]

        dis.blit(square_image, (mouseLocation[0]-(SQUARE_SIZE//2), mouseLocation[1]-(SQUARE_SIZE//2)))