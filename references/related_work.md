# Relation to earlier work

This project studies the quantum state that must persist inside a simulator of a controlled finite-bath process. Classical records are unrestricted. The operational error is uniform over finite intervention sequences and their quantum testers, without a common upper bound on duration or number of interventions.

For the stabilized controllability decomposition, let $`r_j`$ be the dimension of the controllable bath factor in sector $`j`$, and let $`p_j`$ be its initial probability. The central conclusion is

```math
\epsilon_D=\sum_{j:r_j>D}p_j.
```

The algebraic decomposition and the basic quantum-memory bottleneck are inherited ingredients. The contribution is their operational connection: the sector dimensions determine the complete uniform error curve, including arbitrary classical feedforward and sectors of arbitrarily small nonzero weight.

## Precise comparisons

| Earlier result | Ingredient used here | Difference in the present question |
| --- | --- | --- |
| [Kato, Owari and Maruyama, *Annals of Physics* **412**, 168046 (2020)](https://doi.org/10.1016/j.aop.2019.168046), [arXiv:1803.11128v3](https://arxiv.org/abs/1803.11128v3), Theorems 1–2 and 5 | Restricted local control induces a direct sum of controllable factors and invisible multiplicities. For a probe of dimension at least three, each controllable factor is fully controllable jointly with the probe. The structure is stable under further laboratory ancillas. | These are control and representation theorems. Here they supply both a simulator and system-accessible tests against every simulator with smaller persistent quantum memory. Their decomposition is not claimed as new. |
| [Koashi and Imoto, *Physical Review A* **66**, 022318 (2002)](https://doi.org/10.1103/PhysRevA.66.022318), [preprint v2](https://arxiv.org/abs/quant-ph/0101144v2), Theorem 3, Sections VII and VIII.5 | A state family separates into a classical label, a quantum factor and a redundant factor. Preserving the family constrains access to these factors; compression can replace classical information by classical storage. | The three-way information distinction and its compression interpretation are established. The present factors come from a controlled Hamiltonian and the error concerns an entire family of interventions, rather than independent messages from a prescribed ensemble. |
| [Bisio, D’Ariano, Perinotti and Sedlák, *Physical Review A* **85**, 032333 (2012)](https://doi.org/10.1103/PhysRevA.85.032333), [arXiv:1112.3853v1](https://arxiv.org/abs/1112.3853v1), Proposition 3 and Theorem 3 | Classical-assisted quantum memory of a finite comb is characterized by compatible decompositions with rank constraints. Memory optimization must generally be performed across the whole strategy. | The present result evaluates a particular physically generated class: one static finite bath under arbitrary local interventions. The answer is a closed expression in its occupied controllability sectors, not a general replacement for the finite-comb characterization. |
| [Taranto, Quintino, Murao and Milz, *Quantum* **8**, 1328 (2024)](https://doi.org/10.22331/q-2024-05-02-1328), [arXiv:2307.11905v2](https://arxiv.org/abs/2307.11905v2), Definition 3 and Theorem 1 | General classical memory permits measurement outcomes to determine future instruments. For three or more times, it strictly contains mixtures of memoryless processes and is strictly contained in separable processes. | The simulator class here includes this adaptive classical memory. Bath backaction or failure of a common-cause model alone therefore does not prove the required lower bound. The stored-reference test establishes a quantum-memory bottleneck instead. |
| [Goswami et al., *New Journal of Physics* **27**, 114515 (2025)](https://doi.org/10.1088/1367-2630/ae1c64), [arXiv:2412.01998v2](https://arxiv.org/abs/2412.01998v2), Theorem 1, Corollary 1 and Conjecture 1 | A common conserved environment basis gives a mixture of unitary processes for all probing times. Conjecture 1 asks for a static converse for classical common-cause processes. | Common-cause memory is narrower than general classical memory. The present stabilized theorem treats the latter and quantifies its quantum extension. Its state-dependent statement uses occupied sectors; inactive sectors cannot be excluded merely by observing one initial state. It does not identify those different quantifiers with the conjecture’s unstated initial-state quantifier. |

## Why the error curve needs an operational argument

An upper bound follows by retaining the classical sector label, discarding invisible multiplicities and simulating every sector with $`r_j\leq D`$ exactly. Replacing the remaining sectors costs at most their total probability.

For the converse, the control theorem allows a sector to be recorded classically and a fresh entangled payload to be stored in its bath factor. After every accessible quantum carrier is reset, the simulator has only $`D`$ quantum dimensions with which to preserve the payload’s sealed reference. The standard Schmidt-number bound limits an $`r_j`$-dimensional Bell test to probability $`D/r_j`$. Repeating with fresh references turns that fixed dimension gap into a uniform process distinction. This overlap bound is [Terhal and Horodecki, *Physical Review A* **61**, 040301(R) (2000)](https://doi.org/10.1103/PhysRevA.61.040301), [preprint v4](https://arxiv.org/abs/quant-ph/9911117v4), Lemma 1; their Proposition 1 gives the underlying monotonicity. The elementary argument is reproduced in the scientific proof.

This is an unrestricted-time conclusion. The control synthesis may take arbitrarily long, and each repetition requires fresh laboratory preparation, resetting and reference testing. No efficient witness, finite-horizon memory formula, bounded-control guarantee or application-level computational advantage follows from the tail law.

## Background on processes and testers

[Milz and Modi, *PRX Quantum* **2**, 030201 (2021)](https://doi.org/10.1103/PRXQuantum.2.030201), [arXiv:2012.01894v2](https://arxiv.org/abs/2012.01894v2), provides the operational process-tensor background: Section V.4.6 treats temporally correlated testers; V.4.7 treats dilation; VI.1 treats causal breaks; VI.2.1 treats memory bonds. A one-time reduced channel or its lack of information backflow is not the full controlled process.

Bibliographic records are in [references.bib](references.bib). The comparisons above identify the inherited mechanisms and the specific operational addition; they are not an exhaustive priority certificate.
