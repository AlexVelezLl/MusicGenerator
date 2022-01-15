import os
import json
import music21.converter
from utils import check_durations, encode_music, transpose_music_to_CA
from constants import (
  DELIMITER_SYMBOL, 
  MERGED_DATASET_DESTINATION, 
  PREPROCESSED_DATASET_DESTINATION, 
  RAW_DATASET_PATH, 
  SEQUENCE_LENGTH, 
  LOOKUP_TABLE_DESTINATION
)


def preprocess_data():

    # Load training data
    scores = load_training_data(RAW_DATASET_PATH)

    # Create and save encoding for individual scores
    preprocess_individual_scores(scores, PREPROCESSED_DATASET_DESTINATION)

    # Create single file dataset by merging all scores
    create_merged_dataset(PREPROCESSED_DATASET_DESTINATION, MERGED_DATASET_DESTINATION)






def load_training_data(raw_dataset_path):

    scores = []
    for path, _, files in os.walk(raw_dataset_path):

        for file in files:

            if file[-4:] == ".krn":
                score = music21.converter.parse(os.path.join(path, file))
                scores.append(score)
    
    return scores







def preprocess_individual_scores(scores, preprocessed_dataset_destination):

    for i, score in enumerate(scores):
        
        # Filter score with unsupported durations
        duration_complaint = check_durations(score)
        if not duration_complaint: continue        # Ignores this score, move to the next


        # Transpose score to Cmaj/Amin keys
        transposed_score = transpose_music_to_CA(score)


        # Encode score in time-series representation
        encoded_score = encode_music(transposed_score)
        

        # Save encoded score 
        preprocessed_score_path = f'{preprocessed_dataset_destination}/{i}-preprocessed_score.txt'
        with open(preprocessed_score_path, 'w') as fp:
            fp.write(encoded_score)





def create_merged_dataset(preprocessed_dataset_path, merged_dataset_destination):
    merged_timeseries = ''
    song_separator = (DELIMITER_SYMBOL + ' ') * SEQUENCE_LENGTH

    for path, _, files in os.walk(preprocessed_dataset_path):

        for file in files:
            file_path = os.path.join(path, file)

            with open(file_path, 'r') as fp: 
                single_timeseries_score = fp.read()

            merged_timeseries = merged_timeseries + single_timeseries_score + " " + song_separator


    with open(merged_dataset_destination, 'w') as fp:
        fp.write(merged_timeseries)

def convert_songs_to_int(songs):
    with open(LOOKUP_TABLE_DESTINATION, "r") as fp:
        mappings = json.load(fp)

    songs = songs.split()

    int_songs = [mappings[x] for x in songs]

    return int_songs