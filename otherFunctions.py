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

def make_matrix(board): #type(board) == chess.Board()
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


