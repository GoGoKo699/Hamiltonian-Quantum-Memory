# When a static bath has a classical explanation

[Model](model.md) · [Control structure](control_structure.md) · [Memory law](memory_law.md)

Classical memory can be invasive. A classical simulator may measure the incoming system, retain the result, update an arbitrarily large classical record, and condition later channels on that record. Such a model is more general than sampling one static noise label at the beginning. The theorem below excludes this full feedforward class of physical quantum-port emulators when an active controllable bath factor is genuinely quantum. It does not exclude classical numerical prediction given complete classical descriptions.

## Exact boundary for a fixed initial bath

Under the complete all-time intervention model, the following are equivalent:

1. The process has a compatible exact simulator with only classical persistent memory.
2. Every active bath factor has $`r_j=1`$.
3. On the invariant sum of active sectors, the Hamiltonian admits a fixed environment basis that controls system Hamiltonians.

In condition 3 the enlarged laboratory is understood as in the [model](model.md). Since its helper is uncoupled in the physical drift, the controlled-basis form also restricts to the original system Hamiltonian.

The equivalence of 1 and 2 follows immediately from the [memory theorem](memory_law.md) at $`D=1`$:

```math
\epsilon_1^\infty
=\sum_{j:r_j>1}p_j.
```

If 2 holds, the drift decomposition becomes, on active sectors,

```math
H_{E\bar S}
=\bigoplus_{j:p_j>0}
 \left(G_j\otimes I_{\bar S}
       +I_{B_j}\otimes K_j\right).
```

Diagonalize each Hermitian $`G_j`$. Its bath eigenvectors, together with the sector label, form one fixed orthonormal bath basis $`\{|\nu\rangle\}`$ for which

```math
H_{E\bar S}\big|_{\rm active}
=\sum_\nu |\nu\rangle\langle\nu|_E
 \otimes H_\nu^{\bar S}.
```

The scalar bath eigenvalue may be included in $`H_\nu^{\bar S}`$. In the physical drift $`H_{E\bar S}=H_{ES}\otimes I_Z`$ when a helper is used. Taking the normalized partial trace over $`Z`$ yields the same controlled-bath form with system operators $`H_\nu^S`$. This proves 3.

Conversely, suppose 3 holds. Every idle interval has the form

```math
U_t=\sum_\nu |\nu\rangle\langle\nu|_E
 \otimes e^{-itH_\nu^S}.
```

All laboratory operations preserve the bath basis label. Off-diagonal matrix elements of the initial bath state vanish on the final bath trace, so the complete process is reproduced by drawing $`\nu`$ at the start with probability $`\langle\nu|\tau_E|\nu\rangle`$, then applying the corresponding unitary at every idle interval. This is a compatible classical simulator and proves 1.

## Classical common cause versus general classical memory

The simulator just constructed is a **classical common-cause** model: one latent label is drawn once and the conditional evolution is Markovian. It is a convex mixture of unitary process families. The class tested by condition 1 is larger: it includes arbitrary classical measurement and feedforward updates during the experiment.

Thus, for this static finite-bath family with complete controls, allowing classical feedforward does not enlarge the class of exactly classically simulable targets. If it can be simulated with general classical memory, it already has a common-cause explanation. This equivalence is a statement about the entire all-time intervention family. It need not hold for a fixed time grid, restricted instruments, or a finite list of reduced channels.

## Faithful states and inactive sectors

If $`\tau_E`$ is faithful, every sector has positive weight. The boundary then applies to the full Hamiltonian:

```math
\text{exact classical simulation of the complete family}
\quad\Longleftrightarrow\quad
H=\sum_\nu|\nu\rangle\langle\nu|_E\otimes H_\nu^S.
```

The same full-Hamiltonian equivalence holds if classical simulation is required for every initial bath state. A universal initial-state requirement includes a faithful state; the controlled form conversely works for every state.

For a nonfaithful supplied state, the active-sector qualification is essential. A Hamiltonian may have an unused invariant sector containing genuinely quantum interactions. Initializing the bath entirely outside that sector makes those interactions operationally irrelevant for the supplied process. The theorem does not infer a global fixed-basis form from an inactive part of the bath. Inside an active factor, however, even a pure initial state does not avoid the obstruction: controls can replace it by an unknown payload before the full laboratory reset.

## Relation to the Hamiltonian conjecture

Goswami and collaborators, *Hamiltonian characterization of multi-time processes with classical memory*, New J. Phys. **27**, 114515 (2025), [arXiv:2412.01998v2](https://arxiv.org/abs/2412.01998v2), establish the fixed-bath-basis sufficient condition. Their formal Conjecture 1 concerns a time-independent Hamiltonian generating a classical common-cause process for every choice of probing times. Their general classical-memory models also allow feedforward; the two classes must be distinguished.

The present boundary gives a converse for the complete ancillary-assisted process family, with an explicit initial-state qualification, and excludes the broader classical-memory class through the memory theorem. A faithful supplied bath state is sufficient; arbitrary bath preparation is not required. This is not a claim about deciding quantum memory from passive channel tomography alone.

The proof is a connection to the inherited indirect-control decomposition. It does not introduce a new classification of dynamical Lie algebras or a new definition of classical process memory. Entangling eigenvectors by themselves are not the criterion: degeneracies, spectator factors, initial sector weights and the actual control model matter.

## Finite-time caution

A positive value of $`\epsilon_1^\infty`$ says that an arbitrarily accurate classical explanation fails uniformly over unlimited finite experiments. It does not say that a short experiment can distinguish that explanation. If $`H_\lambda=H_0+\lambda V`$, then standard unitary telescoping bounds any tester of total idle duration $`T`$ by a discrepancy at most $`|\lambda|T\lVert V\rVert`$ when $`H_0`$ is used as a stand-in. This bound also covers adaptive interventions by contractivity and summing their branchwise elapsed durations under a hard horizon.

Consequently the limits of weak coupling and long observation need not commute. The [memory law](memory_law.md) preserves that distinction: its horizon statement is a limit without a universal convergence rate.

The [qutrit–qubit example](examples.md) has $`\epsilon_1^\infty=1`$ at every nonzero bath-rotation strength, while a classical stand-in has finite-horizon error at most the strength times $`T`$. It makes the scope of the structural boundary explicit.
