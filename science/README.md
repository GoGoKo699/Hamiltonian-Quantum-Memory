# From a hidden bath to its quantum memory cost

A reduced channel describes what happens between one preparation and one readout. A reused bath can also remember what the laboratory did in between. To emulate that behavior, one needs a causal physical process with the right quantum input/output correlations, not just the right terminal channel.

The [model](model.md) fixes a finite static Hamiltonian and bath state, complete local instruments, finite working ancillas and a hard hidden quantum-memory cap. Classical records are unrestricted. The comparison includes inaccessible reference systems and is uniform over arbitrarily long finite experiments.

The [inherited control structure](control_structure.md) separates the bath into conserved sectors, invisible multiplicities and controllable quantum factors. It explains two operational facts: the conserved sector can be read indirectly through the port, and an unknown payload can be written into each active factor and retrieved after resetting the accessible laboratory. Neither operation is assumed to be fast.

The [memory law](memory_law.md) turns those facts into an exact answer. A simulator retains every factor that fits, recording its sector classically, and omits the others at their total probability cost. Conversely, repeated Bell transmission through each oversized factor defeats every smaller quantum memory, even when the simulator adapts using all preceding classical outcomes. The same argument proves the large-horizon limit without interchanging an infimum and an infinite experiment.

The [classical boundary](classical_boundary.md) is the dimension-one case. For the complete controlled static-bath family, general classical feedforward suffices exactly when a classical common-cause realization already suffices. The statement includes the occupied-sector qualification for a nonfaithful initial bath and does not collapse the hierarchy for general multitime processes on fixed grids.

The [examples](examples.md) give a weighted memory staircase and a fully controllable qutrit–qubit bath. They also prove the finite-time perturbation bound that keeps weak coupling separate from unrestricted observation. The [interpretation](interpretation.md) collects the resource account and physical consequence.

| Reading goal | Route |
| --- | --- |
| Follow the mechanism | Model → control structure → memory law → classical boundary → examples → interpretation |
| Check the theorem | Model’s quantifiers, control theorem transfer, one-round Schmidt-number lemma, repeated finite tester, approximation and horizon limit |
| Inspect attribution | [Primary comparisons](../references/related_work.md) and [bibliography](../references/references.bib) |
| Reproduce finite examples | [Verification](../verification/README.md) |

The sharp tail law is the project’s operational addition. The algebraic classification, classical/quantum/irrelevant distinction, classical-assisted memory convention and Bell-overlap inequality are credited to their prior sources.
