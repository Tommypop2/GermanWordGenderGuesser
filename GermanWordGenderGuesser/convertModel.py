from tensorflow import keras
import tensorflow as tf

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

kerasModel = tf.lite.TFLiteConverter.from_keras_model(model)
convertedModel = kerasModel.convert()
with open("./convertedmodel/germanGenderGuesserModel.tflite", "wb") as f:
    f.write(convertedModel)
