# MusicGenerator

Music generator is an AI project that aims to compose a melody on top of a given short seed melody. It uses two LSTM layers with 256 units each one, and the model was trained with about 1.7k kern western folk songs.

## Inputs

The model recieves 5 parameters as inputs that you can modify:

* Seed melody: A Midi file containing the seed melody `required`
* Note: The key note of the seed melody passed as input. `default C`
* Mode: The key mode of the seed melody passed as input. `default major`
* Tempo: The tempo desired for the output melody.
* Temperature: The sample temperature with which the model will generate the melody. The more temperature the more 'creative' and unpredictable the model is.

## GUI

When you open the frontend, you will see a gui as the following:

At the left side, you can modify the inputs, and select the midi seed file.

Once you have selected the midi file, you will be able to play it.

Then, you can generate the output melody, 

## Members

* Valeria Barzola
* Juan Nebel
* Alex Velez
