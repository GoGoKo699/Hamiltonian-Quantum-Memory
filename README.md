# Hamiltonian Quantum Memory

**Which part of a finite environment must remain quantum inside a physical emulator of its controlled dynamics?** A large bath can contain conserved classical labels, a smaller quantum factor that can store unknown states, and degrees of freedom invisible to the laboratory. This project determines the exact coherent-memory requirement after those roles are separated.

The target is one known, finite, time-independent system–bath Hamiltonian with a specified initial bath state. The laboratory has complete local control, finite working ancillas and arbitrary finite experiment duration. An emulator must accept actual quantum inputs and preserve their correlations with inaccessible references under the same interventions. Classical numerical prediction of described probabilities is a different task.

## Sharp memory–error law

Use the established stabilized control decomposition

```math
\mathcal H_E=\bigoplus_j\mathcal H_{B_j}\otimes\mathcal H_{Q_j},
\qquad r_j=\dim Q_j,\qquad p_j=\mathrm{Tr}(\Pi_j\tau_E).
```

Here j is a conserved sector, its Q factor is controllable through the laboratory port, and its B factor is invisible to future port experiments. This structure is inherited from Kato–Owari–Maruyama; the quantum/classical decomposition and general memory-cost frameworks also have established antecedents. The [related-work account](references/related_work.md) identifies them.

With unrestricted classical records and a hard maximum of D coherent hidden dimensions at every intervention boundary, the optimal uniform full-process error is

```math
\boxed{\displaystyle
\epsilon_D^\infty(H,\tau)=\sum_{j:r_j>D}p_j.}
```

The error uses half operational distance and is uniform over arbitrarily long **finite** experiments. The minimum exact coherent dimension is the largest occupied active-factor dimension. It can be much smaller than the physical bath dimension, and need not equal the initial bath rank.

| Consequence | Meaning |
| --- | --- |
| Exact tail of sector probabilities | Omitted sectors cost their total probability; a smaller coherent carrier cannot improve the unrestricted-time error. |
| Exact classical-memory boundary | Classical persistent memory suffices precisely when every occupied active factor is one-dimensional, even allowing invasive classical feedforward. |
| Finite repeated witness | A sector flag followed by store–reset–retrieve Bell tests gives a lower bound approaching the tail, against every dimension-limited emulator. |
| Finite-horizon limit | The optimal horizon-specific error tends to the same tail as duration grows; no universal convergence rate is claimed. |

The proof combines an exact low-sector emulator with a repeated quantum transmission test. At each designated cut all accessible quantum carriers are erased; only a sealed test reference remains outside the emulator. A D-dimensional hidden memory has Bell overlap at most D/r in an r-dimensional test. This standard one-round bound, iterated under arbitrary classical histories, supplies the sharp converse.

## Read the science

Start with the [connected scientific overview](science/README.md).

| Question | Authoritative account |
| --- | --- |
| What inputs, controls, memory and error are specified? | [Model](science/model.md) |
| What is inherited from indirect-control theory? | [Control structure](science/control_structure.md) |
| Why is the error exactly the omitted sector weight? | [Memory law and full proof](science/memory_law.md) |
| When does arbitrary classical feedforward suffice? | [Classical boundary](science/classical_boundary.md) |
| Can a weak coupling matter only at very long times? | [Examples and limiting order](science/examples.md) |
| Which costs and consequences are established? | [Interpretation and resources](science/interpretation.md) |
| How does the result compare with earlier work? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

The [LLM reading guide](llms.txt) maps detailed questions to the proofs and reproduction route.

## Reproduce the finite checks

```sh
python3 -m pip install -r verification/requirements.txt
python3 verification/check_science.py --output verification/results.json
```

The [verification guide](verification/README.md) states the actual matrix calculations and their limits. The all-size theorem rests on the analytical proof and its imported control theorem, rather than finite tests.

## Learn the mechanism

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the January 2018 standard-layout author manuscript. The [Watrous bridge](learning/WATROUS_BRIDGE.md) connects its channel, distance and entanglement foundations to the control theorem and repeated-memory argument, with conventions translated explicitly.

The [worked storage experiment](learning/WORKED_EXAMPLE.md) follows a Bell pair through an exact SWAP, full port reset, retrieval and measurement, then adds repetition and a rare quantum sector. The [30-milestone map](learning/MILESTONES.md) develops twelve background and eighteen narrative understanding targets in one connected route. Start with the [learning guide](learning/README.md), or use the specialist science route above.

## Scope

The theorem permits ideal local operations, exact resets, unrestricted finite laboratory ancillas and arbitrarily accurate control synthesis. A qubit port may be stabilized by one controllable laboratory qubit; that helper is erased at the memory cuts and is never an extra emulator port. All hidden persistent quantum systems count jointly toward the hard cap. No preshared entanglement or uncounted quantum side channel is supplied to an emulator.

The unlimited-time qualifier is essential. In the explicit qutrit–qubit example, any nonzero transverse bath term makes classical-memory emulation maximally distinguishable over unrestricted time, while a classical stand-in remains close over a fixed short horizon. Efficient identification, shortest witness time, noisy controls, optimal finite-time memory, thermodynamic savings and hardware advantage are outside the established result.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
