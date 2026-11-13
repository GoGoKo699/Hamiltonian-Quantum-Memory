# A sharp memory–error law

[Model](model.md) · [Control structure](control_structure.md) · [Classical boundary](classical_boundary.md)

Let $`r_j,p_j,q_D`$ and the two operational errors be defined in the [model](model.md). Classical storage is unrestricted, while every surviving private quantum register of a simulator is included in the hard dimension bound $`D`$.

## The theorem

For every supplied finite Hamiltonian and initial bath state in that model,

```math
\boxed{\displaystyle
\epsilon_D^\infty(H,\tau)
=\sum_{j:r_j>D}p_j=q_D.}
```

Moreover,

```math
\boxed{\displaystyle
\lim_{T\to\infty}\epsilon_D(T)=q_D.}
```

Thus the minimum dimension for an exact universally compatible simulator is

```math
D_{\mathrm{exact}}
=\max_{j:p_j>0}r_j.
```

For a permitted uniform error $`0\le\epsilon<1`$, the minimum dimension is the smallest integer $`D\ge1`$ satisfying $`q_D\le\epsilon`$. This is a tail of *active controllable-factor dimensions*. It is not an eigenvalue truncation of the entire bath state.

## Upper bound: keep small factors and a classical sector

The [control decomposition](control_structure.md#consequence-for-the-physical-drift) gives an exact compatible model with a classical label $`j`$ and an $`r_j`$-dimensional quantum register. Its interval Hamiltonian acts only on that register and the original physical port $`S`$; the stabilization qubit and further user ancillas remain outside the simulator. On sectors $`r_j\le D`$, embed this register in a common $`D`$-dimensional memory and simulate exactly. On sectors $`r_j>D`$, use any fixed causal $`D`$-memory stand-in with the same initial sector weight. All branches remain trace preserving.

For every tester, the target and simulator are convex mixtures with identical weights; they agree on all low-dimension branches. Total variation, or half trace distance before the final measurement, is therefore at most

```math
\sum_{j:r_j>D}p_j=q_D.
```

The same construction answers every schedule and every horizon. It proves both $`\epsilon_D^\infty\le q_D`$ and $`\epsilon_D(T)\le q_D`$.

## A one-round dimension lemma

Prepare $`|\Phi_r\rangle_{RL}=r^{-1/2}\sum_{a=1}^r|a\rangle_R|a\rangle_L`$, with $`R`$ sealed. A causal encoder may process $`L`$ and an arbitrary preexisting simulator state, but cannot touch $`R`$. At a designated cut erase every accessible working register. Suppose the only surviving private coherent carrier has dimension at most $`D`$, with unlimited classical side information. After arbitrary local decoding, let $`L'`$ be an $`r`$-dimensional output. Then

```math
\Pr[\Phi_r\text{ on }RL']\le\min\{1,D/r\}.
```

To prove this, condition on any classical branch at the cut. Every state on $`R\otimes M_D`$ has Schmidt number at most $`D`$. Local decoding and discarding systems cannot increase that Schmidt number. For a normalized pure output of Schmidt rank $`k\le D`$, write its coefficient matrix as $`Y`$, with $`\|Y\|_2=1`$. Then

```math
|\langle\Phi_r|\psi\rangle|^2
=\frac{|\operatorname{Tr}Y|^2}{r}
\le\frac{\|Y\|_1^2}{r}
\le\frac{k}{r}\le\frac Dr.
```

Convexity gives the same bound for mixed states and arbitrary classical mixtures. Conditioning on a branch with nonzero probability does not create a larger coherent carrier. The probability bound is unconditional over the encoder's current classical outcomes; it remains true for every normalized simulator state supplied by a previous history.

The lemma is the usual finite-dimensional Bell-overlap bound. It does not assume an independent-meter implementation, a pure simulator, or a finite classical alphabet.

## The finite repeated tester

First indirectly read $`j`$ by the [sector-flag operation](control_structure.md#reading-the-conserved-sector). Keep the measured label classically and discard its quantum flag. If $`r_j\le D`$, output failure for the event defined below. If $`r_j>D`$, repeat the following $`r_j`$-dimensional storage test $`n`$ times.

1. Prepare a fresh Bell pair $`\Phi_{r_j}`$ between a payload $`L`$ and a sealed reference $`R`$. It is independent of the process and of every previous history.
2. Compile a SWAP from $`L`$ into the bath factor $`Q_j`$.
3. Apply trace-and-replace to the port and **all accessible working quantum systems**, including the stabilization qubit, payload, flag remnants and controller ancillas. Preserve only the measured classical transcript and the sealed reference. No accessible input-dependent quantum carrier survives.
4. Compile a SWAP from $`Q_j`$ into a fresh payload and perform the Bell measurement on that payload and $`R`$.
5. Record the result classically, dispose of the reference and payload, and reset the working laboratory before preparing the next fresh pair.

The only reference that survives a storage cut is passive and inaccessible to the encoder, simulator and decoder. It cannot be used as an input path around the reset. The terminal Bell measurement checks transmission across that cut. Old references are disposed of before the next round.

Let $`A_n`$ be the event that the flagged sector is high and every Bell test passes. Under ideal effective sector and SWAP operations, the physical bath gives

```math
\Pr_{P_{H,\tau}}(A_n)=q_D.
```

This remains true for arbitrary initial rank or correlations inside a sector. The first encoding transfers the old bath state into a working register that is erased; the new payload in $`Q_j`$ is independent of the invisible multiplicity factor. Retrieval leaves $`Q_j`$ in a fixed state, so the next round is well defined.

For any $`D`$-memory simulator, condition on the flagged label and any preceding observed history in which the earlier rounds passed. The simulator's current private state may depend arbitrarily on that history. The next Bell pair is nevertheless fresh and independent. The one-round lemma gives a conditional pass probability at most $`D/r_j`$. Iterating conditional probabilities yields

```math
\Pr_{\mathsf M}(A_n)
\le\sum_{j:r_j>D}\Pr_{\mathsf M}(j)
       (D/r_j)^n
\le\left(\frac{D}{D+1}\right)^n.
```

The simulator is free to report a different label distribution; the last inequality holds for every distribution, including that choice. Adaptive classical history and entanglement in its counted memory do not change the conditional dimension bound.

## Finite control approximation and lower bound

The preceding ideal effective tester need not be exactly reachable in finite time. For every $`n`$ and every $`\eta>0`$, [control closure](control_structure.md#reachable-operations-closure-is-sufficient) supplies a finite permitted tester whose target event probability is at least $`q_D-\eta`$. Here $`\eta`$ bounds the total operational error of all compiled controls, not a separate uncharged error per gate.

The simulator upper bound remains valid for this actual tester. Its encoding and decoding are just some causal operations separated by the prescribed full reset. The dimension lemma does not require those compiled operations to resemble a SWAP on the simulator's unknown internal memory. Therefore every permitted simulator satisfies the finite bound

```math
\boxed{\displaystyle
d(P_{H,\tau},\mathsf M;\mathsf T_{n,\eta})
\ge q_D-\left(\frac{D}{D+1}\right)^n-\eta.}
```

The tester $`\mathsf T_{n,\eta}`$ is chosen using the target Hamiltonian and $`D`$, independently of the simulator. For every positive $`\delta`$, choose finite $`n`$ and positive $`\eta`$ making the last two terms at most $`\delta`$. Taking the supremum over finite testers proves $`d_\infty(P_{H,\tau},\mathsf M)\ge q_D`$ for every simulator, and then the infimum proves the theorem.

This argument does not exchange an infimum with an infinite experiment. For each requested tolerance, the witness has finitely many interventions and finite duration.

## Horizon-specific simulators

Let $`T_{n,\eta}<\infty`$ be the idle duration of the compiled tester. The same finite lower bound holds against every compatible $`D`$-memory simulator designed for that horizon. Hence

```math
\epsilon_D(T)\ge
q_D-\left(\frac{D}{D+1}\right)^n-\eta,
\qquad T\ge T_{n,\eta}.
```

Monotonicity and the upper bound $`q_D`$ imply $`\lim_{T\to\infty}\epsilon_D(T)=q_D`$. No bound on $`T_{n,\eta}`$ follows from this proof. In particular, a statement about a fixed short horizon cannot replace the limit in the theorem.

## Attribution and scope

The coherent/classical memory convention and compatible causal realizations follow the framework of Bisio, D'Ariano, Perinotti and Sedlák, *Memory cost of quantum protocols*, Phys. Rev. A **85**, 032333 (2012), [arXiv:1112.3853](https://arxiv.org/abs/1112.3853). The bath factors and their controllability come from Kato–Owari–Maruyama. Classical/quantum/irrelevant decompositions also have the Koashi–Imoto antecedent. The contribution here is the sharp operational tail law for the complete static-Hamiltonian family and its repeated-use dimension converse, after those ingredients are credited.

This proof assumes exact resets, ideal local operations, a finite known bath and unrestricted finite experiments. It supplies no efficient pulse compiler or finite-time optimal compression law. It also does not apply to simulators whose uncounted quantum memory can survive an intervention, or to an apparatus with free preshared entanglement to the user.

The lower bound is for physical quantum-port emulation of unknown reference-correlated inputs. It is not a lower bound on classical numerical calculation of the same dynamics. The [example](examples.md) separates the unlimited-horizon obstruction from a finite-time perturbation bound.
