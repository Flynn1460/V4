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


def loadImages(SQUARE_SIZE, size):
    global images, backgroundImage
    images = []

    backgroundImage = pg.image.load("Images/background.png")
    backgroundImage = pg.transform.scale(backgroundImage, (size.get_width(), size.get_height()))

    for pColor in ["w", "b"]:
        for pType in ["P", "N", "B", "R", "Q", "K"]:
            images.append(pg.image.load("Images/"+pColor+pType+".png"))

def resizeImages(SQUARE_SIZE, size):
    global imagesDict, backgroundImage
    imagesDict = {}

    backgroundImage = pg.transform.scale(backgroundImage, (size[0], size[1]))

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
    board = of.boardify_fen(board)

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            try:
                dis.blit(imagesDict[piece], ((y * SQ_SZ) + (coords[0]//3), x * SQ_SZ, SQ_SZ, SQ_SZ))
            
            except:
                pass

def load(dis, board, size, dragItems=(False, False), sideText=False):
    x, y = size.get_width(), size.get_height()
    SQ_SZ = (x - x//3)//8

    dis.blit(backgroundImage, (0, 0))

    drawBoard(dis, (x, y))

    drawImages(dis, board, (x, y))
    resizeImages(SQ_SZ, (x, y))

    if dragItems[0]:
        redoSquare(dis, (x, y), dragItems[1])
        carryPiece(dis, dragItems[0], SQ_SZ)

    if sideText:
        for i in range(len(sideText)):
            dis.blit(sideText[i], pg.Rect(10, 10+(i*40), x//3, 40))

    
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

def pieceAtSquare(board, coords):
    return board[coords[1]][coords[0]]

def loadScoreText(font, results):
    whiteScore, blackScore = (results[0]/2) + results[1], (results[0]/2) + results[2]


    textLines = ["Score : "+str(whiteScore)+" - "+str(blackScore), "Draws: "+str(results[0]), "White Wins: "+str(results[1]),   "Black Wins: "+str(results[2])]

    text = []
    for i in range(len(textLines)):
        text.append(font.render(textLines[i], True, (200, 200, 200)))

    return text