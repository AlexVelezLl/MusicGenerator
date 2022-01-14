from AIModel.melodyGenerator import MelodyGenerator

mg = MelodyGenerator('AIModel/model.h5')
seed = "67 _ 67 _ 67 _ _ 65 64 _ 64 _ 64 _ _"
mg.save_melody(seed.split(), file_name="seed.mid")
