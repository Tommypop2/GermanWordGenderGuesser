from tensorflow import keras
from predictor import Predictor
predictor = Predictor()
while True:
    inp = input("Enter a word: ").lower()
    if (inp == "exit"):
        break
    inp = str(inp).strip()
    predictions = predictor.predict(inp)
    print(predictions)
    print("\n\n")