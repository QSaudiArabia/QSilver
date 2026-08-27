# QSilver39 (Qiskit-only) — 4-Day Schedule → Notebook Map

Maps the locked 4-day QSaudi Arabia schedule (source: `QSilver_Opening_Module_and_4Day_Schedule.md`, Ahmed Elghadban / QSaudi Arabia, English source-of-truth draft) to the actual notebook filenames in this repository. Sessions are 3 hours/day, 18:00–21:00 Riyadh, with two prayer breaks inside the window — real teaching time is roughly 140–160 minutes/day, not a naive 180.

This repo keeps the original upstream QWorld `silver/` folder layout unchanged (flat, not reorganized into day folders) — this file is the only new addition mapping schedule to files, so the repo stays easy to diff/re-sync against upstream QWorld later.

Every notebook below is Qiskit-only. Cirq has been fully removed from this repository (see `README.md` / project history) — `D00_Cirq_Introduction*`, `silver/order.py`, `silver/qft.py`, `silver/operator.ipynb`, and `test/Cirq_installation_and_test.ipynb` from the original upstream repo are intentionally **not** included here, as they are either redundant with Qiskit-based material or superseded by this repo's Qiskit ports.

## Day 1 — Foundations: why quantum algorithms work, and the language of qubits

Tightest day — opening module is new content layered on top of the original material, so C04 moves to Day 2.

- **Opening module** (~40–45 min, tightly run): state of the art / quantum utility today, what makes a quantum algorithm different, a plain-language P/NP/BQP primer, the four quantum-algorithm paradigms (Simulation / Optimization / QML / Algebraic & Search), NISQ + hybrid quantum-classical algorithms, and explicit day-by-day learning objectives. Delivered from the training presentation (not a notebook) — see the Phase 3 training deck once built.
  - Ahmed's 5-minute personal-journey intro opens the course as a standalone slot, ahead of this module.
- **A00 — Qiskit introduction** (lightened to a recap; QBronze already covers Qiskit basics):
  `silver/A00_Qiskit_Introduction.ipynb` | `silver/A00_Qiskit_Introduction_Solutions.ipynb`
- **C01 — Complex number basics**:
  `silver/C01_Complex_Number_Basics.ipynb` | `silver/C01_Complex_Number_Basics_Solutions.ipynb`
- **C02 — Mathematical notations & quantum states with complex numbers**:
  `silver/C02_Mathematical_Notations.ipynb` | `silver/C02_Mathematical_Notations_Solutions.ipynb`
  `silver/C02_Quantum_States_With_Complex_Numbers.ipynb` | `silver/C02_Quantum_States_With_Complex_Numbers_Solutions.ipynb`
- **C03 — Quantum operators with complex numbers**:
  `silver/C03_Quantum_Operators_With_Complex_Numbers.ipynb` | `silver/C03_Quantum_Operators_With_Complex_Numbers_Solutions.ipynb`
- *Homework / pre-read (assigned before Day 1, not taught live)*: `silver/R00_Intro_to_Notebooks.ipynb`, `silver/R01_Python_Reference.ipynb`, `silver/R02_Python_Drawing.ipynb`

**By the end of Day 1**, students can: explain why quantum computers gain advantage through interference rather than brute-force parallelism; correctly place quantum advantage within the P/NP/BQP landscape and explain why Shor's algorithm doesn't imply quantum computers solve NP-hard problems in general; name the four quantum-algorithm paradigms and place factoring/search within them; represent and manipulate qubit states and operators using complex numbers in Qiskit.

## Day 2 — Representing qubits, and the Fourier idea

- **C04 — Quantum gates with complex numbers** (moved from Day 1):
  `silver/C04_Quantum_Gates_With_Complex_Numbers.ipynb` | `silver/C04_Quantum_Gates_With_Complex_Numbers_Solutions.ipynb`
- **C05 — Global and local phase**:
  `silver/C05_Global_And_Local_Phase.ipynb` | `silver/C05_Global_And_Local_Phase_Solutions.ipynb`
- **C06 — State conversion and visualization**:
  `silver/C06_State_Conversion_And_Visualization.ipynb` | `silver/C06_State_Conversion_And_Visualization_Solutions.ipynb`
- **C07 — Bloch sphere**:
  `silver/C07_Bloch_Sphere.ipynb` | `silver/C07_Bloch_Sphere_Solutions.ipynb`
- **C08 — Operations on the Bloch sphere**:
  `silver/C08_Operations_On_Bloch_Sphere.ipynb` | `silver/C08_Operations_On_Bloch_Sphere_Solutions.ipynb`
- **C09 — Multiqubit operations**:
  `silver/C09_Multiqubit_Operations.ipynb` | `silver/C09_Multiqubit_Operations_Solutions.ipynb`
- **D01 — Discrete Fourier Transform** (classical, math-only — quick):
  `silver/D01_Discrete_Fourier_Transform.ipynb` | `silver/D01_Discrete_Fourier_Transform_Solutions.ipynb`
- **D02 — Quantum Fourier Transform** (Qiskit port — derivation + `iqft.py`/`dirac_notation.py` helpers):
  `silver/D02_Quantum_Fourier_Transform.ipynb` | `silver/D02_Quantum_Fourier_Transform_Solutions.ipynb`

**By the end of Day 2**, students can: visualize single-qubit states and operations on the Bloch sphere, including global vs. local phase; extend single-qubit representations to multi-qubit systems; explain the DFT and derive the QFT as its quantum analogue; implement a QFT circuit (and its inverse) in Qiskit from first principles (Hadamard + controlled-phase + swap gates).

## Day 3 — Phase estimation and order finding

- **D03 — Phase Estimation** (Qiskit port — phase kickback, QPE circuit via `qpe.py`, worked examples):
  `silver/D03_Phase_Estimation.ipynb` | `silver/D03_Phase_Estimation_Solutions.ipynb`
- **D04 — Order Finding Algorithm** (Qiskit port — connects QPE to order-finding via `operator_cu.py`, continued fractions via `include/helpers.py`):
  `silver/D04_Order_Finding_Algorithm.ipynb` | `silver/D04_Order_Finding_Algorithm_Solutions.ipynb`

**By the end of Day 3**, students can: explain the phase-kickback mechanism behind controlled-unitary operations; implement a QPE circuit in Qiskit and use it to estimate an unknown eigenvalue; connect phase estimation to the order-finding problem and explain why order-finding is classically hard.

## Day 4 — Shor's Algorithm, and closing the loop

- **D05 — Shor's Algorithm** (Qiskit port — full algorithm walkthrough, factor 21 end-to-end):
  `silver/D05_Shors_Algorithm.ipynb` | `silver/D05_Shors_Algorithm_Solutions.ipynb`
- **Closing**: revisit the Day-1 "where do we stand today" framing now that students have built the whole algorithm themselves — explicit tie-back to the opening talk, and a natural point for Q&A / wrap-up.

**By the end of Day 4**, students can: implement modular exponentiation operators in Qiskit and use them inside an order-finding circuit; use continued fractions to recover an order estimate from measured phase data; walk through Shor's algorithm end-to-end (order-finding → classical post-processing → factors) and explain each step's purpose; articulate honestly what stands between today's hardware and running Shor's algorithm at cryptographically-relevant scale.

## Self-study only (not live-taught)

- **D06 — Shor's Algorithm in More Detail** (Qiskit port — removed from live teaching per Ahmed's call; D05 already carries the algorithm end-to-end. D06's fully-worked N=15 walkthrough is trainee-guide self-study material only):
  `silver/D06_Shors_Algorithm_In_More_Detail.ipynb` | `silver/D06_Shors_Algorithm_In_More_Detail_Solutions.ipynb`

## Reference / credits (not scheduled — background material)

- `silver/S00_Credits.ipynb`, `silver/S01_References.ipynb`
- `test/Qiskit_QuTiP_installation_and_test.ipynb` — installation/environment check, referenced from `content.ipynb`'s "Installation and Test" section
- `installation.pdf` — Anaconda/Jupyter setup guide (framework-agnostic, unaffected by the Cirq removal)

---

*Open items still pending confirmation from QSaudi Arabia before this schedule is fully final: exact prayer-break timing/duration within the 18:00–21:00 window, and whether R00–R02 as pre-reading is acceptable for all cohort members or needs to be taught live. See `QSilver_Opening_Module_and_4Day_Schedule.md` for full detail.*
