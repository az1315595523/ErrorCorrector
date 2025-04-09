class CONFIG:
    INPUT_DIR = 'data/ori_code'
    OUTPUT_DIR = 'data/mutated_code'

    MUTATION_RATE = [
        0.01,   # bracket
        0.02,   # colon
        0.08,   # function
        0.02,   # indent
        0.04,   # module
        0.15,   # operator
        0.05,   # quote
        0.15,   # variable
        0.22,   # condition
        0.08,   # Boundary
        0.08    # Array
        #  total 0.9
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
