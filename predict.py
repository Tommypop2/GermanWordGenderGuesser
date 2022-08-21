from tensorflow import keras
from predictor import Predictor
predictor = Predictor()
while True:
    inp = input("Enter a word: ").lower()
    if (inp == "exit"):
        break
    percentages = predictor.predict(inp)
    for i in percentages:
        key = list(i.keys())[0]
        value = i[key]
        print(f"{value}% chance {key}")
    print("\n\n")
# print(predictionArr[0])
# print(model.predict(
#     [helperFunctions.convertStrToArr("vater"), helperFunctions.convertStrToArr("gesundheit")]))
# print(model.predict([[ord(i) for i in "-" * 68],[ord(i) for i in "-" * 68]]))
# model.summary()
