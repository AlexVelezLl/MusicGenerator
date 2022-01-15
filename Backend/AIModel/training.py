import json
import tensorflow.keras as keras
import numpy as np

from AIModel.constants import LOOKUP_TABLE_DESTINATION, MERGED_DATASET_DESTINATION, DEFAULT_MODEL_PATH, RAW_DATASET_PATH, SEQUENCE_LENGTH
from AIModel.data_preprocessing import convert_songs_to_int

NUM_UNITS = [256]
LOSS = "sparse_categorical_crossentropy"
LEARNING_RATE = 0.001
EPOCHS = 1
BATCH_SIZE = 64

def train(num_units=NUM_UNITS, loss=LOSS, learning_rate=LEARNING_RATE):
    output_units = get_vocabulary_size()

    inputs, targets = generate_training_sequences()

    model = build_model(output_units, num_units, loss, learning_rate)

    model.fit(inputs, targets, epochs=EPOCHS, batch_size=BATCH_SIZE)

    model.save(DEFAULT_MODEL_PATH)


def build_model(output_units, num_units, loss, learning_rate):

    input = keras.layers.Input(shape=(None, output_units))
    x = keras.layers.LSTM(num_units[0])(input)
    x = keras.layers.Dropout(0.2)(x)

    output = keras.layers.Dense(output_units, activation="softmax")(x)

    model = keras.Model(input, output)

    model.compile(loss=loss,
                  optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
                  metrics=["accuracy"])

    model.summary()

    return model


def generate_training_sequences():
    sequence_length = SEQUENCE_LENGTH
    with open(MERGED_DATASET_DESTINATION) as f:
      songs = f.read()
    int_songs = convert_songs_to_int(songs)

    inputs = []
    targets = []

    num_sequences = len(int_songs) - sequence_length
    for i in range(num_sequences):
        inputs.append(int_songs[i:i+sequence_length])
        targets.append(int_songs[i+sequence_length])

    vocabulary_size = get_vocabulary_size()
    inputs = keras.utils.to_categorical(inputs, num_classes=vocabulary_size)
    targets = np.array(targets)

    return inputs, targets


def get_vocabulary_size():
  with open(LOOKUP_TABLE_DESTINATION, "r") as fp:
    mappings = json.load(fp)
  return len(mappings.keys())