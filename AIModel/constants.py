# Durations are limited to the most basic ones 
SUPPORTED_DURATIONS = [
    0.25, # Semicorchea/Step  (ignoramos semicorchea con punto porque usa fusas)
    0.5,  # Corchea
    0.75, # Corchea con punto
    1,    # Negra
    1.5,  # Negra con punto
    2,    # Blanca 
    3,    # Blanca con punto
    4     # Redonda
]
STEP_DURATION = 0.25   # In relation to a quarter note (basically a 16th note)


# PATHS
RAW_DATASET_PATH = 'deutschl/test'
