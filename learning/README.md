# Learning route

Imagine using a device to hold an unknown qubit while every working register in the laboratory is erased. If the device later returns the qubit with its original quantum correlations intact, something quantum must have survived inside it. This project turns that observation into an exact memory requirement for a controlled finite environment.

The selected educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**, using the author's standard-layout manuscript whose preface is dated January 2018. The [author's source page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the manuscript and individual chapters. The [bridge](WATROUS_BRIDGE.md) specifies the relevant sections, notation and additional research ingredients. Reading the entire book is unnecessary for this route.

## Start with a complete experiment

The [worked example](WORKED_EXAMPLE.md) follows a Bell pair through storage, a full laboratory reset and retrieval. It gives every input, output and measured event. A hidden qubit passes its Bell test with probability one; any emulator retaining only classical information passes with probability at most one half. Repetition exposes the memory difference without assuming independent emulator behavior.

## From the example to the result

The [30-milestone map](MILESTONES.md) develops two connected phases. The first twelve milestones assemble states, channels, references, memory cuts and the supplied control structure. The remaining eighteen connect the storage test to repeated tests, conserved sectors, the exact error tail and its physical limits. Within both phases, individual objects lead to the full operational picture.

| Reading goal | Route |
| --- | --- |
| See how quantum memory is tested | [Worked example](WORKED_EXAMPLE.md) |
| Translate the textbook into this project | [Watrous bridge](WATROUS_BRIDGE.md) |
| Follow the project's complete conceptual story | [Milestone map](MILESTONES.md) |
| Inspect the exact assumptions and simulator class | [Scientific model](../science/model.md) |
| Separate inherited control theory from the new memory argument | [Control structure](../science/control_structure.md) and [memory-law proof](../science/memory_law.md) |
| Understand what classical memory can reproduce | [Classical boundary](../science/classical_boundary.md) |
| Check time limits and physical interpretation | [Examples](../science/examples.md) and [resource account](../science/interpretation.md) |

The textbook supplies quantum-information foundations. The control decomposition is an explicitly attributed research theorem, and the repeated-use memory law is proved in this repository. The learning material preserves that division. Its conceptual map does not claim to cover every specialist proof detail.

The main result concerns ideal controls and arbitrarily long finite experiments. It determines a hard coherent-memory dimension, not the shortest experiment, a thermodynamic cost or the runtime of a classical numerical calculation.

[Repository overview](../README.md) · [Scientific overview](../science/README.md) · [Attribution](../references/related_work.md)
