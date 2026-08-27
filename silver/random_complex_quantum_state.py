from random import randrange
def random_complex_quantum_state():
    # quantum state    
    quantum_state=[0,0]
    length_square = 0
    while length_square == 0:
        first_entry_real = randrange(-100,101)
        first_entry_imag = randrange(-100,101)
        second_entry_real = randrange(-100,101)
        second_entry_imag = randrange(-100,101)
        length_square = first_entry_real**2+first_entry_imag**2+second_entry_real**2+second_entry_imag**2
    first_entry_real = first_entry_real / length_square**0.5
    first_entry_imag = first_entry_imag / length_square**0.5
    second_entry_real = second_entry_real / length_square**0.5
    second_entry_imag = second_entry_imag / length_square**0.5
    quantum_state[0] = complex(first_entry_real, first_entry_imag)
    quantum_state[1] = complex(second_entry_real, second_entry_imag)
    return quantum_state
