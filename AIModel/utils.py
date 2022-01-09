from constants import SUPPORTED_DURATIONS
import music21.interval
import music21.pitch
import music21.stream
import music21.key


def check_durations(score):

    for musical_event in score.flat.notesAndRests:
        if musical_event.duration.quarterLength not in SUPPORTED_DURATIONS: return False

    return True





def transpose_music(score, key='n/a', mode='n/a'):
    
    # TODO: Validaciones al user input key y mode (manda basura) (Posiblemente en midi_input_encoder)
    

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




