# Thirty milestones for Hamiltonian quantum memory

[Learning route](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Worked example](WORKED_EXAMPLE.md) · [Scientific account](../science/README.md)

This common map follows one question: which coherent part of a known, finite, static bath must a physical quantum-port emulator retain under arbitrary interventions? It contains exactly thirty project-defined understanding targets. It is independent of any reader's assessment history and does not prescribe a personal teaching or testing procedure.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). Section numbers below refer to the verified standard-layout January 2018 author manuscript identified in the [bridge](WATROUS_BRIDGE.md). Primary research citations supply the control and multitime-process ingredients that the textbook does not cover.

| Phase | Milestones | Why this allocation fits the story |
| --- | --- | --- |
| Background/preliminaries | M01–M12 | Assemble states, references, instruments, memory cuts, operational error and the imported control structure into the actual simulation problem. |
| Narrative/innovation | M13–M30 | Build the indirect storage witness locally, then combine its repeated-use converse with the sector simulator to obtain the tail law, classical boundary and physical limitations. |

Throughout, $`Q_j`$ denotes a controllable bath factor of dimension $`r_j`$, $`p_j`$ its initial sector probability, and $`D`$ the hard maximum persistent quantum dimension of an emulator. Its classical memory is unrestricted. The headline error is uniform over arbitrarily long **finite** experiments; it is not a finite-time efficiency or classical numerical-prediction claim.

## Background/preliminaries — M01–M12

### M01 — A physical port with an unknown input

**Central question:** What must an emulator reproduce when an actual quantum input arrives?

- **Understanding target:** Distinguish quantum-port emulation, including unknown input correlations, from computing probabilities for a fully described experiment.
- **Dependencies and story role:** Entry point; identifies the physical task before introducing a memory resource.
- **Conceptual connection:** Registers and channels become an input/output contract with a user.
- **Source pointers:** Watrous §§2.1–2.2 through the [bridge](WATROUS_BRIDGE.md); [model opening and physical process](../science/model.md#physical-process); [interpretation](../science/interpretation.md).

### M02 — What remains after a subsystem is ignored

**Central question:** When can an unobserved bath component be traced out?

- **Understanding target:** Explain reduced states and why tracing a subsystem preserves all observations on the remaining registers; distinguish this operation from assuming a product state.
- **Dependencies and story role:** Builds on M01; supplies the first local simplification used by the exact simulator.
- **Conceptual connection:** Partial trace permits ignoring an invisible multiplicity even when it is initially correlated with the useful factor.
- **Source pointers:** Watrous §2.1.3; [drift reduction](../science/control_structure.md#consequence-for-the-physical-drift).

### M03 — A reference that records quantum correlations

**Central question:** Why is returning the right reduced payload state an insufficient memory test?

- **Understanding target:** Explain how a sealed reference distinguishes genuine transmission of an unknown quantum state from measurement and repreparation.
- **Dependencies and story role:** Uses M01–M02; makes the later Bell test physically meaningful.
- **Conceptual connection:** Purification turns a statement about all unknown inputs into a reference-correlation requirement.
- **Source pointers:** Watrous §2.1.3; [reference convention](../science/model.md#physical-process); [worked example](WORKED_EXAMPLE.md).

### M04 — Channels must act consistently on larger systems

**Central question:** What changes when a channel's input is entangled with an untouched register?

- **Understanding target:** Explain complete positivity and why the same port operation must remain valid with arbitrary finite references.
- **Dependencies and story role:** Builds on M03; prevents a reduced-state-only interpretation of emulation.
- **Conceptual connection:** The channel framework supplies the reference-complete setting for both simulation and control-approximation errors.
- **Source pointers:** Watrous §§2.2–2.2.2; [distance and quantifiers](../science/model.md#distance-and-order-of-quantifiers).

### M05 — Classical branches and quantum carriers

**Central question:** What may a simulator retain after an instrument produces an outcome?

- **Understanding target:** Separate a measured classical record from a coherent register; recognize that conditioning later channels on a record is allowed.
- **Dependencies and story role:** Uses M04; introduces the strongest classical competitor rather than only a fixed random-field model.
- **Conceptual connection:** Measurements and channels compose into invasive classical feedforward, while classical labels remain diagonal.
- **Source pointers:** Watrous §§2.2 and 2.3; [permitted simulators](../science/model.md#permitted-simulators); [classical-memory distinction](../science/classical_boundary.md#classical-common-cause-versus-general-classical-memory).

### M06 — A reset that closes the accessible path

**Central question:** Which registers must be erased to test whether information survived in the bath?

- **Understanding target:** Identify the port and every accessible working carrier in a trace-and-replace operation, while keeping the reference sealed until readout.
- **Dependencies and story role:** Combines M03–M05; defines the physical cut used in the converse.
- **Conceptual connection:** A reset is a prescribed channel on real wires; hidden surviving quantum carriers belong to the emulator's counted memory.
- **Source pointers:** Watrous §2.2; [simulator contract](../science/model.md#permitted-simulators); [finite repeated tester](../science/memory_law.md#the-finite-repeated-tester); [worked example](WORKED_EXAMPLE.md).

### M07 — Quantum dimension and Bell overlap

**Central question:** How can one Bell measurement reveal that a quantum carrier is too small?

- **Understanding target:** Interpret pure-state Schmidt rank and the mixed-state Schmidt-number extension used locally; explain why a $`D`$-dimensional carrier bounds the Bell overlap by $`D/r`$.
- **Dependencies and story role:** Uses M03–M06; supplies the local dimension obstruction without confusing dimension with entropy.
- **Conceptual connection:** Textbook entanglement foundations support a project-supplied finite-dimensional overlap lemma; the mixed-state extension is a research ingredient.
- **Source pointers:** Watrous §§6.1 and 6.2.1 via the [bridge](WATROUS_BRIDGE.md); [one-round lemma](../science/memory_law.md#a-one-round-dimension-lemma).

### M08 — A hard memory budget on every branch

**Central question:** What resource does $`D`$ constrain when the simulator adapts?

- **Understanding target:** Distinguish a maximum coherent dimension at each intervention boundary from average entropy, expected memory or the bath's initial rank.
- **Dependencies and story role:** Integrates M05–M07; fixes the resource before optimizing an error.
- **Conceptual connection:** Classical alternatives may select different states in one common bounded quantum register, but cannot hide coherence in an uncharged label.
- **Source pointers:** [permitted simulators](../science/model.md#permitted-simulators); [resource contract](../science/interpretation.md#resource-contract); Bisio's research framework in [related work](../references/related_work.md).

### M09 — Operational error as a distinguishable event

**Central question:** How does one event supply a lower bound on whole-process error?

- **Understanding target:** Read total variation and half trace distance in the $`[0,1]`$ convention, and connect them to optimized discrimination.
- **Dependencies and story role:** Uses M04 and M08; introduces the error that the memory theorem actually optimizes.
- **Conceptual connection:** A final measurement converts a quantum-output discrepancy into a probability difference; an unhalved norm would change constants.
- **Source pointers:** Watrous §§3.1 and 3.3.2; [distance definition](../science/model.md#distance-and-order-of-quantifiers).

### M10 — One compatible causal process

**Central question:** Why does matching a collection of terminal channels fail to specify an emulator?

- **Understanding target:** Explain the order of inputs, intervals, interventions and outputs, including adaptive choices and an inaccessible reference.
- **Dependencies and story role:** Combines M01–M09 into the reusable-process viewpoint.
- **Conceptual connection:** Channel composition extends to a physical strategy that must answer future interventions without receiving their private descriptions in advance.
- **Source pointers:** Watrous §§2.2 and 3.3 as foundations; [model](../science/model.md); Bisio/Goswami process dependencies in [related work](../references/related_work.md).

### M11 — Local control can reach a hidden factor

**Central question:** How can an inaccessible bath subsystem become indirectly writable through the port?

- **Understanding target:** Explain the role of the connected control algebra, ancillary stabilization to accessible dimension at least three, and reachable-unitary closure.
- **Dependencies and story role:** Uses M04 and M10; imports the specific research structure that makes the storage witness possible.
- **Conceptual connection:** Complete local control plus a fixed drift produces effective joint operations; associative bath algebra alone does not prove controllability.
- **Source pointers:** [imported Kato statement](../science/control_structure.md#exact-imported-statement); [finite control closure](../science/control_structure.md#reachable-operations-closure-is-sufficient); Kato primary source in [related work](../references/related_work.md). This control classification is outside Watrous.

### M12 — The complete background model

**Central question:** How do the bath structure, laboratory and emulator fit into one experiment?

- **Understanding target:** Identify conserved $`j`$, invisible $`B_j`$, controllable $`Q_j`$, original port $`S`$, reset working ancillas and sealed reference; state the initial-state and all-time promises together.
- **Dependencies and story role:** Integrates M01–M11; completes the background phase as one operational model.
- **Conceptual connection:** The inherited decomposition supplies opportunities for writing information, while quantum channels and the hard resource cap determine what an emulator must preserve.
- **Source pointers:** [model](../science/model.md); [control structure](../science/control_structure.md); [resource table](../science/interpretation.md#resource-contract); [Watrous bridge](WATROUS_BRIDGE.md).

## Narrative/innovation — M13–M30

### M13 — Indirectly reading the conserved label

**Central question:** How can the laboratory learn which bath factor is present without a supplied bath measurement?

- **Understanding target:** Explain a sector-controlled flag operation, its classical outcome probability $`p_j`$, and why sector phases do not affect reduced statistics.
- **Dependencies and story role:** Starts locally from M11–M12; selects the branch on which the new witness will operate.
- **Conceptual connection:** Independent connected control in the actual decomposition makes the sector readable; arbitrary blocks chosen from a matrix representation would not suffice.
- **Source pointers:** [sector readout](../science/control_structure.md#reading-the-conserved-sector); [Kato transfer](../science/control_structure.md#exact-imported-statement).

### M14 — Writing past the bath's initial rank

**Central question:** Why can a pure initial bath factor still carry an arbitrary unknown payload later?

- **Understanding target:** Follow encoding by SWAP, erasure of the old bath state now in the laboratory, and retrieval after a complete working reset.
- **Dependencies and story role:** Uses M06, M12 and M13; constructs the physical storage mechanism before bounding a simulator.
- **Conceptual connection:** The resource is what controls can write into a factor, not how much entropy the factor initially contains.
- **Source pointers:** [payload write and retrieval](../science/control_structure.md#writing-and-retrieving-an-unknown-payload); [worked example](WORKED_EXAMPLE.md).

### M15 — One storage round defeats a smaller carrier

**Central question:** What can a dimension-limited emulator retain across the prescribed reset?

- **Understanding target:** Apply the $`D/r_j`$ Bell bound after every accessible carrier is erased and only counted private memory can carry input correlations forward.
- **Dependencies and story role:** Combines M07–M08 with M14; turns physical storage into a quantitative witness.
- **Conceptual connection:** Reference-complete channel emulation becomes a Schmidt-number obstruction at a single causal cut.
- **Source pointers:** [one-round dimension lemma](../science/memory_law.md#a-one-round-dimension-lemma); [worked example](WORKED_EXAMPLE.md); Watrous entanglement foundations through the [bridge](WATROUS_BRIDGE.md).

### M16 — Fresh references under adaptive history

**Central question:** Why does an earlier successful test not remove the next dimension obstruction?

- **Understanding target:** Explain conditioning on arbitrary previous classical history, allowing an arbitrary residual simulator state, and then preparing a fresh independent Bell pair.
- **Dependencies and story role:** Builds on M05, M10 and M15; closes the adaptive-memory loophole in repetition.
- **Conceptual connection:** Conditional probability can be iterated without assuming independent simulator memories; old quantum outputs and references are disposed of.
- **Source pointers:** [finite repeated tester](../science/memory_law.md#the-finite-repeated-tester); [worked example](WORKED_EXAMPLE.md).

### M17 — One event for many storage rounds

**Central question:** How does repetition turn partial Bell overlap into an asymptotically decisive test?

- **Understanding target:** Derive the all-pass probability bound $`(D/r_j)^n`$ and its uniform high-sector bound $`[D/(D+1)]^n`$.
- **Dependencies and story role:** Uses M09 and M16; assembles the local round into the converse's observable event.
- **Conceptual connection:** The test remains valid if an emulator changes its reported sector distribution; every high label still demands transmission through an oversized carrier.
- **Source pointers:** [repeated event and relabelling bound](../science/memory_law.md#the-finite-repeated-tester); [worked example](WORKED_EXAMPLE.md).

### M18 — Finite compilation is enough

**Central question:** Does the argument require an exactly reachable SWAP or an infinite physical experiment?

- **Understanding target:** Explain finite compiled controls with aggregate error $`\eta`$, and why the emulator's dimension bound holds for the actual compiled operations without assuming they act as its internal SWAP.
- **Dependencies and story role:** Combines M11 and M17; converts the ideal mechanism into permitted finite witnesses.
- **Conceptual connection:** Reference-complete control approximation affects the target probability, while the reset-based dimension lemma applies to every emulator encoding and decoding.
- **Source pointers:** [control closure](../science/control_structure.md#reachable-operations-closure-is-sufficient); [finite lower bound](../science/memory_law.md#finite-control-approximation-and-lower-bound); Watrous §3.3.2 foundations.

### M19 — An exact emulator for each fitting sector

**Central question:** Which bath information must a constructive emulator actually retain?

- **Understanding target:** Keep $`j`$ classically and the reduced $`Q_j`$ state coherently; trace $`B_j`$ and retain no intersector coherence.
- **Dependencies and story role:** Returns to a local construction using M02, M08 and M12; begins the upper-bound half of the contribution.
- **Conceptual connection:** The Hamiltonian reduction works for arbitrary initial correlations inside $`B_jQ_j`$ and leaves all user ancillas outside the simulator's original port.
- **Source pointers:** [exact drift reduction](../science/control_structure.md#consequence-for-the-physical-drift); [memory upper bound](../science/memory_law.md#upper-bound-keep-small-factors-and-a-classical-sector).

### M20 — Combining sector errors

**Central question:** Why does omitting oversized sectors cost only their total probability?

- **Understanding target:** Use an exact model on $`r_j\le D`$ and arbitrary causal stand-ins otherwise to obtain the uniform bound $`q_D=\sum_{r_j>D}p_j`$.
- **Dependencies and story role:** Builds on M09, M13 and M19; turns sector-level construction into a global emulator.
- **Conceptual connection:** Convex mixing charges the weight of replaced branches, while free classical labels avoid summing their coherent dimensions.
- **Source pointers:** [upper-bound proof](../science/memory_law.md#upper-bound-keep-small-factors-and-a-classical-sector); [weighted staircase](../science/examples.md#a-weighted-memory-staircase).

### M21 — Matching the tail from below

**Central question:** Why can no better adaptive emulator beat the same omitted weight?

- **Understanding target:** Combine the high-label all-pass event with finite compilation to read $`q_D-[D/(D+1)]^n-\eta`$, then take the supremum over finite testers before the simulator infimum.
- **Dependencies and story role:** Integrates M17–M20; establishes the central equality $`\epsilon_D^\infty=q_D`$.
- **Conceptual connection:** One chosen finite tester works uniformly against every permitted emulator, so no interchange with an infinite experiment is needed.
- **Source pointers:** [main theorem and converse](../science/memory_law.md); [model quantifiers](../science/model.md#distance-and-order-of-quantifiers).

### M22 — Reading the memory staircase

**Central question:** What coherent register is necessary at a chosen uniform error tolerance?

- **Understanding target:** Read exact dimension $`\max_{p_j>0}r_j`$ and the smallest $`D`$ satisfying $`q_D\le\epsilon`$; translate a hard $`k`$-qubit register to $`D=2^k`$.
- **Dependencies and story role:** Uses M08 and M21; turns the theorem into an operational resource frontier.
- **Conceptual connection:** The frontier is a quantile of active factor dimensions, with plateaus when no new factor fits; it is not a bath-eigenvalue or average-entropy code.
- **Source pointers:** [theorem](../science/memory_law.md#the-theorem); [weighted example](../science/examples.md#a-weighted-memory-staircase); [resource interpretation](../science/interpretation.md).

### M23 — The large-horizon limit

**Central question:** What remains true if a different compatible emulator is designed for each finite horizon?

- **Understanding target:** Explain why each finite witness supplies a lower bound once its compilation time fits, giving $`\lim_{T\to\infty}\epsilon_D(T)=q_D`$ without a convergence rate.
- **Dependencies and story role:** Uses M18 and M21; states the limiting order needed to interpret the global result.
- **Conceptual connection:** Uniform finite witnesses prevent a horizon-specific redesign from evading the asymptotic obstruction, while leaving shortest-time synthesis unresolved.
- **Source pointers:** [horizon-specific simulators](../science/memory_law.md#horizon-specific-simulators); [distance convention](../science/model.md#distance-and-order-of-quantifiers).

### M24 — Excluding invasive classical memory

**Central question:** What does the theorem say when no private coherent register survives?

- **Understanding target:** Set $`D=1`$ and explain why every occupied $`r_j>1`$ obstructs exact emulation even with unlimited classical measurement, updating and feedforward.
- **Dependencies and story role:** Builds on M05, M08 and M21; extracts the genuinely quantum-memory consequence.
- **Conceptual connection:** Failure of a fixed noninvasive noise label is weaker than exclusion of all classical causal emulators; the Bell argument establishes the latter in this model.
- **Source pointers:** [classical boundary](../science/classical_boundary.md#exact-boundary-for-a-fixed-initial-bath); [classical-noise interpretation](../science/interpretation.md#consequence-for-classical-noise-models).

### M25 — A common-cause realization when factors are scalar

**Central question:** Why does a fixed bath basis suffice whenever exact classical emulation is possible here?

- **Understanding target:** Explain the controlled-Hamiltonian form on active sectors and the resulting mixture of unitary process families; distinguish common cause from one memoryless process.
- **Dependencies and story role:** Uses M12 and M24; completes both directions of the static classical boundary.
- **Conceptual connection:** The collapse of general classical feedforward to common cause is specific to this complete static-bath family, not all multitime processes or observation grids.
- **Source pointers:** [fixed-state equivalence](../science/classical_boundary.md#exact-boundary-for-a-fixed-initial-bath); [classical classes](../science/classical_boundary.md#classical-common-cause-versus-general-classical-memory); [correlated classical bath example](../science/examples.md#a-classical-bath-need-not-be-memoryless).

### M26 — Active support and faithful-state qualifiers

**Central question:** Which parts of the full Hamiltonian can a supplied initial bath state make relevant?

- **Understanding target:** Separate inactive sectors from rank-deficient states inside active quantum factors; state when the full-Hamiltonian controlled-basis conclusion follows.
- **Dependencies and story role:** Combines M14, M22 and M25; removes an initial-state loophole from the global interpretation.
- **Conceptual connection:** A faithful state occupies every sector, while a pure state in an occupied controllable factor can still be overwritten with an arbitrary payload.
- **Source pointers:** [faithful and inactive sectors](../science/classical_boundary.md#faithful-states-and-inactive-sectors); [model weights](../science/model.md#stabilized-control-decomposition); [weighted example](../science/examples.md#a-weighted-memory-staircase).

### M27 — A concrete Hamiltonian crosses the boundary

**Central question:** How can a single bath rotation turn a classical factor structure into a quantum one?

- **Understanding target:** Follow the qutrit–qubit family $`H_g=C\otimes Z+gI\otimes X`$: conserved bath labels at $`g=0`$ and a full connected $`\mathfrak{su}(6)`$ algebra at every nonzero $`g`$.
- **Dependencies and story role:** Uses M11 and M24–M26; tests the abstract boundary on one explicit static model.
- **Conceptual connection:** The analytical generator-spanning argument establishes the factor change; finite numerical Lie-rank checks support the example without replacing its proof.
- **Source pointers:** [weak transverse-term example](../science/examples.md#an-arbitrarily-weak-bath-term-changes-the-all-time-answer); [verification scope](../verification/README.md).

### M28 — Weak coupling during a fixed experiment

**Central question:** Why can maximal all-time classical-emulation error coexist with a good short-time classical model?

- **Understanding target:** Apply the perturbation bound $`d_T(P_{H_g},P_{H_0})\le\min\{1,|g|T\}`$ and explain the noncommuting weak-coupling and long-time limits.
- **Dependencies and story role:** Combines M23 and M27; prevents a structural theorem from being promoted into an efficient diagnostic.
- **Conceptual connection:** Unitary-channel continuity controls a fixed elapsed-time budget, while the repeated witness permits a time budget that depends on coupling and desired separation.
- **Source pointers:** Watrous §3.3.2 foundations; [finite-time proof](../science/examples.md#finite-time-proximity-survives); [finite-time caution](../science/classical_boundary.md#finite-time-caution).

### M29 — What is inherited and what is added

**Central question:** What consequential statement remains after the closest ingredients are credited?

- **Understanding target:** Attribute Kato's control classification, Koashi–Imoto's information decomposition, Bisio's memory framework and the Bell-overlap bound; identify the sharp weighted all-time error law and repeated operational converse as the addition.
- **Dependencies and story role:** Integrates M11–M28; locates the contribution in its actual literature and model.
- **Conceptual connection:** A new use of established structure can answer a different operational question, but does not create a new decomposition or settle passive-snapshot memory detection.
- **Source pointers:** [primary comparisons](../references/related_work.md); [proof attribution](../science/memory_law.md#attribution-and-scope); [Hamiltonian-conjecture relation](../science/classical_boundary.md#relation-to-the-hamiltonian-conjecture); [anchor bridge](WATROUS_BRIDGE.md).

### M30 — The whole physical account

**Central question:** Which coherent part of a static bath must survive in any universal physical emulator, and within what limits?

- **Understanding target:** Connect the factor decomposition, original quantum port, sealed-reference reset test, adaptive repetition, exact tail frontier, classical boundary, active-state qualification and finite-time warning in one explanation.
- **Dependencies and story role:** Integrates M13–M29 and the background model; closes the narrative phase with the supported contribution and its scope.
- **Conceptual connection:** The result prices a hidden coherent carrier under ideal complete control and unrestricted finite duration; it supplies neither classical computational hardness nor an efficient control, communication, thermodynamic or hardware advantage.
- **Source pointers:** [scientific overview](../science/README.md); [memory theorem](../science/memory_law.md); [interpretation and resources](../science/interpretation.md); [worked example](WORKED_EXAMPLE.md).
