"""
qpe.py

Qiskit port of QWorld Silver's D03 Task 3 (originally Cirq).
Generic Quantum Phase Estimation: given a black-box controlled-unitary
gate CU (as a Qiskit Gate/Instruction that supports `.power(k)`, e.g.
CPhaseGate, or a UnitaryGate built via `some_unitary_gate.control()`),
estimate the phase φ of an eigenvector loaded into `target`.

Signature mirrors the original: qpe(t, control, target, circuit, CU),
where `control` is a list of t qubit indices, `target` is a list of the
qubit indices holding the eigenvector, `circuit` is a QuantumCircuit, and
CU is the controlled-U gate (first qubit it acts on is the control, the
rest are the target register — exactly like Cirq's `CUi(control[...], *target)`).
"""

from iqft import iqft


def qpe(t, control, target, circuit, CU):
    """Apply phase estimation to `circuit`, in place, and return it."""

    # Apply Hadamard to control qubits
    for q in control:
        circuit.h(q)

    # Apply CU gates
    for i in range(t):
        # Obtain the power of CU gate
        CUi = CU.power(2**i)
        # Apply CUi gate where t-i-1 is the control.
        #
        # Qubit-order note: throughout this port `target[0]` is the "first"/
        # most-significant qubit of the target register (same convention as
        # iqft.py and dirac_notation.py), matching the original Cirq code's
        # big-endian qubit ordering. Qiskit's own gate/statevector convention
        # is little-endian (the *first* qubit passed to a gate is its least
        # significant one), so we must pass the target qubits in reverse to
        # get the matrix built by e.g. operator_cu.py's `Ux(x, N)` (which
        # indexes its permutation matrix the same way the original Cirq code
        # did) to line up correctly. For a single target qubit, or a
        # symmetric operator, this reversal is a no-op.
        circuit.append(CUi, [control[t - i - 1]] + list(reversed(target)))

    # Apply inverse QFT
    iqft(t, control, circuit)

    return circuit
