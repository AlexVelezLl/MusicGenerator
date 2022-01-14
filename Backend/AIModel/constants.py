# Durations are limited to the most basic ones 
# TODO: Esto puede ser reducido a simplemente que sea divisible para 0.25 sin residuo, lo dejo
#       así para que se entienda musicalmente qué ocurre (por ahora)
SUPPORTED_DURATIONS = [
    0.25, # Semicorchea/Step  (ignoramos semicorchea con punto porque usa fusas)
    0.5,  # Corchea
    0.75, # Corchea con punto
    1,    # Negra
    1.25, # Negra ligada a semi-corchea
    1.5,  # Negra con punto
    1.75, # Negra con punto ligada a semi-corchea
    2,    # Blanca 
    2.25, # Blanca ligada a semi-corchea
    2.5,  # Blanca ligada a corchea
    2.75, # Blanca ligada a corchea con punto
    3,    # Blanca con punto
    3.25, # Blanca con punto ligada a semi-corchea
    3.5,  # Blanca con punto ligada a corchea
    3.75, # Blanca con punto ligada a corchea con punto
    4     # Redonda
]
STEP_DURATION = 0.25   # In relation to a quarter note (basically a 16th note)


# Pre-processing
SEQUENCE_LENGTH = 64
DELIMITER_SYMBOL = '/'
NON_MIDI_SYMBOLS = ['r', '_', DELIMITER_SYMBOL]
NUMBER_OF_MIDI_VALUES = 128

# Paths
RAW_DATASET_PATH = 'data/raw_dataset/deutschl/test'
PREPROCESSED_DATASET_DESTINATION = 'data/preprocessed_dataset/individual_scores'
MERGED_DATASET_DESTINATION = 'data/preprocessed_dataset/merged_preprocessed_dataset'
LOOKUP_TABLE_DESTINATION = 'data/resources/lookup_table2.json'
