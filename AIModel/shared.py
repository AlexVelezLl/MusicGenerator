
# Durations are limited to the most basic ones
SUPPORTED_DURATIONS = [
    0.25, # Semicorchea/Step  (ignoramos semicorchea con punto porque usa fusas)
    0.5,  # Corchea
    0.75, # Corchea con punto
    1,    # Negra
    1.5,  # Negra con punto
    2,    # Blanca 
    3,    # Blanca con punto
    4     # Redonda
]





def check_durations(song):

    for musical_event in song.flat.notesAndRests:
        if musical_event.duration.quarterLength not in SUPPORTED_DURATIONS: return False

    return True

