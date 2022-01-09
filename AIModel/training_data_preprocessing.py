import os
import music21.converter
from constants import RAW_DATASET_PATH
from utils import check_durations



def preprocess_data():

    scores = []

    # Load training data
    for path, _, files in os.walk(RAW_DATASET_PATH):

        for file in files:

            if file[-4:] == ".krn":
                score = music21.converter.parse(os.path.join(path, file))
                scores.append(score)




    # Filter scores with unsupported durations
    for score in scores:

        score_is_duration_complaint = check_durations(score)
        if not score_is_duration_complaint: scores.remove(score)





    # Transpose scores to Cmaj/Amin keys


    # Encode songs in time-series representation

    # Create look-up table as vocabulary





if __name__ == '__main__':
    preprocess_data()








# TESTS, TODO: Delete this test

# Check filtering due to durations:
# scores[0].flat.notesAndRests[7].duration.quarterLength = 0.125
# print(scores[0].flat.notesAndRests[7].duration.quarterLength)

