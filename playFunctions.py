import chess as ch, pygame as pg
import otherFunctions as of

def initScreen(dis, text):
    dis.blit(backgroundImage, (0, 0))

    for i in range(len(text)):
        dis.blit(text[i], pg.Rect(10, 10+(i*40), sideWidth, 40))

    pg.display.update()

def updateVars(dimentions):
    global SQ_SZ, width, height, sideWidth, sideHeight

    width, height = dimentions[0], dimentions[1]

    sideWidth, sideHeight = width-height, height

    dimentions = [of.fraction(2, 3, dimentions[0])  ,  dimentions[1]]

    smCoord = of.smOf(dimentions[0], dimentions[1])
    SQ_SZ = smCoord//8

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


def drawImages(dis, board):
    board = of.boardify_fen(board)

    for x in range(8):
        for y in range(8):
            piece = board[x][y]
            try:
                dis.blit(imagesDict[piece], ((y * SQ_SZ) + (sideWidth), x * SQ_SZ, SQ_SZ, SQ_SZ))
            
            except:
                pass

def loadImages():
    global images, backgroundImage
    images = []

    backgroundImage = pg.image.load("Images/background.png")
    backgroundImage = pg.transform.scale(backgroundImage, (width, height))

    for pColor in ["w", "b"]:
        for pType in ["P", "N", "B", "R", "Q", "K"]:
            images.append(pg.image.load("Images/"+pColor+pType+".png"))

def resizeImages():
    global imagesDict, backgroundImage
    imagesDict = {}

    backgroundImage = pg.transform.scale(backgroundImage, (width, height))

    i = -1
    for pColor in ["w", "b"]:
        for pType in ["P", "N", "B", "R", "Q", "K"]:
            i += 1

            if pColor == "w":
                imagesDict[pType] = pg.transform.scale(images[i], (SQ_SZ, SQ_SZ))
            elif pColor == "b":
                imagesDict[pType.lower()] = pg.transform.scale(images[i], (SQ_SZ, SQ_SZ))


def drawBoard(dis):
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
            pg.draw.rect(dis, CURRENT_COLOR, ((y * SQ_SZ) + (sideWidth), x * SQ_SZ, SQ_SZ, SQ_SZ))

            # Flip the square color
            CURRENT_VAL = CURRENT_VAL^1
            CURRENT_COLOR = SQUARE_COLOR_LIST[CURRENT_VAL]

def redoSquare(dis, startCoords):
    squareFill = of.colourBin(startCoords)
    pg.draw.rect(dis, squareFill, ((startCoords[0] * SQ_SZ) + (sideWidth), startCoords[1] * SQ_SZ, SQ_SZ, SQ_SZ))


def load(dis, board, size, dragItems=(False, False)):
    dis.blit(backgroundImage, (0, 0))
    x, y = size.get_width(), size.get_height()
    updateVars((x, y))

    drawBoard(dis)

    resizeImages()
    drawImages(dis, board)

    if dragItems[0]:
        redoSquare(dis, dragItems[1])
        carryPiece(dis, dragItems[0])
    
    pg.display.update(300, 0, width, height)

def loadEvents():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()


def getBoardHover(mousePos):
    mousePosition = [  (mousePos[0] - sideWidth) // SQ_SZ  ,  (mousePos[1]) // SQ_SZ  ]

    return mousePosition

def carryPiece(dis, piece):
    if piece != ".":
        mouseLocation = pg.mouse.get_pos()

        square_image = imagesDict[piece]

        dis.blit(square_image, (mouseLocation[0]-(SQ_SZ//2), mouseLocation[1]-(SQ_SZ//2)))

def pieceAtSquare(board, coords):
    return board[coords[1]][coords[0]]

def loadScoreText(font, results):
    whiteScore, blackScore = (results[0]/2) + results[1], (results[0]/2) + results[2]


    textLines = ["Score : "+str(whiteScore)+" - "+str(blackScore), "Draws: "+str(results[0]), "White Wins: "+str(results[1]),   "Black Wins: "+str(results[2])]

    text = []
    for i in range(len(textLines)):
        text.append(font.render(textLines[i], True, (200, 200, 200)))

    return text

