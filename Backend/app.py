from flask import Flask, jsonify, request
from constants import notes, modes
from flask_cors import CORS
from midi2audio import FluidSynth
import datetime

from AIModel.melodyGenerator import MelodyGenerator
from AIModel.midi_input_encoder import encode_midi_input
from constants import PATH_SEEDS, PATH_OUTPUTS

app = Flask(__name__)
cors = CORS(app)

mg = MelodyGenerator(model_path='AIModel/model.h5')

@app.route("/midi/convertToMP3", methods=['POST'])
def transformMidi():
    timestamp = datetime.datetime.now()
    timestamp= timestamp.strftime("%Y%m%d%H%M%S")
    destiny_file = PATH_SEEDS + timestamp
    with open(f'{destiny_file}.mid', 'wb') as f:
      f.write(request.data)
    fs = FluidSynth("resources/FluidR3Mono_GM.sf3")
    fs.midi_to_audio(f'{destiny_file}.mid', f'{destiny_file}.mp3')
    return jsonify({"url_file": f'{destiny_file}.mp3' })



@app.route("/generateMelody", methods=["POST"]) 
def generateMelody(): 
    note = request.json['note']
    if (note not in notes):
      return jsonify({"message": "Invalid note"}), 400

    mode = request.json['mode']
    if (mode not in modes):
      return jsonify({"message": "Invalid mode"}), 400

    temperature = request.json['temperature']
    if (temperature <= 0.1 or temperature > 1):
      return jsonify({"message": "Invalid temperature"}), 400

    midi_file = request.json['midi_file']
    seed_midi_file = PATH_SEEDS + midi_file
    output_midi_file = PATH_OUTPUTS + midi_file
    output_mp3_file = output_midi_file.replace(".mid", ".mp3")

    melody = encode_midi_input(note, mode, seed_midi_file)
    generated_melody = mg.generate_melody(melody, temperature=temperature)
    mg.save_melody(generated_melody, file_name=output_midi_file, key=note, mode=mode)

    fs = FluidSynth("resources/FluidR3Mono_GM.sf3")
    fs.midi_to_audio(output_midi_file, output_mp3_file)

    return jsonify({
      "midiFile": output_midi_file,
      "mp3File": output_mp3_file
      }), 200 

if __name__ == '__main__':
  app.run(debug=True)