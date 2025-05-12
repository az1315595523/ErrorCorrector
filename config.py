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
    MUTATION_SIZE = 50
    MUTATION_RATE = [
        0.015,   # bracket
        0.015,   # colon
        0.050,   # function
        0.025,   # indent
        0.080,   # module
        0.130,   # operator
        0.020,   # quote
        0.125,   # variable
        0.130,   # condition
        0.120,   # Boundary
        0.042,   # Array
        0.058,   # ArgMutator
        0.090,   # ControlFlowMutator
        0.085    # EmptyStructureMutator
        #  total 0.985
    ]
    MUTATION_TIMES_RATE = [
        0.0235,
        0.0350,
        0.0490,
        0.0645,
        0.0800,
        0.0932,
        0.1022,
        0.1052,
        0.1022,
        0.0932,
        0.0800,
        0.0645,
        0.0490,
        0.0350,
        0.0235
    ]

