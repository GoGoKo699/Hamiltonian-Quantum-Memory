#!/usr/bin/env python3
"""Finite matrix checks for Hamiltonian Quantum Memory; not a proof certificate."""

from __future__ import annotations

import argparse
import json
import platform
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import block_diag, expm
import sympy as sp

SEED = 20261113
TOL = 2e-10


def kron(*items):
    result = np.array([[1.0 + 0j]])
    for item in items:
        result = np.kron(result, item)
    return result


def bell(r):
    v = np.eye(r, dtype=complex).reshape(-1) / np.sqrt(r)
    return np.outer(v, v.conj())


def pure(v):
    v = np.asarray(v, dtype=complex)
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())


def trace_distance(a, b):
    difference = (a - b + (a - b).conj().T) / 2
    return float(np.abs(np.linalg.eigvalsh(difference)).sum() / 2)


def partial_trace(rho, dims, keep):
    """Trace other factors, retaining the original order of factors in keep."""
    keep = sorted(keep)
    tensor = rho.reshape(tuple(dims) * 2)
    remaining = list(dims)
    for axis in reversed(range(len(dims))):
        if axis not in keep:
            tensor = np.trace(tensor, axis1=axis, axis2=axis + len(remaining))
            remaining.pop(axis)
    size = int(np.prod(remaining))
    return tensor.reshape(size, size)


def permute_factors(rho, dims, order):
    axes = list(order) + [len(dims) + x for x in order]
    return rho.reshape(tuple(dims) * 2).transpose(axes).reshape(rho.shape)


def swap_matrix(dims, first, second):
    assert dims[first] == dims[second]
    size = int(np.prod(dims))
    u = np.zeros((size, size), dtype=complex)
    for index in range(size):
        digits = list(np.unravel_index(index, dims))
        digits[first], digits[second] = digits[second], digits[first]
        u[np.ravel_multi_index(tuple(digits), dims), index] = 1
    return u


def reset_factor(rho, dims, factor):
    """Actual trace-and-replace CPTP map, identity on every other factor."""
    result = np.zeros_like(rho)
    for index in range(dims[factor]):
        k = np.zeros((dims[factor], dims[factor]), dtype=complex)
        k[0, index] = 1
        factors = [np.eye(d) for d in dims]
        factors[factor] = k
        full = kron(*factors)
        result += full @ rho @ full.conj().T
    return result


def random_density(rng, dimension, rank=None):
    rank = dimension if rank is None else rank
    a = rng.normal(size=(dimension, rank)) + 1j * rng.normal(size=(dimension, rank))
    rho = a @ a.conj().T
    return rho / np.trace(rho)


def random_unitary(rng, dimension):
    a = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    q, r = np.linalg.qr(a)
    phases = np.diag(r)
    return q @ np.diag(phases / np.abs(phases)).conj()


def checked(name, condition):
    if not condition:
        raise AssertionError(name)


def check_storage_cut(rng):
    """Swap a Bell half into Q, erase L, then retrieve; include correlated BQ."""
    rows = []
    for r in (2, 3, 4):
        b = 2
        dims = [r, r, b, r]  # R(sealed), L(accessible), B(invisible), Q(bath).
        swap = swap_matrix(dims, 1, 3)
        checked("SWAP unitarity", np.linalg.norm(swap.conj().T @ swap - np.eye(swap.shape[0])) < TOL)
        for initial_rank in (1, b * r):
            tau = random_density(rng, b * r, initial_rank)
            initial = kron(bell(r), tau)
            written = swap @ initial @ swap.conj().T
            after_reset = reset_factor(written, dims, 1)
            # R is untouched by every map; all accessible L input is physically erased.
            checked("reset L is fixed", trace_distance(partial_trace(after_reset, dims, [1]), pure([1] + [0] * (r - 1))) < TOL)
            retrieved = swap @ after_reset @ swap.conj().T
            output = partial_trace(retrieved, dims, [0, 1])
            fidelity = float(np.trace(bell(r) @ output).real)
            error = trace_distance(output, bell(r))
            checked("Bell transmission after full reset", fidelity > 1 - TOL and error < TOL)
            # Classicalizing the only bath carrier destroys exactly its off-diagonal terms.
            dephased = np.zeros_like(after_reset)
            for a in range(r):
                projector = np.diag([float(a == c) for c in range(r)])
                k = kron(np.eye(r), np.eye(r), np.eye(b), projector)
                dephased += k @ after_reset @ k
            classical_output = partial_trace(swap @ dephased @ swap.conj().T, dims, [0, 1])
            classical_pass = float(np.trace(bell(r) @ classical_output).real)
            classical_distance = trace_distance(classical_output, bell(r))
            checked("classical carrier fails Bell test", abs(classical_pass - 1 / r) < TOL)
            checked("classical complete-channel loss", abs(classical_distance - (1 - 1 / r)) < TOL)
            rows.append({"payload_dimension": r, "invisible_dimension": b, "initial_BQ_rank": initial_rank,
                         "quantum_bell_pass": fidelity, "quantum_half_trace_error": error,
                         "dephased_bell_pass": classical_pass, "dephased_half_trace_error": classical_distance})
    # A product Bell measurement on two genuinely constructed reset/dephasing outputs.
    r = 2
    ideal = kron(bell(r), bell(r))
    classical = np.diag(np.diag(bell(r)))
    two_round_output = kron(classical, classical)
    two_round_pass = float(np.trace(ideal @ two_round_output).real)
    checked("two-round Bell event", abs(two_round_pass - 0.25) < TOL)
    return {"cases": rows, "two_round_classical_pass": two_round_pass,
            "scope": "Ideal effective SWAPs and exact resets; no Hamiltonian pulse synthesis is tested."}


def compression_output(r, d):
    """A physical D-memory encoder with classical block label and local decoder."""
    source = bell(r)
    output = np.zeros_like(source)
    completeness = np.zeros((r, r), dtype=complex)
    branches = []
    for start in range(0, r, d):
        count = min(d, r - start)
        encoder = np.zeros((d, r), dtype=complex)
        for a in range(count):
            encoder[a, start + a] = 1
        completeness += encoder.conj().T @ encoder
        encoded = kron(np.eye(r), encoder) @ source @ kron(np.eye(r), encoder).conj().T
        decoder = encoder.conj().T
        decoded = kron(np.eye(r), decoder) @ encoded @ kron(np.eye(r), decoder).conj().T
        output += decoded
        branches.append(float(np.trace(encoded).real))
    checked("encoder instrument CPTP", np.linalg.norm(completeness - np.eye(r)) < TOL)
    checked("decoder output normalized", abs(np.trace(output) - 1) < TOL)
    checked("sealed reference marginal unchanged", trace_distance(partial_trace(output, [r, r], [0]), np.eye(r) / r) < TOL)
    return output, branches


def check_dimension_bound(rng):
    rows = []
    worst_margin = 1.0
    for r in range(2, 7):
        for d in range(1, r + 1):
            # Actual R x M state plus an isometric local decoder M -> L.
            state = random_density(rng, r * d, min(3, r * d))
            v = random_unitary(rng, r)[:, :d]
            decoded = kron(np.eye(r), v) @ state @ kron(np.eye(r), v).conj().T
            pass_probability = float(np.trace(bell(r) @ decoded).real)
            bound = d / r
            checked("all tested D-carrier Bell overlaps", pass_probability <= bound + TOL)
            worst_margin = min(worst_margin, bound - pass_probability)
            # A Schmidt-rank-D state saturates the mathematical overlap inequality.
            coefficients = np.zeros((r, r), dtype=complex)
            coefficients[np.arange(d), np.arange(d)] = 1 / np.sqrt(d)
            saturating_state = pure(coefficients.reshape(-1))
            pure_pass = float(np.trace(bell(r) @ saturating_state).real)
            checked("rank-D state saturation", abs(pure_pass - bound) < TOL)
            output, branch_probabilities = compression_output(r, d)
            channel_pass = float(np.trace(bell(r) @ output).real)
            checked("physical compression respects bound", channel_pass <= bound + TOL)
            if r % d == 0:
                checked("physical divisible-block saturation", abs(channel_pass - bound) < TOL)
            rows.append({"payload_dimension": r, "memory_dimension": d,
                         "random_decoded_bell_pass": pass_probability, "bound": bound,
                         "pure_rank_D_saturation": pure_pass, "physical_block_channel_pass": channel_pass,
                         "classical_branch_probabilities": branch_probabilities,
                         "physical_channel_saturates": r % d == 0})
    return {"cases": rows, "smallest_random_case_margin": worst_margin,
            "scope": "Finite matrix witnesses for Schmidt-number/Bell overlap; no arbitrary-channel optimization or general converse is inferred."}


def hermitian_coordinates(a):
    """An exact real coordinate map, not an approximate complex rank test."""
    n = a.rows
    result = [sp.re(a[i, i]) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            result.extend([sp.re(a[i, j]), sp.im(a[i, j])])
    return result


def su3_hermitian_generators():
    out = []
    for i in range(3):
        for j in range(i + 1, 3):
            real = sp.zeros(3)
            real[i, j] = real[j, i] = 1
            imag = sp.zeros(3)
            imag[i, j], imag[j, i] = -sp.I, sp.I
            out.extend([real, imag])
    out.extend([sp.diag(1, -1, 0), sp.diag(1, 1, -2)])
    return out


def exact_lie_dimension(g):
    """Breadth-first closure under i[A,B], with rational real row elimination."""
    c, x, z = sp.diag(-1, 0, 1), sp.Matrix([[0, 1], [1, 0]]), sp.diag(1, -1)
    drift = sp.kronecker_product(c, z) + g * sp.kronecker_product(sp.eye(3), x)
    candidates = [sp.kronecker_product(a, sp.eye(2)) for a in su3_hermitian_generators()] + [drift]
    pivots = {}
    matrices = []
    queue = deque()

    def add(a):
        nonlocal matrices
        checked("Hermitian Lie element", a == a.conjugate().T)
        checked("traceless Lie element", sp.trace(a) == 0)
        v = hermitian_coordinates(a)
        for pivot in sorted(pivots):
            factor = v[pivot]
            if factor:
                v = [sp.cancel(value - factor * old) for value, old in zip(v, pivots[pivot])]
        pivot = next((i for i, value in enumerate(v) if value != 0), None)
        if pivot is None:
            return False
        scale = v[pivot]
        pivots[pivot] = [sp.cancel(value / scale) for value in v]
        matrices.append(a)
        queue.append(a)
        return True

    for candidate in candidates:
        add(candidate)
    brackets = 0
    while queue:
        a = queue.popleft()
        for b in list(matrices):
            bracket = sp.I * (a * b - b * a)
            brackets += 1
            add(bracket)
            if len(matrices) == 35:
                return {"g": str(g), "dimension": 35, "brackets_examined": brackets,
                        "certificate": "35 exact rational independent traceless Hermitian matrices span su(6)."}
    # Queue exhaustion means every basis pair has been tested at some stage.
    return {"g": str(g), "dimension": len(matrices), "brackets_examined": brackets,
            "certificate": "Exact rational bracket closure exhausted; no floating rank threshold used."}


def check_lie_closure():
    rows = [exact_lie_dimension(sp.Rational(g)) for g in (0, 1, sp.Rational(1, 3))]
    checked("zero-g closure dimension", rows[0]["dimension"] == 16)
    checked("nonzero-g closure dimensions", all(row["dimension"] == 35 for row in rows[1:]))
    return {"cases": rows,
            "scope": "Exact closure at g=0,1,1/3 only; the all-nonzero-g assertion uses the analytical spanning proof."}


def apply_port_kraus(rho, operators, r=3, e=2):
    out = np.zeros_like(rho)
    for a in operators:
        k = kron(np.eye(r), a, np.eye(e))
        out += k @ rho @ k.conj().T
    return out


def adaptive_outputs(g, total_time, tau, port_controls):
    c, x, z = np.diag([-1, 0, 1]), np.array([[0, 1], [1, 0]]), np.diag([1, -1])
    h = kron(c, z) + g * kron(np.eye(3), x)
    state = kron(bell(3), tau)  # R, S, E.
    first = kron(np.eye(3), expm(-1j * 0.25 * total_time * h))
    state = first @ state @ first.conj().T
    k0 = np.diag(np.sqrt([0.8, 0.3, 0.65]))
    k1 = np.diag(np.sqrt([0.2, 0.7, 0.35]))
    branches = []
    for outcome, measurement in enumerate((k0, k1)):
        branch = apply_port_kraus(state, [measurement])
        control = kron(np.eye(3), port_controls[outcome], np.eye(2))
        branch = control @ branch @ control.conj().T
        # The longest branch has total idle duration exactly the declared horizon.
        duration = (0.4 if outcome == 0 else 0.75) * total_time
        evolution = kron(np.eye(3), expm(-1j * duration * h))
        branch = evolution @ branch @ evolution.conj().T
        branches.append(partial_trace(branch, [3, 3, 2], [0, 1]))
    return branches


def check_perturbation(rng):
    rows = []
    controls = [random_unitary(rng, 3), random_unitary(rng, 3)]
    for initial_rank in (1, 2):
        tau = random_density(rng, 2, initial_rank)
        for g in (0.01, 0.1, 0.4):
            for time in (0.2, 1.0, 3.0):
                target = adaptive_outputs(g, time, tau, controls)
                stand_in = adaptive_outputs(0, time, tau, controls)
                # Distinct classical measurement outcomes are orthogonal output flags.
                error = sum(trace_distance(a, b) for a, b in zip(target, stand_in))
                bound = min(1.0, abs(g) * time)
                checked("adaptive hard-horizon perturbation bound", error <= bound + TOL)
                checked("instrument output trace", abs(sum(np.trace(a) for a in target) - 1) < TOL)
                rows.append({"g": g, "hard_horizon": time, "initial_bath_rank": initial_rank,
                             "flagged_half_trace_distance": error, "duhamel_bound": bound})
    checked("perturbation experiment is nontrivial", max(x["flagged_half_trace_distance"] for x in rows) > 1e-3)
    return {"cases": rows,
            "scope": "One explicit adaptive two-interval instrument with sealed reference and all outcome flags retained; not optimization over testers or a finite-time memory formula."}


def check_sector_weights(rng):
    r_values, b_values = [1, 2, 4], [2, 1, 2]
    prescribed = np.array([0.6, 0.3, 0.1])
    sizes = [r * b for r, b in zip(r_values, b_values)]
    vectors = []
    for size, weight in zip(sizes, prescribed):
        vector = rng.normal(size=size) + 1j * rng.normal(size=size)
        vectors.append(np.sqrt(weight) * vector / np.linalg.norm(vector))
    tau = pure(np.concatenate(vectors))  # Includes off-diagonal sector coherence.
    offsets = np.cumsum([0] + sizes)
    observed = []
    q_states = []
    full_interval, effective_interval = [], []
    for j, (r, b) in enumerate(zip(r_values, b_values)):
        block = tau[offsets[j]:offsets[j + 1], offsets[j]:offsets[j + 1]]
        weight = float(np.trace(block).real)
        observed.append(weight)
        q_states.append(partial_trace(block, [b, r], [1]))  # Unnormalized p_j sigma_Qj.
        q_port = random_unitary(rng, r * 3)
        invisible = random_unitary(rng, b)
        full_interval.append(kron(invisible, q_port))
        effective_interval.append(q_port)
    full_u = block_diag(*full_interval)
    effective_u = block_diag(*effective_interval)
    # Initial order R,S,E -> R,E,S, for block-diagonal bath-sector evolutions.
    initial_full = permute_factors(kron(bell(3), tau), [3, 3, sum(sizes)], [0, 2, 1])
    effective_tau = block_diag(*q_states)
    initial_effective = permute_factors(kron(bell(3), effective_tau), [3, 3, sum(r_values)], [0, 2, 1])
    control = random_unitary(rng, 3)
    outputs = []
    for state, env_dimension, interval in ((initial_full, sum(sizes), full_u),
                                            (initial_effective, sum(r_values), effective_u)):
        u = kron(np.eye(3), interval)
        state = u @ state @ u.conj().T
        k = kron(np.eye(3), np.eye(env_dimension), control)
        state = k @ state @ k.conj().T
        state = u @ state @ u.conj().T
        outputs.append(partial_trace(state, [3, env_dimension, 3], [0, 2]))
    reduction_error = trace_distance(*outputs)
    checked("sector weight recovery", np.max(np.abs(np.array(observed) - prescribed)) < TOL)
    checked("sector coherences and invisible factors do not affect this controlled output", reduction_error < TOL)
    staircase = {str(d): float(sum(p for p, r in zip(observed, r_values) if r > d)) for d in (1, 2, 3, 4)}
    checked("weighted staircase example", np.max(np.abs(np.array(list(staircase.values())) - [0.4, 0.1, 0.1, 0])) < TOL)
    # An actual compression channel in the only r>D sector, followed by two Bell tests.
    output, _ = compression_output(4, 2)
    two_round_pass = float(np.trace(kron(bell(4), bell(4)) @ kron(output, output)).real)
    weighted_pass = observed[2] * two_round_pass
    checked("weighted finite repeated event", abs(weighted_pass - 0.025) < TOL)
    return {"controllable_dimensions": r_values, "invisible_dimensions": b_values,
            "actual_projector_weights": observed, "tail_by_memory_dimension": staircase,
            "two_interval_reference_complete_reduction_error": reduction_error,
            "D2_two_round_physical_bath_event": observed[2],
            "D2_two_round_block_compressor_event": weighted_pass,
            "scope": "Known prescribed block structure, not an algorithm inferring the decomposition; two actual controlled intervals and a finite repeated compression witness."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    rng = np.random.default_rng(SEED)
    report = {"generated_at_utc": datetime.now(timezone.utc).isoformat(), "random_seed": SEED,
              "tolerance": TOL, "environment": {"python": platform.python_version(), "numpy": np.__version__,
                "scipy": scipy.__version__, "sympy": sp.__version__},
              "status": "running", "checks": {}}
    for name, function in (("storage_cut", lambda: check_storage_cut(rng)),
                           ("dimension_bound", lambda: check_dimension_bound(rng)),
                           ("exact_lie_closure", check_lie_closure),
                           ("finite_time_perturbation", lambda: check_perturbation(rng)),
                           ("weighted_sectors", lambda: check_sector_weights(rng))):
        report["checks"][name] = function()
        print(f"PASS {name}", flush=True)
    report["status"] = "passed"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Saved {args.output}")


if __name__ == "__main__":
    main()
