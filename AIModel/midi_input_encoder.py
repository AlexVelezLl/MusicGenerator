from utils import check_durations, encode_music, transpose_music
import music21.stream
import music21.converter
import music21.pitch
import music21.interval
import music21.note


# USER INPUTS
# MIDI_INPUT_PATH = 'inputs/test_melody_Ema.mid'
# KEY = 'E'       # 12 Notes
# MODE = 'major'  # major or minor

MIDI_INPUT_PATH = 'inputs/test_melody_Cmin.mid'
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


    return encoded_seed



if __name__ == "__main__":
    input_seed = encode_midi_input(KEY, MODE)






    
# TODO: Delete tests
# General tests
    # print(f'{MIDI_INPUT_PATH} is duration complaint: {seed_is_duration_complaint}')
    # raw_input_midi_seed.show()
    # transposed_seed.show()
    # print(encoded_seed)


# Duration complaint
    # for event in raw_input_midi_seed.flat.notesAndRests:
    #     print(f'Duration of event {event}: {event.duration.quarterLength}')





# TODO:
# ARTURO:
# - Probar si Music21 es capaz de redondear correctamente valores cuando Arturo toca a pelo o necesitan ser duraciones grideadas.
# - Mira si existe alguna armadura en metadata cuando Arturo toca una melodía MIDI en un keyb.
# - Si sí existen armaduras en MIDI keyb: Mira si el problema de las armaduras se mantiene al transponer (ergo, la armadura del MIDI metadata no coincide con la verdadera armadura)
# - Es muy posible que Cmaj sea un valor por defecto, vas a tener que hacer que el script pueda setear el key a cmaj (quiero poder .show() y que la armadura sea Cmaj, cuando ya esté transpuesto para evitar problemas futuros)
# - Consultar qué hacer con el mensaje en caso de que las duraciones no sean aceptables.
# - Posiblemente hay código reutilizable en el proceso de transposición entre preprocessing y encoding.
# - Refactor input constants so that it connects with GUI.
