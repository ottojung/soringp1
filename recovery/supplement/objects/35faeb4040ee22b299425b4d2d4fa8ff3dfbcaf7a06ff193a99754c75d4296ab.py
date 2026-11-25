#!/usr/bin/env python3
"""Independent audit of the 'labelled strategy certificates are >= n!' claim.

Scope question.  The #301 claim (2026-10-19, "Poly(N) certificates for
SORT-BOUND-U") states that every correct comparison strategy has >= n!
terminal nodes, that this is *representation-independent*, and that the
S_n-quotient DAG is the *only* strategy representation that can be
polynomial.  We audit this against three representation families:

  (A) explicit output-labelled decision tree / hash-consed poset DAG
      (un-quotiented): terminal nodes are the n! distinct total orders;
  (B) S_n-quotient DAG: all total orders fold to one class;
  (C) transcript-based program / circuit: computes the next comparison from
      the remembered transcript; no per-permutation sink is materialised.

The audit separates *representation size* from *verification complexity* and
then builds a concrete coNP-hardness reduction showing that a poly-size
program is not *self-certifying*.

Stdlib only.  Experiments and paper-level deductions; no complexity-class
claim about SORT-BOUND-U is made.
"""

from __future__ import annotations

import itertools
import math
import sys

sys.path.insert(0, ".")
from scripts.adversary_certificates import (  # noqa: E402
    extend, incomparable_pairs, is_total, minimax_values, relabel_dual,
)


# --------------------------------------------------------------------------
# (A)+(B): explicit / quotient strategy DAG node and leaf counts
# --------------------------------------------------------------------------

def explicit_strategy_counts(n):
    """Union-of-all-optimal-moves DAG.  Returns (nodes, leaves, quotient)."""
    m = minimax_values(n)
    empty = (0,) * n
    nodes = {}
    leaves = set()

    def build(P):
        if P in nodes:
            return nodes[P]
        nid = len(nodes)
        nodes[P] = nid
        if is_total(P):
            leaves.add(nid)
            return nid
        f = m[P]
        for (i, j) in incomparable_pairs(P):
            a = extend(P, i, j)
            b = extend(P, j, i)
            if 1 + max(m[a], m[b]) == f:
                build(a)
                build(b)
        return nid

    build(empty)
    quot = len({relabel_dual(P) for P in nodes})
    return len(nodes), len(leaves), quot


def report_explicit():
    print("=" * 74)
    print("(A)/(B) EXPLICIT vs QUOTIENT STRATEGY-DAG SIZES (union of all optimal moves)")
    print("=" * 74)
    print(f"{'n':>2} {'n!':>7} {'DAG nodes':>10} {'DAG leaves':>11} "
          f"{'quotient':>9} {'nodes>=n!?':>10}")
    for n in range(2, 7):
        nodes, leaves, quot = explicit_strategy_counts(n)
        print(f"{n:>2} {math.factorial(n):>7} {nodes:>10} {leaves:>11} "
              f"{quot:>9} {str(nodes >= math.factorial(n)):>10}")
    print()
    print("Observation: leaves = n! exactly; nodes >= n! (so an explicit DAG is")
    print("exponential in N = n+k+1 for informative k).  The quotient folds all")
    print("total orders to one class and is far smaller.")
    print()


# --------------------------------------------------------------------------
# (C): transcript-based comparison programs
# --------------------------------------------------------------------------

class SimResult:
    __slots__ = ("correct", "steps", "output")

    def __init__(self, correct, steps, output):
        self.correct = correct
        self.steps = steps
        self.output = output


def simulate(prog, arr, budget):
    """Run a transcript-based program on one input permutation.

    prog(n, transcript) -> ('cmp', i, j) or ('stop', output_perm)
    transcript is a tuple of (i, j, outcome) with outcome = arr[i] < arr[j].
    output_perm must be the tuple of indices sorted by increasing value.
    """
    n = len(arr)
    transcript = []
    for _ in range(budget + 1):
        action = prog(n, transcript)
        if action[0] == "stop":
            correct = tuple(action[1]) == tuple(sorted(range(n), key=lambda i: arr[i]))
            return SimResult(correct, len(transcript), action[1])
        _, i, j = action
        outcome = arr[i] < arr[j]
        transcript.append((i, j, outcome))
    return SimResult(False, budget + 1, None)


def check_program(prog, n, budget):
    """Check over all n! inputs; returns (all_correct, witness_perm)."""
    for perm in itertools.permutations(range(n)):
        r = simulate(prog, perm, budget)
        if not r.correct:
            return False, perm
    return True, None


def make_reduction_program(m, phi):
    """UNSAT -> correct sorting program.

    n = 2m keys.  Read x_i = [key_{2i} > key_{2i+1}].  If phi(x) holds, stop
    and output a fixed wrong order (identity); else compare all pairs and
    output the true order.  The program is correct iff phi is unsatisfiable.
    """
    n = 2 * m
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]

    def prog(nn, transcript):
        if len(transcript) < m:
            k = len(transcript)
            return ("cmp", 2 * k, 2 * k + 1)
        x = [0] * m
        for (i, j, outcome) in transcript[:m]:
            # outcome True means arr[i] < arr[j]; x = 1 iff arr[2k] > arr[2k+1]
            x[i // 2] = 0 if outcome else 1
        if phi(x):
            return ("stop", tuple(range(n)))  # identity: wrong for most orders
        done = len(transcript) - m
        if done < len(pairs):
            i, j = pairs[done]
            return ("cmp", i, j)
        # reconstruct the total order from the recorded pair outcomes
        below = [0] * n
        for (i, j, outcome) in transcript[m:]:
            if outcome:
                below[j] += 1
            else:
                below[i] += 1
        order = tuple(sorted(range(n), key=lambda a: below[a]))
        return ("stop", order)

    return prog


def report_program_reduction():
    print("=" * 74)
    print("(C) SELF-CERTIFICATION BARRIER: reduction UNSAT <= V_SORT")
    print("=" * 74)
    budget = 4 + 6  # reading 2 + all 6 pairs, n=4

    phi_sat = lambda x: x[0] and x[1]                 # satisfiable
    phi_unsat = lambda x: x[0] and (not x[0])         # unsatisfiable

    for name, phi, expect in [("x1 AND x2 (SAT)", phi_sat, False),
                              ("x1 AND NOT x1 (UNSAT)", phi_unsat, True)]:
        prog = make_reduction_program(2, phi)
        ok, witness = check_program(prog, 4, budget)
        print(f"  phi = {name:24s}  program_correct={ok}  expected={expect}"
              + ("" if ok else f"   witness perm={witness}"))
    print()
    print("A poly-time V_SORT (decide whether a given program is a correct")
    print("budget-k sorting strategy) would decide UNSAT in poly time on these")
    print("poly-size instances; hence V_SORT is coNP-hard.  In coNP, a failing")
    print("permutation is a poly witness.  Therefore V_SORT is coNP-complete.")
    print()


def main():
    report_explicit()
    report_program_reduction()
    print("=" * 74)
    print("SCOPE VERDICT")
    print("=" * 74)
    print("The >= n! bound holds for (A) un-quotiented explicit poset/decision")
    print("representations whose terminals materialise the n! total orders.")
    print("It does NOT hold for (B) the S_n quotient (all totals fold to one),")
    print("nor for (C) transcript-based programs (mergesort is a poly-size")
    print("counterexample).  Hence it is representation-specific, not")
    print("representation-independent, and (B) is not the only poly route.")


if __name__ == "__main__":
    main()
