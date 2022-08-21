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
    genderVal = indexOf(predictionArr[0], max(predictionArr[0]))
    genders = {0: "masculine", 1: "feminine", 2: "neuter"}
    print(genders[genderVal])
    # print(predictionArr[0])
# print(model.predict(
#     [helperFunctions.convertStrToArr("vater"), helperFunctions.convertStrToArr("gesundheit")]))
# print(model.predict([[ord(i) for i in "-" * 68],[ord(i) for i in "-" * 68]]))
# model.summary()
