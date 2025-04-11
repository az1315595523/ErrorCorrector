class CONFIG:
    INPUT_DIR = 'data/ori_code'
    OUTPUT_DIR = 'data/mutated_code'

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
