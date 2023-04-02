from string import digits
import random

def createOpeningBook():
    file = open("Openings/PROCESSED_VIENNA.txt", "r")
    text = file.readlines()
    file.close()

    finalList = []
    for i in range(len(text)):
        listGame = (text[i].split("."))[1:]

        newList = []
        for move in listGame:
            splitMove = move.split()
            newList.append(splitMove[:-1][0])
            try:
                newList.append(splitMove[:-1][1])
            except:
                continue

        finalList.append(newList)

    return finalList


def searchOpeningBook(openingBookList, currentMoveList):
    if len(currentMoveList) == 0:
        selectedGame = random.choice(openingBookList)

        return selectedGame[0]

    for moveNumber in range(len(currentMoveList)):
        for openingGame in openingBookList:
            try:
                isInOpening = openingGame[moveNumber], currentMoveList[moveNumber]
            
            except:    
                return None