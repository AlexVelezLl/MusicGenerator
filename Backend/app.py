from flask import Flask, jsonify, request, send_file, redirect, url_for 
from constants import notes, modes
from flask_cors import CORS
from midi2audio import FluidSynth
from constants import PATH_MP3, PATH_MIDI
import datetime


app = Flask(__name__)
cors = CORS(app)


@app.route("/midi/convertToMP3", methods=['POST'])
def hello_world():
    with open('file.mid', 'wb') as f:
      f.write(request.data)
    fs = FluidSynth("resources/FluidR3Mono_GM.sf3")
    timestamp = datetime.datetime.now()
    timestamp= timestamp.strftime("%Y%m%d%H%M%S")
    destiny_file = PATH_MP3 + timestamp + ".mp3"
    fs.midi_to_audio('file.mid', 'static/'+destiny_file)
    return jsonify({"url_file": f'static/{destiny_file}' })



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

if __name__ == '__main__':
  app.run(debug=True)