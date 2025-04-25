class CONFIG:

    ENCODER_PATH = "Corrector/graphcodebert/graphcodebert-base"
    DECODER_PATH = "Corrector/codeGPT/CodeGPT-small-py"
    TRAIN_DATA_DIR = "data/dataset"
    SAVE_DIR = "Corrector/CorrectorModel"
    LOG_DIR = "Corrector/log"

    NO_CUDA = False
    MAX_SOURCE_LENGTH = 512
    MAX_TARGET_LENGTH = 512

    WEIGHT_DECAY = 0.0
    ADAM_EPSILON = 1e-8
    GRADIENT_ACCUMULATION_STEPS = 1
    MAX_LENGTH = 256
    BATCH_SIZE = 2
    LEARNING_RATE = 1e-5
    EPOCHS = 20
    BEAM_SIZE = 10

    INPUT_DIR = 'data/ori_code'
    OUTPUT_DIR = 'data/mutated_code'
    MUTATION_SIZE = 10
    MUTATION_RATE = [
        0.005,   # bracket
        0.005,   # colon
        0.080,   # function
        0.005,   # indent
        0.040,   # module
        0.200,   # operator
        0.005,   # quote
        0.200,   # variable
        0.200,   # condition
        0.120,   # Boundary
        0.120    # Array
        #  total 0.98
    ]
    MUTATION_TIMES_RATE = [
        0.01,
        0.04,
        0.06,
        0.09,
        0.13,
        0.17,
        0.17,
        0.13,
        0.09,
        0.06,
        0.04,
        0.01
    ]
