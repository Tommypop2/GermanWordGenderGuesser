def convertStrToArr(string):
    string = str(string)
    data = []
    for i in string:
        data.append(ord(i))
    dataLen = len(data)
    while dataLen < 72:
        data.append(0)
        dataLen += 1
    return data
