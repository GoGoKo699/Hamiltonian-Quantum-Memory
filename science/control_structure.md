# The inherited control structure and its operational use

[Model](model.md) · [Memory law](memory_law.md) · [Classical boundary](classical_boundary.md)

The bath decomposition in this project is inherited from Kato, Owari and Maruyama, *Algebra and Hilbert space structures induced by quantum probes*, Annals of Physics **412**, 168046 (2020), [arXiv:1803.11128v3](https://arxiv.org/abs/1803.11128v3). The preprint's displayed title is *Hilbert space structure induced by quantum probes*. We use its Theorems 1–2 and the ancillary enlargement discussed in Theorem 5. This page states the needed transfer explicitly; the classification itself is not a new result.

## Exact imported statement

Order the physical Hilbert space as $`E\otimes\bar S`$, with $`d=\dim\bar S\ge3`$. Let

```math
\mathfrak L=\mathrm{Lie}_{\mathbb R}
 \left(iH_{E\bar S},\ I_E\otimes\mathfrak{su}(d)\right),
```

where $`H_{E\bar S}=H`$ or $`H\otimes I_Z`$ as in the [model](model.md). Let $`\mathfrak L_c`$ be the smallest ideal containing all local controls, and let $`\mathfrak L_d`$ be its commutant inside the skew-Hermitian operators. The imported theorems give

```math
\mathfrak L_c\subseteq\mathfrak L
 \subseteq\mathfrak L_c+\mathfrak L_d,
\qquad
\mathfrak L_c\cap\mathfrak L_d=\{0\},
```

and a bath decomposition for which

```math
\mathcal H_E=\bigoplus_j\mathcal H_{B_j}\otimes\mathcal H_{Q_j},
```

```math
\mathfrak L_c
=\bigoplus_j I_{B_j}\otimes\mathfrak{su}(r_jd),
\qquad
\mathfrak L_d
=\bigoplus_j\mathfrak u(\dim B_j)\otimes I_{Q_j\bar S}.
```

The same bath decomposition survives further finite enlargement of the accessible laboratory. If $`A`$ is appended and completely controlled with $`\bar S`$, the connected factors become $`\mathfrak{su}(r_jd\dim A)`$ and the disconnected factors remain bath-only on $`B_j`$.

For an original qubit port, adding one controllable laboratory qubit makes the accessible dimension four and places it in this case. This step is material: without enlargement the source's Theorem 3 permits proper Jordan-algebra structures. A full associative bath algebra alone does not justify a SWAP under qubit-only unitary controls.

## Consequence for the physical drift

Because $`iH_{E\bar S}\in\mathfrak L_c+\mathfrak L_d`$, Hermitian operators $`K_j`$ on $`Q_j\otimes\bar S`$ and $`G_j`$ on $`B_j`$ exist such that

```math
H_{E\bar S}
=\bigoplus_j
 \left(I_{B_j}\otimes K_j
       +G_j\otimes I_{Q_j\bar S}\right).
```

Scalar phases can be allocated between the terms without changing the process. The two terms commute. Every local laboratory instrument also acts identically on $`B_j`$ and preserves $`j`$. Therefore all future reduced laboratory statistics are reproduced by the following exact model: draw $`j`$ with probability $`p_j`$, retain

```math
\tau_{Q_j}
=p_j^{-1}\mathrm{Tr}_{B_j}(\Pi_j\tau_E\Pi_j)
```

when $`p_j>0`$, and evolve $`Q_j\bar S`$ with $`K_j`$. Tracing out $`B_j`$ at the beginning is valid even if it is initially correlated with $`Q_j`$: its subsequent unitary acts on $`B_j`$ alone. Off-diagonal $`j`$ blocks never contribute after the final bath trace. This proves the exact simulator used in the upper bound.

The stabilization qubit remains an actual laboratory system, not an extra simulator port. To see this explicitly, when $`\bar S=S\otimes Z`$ the physical drift is $`H_{ES}\otimes I_Z`$. Set $`\widehat K_j=(\dim Z)^{-1}\mathrm{Tr}_ZK_j`$. Taking that normalized partial trace in the drift decomposition, tensoring back with $`I_Z`$, and subtracting the original equality gives

```math
K_j=\widehat K_j\otimes I_Z.
```

Thus the simulator's idle evolution acts on $`Q_j\otimes S`$ alone. The user's controls on $`S\otimes Z`$ are applied outside it, exactly as in the physical experiment. The same observation applies to every further appended laboratory ancilla. No access to a user's private ancillary register is supplied to the simulator.

## Reachable operations: closure is sufficient

We use the Lie statement only to obtain arbitrarily accurate **finite** controls. The available primitives are positive idle times and local laboratory unitaries. Their closure in the compact unitary group contains inverses: recurrence of a unitary's powers approximates its inverse by positive powers. Product and commutator formulas then show that the closure contains $`e^X`$ for every $`X\in\mathfrak L`$, in particular for every connected generator. Thus every desired product of sector-wise special unitaries can be approximated in operator norm by a finite allowed sequence.

This argument needs no exact negative-time query and gives no useful time bound. It is also enough when the generated analytic subgroup is not closed. For any particular finite experiment and any positive error tolerance, choose its finite compilations before running the experiment. Operator-norm errors telescope through unitary channels; arbitrary intervening instruments do not increase trace distance. Hence its total operational error can be made as small as required.

The disconnected drift is harmless for this transfer. It acts only on invisible $`B_j`$ factors and commutes with every connected operation. One can either use full-group approximation or ignore its residual bath-only evolution; neither changes the laboratory statistics.

## Reading the conserved sector

Append a laboratory flag $`F`$ with orthonormal states $`|1\rangle,\ldots,|J\rangle`$, initially in one fixed state. For each sector choose a flag unitary $`V_j`$ sending that state to $`|j\rangle`$. The desired operation is

```math
V=\bigoplus_j
 I_{B_jQ_j\bar S}\otimes V_j.
```

The connected algebra after enlargement supplies independent full special unitaries on the $`Q_j\bar SF`$ blocks. Multiplying $`V_j`$ by a scalar makes each block determinant one; this adds only a sector phase, which vanishes from every reduced laboratory statistic. Consequently a finite compiled operation approximates the desired sector readout arbitrarily well. Measuring $`F`$ gives $`j`$ with probability $`p_j`$ and leaves that sector invariant. The quantum flag is then discarded; its measured value is retained only classically.

No bath measurement is supplied for free. This is an indirect operation compiled through the port. Its potentially large compilation cost is precisely why the theorem is an unrestricted-horizon statement.

## Writing and retrieving an unknown payload

On a known sector $`j`$, append an $`r_j`$-dimensional payload $`L`$. Independent full connected control on $`Q_j\bar SL`$ supplies

```math
W_j=\mathrm{SWAP}_{Q_j,L}\otimes I_{\bar S},
```

again up to an irrelevant phase and arbitrarily small finite compilation error. Controls on other sectors may be chosen arbitrarily. If a common fixed laboratory dimension is desired, embed each payload in an $`r_j`$-dimensional subspace of a register of dimension $`\max_jr_j`$ and extend the indicated SWAP unitarily on its complement.

Initially $`Q_j`$ may be correlated with $`B_j`$. After swapping a fresh payload into $`Q_j`$, those old correlations are carried by $`L`$, which is discarded at the subsequent reset. The stored payload is then independent of $`B_j`$. A second SWAP after the reset returns the unknown state to a fresh payload. This realizes a perfect effective identity channel across a complete working-laboratory reset in the closure of finite allowed experiments.

This is the point at which the control theorem enters the memory converse. The remaining [memory argument](memory_law.md) is a statement about causal dimension-limited simulators, not a further controllability theorem.
