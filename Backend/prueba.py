import datetime
from midi2audio import FluidSynth
from constants import PATH_WAV, PATH_MIDI

# fs = FluidSynth("./resources/FluidR3Mono_GM.sf3")
# fs.midi_to_audio('mel.mid', PATH_WAV+'output.wav')
a = datetime.datetime.now()
# a -> 20220112232115
a= a.strftime("%Y%m%d%H%M%S") 
print(a)