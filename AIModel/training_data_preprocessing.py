import os
import music21.converter
from constants import PREPROCESSED_DATASET_DIRECTORY, RAW_DATASET_PATH
from utils import check_durations, encode_music, transpose_music



def preprocess_data():

    scores = []

    # Load training data
    for path, _, files in os.walk(RAW_DATASET_PATH):

        for file in files:

            if file[-4:] == ".krn":
                score = music21.converter.parse(os.path.join(path, file))
                scores.append(score)



    for i, score in enumerate(scores):
        
        # TODO: PONLO COMO TUT
        # Filter score with unsupported durations
        duration_complaint = check_durations(score)
        if not duration_complaint: scores.remove(score)



        # Transpose score to Cmaj/Amin keys
        score = transpose_music(score)


        # Encode score in time-series representation
        encoded_score = encode_music(score)
        


        # Save encoded score 
        preprocessed_score_path = f'{PREPROCESSED_DATASET_DIRECTORY}/{i}-preprocesssed_score'
        with open(preprocessed_score_path, 'w') as fp:
            fp.write(encoded_score)




    # Create look-up table as vocabulary





if __name__ == '__main__':
    preprocess_data()








# TESTS, TODO: Delete this test

# Check filtering due to durations:
# scores[0].flat.notesAndRests[7].duration.quarterLength = 0.125
# print(scores[0].flat.notesAndRests[7].duration.quarterLength)

