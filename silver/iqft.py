"""
iqft.py

Qiskit port of QWorld Silver's D02 Task 9 (originally Cirq).
Both qft() and iqft() live here so downstream notebooks (D03-D06) can
`from iqft import qft, iqft` exactly like the original `%run iqft.py` /
`%load iqft.py` pattern, just adapted to plain imports.

Signature mirrors the original as closely as possible: qft(n, qubits, circuit)
and iqft(n, qubits, circuit), where `circuit` is a QuantumCircuit and
`qubits` is a list/range of qubit indices (or Qubit objects) inside it —
this lets these functions be applied to a sub-register of a larger circuit,
which D04/D05/D06 need (the QFT is only applied to the control register,
not the whole circuit).
"""

from math import pi


def qft(n, qubits, circuit):
    """Apply QFT to `qubits` (length n) of `circuit`, in place."""
    for i in range(n):
        circuit.h(qubits[i])

        k = 2
        for j in range(i + 1, n):
            circuit.cp(2 * pi / 2**k, qubits[j], qubits[i])
            k += 1

    for i in range(n // 2):
        circuit.swap(qubits[i], qubits[n - i - 1])

    return circuit


def iqft(n, qubits, circuit):
    """Apply QFT^dagger to `qubits` (length n) of `circuit`, in place."""
    for i in range(n // 2):
        circuit.swap(qubits[i], qubits[n - i - 1])

    for i in range(n - 1, -1, -1):
        k = n - i
        for j in range(n - 1, i, -1):
            circuit.cp(-2 * pi / 2**k, qubits[j], qubits[i])
            k -= 1
        circuit.h(qubits[i])

    return circuit
