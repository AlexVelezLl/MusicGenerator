from shared import check_durations, STEP_DURATION
import music21.stream
import music21.converter
import music21.pitch
import music21.interval
import music21.note


# USER INPUTS
MIDI_INPUT_PATH = 'inputs/test_melody_Emaj.mid'
KEY = 'E'       # 12 Notes
MODE = 'major'  # major or minor



def encode_midi_input():

    # Load the MIDI melody
    raw_input_midi_seed = music21.converter.parse(MIDI_INPUT_PATH) 


    # Check for non-supported note/rest durations
    seed_is_duration_complaint = check_durations(raw_input_midi_seed)
    if(not seed_is_duration_complaint):
        # TODO: Mandar un mensaje de error que diga que no mande notes/rest con fracciones menor a 16th (fusas, semi-fusas, semi-corcheas con punto y silencios respectivos)
        pass
    
    

    # Transpose the melody
    interval = music21.interval.Interval(music21.pitch.Pitch(KEY), music21.pitch.Pitch('C'))
    transposed_seed = raw_input_midi_seed.transpose(interval)



    # Encode seed in time series string
    encoded_seed = []

    for musical_event in transposed_seed.flat.notesAndRests:

        # Get event type (Note or Rest)
        if isinstance(musical_event, music21.note.Note):
            event_type = musical_event.pitch.midi  
        else: # It's a Rest
            event_type = "r"

        # Get event duration
        num_of_steps = int(musical_event.duration.quarterLength / STEP_DURATION) # Event duration

        # Encode event and it's duration
        for step in range(num_of_steps):
            if step == 0:
                encoded_seed.append(event_type) 
            else:
                encoded_seed.append("_") 


    # Make string out of whole list list
    encoded_seed = " ".join(map(str, encoded_seed))


    # TODO: Delete these tests
    # raw_input_midi_seed.show()
    # transposed_seed.show()
    # print(encoded_seed)

    return encoded_seed




if __name__ == "__main__":
    input_seed = encode_midi_input()






    






# TODO:
# ARTURO:
# - Probar si Music21 es capaz de redondear correctamente valores cuando Arturo toca a pelo o necesitan ser duraciones grideadas.
# - Mira si existe alguna armadura en metadata cuando Arturo toca una melodía MIDI en un keyb.
# - Si sí existen armaduras en MIDI keyb: Mira si el problema de las armaduras se mantiene al transponer (ergo, la armadura del MIDI metadata no coincide con la verdadera armadura)
# - Es muy posible que Cmaj sea un valor por defecto, vas a tener que hacer que el script pueda setear el key a cmaj (quiero poder .show() y que la armadura sea Cmaj, cuando ya esté transpuesto para evitar problemas futuros)
# - Consultar qué hacer con el mensaje en caso de que las duraciones no sean aceptables.
# - Posiblemente hay código reutilizable en el proceso de transposición entre preprocessing y encoding.
# - Refactor input constants so that it connects with GUI.
