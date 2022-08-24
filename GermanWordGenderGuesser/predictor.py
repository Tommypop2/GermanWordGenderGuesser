from tensorflow import keras
import helperFunctions


class Predictor():
    def __init__(self) -> None:
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
        inp = str(word).lower()
        predictionArr = self.model.predict(
            [helperFunctions.convertStrToArr(inp)])
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
        return percentages
        # for i in percentages:
        #     key = list(i.keys())[0]
        #     value = i[key]
        #     print(f"{value}% chance {key}")
        # print("\n\n")

    def getModelSummary(self):
        return self.model.summary()
