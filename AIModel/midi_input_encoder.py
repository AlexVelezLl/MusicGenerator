from utils import check_durations, encode_music, transpose_music
import music21.stream
import music21.converter
import music21.pitch
import music21.interval
import music21.note


# USER INPUTS
# MIDI_INPUT_PATH = 'data/inputs/test_melody_Ema.mid'
# KEY = 'E'       # 12 Notes
# MODE = 'major'  # major or minor

MIDI_INPUT_PATH = 'data/inputs/test_melody_Cmin.mid'
KEY = 'C'       # 12 Notes
MODE = 'minor'  # major or minor



def encode_midi_input(key, mode):

    # Load the MIDI melody
    raw_input_midi_seed = music21.converter.parse(MIDI_INPUT_PATH) 

    # Check for non-supported note/rest durations
    seed_is_duration_complaint = check_durations(raw_input_midi_seed)
    if(not seed_is_duration_complaint):
        # TODO: Mandar un mensaje de error que diga que no mande notes/rest con fracciones menor a 16th (fusas, semi-fusas, semi-corcheas con punto y silencios respectivos)
        pass
    
    

    # Transpose the melody
    transposed_seed = transpose_music(raw_input_midi_seed, key=key, mode=mode)



    # Encode seed in time series string
    encoded_seed = encode_music(transposed_seed)



    # TODO: Maybe also encode in integer representation and then one-hot to directly send to
    # the LSTM.


    # TODO: Delete tests
    # General tests
    # print(f'{MIDI_INPUT_PATH} is duration complaint: {seed_is_duration_complaint}')
    # raw_input_midi_seed.show()
    # transposed_seed.show()
    # print(encoded_seed)


    return encoded_seed



if __name__ == "__main__":
    input_seed = encode_midi_input(KEY, MODE)



