from flask import Flask
import notes, modes from constants

app = Flask(__name__)

@app.route("/midi/convertToMP3")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/generateMelody", methods=["POST"])
def generateMelody():
    note = request.json['note']
    if(note not in notes):

    mode = request.json['mode']
    temperature = request.json['temperature']

    return {}
