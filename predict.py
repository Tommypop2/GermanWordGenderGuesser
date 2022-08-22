from tensorflow import keras
from predictor import Predictor
predictor = Predictor()
while True:
    inp = input("Enter a word: ").lower()
    if (inp == "exit"):
        break
    inp = str(inp).strip()
    percentages = predictor.predict(inp)
    for i in percentages:
        key = list(i.keys())[0]
        value = i[key]
        print(f"{value}% chance {key}")
    print("\n\n")