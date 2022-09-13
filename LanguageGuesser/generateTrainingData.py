import numpy as np
import random
import json

def genTrainingData(inpStrs, language):
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
    y_train = np.array(language)
    return x_train, y_train


def getWordsandLanguage():
    words = []
    genders = []
    with open("./english.json", "r", encoding="utf-8") as f:
        englishWords = json.loads(f.read())
    englishWords = [str(i).lower() for i in englishWords]
    with open("./french.json", "r", encoding="utf-8") as f:
        frenchWords = json.loads(f.read())
    frenchWords = [str(i).lower() for i in frenchWords]
    with open("./spanish.json", "r", encoding="utf-8") as f:
        spanishWords = json.loads(f.read())
    spanishWords = [str(i).lower() for i in spanishWords]
    words = englishWords + frenchWords + spanishWords
    wordLanguages = [[1,0,0] for i in range(len(englishWords))] + [[0,1,0] for i in range(len(frenchWords))] + [[0,0,1] for i in range(len(spanishWords))]
    joined_arrs = list(zip(words, wordLanguages))
    random.shuffle(joined_arrs)
    shuffledWords, shuffledWordLanguages = zip(*joined_arrs)
    # random.shuffle(englishWords)
    # for i in englishWords:
    #     x = i.split("{")

    #     gender = None
    #     if (x[1][0] == "m"):
    #         gender = [1, 0, 0]
    #     if (x[1][0] == "f"):
    #         gender = [0, 1, 0]
    #     if (x[1][0] == "n"):
    #         gender = [0, 0, 1]
    #     word = x[0].replace(" ", "")
    #     words.append(word)
    #     genders.append(gender)
    return shuffledWords, shuffledWordLanguages
