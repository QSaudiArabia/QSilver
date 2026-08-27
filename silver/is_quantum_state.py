# testing whether a given quantum state is valid
def is_quantum_state(quantum_state):
    length_square = 0
    for i in range(len(quantum_state)):
        length_square += abs(quantum_state[i])**2
    print("summation of entry squares is",length_square)
    # there might be precision problem
    # the length may be very close to 1 but not exactly 1
    # so we use the following trick
    if (length_square - 1)**2 < 0.00000001: return True 
    return False
for i in range(10):
    new_state = random_complex_quantum_state()
    print(new_state)
    print("Is it valid?",is_quantum_state(new_state))
