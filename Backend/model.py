import json
from AIModel.data_preprocessing import preprocess_data
from AIModel.melodyGenerator import MelodyGenerator
from AIModel.training import train
from AIModel.constants import LOOKUP_TABLE_DESTINATION

def preprocess():
  preprocess_data()

def generateMelody():
  mg = MelodyGenerator()
  seed = "67 _ 67 _ 67 _ _ 65 64 _ 64 _ 64 _ _"
  melody = mg.generate_melody(seed, temperature=0.05)
  mg.save_melody(melody, file_name="seed.mid")

if __name__ == "__main__":
  # preprocess()
  train()
  # generateMelody()