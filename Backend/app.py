from flask import Flask, jsonify, request, send_file
from constants import notes, modes
from midi2audio import FluidSynth

app = Flask(__name__)

@app.route("/midi/convertToMP3", methods=['POST'])
def hello_world():
    with open('file.mid', 'wb') as f:
      f.write(request.data)
    fs = FluidSynth("resources/FluidR3Mono_GM.sf3")
    fs.midi_to_audio('file.mid', 'output.wav')
    return send_file('output.wav', mimetype='audio/x-wav')

@app.route("/generateMelody", methods=["POST"])
def generateMelody():
    note = request.json['note']
    if (note not in notes):
      return jsonify({"message": "Invalid note"}), 400
    mode = request.json['mode']
    if (mode not in modes):
      return jsonify({"message": "Invalid mode"}), 400
    temperature = request.json['temperature']
    if (temperature < 0 or temperature > 100):
      return jsonify({"message": "Invalid temperature"}), 400
    return jsonify({"message": "Melody generated"}), 200