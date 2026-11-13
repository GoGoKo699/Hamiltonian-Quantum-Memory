# Store a qubit, erase the laboratory, retrieve it

[Learning route](README.md) · [Textbook bridge](WATROUS_BRIDGE.md) · [Memory-law proof](../science/memory_law.md)

A device is useful as quantum memory if it can return an unknown state together with its correlations. We test this using one half of a Bell pair. The other half stays sealed, so it cannot secretly carry the payload back to the device.

## The device and its input

Let the visible port $`S`$ and hidden bath $`E`$ each be one qubit. Their known static Hamiltonian is

```math
H=J W_{ES},\qquad J>0,
```

where the SWAP operator $`W_{ES}`$ exchanges their states and satisfies $`W_{ES}^2=I`$. Consequently

```math
e^{-itH}=\cos(Jt)I-i\sin(Jt)W_{ES}.
```

At $`t_*=\pi/(2J)`$, this is a SWAP up to a physically irrelevant global phase. The bath starts in any fixed supplied density operator $`\tau_E`$, independent of the laboratory.

Prepare the port and a reference qubit $`R`$ in

```math
|\Phi_2\rangle_{RS}
=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

The reference is now sealed. It has no interaction with the port, the bath or a controller until the final measurement. The port alone has the known mixed state $`I/2`$, but returning that local state is insufficient: its correlations with $`R`$ must survive. The emulator receives the actual port, and has no access to $`R`$ or an alternative input path.

## Follow one complete round

Write $`\Phi_{RS}=|\Phi_2\rangle\langle\Phi_2|_{RS}`$. The three relevant stages are

```math
\Phi_{RS}\otimes\tau_E
\ \xrightarrow{\text{write SWAP}}\
\Phi_{RE}\otimes\tau_S
\ \xrightarrow{\text{reset }S}\
\Phi_{RE}\otimes|0\rangle\langle0|_S
\ \xrightarrow{\text{read SWAP}}\
\Phi_{RS}\otimes|0\rangle\langle0|_E.
```

Each SWAP takes idle duration $`t_*`$. The middle intervention discards the port and prepares it in $`|0\rangle`$. Any additional accessible working or controller qubits would be discarded too. In this simple device none are needed. The reference is the only surviving laboratory quantum system, and its seal prevents a bypass.

After retrieval, measure the pair $`RS`$ using two outcomes:

```math
P_{\mathrm{pass}}=\Phi_{RS},\qquad
P_{\mathrm{fail}}=I_{RS}-\Phi_{RS}.
```

The physical device passes with probability one. The bath ends in $`|0\rangle`$, so another round can start with a fresh Bell pair without refreshing the bath. This explicit Hamiltonian supplies exact SWAPs; the general theorem instead obtains its storage operations through the inherited control result.

## What a purely classical emulator can do

A classical-memory emulator may measure, retain arbitrarily many classical outcomes and adapt its later behavior. It may use temporary quantum systems during each interval. At the cut, however, the port is erased and no hidden quantum system may survive: this is hard coherent dimension $`D=1`$.

After the cut, the sealed reference and any later returned output must have a separable state, of the form

```math
\rho_{RS}=\sum_x a_x\,\sigma_R^{(x)}\otimes\omega_S^{(x)},
\qquad a_x\ge0,\quad\sum_xa_x=1.
```

For a normalized product vector $`|u\rangle_R|v\rangle_S`$, Cauchy–Schwarz gives

```math
|\langle\Phi_2|u\otimes v\rangle|^2
=\frac{|u_0v_0+u_1v_1|^2}{2}
\le\frac12.
```

Decomposing mixed product states into pure ones and taking convex combinations preserves the bound. Therefore every such emulator has Bell acceptance at most one half. Measuring the input in the computational basis, retaining the outcome and returning the corresponding basis state attains one half, illustrating the difference between preserving a classical bit and preserving the full qubit.

The test counts both outcomes. Discarding failed rounds would change the task.

## Repeat against an adaptive emulator

Use a fresh independent Bell pair in every round. After measuring one round, discard its reference and payload and reset the laboratory before starting the next. The emulator may retain all classical history and change its strategy.

Conditional on any history in which earlier tests passed, the next fresh pair still faces the same erased-laboratory cut. The next conditional passing probability is at most one half. Thus

```math
\Pr_{\mathrm{physical}}(\text{all }n\text{ pass})=1,
\qquad
\Pr_{\mathrm{classical}}(\text{all }n\text{ pass})\le2^{-n}.
```

This multiplication uses conditional probabilities, not an assumption of independent emulator errors. The event difference lower-bounds total variation, giving separation at least $`1-2^{-n}`$.

| Rounds | Physical all-pass probability | Classical all-pass ceiling | Guaranteed separation |
| --- | --- | --- | --- |
| 1 | 1 | 1/2 | 1/2 |
| 3 | 1 | 1/8 | 7/8 |
| 6 | 1 | 1/64 | 63/64 |

Each experiment is finite. The separation approaches one as the number of rounds grows; the table does not claim perfect discrimination in one fixed finite experiment.

## Add a rare quantum sector

Now consider a device with the supplied controllability structure $`r_0=1`$, $`r_1=2`$, and initial sector weights $`1-p`$ and $`p`$. Assume the independent sector control required in [the scientific model](../science/model.md), including its indirectly compiled sector readout. The scalar sector needs only classical hidden storage. The two-dimensional sector supports the storage experiment above.

Read the sector into a flag, measure the flag and discard its quantum register. Keep only its classical value. Define event $`A_n`$ as: the flag reports the two-dimensional sector and every one of $`n`$ subsequent Bell tests passes. For the ideal effective operations,

```math
\Pr_{\mathrm{physical}}(A_n)=p,
\qquad
\Pr_{D=1}(A_n)\le2^{-n}.
```

The second bound lets the emulator choose any flag distribution. Requiring it to reproduce the target flag distribution would be an extra restriction and is unnecessary. The ideal event gives separation at least $`p-2^{-n}`$. For a general Hamiltonian realizing these sectors, finite control compilation gives, for any chosen total operational error $`\eta>0`$, a finite experiment with separation at least $`p-2^{-n}-\eta`$. This is one error budget for the whole compiled experiment.

Conversely, a classical emulator can simulate the scalar sector exactly and replace the quantum sector, giving uniform error at most $`p`$. Repetition approaches this same number from below. The exact all-time optimum is therefore $`\epsilon_1^\infty=p`$, while dimension $`D=2`$ represents both sectors exactly.

For example, if $`p=1/4`$, the ideal six-round lower bound is $`15/64`$ and the matching uniform upper bound is $`1/4`$. Finite compilation gives the former bound minus $`\eta`$. Rare sectors reduce the unavoidable operational discrepancy, even though their occupied quantum factor still requires a qubit for exact universal emulation.

## Resource account and scope

| Item | Treatment in the simple SWAP experiment |
| --- | --- |
| Hidden persistent quantum state | One bath qubit; every emulator hidden carrier is included in its hard cap. |
| Visible quantum systems | One port and one fresh sealed reference per round, used sequentially. |
| Input and output | A reference-correlated qubit enters; a qubit returns for a Bell measurement. |
| Preparations and measurements | One fresh Bell pair and one two-outcome Bell measurement per round. |
| Erasure | The port and all accessible work registers are erased at the storage cut; old test registers are discarded between rounds. |
| Bath reuse | The same bath persists; the read SWAP leaves it in a fixed state for the next round. |
| Idle duration | Two intervals per round, total $`2nt_*`$ for $`n`$ rounds. |
| Classical records | All labels, pass/failure outcomes and adaptation are allowed. |

These are ideal preparations, resets and controls. The general weighted-sector example may require long control compilation and is not assigned the explicit SWAP duration. The main theorem proves a structural memory cost over arbitrary finite experiments, with no universal shortest witness time or noisy-control guarantee.

[Next: the complete milestone map](MILESTONES.md) · [Exact proof and quantifiers](../science/memory_law.md) · [Physical limitations](../science/interpretation.md)
