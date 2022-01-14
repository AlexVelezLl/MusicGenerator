from AIModel.utils import check_durations, encode_music, transpose_music_to_CA
import music21.stream
import music21.converter
import music21.pitch
import music21.interval
import music21.note


# USER INPUTS
# MIDI_INPUT_PATH = 'data/inputs/test_melody_Ema.mid'
# KEY = 'E'       # 12 Notes
# MODE = 'major'  # major or minor
def encode_midi_input(key, mode, midi_file):

    # Load the MIDI melody
    raw_input_midi_seed = music21.converter.parse(midi_file) 

    # Check for non-supported note/rest durations
    seed_is_duration_complaint = check_durations(raw_input_midi_seed)
    if(not seed_is_duration_complaint):
        raise ValueError("Input MIDI file contains unsupported note/rest durations.")

    # Transpose the melody
    transposed_seed = transpose_music_to_CA(raw_input_midi_seed, key=key, mode=mode)



    # Encode seed in time series string
    encoded_seed = encode_music(transposed_seed)

    return encoded_seed