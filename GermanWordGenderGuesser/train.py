import numpy as np
import tensorflow as tf
from tensorflow import keras
import generateTrainingData
import helperFunctions
iterations = 0
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
while iterations < 1:
    words, genders = generateTrainingData.separateNounsFromGenders()
    words, genders = generateTrainingData.genTrainingData(words, genders)
    ratio = 0.9
    train_count = int(len(words) * ratio)
    test_count = len(words) - train_count
    x_train = words[:train_count]
    y_train = genders[:train_count]
    # x_train = words
    # y_train = genders
    x_val = words[test_count:]
    y_val = genders[test_count:]

    losses = model.fit(x_train, y_train,

                       validation_data=(x_val, y_val),


                       batch_size=64,
                       epochs=200,

                       )

    model.save_weights("./weights")
    print(model.summary())
    print(model.predict(
        [helperFunctions.convertStrToArr("vater"), helperFunctions.convertStrToArr("gesundheit")]))
    iterations += 1
# print(model.predict([[ord(i) for i in "-" * 68],[ord(i) for i in "-" * 68]]))
# model.summary()
