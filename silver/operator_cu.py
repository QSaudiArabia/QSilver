"""
operator_cu.py

Qiskit port of QWorld Silver's shared `operator_cu.py` (originally Cirq),
used by D03 Task 6 (a fixed "mystery" controlled-unitary with an unknown
eigenvalue, for practicing phase estimation) and by D04-D06 (`Ux(x, N)`,
the modular-multiplication operator used throughout order finding and
Shor's algorithm).

Both are ported the same way: build the raw unitary matrix (unchanged
math from the original) and wrap the already-controlled matrix directly
as a single Qiskit `UnitaryGate` — the direct analogue of Cirq's
`cirq.MatrixGate(u).controlled()`. This is also exactly the general
"permutation-matrix" approach IBM's own Shor's-algorithm tutorial uses
for its `mod_mult_gate`.

Implementation note: building the controlled matrix by hand and wrapping
*that* in one `UnitaryGate` is functionally identical to
`UnitaryGate(u).control(1)` (verified numerically) but avoids Qiskit's
general controlled-gate synthesis path, which is dramatically slower for
a matrix this size (~5s vs ~5ms per call for the N=42 case used in D04
Task 7) — worth doing since `qpe()` calls `.power()` on this gate once
per control qubit. Qiskit's qubit convention makes the *first* qubit
passed to a gate its least-significant one, so the control qubit (passed
first, per `qpe.py`) sits on the matrix's LSB, not as a simple upper-left/
lower-right block split — the controlled matrix is `kron(I, P0) + kron(u, P1)`
with `P0 = |0><0|`, `P1 = |1><1|`, not `scipy.linalg.block_diag(I, u)`
(that alternative was tried and is silently wrong for anything but a
diagonal U, where swapping which half is "block 0" happens not to matter).
"""

import numpy as np
from qiskit.circuit.library import UnitaryGate

_P0 = np.array([[1, 0], [0, 0]], dtype=complex)  # |0><0|
_P1 = np.array([[0, 0], [0, 1]], dtype=complex)  # |1><1|


def _controlled_matrix(u):
    """Build the matrix for controlled-`u`, control qubit on the LSB (matches
    Qiskit's "first qubit passed to a gate is its LSB" convention, with the
    control passed first — see module docstring)."""
    dim = u.shape[0]
    return np.kron(np.eye(dim), _P0) + np.kron(u, _P1)


# --- D03 Task 6: fixed operator with an unknown eigenvalue, for practice ---
array = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -0.4762382 + 0.87931631j]])

U = UnitaryGate(array, label="U")
CU = UnitaryGate(_controlled_matrix(array), label="CU")


# --- D04-D06: general modular-multiplication operator ---
def Ux(x, N):
    """Controlled "multiply by x mod N" operator, as a Qiskit Gate.

    Apply as `circuit.append(Ux(x, N), [control_qubit] + target_qubits)`
    where `target_qubits` holds a k-qubit register (k = ceil(log2(N))).
    """

    k = 1
    while N > 2**k:
        k = k + 1

    u = np.zeros([2**k, 2**k], dtype=complex)

    for i in range(N):
        u[x * i % N][i] = 1
    for i in range(N, 2**k):
        u[i][i] = 1

    XU = UnitaryGate(_controlled_matrix(u), label=f"CU_{x}")
    return XU
