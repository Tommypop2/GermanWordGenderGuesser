import random
from predictor import Predictor

predictor = Predictor()
chars = "abcdefghijklmnopqrstuvwxyz1234567890"
desiredWordLength = 10
while True:
    word = ""
    for i in range(desiredWordLength):
        word += chars[random.randint(0, len(chars) - 1)]
    results = predictor.predict(word)
    percentages = []
    for i in results:
        key = list(i.keys())[0]
        value = i[key]
        percentages.append(value)
    if(round(percentages[0]) == 33 and round(percentages[1]) == 33 and round(percentages[2]) == 33):
        print("Found")
        print(word)
        break
