import json
import numpy as np
import tensorflow.keras as keras
import music21 as m21

from AIModel.constants import SEQUENCE_LENGTH, LOOKUP_TABLE_DESTINATION
from AIModel.utils import transpose_music_from_CA
from AIModel.constants import DEFAULT_MODEL_PATH

class MelodyGenerator:
    """A class that wraps the LSTM model and offers utilities to generate melodies."""

    def __init__(self, model_path=DEFAULT_MODEL_PATH):
        """Constructor that initialises TensorFlow model"""

        self.model_path = model_path
        self.model = keras.models.load_model(model_path)

        with open(LOOKUP_TABLE_DESTINATION, "r") as fp:
            self._mappings = json.load(fp)

        self._start_symbols = ["/"] * SEQUENCE_LENGTH


    def generate_melody(
      self, 
      seed, 
      num_steps=500, 
      max_sequence_length=SEQUENCE_LENGTH, 
      temperature=1.0
    ):
        seed = seed.split()
        melody = seed
        seed = self._start_symbols + seed

        seed = [self._mappings[symbol] for symbol in seed]

        for _ in range(num_steps):

            seed = seed[-max_sequence_length:]

            onehot_seed = keras.utils.to_categorical(seed, num_classes=len(self._mappings))
            
            # (1, max_sequence_length, num of symbols in the vocabulary)
            onehot_seed = onehot_seed[np.newaxis, ...]

            probabilities = self.model.predict(onehot_seed)[0]

            output_int = self._sample_with_temperature(probabilities, temperature)

            seed.append(output_int)

            # map int to our encoding
            output_symbol = [k for k, v in self._mappings.items() if v == output_int][0]

            # check whether we're at the end of a melody
            if output_symbol == "/":
                break

            melody.append(output_symbol)

        return melody


    def _sample_with_temperature(self, probabilites, temperature):

        predictions = np.log(probabilites) / temperature
        probabilites = np.exp(predictions) / np.sum(np.exp(predictions))

        choices = range(len(probabilites))
        index = np.random.choice(choices, p=probabilites)

        return index


    def save_melody(
      self,
      melody,
      step_duration=0.25,
      format="midi",
      file_name="mel.mid",
      key="C",
      mode="major",
      tempo=120
    ):
        stream = m21.stream.Stream()

        start_symbol = None
        step_counter = 1

        # parse all the symbols in the melody and create note/rest objects
        for i, symbol in enumerate(melody):

            # handle case in which we have a note/rest and its not the end of the melody
            if symbol != "_" or i + 1 == len(melody):

                # ensure we're dealing with note/rest beyond the first one
                if start_symbol is not None:

                    quarter_length_duration = step_duration * step_counter # 0.25 * 4 = 1

                    if start_symbol == "r":
                        m21_event = m21.note.Rest(quarterLength=quarter_length_duration)

                    else:
                        m21_event = m21.note.Note(int(start_symbol), quarterLength=quarter_length_duration)

                    stream.append(m21_event)

                    step_counter = 1

                start_symbol = symbol

            # handle case in which we have a prolongation sign "_"
            else:
                step_counter += 1
        stream = transpose_music_from_CA(stream, key, mode)

        tempo_factor = 120 / tempo
        
        stream = stream.scaleOffsets(tempo_factor).scaleDurations(tempo_factor)
        stream.write(format, file_name)
