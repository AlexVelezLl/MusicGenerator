import os
import music21.converter
from utils import check_durations, encode_music, transpose_music
from constants import DELIMITER_SYMBOL, MERGED_DATASET_PATH, PREPROCESSED_DATASET_DIRECTORY, RAW_DATASET_PATH, SEQUENCE_LENGTH



def preprocess_data():

    scores = []

    # Load training data
    for path, _, files in os.walk(RAW_DATASET_PATH):

        for file in files:

            if file[-4:] == ".krn":
                score = music21.converter.parse(os.path.join(path, file))
                scores.append(score)



    # Create and save encoding for individual scores
    for i, score in enumerate(scores):
        
        # Filter score with unsupported durations
        duration_complaint = check_durations(score)
        if not duration_complaint: continue        # Ignores this score, move to the next


        # Transpose score to Cmaj/Amin keys
        transposed_score = transpose_music(score)


        # Encode score in time-series representation
        encoded_score = encode_music(transposed_score)
        

        # Save encoded score 
        preprocessed_score_path = f'{PREPROCESSED_DATASET_DIRECTORY}/{i}-preprocessed_score'
        with open(preprocessed_score_path, 'w') as fp:
            fp.write(encoded_score)




    # Create single file dataset by merging all scores
    merged_timeseries = ''
    song_separator = (DELIMITER_SYMBOL + ' ') * SEQUENCE_LENGTH

    for path, _, files in os.walk(PREPROCESSED_DATASET_DIRECTORY):

        for file in files:
            file_path = os.path.join(path, file)

            with open(file_path, 'r') as fp: 
                single_timeseries_score = fp.read()

            merged_timeseries = merged_timeseries + single_timeseries_score + " " + song_separator

    with open(MERGED_DATASET_PATH, 'w') as fp:
        fp.write(merged_timeseries)





    # TODO: Delete tests
    # score = scores[0]
    # transposed_score = transpose_music(score)
    # encoded_score = encode_music(transposed_score)
    # print(f'is duration complaint: {check_durations(score)}')
    # score.show()
    # transposed_score.show()
    # print(encoded_score)


if __name__ == '__main__':
    preprocess_data()

