from tensorflow import keras
import helperFunctions


class Predictor():
    def __init__(self):
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
        self.model = model

    def predict(self, word):
        strasArr = helperFunctions.convertStrToArr(word)
        prediction = self.model.predict([strasArr])
        print(prediction)
