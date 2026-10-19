#!/usr/bin/env python3
"""Retrograde (backward) exact evaluation of the sorting number S(n) on tiny n.

Model (matches docs/problem.md and scripts/state_compression.py):
  * n distinct labelled keys; a state is a transitively closed strict partial
    order on {0,...,n-1}, stored as a tuple ``succ`` of successor bitmasks
    (bit j of succ[i] is set iff i < j).
  * Comparing an incomparable pair {i,j} yields the two children
    ``extend(P,i,j)`` and ``extend(P,j,i)`` (transitive closure).
  * ``F(P)`` is the minimum number of remaining worst-case comparisons that
    suffices to finish sorting from P; F(P)=0 iff P is a chain, and
    F(antichain_n)=S(n).
  * ``CanSort(P,d)`` means F(P) <= d.

Algorithm: retrograde / layer-wise BACKWARD evaluation.
  1. Enumerate every labelled poset on n elements by exhaustive 3-state
     relation generation (each unordered pair is '<', '>' or incomparable) and
     keep the transitive ones.  For n=4 this is the 219 states A001035(4).
  2. Build every legal forward comparison transition and INVERT the finite
     transition graph, storing predecessor lists plus a per-(state,
     comparison) counter.
  3. Evaluate winning layers bottom-up: W_0 = chains; a state enters W_d
     exactly when some comparison has BOTH children in W_{d-1}.  A single
     sweep over the reverse edges then gives F(P) for every state.

This is NOT the source's algorithm.  Stober-Weiss (ALENEX 2023,
arXiv:2206.05597) enumerate predecessors on the fly by iterating Hasse-diagram
edges and running ``enumeratePredecessors`` (Section 4.1 Lemma 4.1, Section 4.2
Lemma 4.2, Section 5.7 Lemma 5.1/5.2 and Corollary 5.1).  Their Section 4.1 and
5.7 point is that for one fixed comparison (u,v) a child can have MULTIPLE
predecessors P', because different subsets of the transitively implied edges may
already be present in P'.  We sidestep that subtlety by enumerating all states
offline; the price is storage O(A001035(n) * n^2), which is NOT polynomial
space.  The paper's method is the scalable one; this is a transparent finite
fixture.

The forward recursion below is used ONLY as an independent cross-check and is
separate from the retrograde machinery.  This is a finite n <= 4 experiment: it
proves nothing asymptotic and says nothing about P, NP or EXPTIME.
"""

import argparse
import itertools
from functools import lru_cache


# --------------------------------------------------------------------------
# Poset representation: tuple of successor bitmasks, transitively closed.
# --------------------------------------------------------------------------

def extend(succ, i, j):
    """Add i < j to an already transitively closed poset; return the closure."""
    out = list(succ)
    new_greater = succ[j] | (1 << j)
    for x in range(len(succ)):
        if x == i or (succ[x] & (1 << i)):
            out[x] |= new_greater
    return tuple(out)


def incomparable_pairs(succ, n):
    return [
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if not (succ[i] & (1 << j)) and not (succ[j] & (1 << i))
    ]


def is_chain(succ, n):
    return not incomparable_pairs(succ, n)


def _transitive(lt, n):
    for a in range(n):
        row_a = lt[a]
        for b in range(n):
            if row_a[b]:
                row_b = lt[b]
                for c in range(n):
                    if row_b[c] and not row_a[c]:
                        return False
    return True


def enumerate_posets(n):
    """Every labelled poset on {0,...,n-1}, by exhaustive 3-state relation
    generation.  Each unordered pair is '<', '>' or incomparable; keep the
    transitive assignments.  Returns (posets, index) with posets a list of
    successor tuples and index a dict succ -> position."""
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    index = {}
    posets = []
    for choice in itertools.product((0, 1, 2), repeat=len(pairs)):
        lt = [[False] * n for _ in range(n)]
        for (i, j), c in zip(pairs, choice):
            if c == 1:
                lt[i][j] = True
            elif c == 2:
                lt[j][i] = True
        if not _transitive(lt, n):
            continue
        succ = tuple(sum(1 << j for j in range(n) if lt[i][j]) for i in range(n))
        if succ not in index:
            index[succ] = len(posets)
            posets.append(succ)
    return posets, index


def comparison_reachable(n):
    """Forward breadth-first closure from the antichain under legal
    comparisons.  Used as a fixture check that the exhaustive enumeration
    equals the comparison-reachable set (which, on labelled states, is all
    posets)."""
    start = (0,) * n
    seen = {start}
    stack = [start]
    while stack:
        p = stack.pop()
        for (i, j) in incomparable_pairs(p, n):
            for child in (extend(p, i, j), extend(p, j, i)):
                if child not in seen:
                    seen.add(child)
                    stack.append(child)
    return seen


# --------------------------------------------------------------------------
# Retrograde layer sweep over the inverted finite transition graph.
# --------------------------------------------------------------------------

class Retrograde:
    """Backward DP result for one n.

    The reverse transition graph is built OFFLINE from every enumerated state
    (all-poset graph construction).  This is deliberately NOT the source's
    on-the-fly Hasse-edge predecessor generation (``enumeratePredecessors``,
    Section 5.7); see the module docstring for the distinction.

    Attributes:
      posets        list of all labelled poset states
      index         succ -> position
      F             list; F[p] = minimum remaining worst-case comparisons
      S             F of the antichain = S(n)
      moves_of      moves_of[p] = list of move ids available at state p
      move_owner    move id -> state
      move_pair     move id -> compared pair (i, j)
      move_children move id -> (child_ij, child_ji)
      pred          pred[c] = list of move ids whose child is c
    """

    def __init__(self, n):
        self.n = n
        self.posets, self.index = enumerate_posets(n)
        N = len(self.posets)
        self.moves_of = [[] for _ in range(N)]
        self.pred = [[] for _ in range(N)]
        self.move_owner = []
        self.move_pair = []
        self.move_children = []
        for p in range(N):
            for (i, j) in incomparable_pairs(self.posets[p], n):
                c1 = self.index[extend(self.posets[p], i, j)]
                c2 = self.index[extend(self.posets[p], j, i)]
                mid = len(self.move_owner)
                self.move_owner.append(p)
                self.move_pair.append((i, j))
                self.move_children.append((c1, c2))
                self.moves_of[p].append(mid)
                self.pred[c1].append(mid)
                self.pred[c2].append(mid)
        self.F = [None] * N
        self._layer_sweep()
        self.antichain = self.index[(0,) * n]
        self.S = self.F[self.antichain]

    def _layer_sweep(self):
        remaining = [2] * len(self.move_owner)
        layer = []
        for p in range(len(self.posets)):
            if not self.moves_of[p]:
                self.F[p] = 0
                layer.append(p)
        d = 0
        while layer:
            nxt = []
            for c in layer:
                for mid in self.pred[c]:
                    remaining[mid] -= 1
                    if remaining[mid] == 0:
                        p = self.move_owner[mid]
                        if self.F[p] is None:
                            self.F[p] = d + 1
                            nxt.append(p)
            d += 1
            layer = nxt
        if any(f is None for f in self.F):
            raise AssertionError("retrograde sweep left states unassigned")

    def state_count(self):
        return len(self.posets)

    def move_count(self):
        return len(self.move_owner)

    def witness_move(self, p):
        """A move at p achieving F(p) = 1 + max(F(children))."""
        target = self.F[p]
        for mid in self.moves_of[p]:
            c1, c2 = self.move_children[mid]
            if 1 + max(self.F[c1], self.F[c2]) == target:
                return mid
        raise AssertionError("no witnessing move")

    def certificate(self, p=None):
        """Nested backward certificate: at each internal node, a comparison and
        references to both children, recursively down to chains."""
        if p is None:
            p = self.antichain
        counter = [0]

        def build(q):
            node = {
                "id": counter[0],
                "succ": self.posets[q],
                "F": self.F[q],
            }
            counter[0] += 1
            if self.F[q] == 0:
                node["leaf"] = True
                return node
            mid = self.witness_move(q)
            c1, c2 = self.move_children[mid]
            node["leaf"] = False
            node["compare"] = self.move_pair[mid]
            node["children"] = [build(c1), build(c2)]
            return node

        return build(p)

    def check_certificate(self, node):
        """Verify the certificate is a genuine backward witness: leaves are
        chains, each internal node's stored comparison really produces the two
        referenced children, and F(parent) = 1 + max(F(children))."""
        if node["leaf"]:
            return self.F[self.index[node["succ"]]] == 0
        if node["F"] == 0:
            return False
        c1, c2 = node["children"]
        i, j = node["compare"]
        if extend(node["succ"], i, j) != c1["succ"]:
            return False
        if extend(node["succ"], j, i) != c2["succ"]:
            return False
        if node["F"] != 1 + max(c1["F"], c2["F"]):
            return False
        return self.check_certificate(c1) and self.check_certificate(c2)

    def certificate_height(self, node):
        if node["leaf"]:
            return 0
        return 1 + max(self.certificate_height(c) for c in node["children"])


# --------------------------------------------------------------------------
# Independent forward oracle (validation only): recursive memoized minimax.
# --------------------------------------------------------------------------

def make_forward_oracle(n):
    @lru_cache(maxsize=None)
    def can_sort(succ, d):
        pairs = incomparable_pairs(succ, n)
        if not pairs:
            return True
        if d == 0:
            return False
        return any(
            can_sort(extend(succ, i, j), d - 1) and can_sort(extend(succ, j, i), d - 1)
            for (i, j) in pairs
        )

    return can_sort


def predecessors_for_pair(posets, child_succ, i, j):
    """All states P for which (i,j) is a legal (incomparable) comparison and
    extend(P,i,j) == child_succ.  This directly exhibits the source's point
    that one comparison can have several predecessors."""
    return [
        P
        for P in posets
        if not (P[i] & (1 << j))
        and not (P[j] & (1 << i))
        and extend(P, i, j) == child_succ
    ]


def find_multi_predecessor(R):
    """Smallest example where a single comparison (i,j) leading to one child
    has at least two distinct predecessors.  Returns (child, pair, preds) or
    None."""
    for mid in range(len(R.move_owner)):
        c1, c2 = R.move_children[mid]
        i, j = R.move_pair[mid]
        for child, a, b in ((c1, i, j), (c2, j, i)):
            preds = predecessors_for_pair(R.posets, R.posets[child], a, b)
            if len(preds) >= 2:
                return R.posets[child], (a, b), preds
    return None


# --------------------------------------------------------------------------
# Validation and reporting.
# --------------------------------------------------------------------------

KNOWN_S = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5}
A001035 = {0: 1, 1: 1, 2: 3, 3: 19, 4: 219}


def target_n4_posets(n=4):
    """A handful of named n=4 posets, each built by legal comparisons so it is
    guaranteed transitively closed and present in the enumerated state set."""
    A = (0,) * n
    return {
        "antichain": A,
        "chain": extend(extend(extend(A, 0, 1), 1, 2), 2, 3),
        "one_pair": extend(A, 0, 1),
        "two_pairs": extend(extend(A, 0, 1), 2, 3),
        "chain3_plus_isolated": extend(extend(A, 0, 1), 1, 2),
        "two_minima_vee": extend(extend(A, 0, 2), 1, 2),
        "two_maxima_wedge": extend(extend(A, 0, 2), 0, 3),
    }


def validate(n_max=4, d_max=5):
    """Comprehensive validation.  For EVERY poset on n <= n_max and every
    d <= d_max, checks that the retrograde F and the independent forward
    CanSort agree.  ``validate(4, 5)`` is the offline n=4 sweep and is intended
    as a documented offline check, not a CI test; CI runs the bounded
    ``validate(n_max=3)`` plus ``validate_targeted_n4`` instead.

    Returns (rows, cross_checks, all_ok)."""
    rows = []
    cross_checks = 0
    ok = True
    for n in range(0, n_max + 1):
        R = Retrograde(n)
        rows.append(
            {
                "n": n,
                "states": R.state_count(),
                "moves": R.move_count(),
                "S": R.S,
                "known_S": KNOWN_S.get(n),
                "a001035": A001035.get(n),
            }
        )
        if R.state_count() != A001035.get(n):
            ok = False
        if R.S != KNOWN_S.get(n):
            ok = False
        if comparison_reachable(n) != set(R.posets):
            ok = False
        can_sort = make_forward_oracle(n)
        for succ in R.posets:
            f = R.F[R.index[succ]]
            for d in range(0, d_max + 1):
                cross_checks += 1
                if can_sort(succ, d) != (f <= d):
                    ok = False
    return rows, cross_checks, ok


def validate_targeted_n4(d_max=5):
    """Bounded n=4 validation for CI: the antichain, the chain, and several
    structured posets, each checked against the forward oracle for all
    d <= d_max.  Returns (F_by_name, cross_checks, all_ok)."""
    R = Retrograde(4)
    can_sort = make_forward_oracle(4)
    F_by_name = {}
    cross_checks = 0
    ok = R.S == 5
    for name, succ in target_n4_posets(4).items():
        if succ not in R.index:
            raise AssertionError(f"target poset {name} not in state set")
        f = R.F[R.index[succ]]
        F_by_name[name] = f
        for d in range(0, d_max + 1):
            cross_checks += 1
            if can_sort(succ, d) != (f <= d):
                ok = False
    return F_by_name, cross_checks, ok


def _print_tree(R, node, indent=0):
    pad = "  " * indent
    if node["leaf"]:
        print(f"{pad}leaf succ={node['succ']} F={node['F']}")
        return
    i, j = node["compare"]
    print(f"{pad}succ={node['succ']} F={node['F']}  compare ({i},{j})")
    c1, c2 = node["children"]
    print(f"{pad}  child {i}<{j}: id={c1['id']} succ={c1['succ']} F={c1['F']}")
    print(f"{pad}  child {j}<{i}: id={c2['id']} succ={c2['succ']} F={c2['F']}")
    _print_tree(R, c1, indent + 2)
    _print_tree(R, c2, indent + 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-n", type=int, default=4)
    ap.add_argument("--d-max", type=int, default=5)
    args = ap.parse_args()

    rows, checks, ok = validate(args.max_n, args.d_max)

    print("Retrograde (backward) DP on labelled posets, n <= %d" % args.max_n)
    print("n | states A001035 | moves | S(n) retrograde | S(n) known | match")
    for r in rows:
        match = r["S"] == r["known_S"] and r["states"] == r["a001035"]
        print(
            f"{r['n']} | {r['states']} (ref {r['a001035']}) | {r['moves']} "
            f"| {r['S']} | {r['known_S']} | {match}"
        )
    print()
    print(
        "Comprehensive OFFLINE cross-check: %d (poset, d) pairs with d <= %d "
        "agree with independent CanSort: %s" % (checks, args.d_max, ok)
    )
    fnames, tchecks, tok = validate_targeted_n4(args.d_max)
    print(
        "Bounded CI cross-check (n=4 targeted, %d pairs): %s; F by poset: %s"
        % (tchecks, tok, fnames)
    )
    print(
        "Storage note: reverse graph + counters are O(#states * n^2) = "
        "non-polynomial space (A001035 grows super-polynomially)."
    )

    n = 4
    R = Retrograde(n)
    cert = R.certificate()
    print()
    print(f"Backward certificate for the antichain on n={n}, depth S({n})={R.S}:")
    print(f"  root succ={R.posets[R.antichain]} F={R.F[R.antichain]}")
    _print_tree(R, cert, indent=1)
    print()
    print(
        "  certificate valid (children/compare/F consistent): "
        f"{R.check_certificate(cert)}"
    )
    print(
        f"  certificate height: {R.certificate_height(cert)} (must equal S({n})={R.S})"
    )

    found = find_multi_predecessor(R)
    print()
    print("Multiple predecessors for one comparison (source Section 4.1/5.7):")
    if found is None:
        print("  none found (unexpected)")
    else:
        child, pair, preds = found
        print(f"  child succ={child}; comparison {pair}; predecessors={preds}")


if __name__ == "__main__":
    main()
