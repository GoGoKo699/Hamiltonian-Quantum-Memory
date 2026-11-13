# From Watrous to Hamiltonian quantum memory

[Learning route](README.md) · [Worked example](WORKED_EXAMPLE.md) · [Milestone map](MILESTONES.md)

The one educational anchor is John Watrous, *The Theory of Quantum Information* (2018). Section references below identify the **January 2018 author manuscript, standard layout** available from the [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/). The [front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) verifies its section names and preface date. The project supplies the steps needed beyond those foundations.

## Relevant textbook sections

| Section in the selected manuscript | Foundation | Its use here |
| --- | --- | --- |
| [2.1 Registers and states](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), especially 2.1.3, Reductions and purifications of quantum states | Joint states and partial traces | A returned payload must preserve its correlations with a reference. |
| [2.2 Quantum channels](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), especially 2.2.1–2.2.2 | Completely positive, trace-preserving transformations and their representations | Preparations, idle evolutions and resets are actual physical maps. |
| [2.3 Measurements](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Outcomes obtained from positive measurement operators | A Bell test produces a pass or failure; both outcomes count. |
| [3.1 Quantum state discrimination](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) and 3.3, Channel distances and discrimination, especially 3.3.2 | Distinguishability and reference-assisted channel norms | The emulator must match operational observations, including correlated inputs. |
| [6.1 Separability](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), especially 6.1.2, and 6.2.1, Entanglement transformation | Quantum correlations and restrictions on local processing | Classical records cannot carry an arbitrary entangled payload across an erased laboratory. |

These are entry points rather than a claim that the book proves the project's control or process-memory theorems. In particular, Section 2.3 concerns measurements; purification belongs to Section 2.1.3.

## The physical roles behind the notation

| Project symbol | Physical role |
| --- | --- |
| $`S`$ | The visible quantum port through which the laboratory interacts. |
| $`E`$ | The inaccessible finite bath, initially independent of laboratory inputs. |
| $`A`$ | Finite laboratory work systems; they are erased at storage cuts. |
| $`R`$ | The sealed test reference, retained only to check the retrieved payload. |
| $`Q_j`$ | The bath factor that can store arbitrary quantum information in sector $`j`$. |
| $`B_j`$ | An invisible bath multiplicity factor whose state need not be retained. |
| $`D`$ | The hard maximum dimension of all persistent private emulator quantum systems together. |
| $`p_j`$ | The probability that the supplied initial bath occupies sector $`j`$. |

The book's registers and channels can represent every item in one finite experiment. Here the letters emphasize their distinct physical permissions. A reference is not an extra emulator input. A classical record must remain classical; its many possible labels do not supply a coherent quantum carrier.

## Three translations that matter

### A reset erases correlations as well as a local state

For a working register $`W`$, a reset to a fixed state $`\omega_W`$ is

```math
\mathcal R_W(X)=\operatorname{Tr}(X)\,\omega_W.
```

When applied to part of a joint state, it discards that register and prepares a replacement independent of the rest. Keeping a purification in another accessible work register would defeat this reset. The distinguishing experiment therefore erases **all** accessible quantum work systems, not just the port. The sealed reference survives, but cannot interact with any controller across the cut.

### A probability is the directly measured quantity

For a two-qubit Bell state $`|\Phi_2\rangle=(|00\rangle+|11\rangle)/\sqrt2`$, the pass probability on output state $`\rho_{RS}`$ is

```math
P_{\mathrm{pass}}
=\langle\Phi_2|\rho_{RS}|\Phi_2\rangle.
```

Watrous uses the unsquared, or root, fidelity convention. For this pure target the displayed probability equals the **square** of that fidelity. The proof uses the probability itself. A favorable conditional outcome is not free success: all failed outcomes remain in the distribution.

### The distance includes a factor of one half

The project's state-distance convention is $`\tfrac12\|\rho-\sigma\|_1`$. Its one-channel analogue is half the completely bounded trace norm from Section 3.3.2, commonly called the diamond norm. A process has several intervention slots, so [the model](../science/model.md#distance-and-order-of-quantifiers) optimizes distinguishability over finite causal experiments rather than replacing the whole process by one passive channel snapshot.

The normalized Bell projector used in a test has trace one. Under the usual unnormalized Choi convention, the Choi operator of a qubit identity channel is twice that projector. This normalization changes neither the physical channel nor the test, but it matters when reading formulas.

## What must be added to the textbook foundations

**A causal memory model.** The emulator receives actual quantum inputs as they arrive. It cannot receive the unknown state of the reference or future private choices. It may adapt using an unlimited classical history. Its coherent storage is bounded at every intervention boundary. This is stronger than asking for a numerical prediction of a fully described experiment. The definitions and quantifiers are in [the model](../science/model.md).

**An inherited control theorem.** The Kato–Owari–Maruyama theorem supplies the stabilized bath decomposition

```math
\mathcal H_E=\bigoplus_j\mathcal H_{B_j}\otimes\mathcal H_{Q_j}.
```

Its independent connected control allows a sector to be recorded classically and an unknown payload to be written into and retrieved from $`Q_j`$. A qubit port is first enlarged by a controllable laboratory qubit; that helper is also erased at the memory cuts. [Control structure](../science/control_structure.md) states the imported theorem, the required closure argument and the resulting operations. These are research-level dependencies, not topics attributed to Watrous.

**A repeated operational argument.** A memory of dimension $`D`$ can preserve Bell overlap at most $`D/r`$ across a complete working-laboratory reset for an $`r`$-dimensional payload. The mixed-state Schmidt-number bound is an inherited ingredient, with attribution and proof in [the memory argument](../science/memory_law.md#a-one-round-dimension-lemma). Fresh references let that bound be applied after every prior classical history. This does not require independent emulator errors.

For $`n`$ repeated tests and total control-approximation error $`\eta`$, one finite tester has separation at least

```math
q_D-\left(\frac{D}{D+1}\right)^n-\eta,
\qquad
q_D=\sum_{j:r_j>D}p_j.
```

An emulator can also reproduce every sector with $`r_j\leq D`$ exactly and replace the others at total error at most $`q_D`$. These two directions give the [sharp law](../science/memory_law.md)

```math
\epsilon_D^\infty(H,\tau)=q_D.
```

Each chosen tester is finite, but approaching the tail can require longer experiments and more accurate control. The theorem does not supply a universal witness time. The [worked example](WORKED_EXAMPLE.md) makes the storage cut explicit; [the scientific examples](../science/examples.md) show why a weak bath term can be negligible at fixed time and decisive over unrestricted time.

[Learning route](README.md) · [Milestone map](MILESTONES.md) · [Sources and attribution](../references/related_work.md)
