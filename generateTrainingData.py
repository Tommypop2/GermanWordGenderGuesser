import numpy as np
import random


def genTrainingData(inpStrs, inpGenders):
    inpStrs = [str(i).lower() for i in inpStrs]
    inpStrArr = []
    for i in inpStrs:
        dataToAppend = []
        for x in i:
            dataToAppend.append(ord(x))
        arrLen = len(dataToAppend)
        while arrLen < 72:
            dataToAppend.append(0)
            arrLen += 1
        inpStrArr.append(dataToAppend)

    inpStrNumpyArr = np.array(inpStrArr)
    x_train = inpStrNumpyArr
    y_train = np.array(inpGenders)
    return x_train, y_train


def separateNounsFromGenders():
    words = []
    genders = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        file = f.readlines()
        random.shuffle(file)
        for i in file:
            x = i.split("{")

            gender = None
            if (x[1][0] == "m"):
                gender = [1, 0, 0]
            if (x[1][0] == "f"):
                gender = [0, 1, 0]
            if (x[1][0] == "n"):
                gender = [0, 0, 1]
            word = x[0].replace(" ", "")
            words.append(word)
            genders.append(gender)
    return words, genders
