"""
dirac_notation.py

Small helper authored for the Qiskit port of QWorld's Silver material.

Cirq's simulator prints statevectors by default in a compact ket-notation
string, e.g. "0.5|00⟩ - 0.5|01⟩ + 0.5|10⟩ - 0.5|11⟩". Qiskit has no exact
built-in equivalent, so this reproduces that style for a qiskit
Statevector (or anything Statevector(...) accepts, e.g. a QuantumCircuit)
so the ported notebooks read the same way the original Cirq ones did.
"""

from qiskit.quantum_info import Statevector


def _format_amplitude(amp, tol):
    re, im = amp.real, amp.imag
    if abs(im) < tol:
        return f"{re:.4g}", re >= 0
    if abs(re) < tol:
        return f"{im:.4g}j", im >= 0
    sign = "+" if im >= 0 else "-"
    return f"({re:.4g}{sign}{abs(im):.4g}j)", True


def dirac_notation(state, tol=1e-8):
    """Format a statevector in ket notation, e.g. '0.5|00> - 0.5|01> + ...'.

    Parameters
    ----------
    state : Statevector | QuantumCircuit | array-like
        Anything qiskit.quantum_info.Statevector(...) accepts.
    tol : float
        Amplitudes with magnitude below this are dropped (numerical noise).
    """
    if not isinstance(state, Statevector):
        state = Statevector(state)

    n = state.num_qubits

    # Qiskit's native bit order puts qubit 0 as the rightmost (least
    # significant) character. The original Cirq notebooks print qubit 0
    # (the "first" qubit, q1) as the LEFTMOST character instead — e.g.
    # Cirq's |10> means "q1=1, q2=0". Reversing here matches that
    # convention so this reads the same way the original notebooks did,
    # and matches how qft()/iqft() in iqft.py are written (qubits[0] is
    # treated as the "first" qubit throughout, exactly as in the original
    # Cirq code, not as Qiskit's own least-significant qubit). Terms are
    # then sorted by that Cirq-style index so they print in the same
    # ascending order Cirq's default output used, not Qiskit's native order.
    entries = []
    for idx, amp in enumerate(state.data):
        if abs(amp) < tol:
            continue
        label = format(idx, f"0{n}b")[::-1]
        cirq_order_idx = int(label, 2)
        entries.append((cirq_order_idx, label, amp))
    entries.sort(key=lambda e: e[0])

    parts = []
    for _, label, amp in entries:
        coeff, positive = _format_amplitude(amp, tol)
        coeff = coeff.lstrip("-")
        parts.append(("+" if positive else "-", f"{coeff}|{label}⟩"))

    if not parts:
        return "0"

    first_sign, first_term = parts[0]
    out = first_term if first_sign == "+" else f"-{first_term}"
    for sign, term in parts[1:]:
        out += f" {sign} {term}"
    return out
