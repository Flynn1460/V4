import otherFunctions as of
import playFunctions as pf

def playerPlay():
    colour = of.opt("Which colour do you want to play?", "w", "b")
    depth = of.opt("What depth should the computer search to? (rec 4)", "int")
    if colour == "w":
        playerMove(colour)
    
    playerGameLoop(colour)
    return

def computerPlay():
    pass


def playerGameLoop(colour):
    colourFlipped = of.flipColour(colour)
    while True:
        engineMove(colourFlipped)
        
        if pf.isGameEnd():
            return

        playerMove(colour)

        if pf.isGameEnd():
            return
        
        continue

def computerGameLoop():
    pass


def playerMove(colour):
    pass

def engineMove(colour):
    pass



while True:
    gamemode = of.opt("What gamemode do you want to play?", "player", "computer")

    if gamemode == "player":
        playerPlay()
    elif gamemode == "computer":
        computerPlay()

    playAgain = of.opt("Play again?", "yes", "no")

    if playAgain == "yes":
        continue
    elif playAgain == "no":
        quit()