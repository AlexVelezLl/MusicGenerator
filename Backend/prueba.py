from midi2audio import FluidSynth

fs = FluidSynth("FluidR3Mono_GM.sf3")
fs.midi_to_audio('mel.mid', 'output.wav')
