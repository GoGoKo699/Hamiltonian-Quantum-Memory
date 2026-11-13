# Model and operational question

[Control structure](control_structure.md) · [Memory law](memory_law.md) · [Classical boundary](classical_boundary.md)

The object being approximated is a finite bath reused under arbitrary interventions. A simulator must reproduce one causal experiment as its inputs and interventions arrive. It does not receive a description of future private choices or the state of an inaccessible reference. The task is physical emulation through a quantum port, preserving arbitrary input and reference correlations. It is not classical numerical prediction of probabilities for a fully described experiment; unrestricted classical computation can perform that different task in finite dimension.

## Physical process

Let $`S`$ be a finite-dimensional accessible port with $`d_S\ge2`$, and let $`E`$ be a finite-dimensional inaccessible environment. Fix a known Hermitian Hamiltonian $`H`$ on $`E\otimes S`$, with $`\hbar=1`$, and a known environment state $`\tau_E`$. Every experiment starts with $`\tau_E`$ independent of the laboratory and its references. Between interventions the physical joint evolution is

```math
U_t=e^{-itH},\qquad t\ge0.
```

The bath is not refreshed between intervals. Its state need not be pure, faithful, thermal, or stationary under its local Hamiltonian.

The laboratory may append arbitrary finite working systems $`A`$, initially independent of $`E`$, and perform instantaneous quantum instruments on $`S\otimes A`$. Such instruments include unitaries, preparations, measurements, discards, and trace-and-replace channels. Idle intervals may be chosen adaptively using the observed classical record. Each experiment has finitely many interventions and finite total idle duration, although neither quantity has a common bound in the main theorem. There is no direct operation on $`E`$.

A reference $`R`$ may be entangled with a laboratory input. It is not supplied to the process or simulator. In the storage tests used below it is sealed: it does not interact with the port or any controller until the terminal Bell measurement. This reference is retained to test quantum transmission; it is not a carrier around a reset.

The main theorem uses ideal local controls and unrestricted finite ancillary dimensions. These are resource assumptions. It gives no bound on the time, pulse count, precision, or computation required to compile an indirectly accessible bath operation.

## Stabilized control decomposition

If $`d_S\ge3`$, set $`\bar S=S`$. If $`d_S=2`$, append one laboratory qubit $`Z`$ and set $`\bar S=S\otimes Z`$. The extended drift is $`H\otimes I_Z`$; the laboratory controls $`\bar S`$ completely. The auxiliary qubit belongs to the working laboratory and is reset with it in the converse tests.

Apply the inherited Kato–Owari–Maruyama control decomposition to this port of dimension at least three. It gives

```math
\mathcal H_E=\bigoplus_{j=1}^{J}
 \mathcal H_{B_j}\otimes\mathcal H_{Q_j},
\qquad r_j=\dim\mathcal H_{Q_j}.
```

Here $`B_j`$ is an invisible multiplicity factor, $`Q_j`$ is an indirectly controllable factor, and $`j`$ is a conserved sector. The proof transfer and ancillary stability are stated in [Control structure](control_structure.md). Further finite laboratory ancillas preserve these same bath factors. The decomposition is used as a mathematical invariant of the supplied Hamiltonian and control model; it is not inferred for free from experimental data.

Let $`\Pi_j`$ project onto sector $`j`$, and define

```math
p_j=\mathrm{Tr}(\Pi_j\tau_E),\qquad
q_D=\sum_{j:r_j>D}p_j,\qquad D\in\mathbb N,\ D\ge1.
```

The weights depend on the supplied initial bath state. Sectors with $`p_j=0`$ are inactive. A positive semidefinite state has no matrix elements connecting a zero-weight sector to another sector, so omitting an inactive sector loses no initial support. Rank deficiency *inside* an active $`Q_j`$ does not remove that factor: later laboratory controls can write a new unknown state into it.

## Permitted simulators

A $`D`$-memory simulator is a causal realization with a private quantum memory of dimension at most $`D`$ at **every intervention boundary**, together with unrestricted classical memory. The bound is a hard maximum on every classical branch, not an average dimension or an average number of qubits. A classical register remains diagonal in its designated basis; it is not an uncharged coherent system.

The simulator may begin in any fixed private state independent of laboratory inputs and references. During an idle interval it may use arbitrary ephemeral quantum systems, provided that only its counted memory and its classical record survive to the next intervention boundary. It may depend on the current duration, elapsed time and past classical information. It need not be a Hamiltonian dilation, Markovian semigroup, or finite-state classical model.

The simulator exposes the same physical port $`S`$. The laboratory applies its actual instrument to that port and its own ancillas. In particular, a trace-and-replace intervention physically erases the port output; a simulator may not reinterpret that requested channel as a nondestructive update on an extra hidden port. Every hidden quantum carrier that survives the boundary is part of its $`D`$-dimensional memory. No initial entanglement is shared with the laboratory.

One compatible realization must answer the whole family of finite schedules and interventions. This prevents fitting a separate terminal channel after learning an entire experiment. The lower bound will in fact use one finite tester that works against every permitted simulator, including adaptive ones.

## Distance and order of quantifiers

A tester $`\mathsf T`$ specifies a finite causal laboratory experiment and a final measurement. Its outcome distribution includes every retained classical flag, including failures. Write $`P_{H,\tau}`$ for the physical process family and $`\mathsf M`$ for a compatible simulator. Define

```math
d_\infty(P_{H,\tau},\mathsf M)
=\sup_{\mathsf T\ \mathrm{finite}}
 \mathrm{TV}\!\left(
 p_{\mathsf T[P_{H,\tau}]},p_{\mathsf T[\mathsf M]}\right),
```

```math
\epsilon_D^\infty(H,\tau)
=\inf_{\mathsf M\in\mathfrak M_D}
 d_\infty(P_{H,\tau},\mathsf M).
```

Total variation lies in $`[0,1]`$. Equivalently, allow a final quantum output and optimize its half trace distance over testers; a final Helstrom measurement gives the same quantity. The tester may retain quantum working memory, as in the usual complete operational norm. The converse deliberately erases that working memory at its designated storage cuts, except for a sealed reference that cannot feed information back.

For a finite horizon $`T`$, restrict testers to total idle duration at most $`T`$ and let the simulator be compatible with all such experiments. It may be designed for that horizon. Denote the corresponding optimum by $`\epsilon_D(T)`$. Then

```math
\epsilon_D(T)\le\epsilon_D^\infty(H,\tau),
```

and $`\epsilon_D(T)`$ is nondecreasing with $`T`$. No uniform bound on intervention count is imposed at a fixed horizon. The [memory theorem](memory_law.md) proves both

```math
\epsilon_D^\infty(H,\tau)=q_D,
\qquad
\lim_{T\to\infty}\epsilon_D(T)=q_D.
```

It does not identify $`\epsilon_D(T)`$ at a specified finite time, or a universal convergence rate.

## What is charged and what is concluded

The optimized resource is the coherent dimension retained by a simulator across interventions. Classical storage, ephemeral processing and ideal laboratory controls are free in this structural model. Physical bath dimension and laboratory ancilla dimension are separate quantities. The result is neither a thermodynamic memory cost nor an efficient characterization algorithm.

The theorem concerns arbitrary interventions and arbitrary finite horizons. Passive channel snapshots, one fixed observation grid, bounded controller memory, noisy control and bounded compilation time define different problems. In particular, a weak coupling can be negligible at every fixed short horizon even though it changes the unlimited-horizon answer. The [explicit example](examples.md) exhibits this order of limits.
