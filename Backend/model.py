from AIModel.data_preprocessing import preprocess_data
from AIModel.melodyGenerator import MelodyGenerator
from AIModel.training import train
from AIModel.constants import LOOKUP_TABLE_DESTINATION
import music21 as m21
import os
import random as r
def preprocess():
  preprocess_data()

def generateMelody():
  mg = MelodyGenerator()
  seed = "67 _ 67 _ 67 _ _ 65 64 _ 64 _ 64 _ _"
  # melody = mg.generate_melody(seed, temperature=0.05)
  mg.save_melody(seed.split(" "), file_name="seed.mid")

def kern_to_midi():
  dataset = 'AIModel/data/raw_dataset/deutschl/erk'
  num_songs = 0
  for path, _, files in os.walk(dataset):
        for file in files:

            if file[-4:] == ".krn":
                if num_songs == 5:
                    return
                score = m21.converter.parse(os.path.join(path, file))
                      # Get key by metadata
                parts = score.getElementsByClass(m21.stream.Part)
                measures_part0 = parts[0].getElementsByClass(m21.stream.Measure) 
                key = measures_part0[0][4] # Here is where key resides if in metadata

                # If that fails, estimate key
                if not isinstance(key, m21.key.Key):
                    key = score.analyze("key") 
                mode = key.mode
                tonic = key.tonic
                # print("Key: ", tonic, " ", mode)
                if str(mode)=='major' and str(tonic) == 'C':
                    score.write('midi', 'AIModel/data/tests/'+file+'.mid')
                    print("Found a song" + file)
                    print("Key: ", tonic, " ", mode)
                print("Processed: " + file)
                

  

if __name__ == "__main__":
  # preprocess()
  train()
  # kern_to_midi()
  # generateMelody()