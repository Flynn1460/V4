import chess

SQ_COLOR_WHITE = (237, 214, 176)
SQ_COLOR_BLACK = (184, 135, 98)

def opt(question, *args):
    print()
    value = -100

    # A 2 choice question
    if len(args) == 2:
        while value != args[0] and value != args[1]:
            value = input(r"{} ({}, {}) : ".format(question, args[0], args[1]))
        
        return value

    # A positive int option
    elif len(args) == 1 and args[0] == "int":
        while not value > 0:
            try:
                value = int(input(r"{} : ".format(question)))

            except:
                continue
        
        return value

def flipColour(colour):
    if colour == "w":
        return "b"
    if colour == "b":
        return "w"
    else:
        return None


def boardify_fen(board): #type(board) == chess.Board()
    pgn = board.epd()
    foo = []  #Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = []  #This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo

def undo_matrix_move(move):
    move[0], move[1] = int(move[0]), int(move[1])
    
    return (move[1] * 8) + move[0]

def getOutcome(outcomeInfo, results):
    
    if outcomeInfo.result()[0:3] == "1/2":
        results[0] += 1
        return results

    elif outcomeInfo.result()[0] == "1":
        results[1] += 1
        return results
    
    elif outcomeInfo.result()[2] == "1":
        results[2] += 1
        return results
    
def copyVar(var, opt1, opt2):
    if var == opt1:
        return opt1
    elif var == opt2:
        return opt2

def smOf(var1, var2):
    if var1 > var2:
        return var2
    
    elif var1 < var2:
        return var1
    
    elif var1 == var2:
        return var1

    else:
        print(var1, var2)
        quit()

def coordsToString(start, end):
    letNumDict = {"0" : "a", "1" : "b", "2" : "c", "3" : "d", "4" : "e", "5" : "f", "6" : "g", "7" : "h"}
    reverseNums = {"1" : "8", "2" : "7", "3" : "6", "4" : "5", "5" : "4", "6" : "3", "7" : "2", "8" : "1"}

    startCoord = letNumDict[str(start[0])] + reverseNums[str(start[1]+1)]
    endCoord = letNumDict[str(end[0])] + reverseNums[str(end[1]+1)]

    move = (startCoord + endCoord)

    return move

def colourBin(coordinates):
    squareBinary = [bool(coordinates[0] % 2), bool(coordinates[1] % 2)]
    colour_bool = squareBinary[0] ^ squareBinary[1]

    if colour_bool:
        return SQ_COLOR_BLACK
    
    else:
        return SQ_COLOR_WHITE

