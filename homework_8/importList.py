from random import randrange as rn
# Генератор имен
returnList = []
# Импортирует txt


def createList(pathFile):
    returnList = []
    with open(pathFile, 'r', encoding='UTF-8') as file:
        allFile = file.readlines()
        for el in allFile:
            if len(returnList) < len(allFile)-1:
                returnList.append(el[:len(el)-1])
            else:
                returnList.append(el)
    return returnList
