from constants import LOOKUP_TABLE_DESTINATION, NON_MIDI_SYMBOLS, NUMBER_OF_MIDI_VALUES, SUPPORTED_DURATIONS, STEP_DURATION
import json
import music21.interval
import music21.pitch
import music21.stream
import music21.key
import music21.note


def check_durations(score):

    for musical_event in score.flat.notesAndRests:
        if musical_event.duration.quarterLength not in SUPPORTED_DURATIONS: return False

    return True





def transpose_music(score, key='n/a', mode='n/a'):
    
    # No user input (training)
    if key == 'n/a':
    
        # Get key by metadata
        parts = score.getElementsByClass(music21.stream.Part)
        measures_part0 = parts[0].getElementsByClass(music21.stream.Measure) 
        key = measures_part0[0][4] # Here is where key resides if in metadata

        # If that fails, estimate key
        if not isinstance(key, music21.key.Key):
            key = score.analyze("key") 

        # Get mode
        mode = key.mode

    # Get interval
    if mode=='major':
        interval = music21.interval.Interval(get_pitch(key), music21.pitch.Pitch('C'))  
    elif mode=='minor': 
        interval = music21.interval.Interval(get_pitch(key), music21.pitch.Pitch('A'))  
    else: # Modal music, no need to transpose (should not happen or very marginal case)
        interval = music21.interval.Interval("P1") 


    # Transpose
    transposed_score = score.transpose(interval)
    return transposed_score



def get_pitch(key):

    if isinstance(key, music21.key.Key): return key.tonic
    return music21.pitch.Pitch(key)









def encode_music(transposed_score):

    # Encode seed in time series string
    encoded_score = []

    for musical_event in transposed_score.flat.notesAndRests:

        # Get event type (Note or Rest)
        if isinstance(musical_event, music21.note.Note):
            event_type = musical_event.pitch.midi  
        else: # It's a Rest
            event_type = "r"

        # Get event duration
        num_of_steps = int(musical_event.duration.quarterLength / STEP_DURATION) # Event duration

        # Encode event and it's duration
        encoded_score += [event_type] + ["_"] * (num_of_steps - 1)


    # Make string out of whole list 
    encoded_score = " ".join(map(str, encoded_score))
    return encoded_score






def create_lookup_table():

    look_up_table = {}

    for i in range(NUMBER_OF_MIDI_VALUES):
        look_up_table[str(i)] = i

    for i, non_midi_symbol in enumerate(NON_MIDI_SYMBOLS):
        look_up_table[non_midi_symbol] = i + NUMBER_OF_MIDI_VALUES

    with open(LOOKUP_TABLE_DESTINATION, 'w') as fp:
        json.dump(look_up_table, fp, indent=4)













