import numpy as np


def genValidationData(inpStrs=["Vater", "Mutter", "Uhr", "Opa", "Käse"], inpGenders=[[1, 0, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0]]):
    print(inpStrs)
    inpStrs = [str(i).lower() for i in inpStrs]
    inpStrArr = []
    for i in inpStrs:
        dataToAppend = []
        for x in i:
            dataToAppend.append(ord(x))
        inpStrArr.append(dataToAppend)
    while len(inpStrArr) < 72:
        inpStrArr.append(0)
    inpStrNumpyArr = np.array(inpStrArr)
    x_train = inpStrNumpyArr
    y_train = np.array(inpGenders)
    return x_train, y_train
