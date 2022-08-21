from operator import indexOf
from tensorflow import keras
import helperFunctions
model = keras.Sequential([
    keras.layers.Dense(
        units=72, activation="relu"),
    keras.layers.Dense(units=144, activation='relu'),
    keras.layers.Dense(units=288, activation='relu'),
    keras.layers.Dense(units=1152, activation='relu'),
    keras.layers.Dense(units=288, activation="relu"),
    keras.layers.Dense(units=144, activation="relu"),
    keras.layers.Dense(units=72, activation="relu"),
    keras.layers.Dense(units=36, activation="relu"),
    keras.layers.Dense(units=18, activation="relu"),
    keras.layers.Dense(units=9, activation="relu"),
    keras.layers.Dense(units=3, activation="softmax")
])


model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy'])
model.load_weights("./weights")
model.build(input_shape=(None, 72))

print(model.summary())
while True:
    inp = input("Enter a word: ").lower()
    if (inp == "exit"):
        break
    predictionArr = model.predict([helperFunctions.convertStrToArr(inp)])
    scaler = 100/sum(predictionArr[0])
    percentages = [{"masculine": round(predictionArr[0][0] * scaler, 2)},
                   {"feminine": round(predictionArr[0][1] * scaler, 2)},
                   {"neuter": round(predictionArr[0][2] * scaler, 2)}]
    while True:
        swaps = 0
        for i in range(1, len(percentages)):
            currentElement = percentages[i]
            previousElement = percentages[i-1]
            if (currentElement[list(percentages[i].keys())[0]] > previousElement[list(percentages[i-1].keys())[0]]):
                percentages[i] = previousElement
                percentages[i-1] = currentElement
                swaps += 1
        if (swaps == 0):
            break
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
