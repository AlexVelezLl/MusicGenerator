from shared import check_durations
import music21.stream
import music21.converter


# PATH CONSTANTS
MIDI_INPUT_PATH = 'input/test_melody.mid'



def encode_midi_input():


    # Load the MIDI melody
    input_seed = music21.converter.parse(MIDI_INPUT_PATH) 



    # Check for non-supported note/rest durations
    seed_is_duration_complaint = check_durations(input_seed)
    print(seed_is_duration_complaint)
    if(not seed_is_duration_complaint):
        # TODO: Mandar un mensaje de error que diga que no mande notes/rest con fracciones menor a 16th (fusas, semi-fusas, semi-corcheas con punto y silencios respectivos)
        pass
    
    

    # Transpose the melody

    # Encode in time series string


    return input_seed




if __name__ == "__main__":
    input_seed = encode_midi_input()






# TODO:
# 1. Arregla el check_durations
# 1. Cómo hago un código que pase el key por consola.
