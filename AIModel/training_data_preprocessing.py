from constants import RAW_DATASET_PATH
import os
import music21.converter



def preprocess_data():

    scores = []

    # Load training data
    for path, _, files in os.walk(RAW_DATASET_PATH):

        for file in files:

            if file[-4:] == ".krn":
                score = music21.converter.parse(os.path.join(path, file))
                scores.append(score)


if __name__ == '__main__':
    preprocess_data()

