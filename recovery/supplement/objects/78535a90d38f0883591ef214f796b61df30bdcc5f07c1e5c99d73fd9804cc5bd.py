#!/usr/bin/env python3
"""Self-reducibility of SORT-BOUND-U: decision vs search (unary, Phoebe only).

Sharp question.  Given a decision oracle for

    SORT-BOUND-U = { 1^n # 1^k : S(n) <= k },

can one construct an optimal comparison strategy for the antichain A_n within
budget k in polynomial time?

Referee correction (Antonina #301, 2026-10-21) fixes the search notion: the
explicit optimal tree for A_n has >= n! leaves, hence exponential output
length in unary n, so it cannot be produced by a poly(n)-time oracle Turing
reduction even when every oracle answer costs one step.  The polynomial-size
search output is the NEXT COMPARISON (equivalently a succinct online program
for adaptive next comparisons).  This probe therefore studies:

  (A) family preservation: is the comparison child of A_n again an antichain?
  (B) circularity: F(A_n + a<b) = S(n) - 1, so the child decision query is
      equivalent to the parent query (no strictly smaller instance).
  (C) oracle domains: root S(n) oracle vs general-poset subproblem oracle.
  (D) the general-poset subproblem oracle suffices for the next-comparison
      policy; the root S(n) oracle does not, because the child is a general
      poset.
  (E) explicit full tree / succinct DAG output sizes.

No PR, no Lean, no P/NP or class-separation claim.  Experiment + paper proof.
"""

import argparse
from functools import lru_cache

from state_compression import (
    extend,
    incomparable_pairs,
    linear_extensions,
    make_refined_canon,
)


# --------------------------------------------------------------------------
# Exact minimax on labelled posets (n <= 6) and on the S_n quotient (n >= 7).
# --------------------------------------------------------------------------

def labelled_F(n):
    states = {}

    def solve(succ):
        if succ in states:
            return states[succ]
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            states[succ] = 0
            return 0
        best = 1 + min(
            max(solve(extend(succ, i, j)), solve(extend(succ, j, i)))
            for i, j in pairs
        )
        states[succ] = best
        return best

    solve((0,) * n)
    return states


def quotient_F(n):
    """Exact minimax on isomorphism classes of posets under S_n relabelling."""
    canon_fn = make_refined_canon(n)
    states = {}

    def solve(c):
        if c in states:
            return states[c]
        pairs = incomparable_pairs(c, n)
        if not pairs:
            states[c] = 0
            return 0
        best = 1 + min(
            max(solve(canon_fn(extend(c, i, j))),
                solve(canon_fn(extend(c, j, i))))
            for i, j in pairs
        )
        states[c] = best
        return best

    root = canon_fn((0,) * n)
    solve(root)
    return states, canon_fn, root


def solve_states(n):
    """Return (S, states, root, is_quotient)."""
    if n <= 6:
        st = labelled_F(n)
        return st[(0,) * n], st, (0,) * n, False
    st, canon_fn, root = quotient_F(n)
    return st[root], st, root, True


def is_antichain(succ, n):
    """A state is an antichain iff it has no relations at all."""
    return all(s == 0 for s in succ)


def is_total(succ, n):
    return all(
        (succ[i] >> j & 1) or (succ[j] >> i & 1)
        for i in range(n) for j in range(i + 1, n)
    )


def describe_child(succ, n):
    """Coarse structural tag for a child of A_n + a<b (n>=2)."""
    if is_antichain(succ, n):
        return "antichain"
    if is_total(succ, n):
        return "total"
    # count 2-chain components heuristically: relations = edges of Hasse.
    rel = sum(bin(succ[i]).count("1") for i in range(n))
    return f"general(rel={rel})"


# --------------------------------------------------------------------------
# (A),(B) root symmetry and child circularity.
# --------------------------------------------------------------------------

def root_and_child(n, states, root, is_quotient, canon_fn=None):
    S = states[root]
    pairs = incomparable_pairs(root, n)
    Qs = []
    for i, j in pairs:
        a, b = extend(root, i, j), extend(root, j, i)
        if is_quotient:
            a, b = canon_fn(a), canon_fn(b)
        Qs.append(1 + max(states[a], states[b]))
    optimal = sum(1 for q in Qs if q == S)
    child = extend(root, 0, 1)          # A_n + 0<1, representative
    if is_quotient:
        child = canon_fn(child)
    Fchild = states[child]
    child_children = [extend(child, i, j)
                      for i, j in incomparable_pairs(child, n)]
    kinds = sorted({describe_child(c, n) for c in child_children})
    return dict(n=n, S=S, pairs=len(pairs), optimal=optimal,
                distinct_Q=sorted(set(Qs)), child=Fchild,
                S_minus_1=S - 1, child_antichain=is_antichain(child, n),
                child_children_kinds=kinds)


# --------------------------------------------------------------------------
# (C),(D) oracle domains.
# --------------------------------------------------------------------------

def oracle_call_upper_bound(n, k, states, root, is_quotient=False,
                            canon_fn=None):
    """Next-comparison policy with a GENERAL-POSET threshold oracle.

    At a state P with remaining budget d >= F(P), the policy tries all
    incomparable pairs and queries both children with budget d-1; a pair with
    both answers YES exists by F(P) <= d.  Returns (calls, found, q).
    """
    calls = [0]

    def key(P):
        return canon_fn(P) if is_quotient else P

    def oracle(P, d):
        calls[0] += 1
        return states[key(P)] <= d

    def next_comparison(P, d):
        for i, j in incomparable_pairs(P, n):
            if oracle(extend(P, i, j), d - 1) and oracle(extend(P, j, i), d - 1):
                return (i, j)
        return None

    q = next_comparison(root, k)
    return calls[0], q is not None, q


def policy_tree_size(n, states, root, is_quotient=False, canon_fn=None):
    """Nodes in the single-policy tree (first optimal move at each node).

    A single optimal policy is a reduced tree with exactly 2*n!-1 nodes
    (Theorem 2.1 / Observation 2.5 of docs/research-strategy-certificates.md).
    It visits only a small subset of all reachable posets, so a general poset
    P need not be a node of the A_n policy tree.
    """
    def key(P):
        return canon_fn(P) if is_quotient else P

    seen = set()

    def walk(P):
        if P in seen:
            return
        seen.add(P)
        val = states[key(P)]
        if val == 0:
            return
        for i, j in incomparable_pairs(P, n):
            a, b = extend(P, i, j), extend(P, j, i)
            if states[key(a)] <= val - 1 and states[key(b)] <= val - 1:
                walk(a)
                walk(b)
                return

    walk(root)
    return len(seen)


def worst_case_oracle_calls(n, states, is_quotient=False, canon_fn=None):
    """Max/average general-poset-oracle calls to output one next comparison.

    For every reachable state P we ask for the next comparison at the minimal
    budget d = F(P); a valid pair always exists.  This is the per-query cost
    of the polynomial-size search output (the next comparator).
    """
    def key(P):
        return canon_fn(P) if is_quotient else P

    max_calls = 0
    total = 0
    count = 0
    failures = 0
    for P, val in states.items():
        if val == 0:
            continue
        calls = 0
        found = False
        for i, j in incomparable_pairs(P, n):
            calls += 2
            a, b = extend(P, i, j), extend(P, j, i)
            if states[key(a)] <= val - 1 and states[key(b)] <= val - 1:
                found = True
                break
        if not found:
            failures += 1
        max_calls = max(max_calls, calls)
        total += calls
        count += 1
    return max_calls, (total / count if count else 0.0), count, failures


def root_oracle_cannot_answer_child(n, states):
    """The root S(n) oracle answers only antichain queries.

    The child P = A_n + a<b is a general poset; the oracle has no entry for
    it.  Show that F of general posets is not a function of n alone by
    exhibiting two reachable posets on the same n with different F.
    """
    by_F = {}
    for succ, val in states.items():
        by_F.setdefault(val, []).append(succ)
    vals = sorted(by_F)
    if len(vals) < 2:
        return None
    a = by_F[vals[0]][0]
    b = by_F[vals[-1]][0]
    return (vals[0], a, vals[-1], b)


def same_e_diff_F(n, states):
    """Witness that F is not determined by (n, e(P)): same n, same e, diff F."""
    by_e = {}
    for succ, val in states.items():
        by_e.setdefault(linear_extensions(succ, n), set()).add(val)
    for e, vals in sorted(by_e.items()):
        if len(vals) > 1:
            return e, sorted(vals)
    return None


# --------------------------------------------------------------------------
# (E) output sizes.
# --------------------------------------------------------------------------

def tree_and_dag_sizes(n, states):
    """Explicit tree size = 2*n!-1; reachable-state count as DAG upper bound."""
    import math
    leaves = math.factorial(n)
    return 2 * leaves - 1, len(states)


# --------------------------------------------------------------------------
# Driver.
# --------------------------------------------------------------------------

KNOWN = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 12: 30}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=8)
    ap.add_argument("--oracle-n", type=int, default=8)
    args = ap.parse_args()

    print("=" * 78)
    print("A/B. Root symmetry, child circularity, family non-preservation")
    print("=" * 78)
    print("n | S(n) | C(n,2) | optimal | distinct Q | F(child) | S-1 | "
          "child antichain? | child's children kinds")
    for n in range(2, args.max_n + 1):
        S, states, root, isq = solve_states(n)
        canon_fn = make_refined_canon(n) if isq else None
        r = root_and_child(n, states, root, isq, canon_fn)
        print(f"{n} | {r['S']} | {r['pairs']} | {r['optimal']} | "
              f"{r['distinct_Q']} | {r['child']} | {r['S_minus_1']} | "
              f"{r['child_antichain']} | {r['child_children_kinds']}")
    print("Reading: every root move is optimal (one S_n-orbit); the child "
          "F(A_n+a<b)=S(n)-1, so the child decision query is the parent query; "
          "the child is never an antichain and its children are general posets.")

    print()
    print("=" * 78)
    print("C/D. Oracle domains: subproblem oracle vs root S(n) oracle")
    print("=" * 78)
    n = args.oracle_n
    S, states, root, isq = solve_states(n)
    canon_fn = make_refined_canon(n) if isq else None
    for k in range(S, S + 3):
        calls, found, q = oracle_call_upper_bound(
            n, k, states, root, isq, canon_fn)
        print(f"n={n} k={k} (>=S={S}): next-comparison found={found} q={q} "
              f"general-poset-oracle calls={calls}")
    print("Root S(n) oracle: only antichain queries.  Child P=A_n+a<b is "
          "general, so the oracle has no entry for it.")
    if not isq:
        w = root_oracle_cannot_answer_child(n, states)
        if w:
            print(f"  witness: reachable posets with F={w[0]} and F={w[2]} on "
                  f"the same n={n}; F is not a function of n alone.")
        se = same_e_diff_F(n, states) if n <= 5 else None
        if se:
            print(f"  witness: #lin.ext={se[0]} with F in {se[1]}; F is not a "
                  f"function of (n, e(P)).")
    else:
        print("  (labelled witnesses shown for n<=6; quotient used for n=7,8)")

    mc, ac, cc, fail = worst_case_oracle_calls(n, states, isq, canon_fn)
    print(f"  per-query general-poset-oracle calls over {cc} non-total states: "
          f"max={mc} avg={ac:.2f} failures={fail} "
          f"(<=2*C(n,2)={2*(n*(n-1)//2)})")
    if not isq:
        import math
        pt = policy_tree_size(n, states, root)
        print(f"  A_n single-policy tree nodes={pt} (=2*n!-1={2*math.factorial(n)-1}) "
              f"vs reachable states={len(states)}; policy covers "
              f"{100*pt/len(states):.2f}% of posets, so a general P is usually "
              f"not a policy node.")

    print()
    print("=" * 78)
    print("E. Output sizes: explicit tree vs reachable-state DAG")
    print("=" * 78)
    print("n | S(n) | explicit tree 2n!-1 | reachable states (DAG <=)")
    for n in range(2, args.max_n + 1):
        S, states, root, isq = solve_states(n)
        t, d = tree_and_dag_sizes(n, states)
        tag = "quotient classes" if isq else "labelled states"
        print(f"{n} | {KNOWN.get(n, S)} | {t} | {d} ({tag})")
    print("Explicit tree is exponential in unary n; only the next comparator "
          "(or a succinct online program) is a polynomial-size search output.")


if __name__ == "__main__":
    main()
