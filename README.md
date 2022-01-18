# MusicGenerator

Music generator is an AI project that aims to compose a melody on top of a given short seed melody. It uses two LSTM layers with 256 units each one, and the model was trained with about 1.7k kern western folk songs.

## Inputs

The model recieves 5 parameters as inputs that you can modify:

* Seed melody: A Midi file containing the seed melody `required`
* Note: The key note of the seed melody passed as input. `default C`
* Mode: The key mode of the seed melody passed as input. `default major`
* Tempo: The tempo desired for the output melody. `default 120BPM`
* Temperature: The sample temperature with which the model will generate the melody. The more temperature the more 'creative' and unpredictable the model is. `default 0.2`

## GUI

When you open the frontend, you will see a gui as the following:

![Capture1](https://raw.githubusercontent.com/AlexVelezLl/MusicGenerator/main/images/Capture1.png)

At the left side, you can modify the inputs, and select the midi seed file.

Once you have selected the midi file, you will be able to play it.

![Capture2](https://raw.githubusercontent.com/AlexVelezLl/MusicGenerator/main/images/Capture2.png)

Then, you can generate the output melody.

![Capture3](https://raw.githubusercontent.com/AlexVelezLl/MusicGenerator/main/images/Capture3.png)

Once generated the output melody, you can play it, and download it in MIDI or MP3 formats.

![Capture4](https://raw.githubusercontent.com/AlexVelezLl/MusicGenerator/main/images/Capture4.png)

## Members

* Valeria Barzola
* Juan Nebel
* Alex Velez

## Credits
* This proyect's ML implementation is based (and possible) thanks to another RNN-LSTM project by [musikalkemist](https://github.com/musikalkemist/generating-melodies-with-rnn-lstm)
* This project also took inspiration primarily from the "Generating Music using LSTM" paper by Priya Varshini G.

