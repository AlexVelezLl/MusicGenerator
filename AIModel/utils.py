from constants import SUPPORTED_DURATIONS


def check_durations(song):

    for musical_event in song.flat.notesAndRests:
        if musical_event.duration.quarterLength not in SUPPORTED_DURATIONS: return False

    return True

