from operator import contains
from random import shuffle, randint
import numpy as np
import json


def separateNounsFromGenders():
    words = []
    genders = []
    with open("./nouns.csv", "r", encoding="utf-8") as f:
        file = f.readlines()
    shuffle(file)
    for i in file:
        splitLine = i.split(",")
        if (splitLine[1] == ""):
            continue
        if (splitLine[1] == "\n"):
            continue
        word = splitLine[0].lower()
        
        genderArr = splitLine[1]
        if (contains(genderArr, "[") == False):
            continue
        gender = None
        if (contains(genderArr, "masculine")):
            gender = [1, 0, 0]
        elif (contains(genderArr, "feminine")):
            gender = [0, 1, 0]
            randomInt = randint(1,100)
            if((randomInt <= 18.2486865) == False):
                continue
        elif (contains(genderArr, "plural")):
            gender = [0, 0, 1]
            randomInt = randint(1,100)
            if((randomInt <= 1.18819558) == False):
                continue
        if (gender == None):
            continue
        words.append(word)
        genders.append(gender)
    return words, genders




def genTrainingData(inpNouns, inpGenders):
    inpNouns = [str(i).lower() for i in inpNouns]
    inpNounsAsArrOfInts = []
    for i in inpNouns:
        dataToAppend = []
        for x in i:
            dataToAppend.append(ord(x))
        arrLen = len(dataToAppend)
        while arrLen < 72:
            dataToAppend.append(0)
            arrLen += 1
        inpNounsAsArrOfInts.append(dataToAppend)
    x_train = np.array(inpNounsAsArrOfInts)
    y_train = np.array(inpGenders)
    return x_train, y_train
