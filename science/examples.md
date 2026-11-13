# Examples and the order of limits

The [memory law](memory_law.md) is a structural statement about a fixed bath reused for arbitrarily long finite experiments. These examples explain what its dimensions and probabilities mean, and why it does not replace finite-time modeling.

## A weighted memory staircase

Consider three controllable bath sectors with

```math
(r_1,r_2,r_3)=(1,2,4),\qquad
(p_1,p_2,p_3)=(3/5,3/10,1/10).
```

The factors carrying these dimensions are the irreducible controllable factors in the [control decomposition](control_structure.md), not arbitrary chosen blocks. Independent full control in different sectors is essential. One way to realize this structure is a qutrit port coupled to three inequivalent blocks with full connected algebras on the port and each active factor. Invisible multiplicity spaces can have any finite size without changing the answer.

| Hard persistent quantum dimension | Optimal uniform process error | Memory interpretation |
| --- | --- | --- |
| 1 | 2/5 | Classical records alone omit both quantum sectors. |
| 2 | 1/10 | One qubit stores the two-level factor; the four-level factor is omitted. |
| 3 | 1/10 | A third level does not reach the next irreducible factor. |
| 4 or larger | 0 | Every occupied factor is represented exactly. |

The error is weighted by sector probability. The quantum factor cannot be partially represented at a smaller dimension with a better *uniform all-time* error: repeated transmission tests eventually expose any such replacement. This is a statement about preserving actual quantum-port correlations. A numerical program predicting specified probabilities has a different task.

Even an initially pure state in the four-level factor still requires four levels for exact universal emulation. The laboratory can overwrite that factor with an arbitrary unknown payload. Initial bath entropy does not bound what the bath can subsequently retain.

## An arbitrarily weak bath term changes the all-time answer

Let the accessible port be a qutrit and the bath one qubit. In units with the longitudinal coupling equal to one, set

```math
C=\mathrm{diag}(-1,0,1),\qquad
H_g=C\otimes Z+g I_3\otimes X,
```

where the first tensor factor is the port. Every port Hamiltonian is controllable. Fix any initial bath density operator, including a pure one or the maximally mixed state.

### Zero transverse term

At zero transverse term the two eigenspaces of bath Z are invariant. Conditional on its eigenvalue, the port evolves under C or minus C. Thus one classical bit is an exact hidden memory for every controlled experiment.

The connected Lie algebra has dimension 16 and is the direct sum of two copies of su(3). To see this, port controls supply su(3) tensored with the bath identity; the nonzero traceless C and the simplicity of su(3) give su(3) tensored with Z. Their commutators close within these two spaces. Both controllable-factor spaces have dimension one; only sectors of nonzero initial weight are occupied.

### Any nonzero transverse term

For every nonzero g the dynamical Lie algebra is su(6), of dimension 35. Here is an explicit spanning argument using Hermitian generators and the bracket i[A,B].

1. Conjugate the drift by a finite unitary twirl on the qutrit. Averaging eliminates its traceless C term, so the real linear span contains the bath-only X term. Subtraction then isolates C tensored with Z.
2. Commuting with arbitrary port generators yields all traceless qutrit generators tensored with Z. Commuting those with the bath X generator yields the corresponding Y generators.
3. For a traceless qutrit matrix A whose square is not scalar, the bracket of A tensored with Y and A tensored with Z gives a multiple of A squared tensored with X. Subtract its scalar part using the already available bath-only X generator. The remaining nonzero traceless qutrit term, and its port commutators, yield all traceless qutrit generators tensored with X.
4. Brackets between the X and Y families produce A squared tensored with Z. Subtracting the traceless part now isolates the bath-only Z generator. Its bracket with bath-only X yields bath-only Y.

These are the 32 qutrit-traceless generators tensored with the four Pauli-basis elements, plus the three bath-only traceless generators. They span all 35 dimensions of su(6). The overall identity is irrelevant.

The stabilized control decomposition therefore has a single two-dimensional active bath factor. By the memory law,

```math
\epsilon_1(H_g)=1\quad(g\ne0),\qquad
\epsilon_2(H_g)=0.
```

Every realization with only classical persistent internal memory can eventually be distinguished with error separation arbitrarily close to one. The statement permits a different long finite witness for each desired separation. It does not assert a single finite experiment attaining distance exactly one.

## Finite-time proximity survives

For any two bounded Hamiltonians with the same initial bath state, the half strategy distance over testers with total free-evolution duration at most T obeys

```math
d_T(\mathsf P_H,\mathsf P_K)
\le\min\{1,T\lVert H-K\rVert\}.
```

For one interval, Duhamel's formula gives the operator-norm propagator difference at most its duration times the Hamiltonian difference. The half diamond distance of the corresponding unitary channels is at most that propagator difference. Insert identical laboratory operations between intervals and telescope; complete positivity makes every subsequent channel contract trace distance. Adaptive classical branches are handled by keeping their records and using the same hybrid argument, with the pathwise total duration bound. No bound on the number of instantaneous contacts is needed.

For the explicit family this yields

```math
d_T(\mathsf P_{H_g},\mathsf P_{H_0})
\le\min\{1,|g|T\}.
```

The zero-transverse model has an exact classical-memory realization, so it is also a classical approximation to the nonzero-transverse process with this error over a fixed horizon. Its unrestricted-time error tends to one by the theorem. Thus an arbitrarily weak nonzero bath term can be negligible during a fixed experiment and decisive over unrestricted time. The order of limits is material; no uniform finite-time memory threshold is inferred.

## A classical bath need not be memoryless

Take a bath with two conserved labels and two distinct conditional port Hamiltonians. Its future response depends on the initially sampled label, and earlier measurements can reveal that label. The process can therefore have temporal correlations while requiring no coherent hidden memory. It is a classical common-cause process, not generally one Markovian process.

Conversely, noncommuting bath dynamics or an entangled Hamiltonian eigenvector alone is not the theorem's criterion. Invisible multiplicities and unoccupied invariant sectors do not carry operational memory. Use the occupied active factors of the stabilized control decomposition, as explained in the [classical boundary](classical_boundary.md).

Next: [physical interpretation and resources](interpretation.md) · [reproduction and verification](../verification/README.md).
