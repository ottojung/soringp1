#!/usr/bin/env python3
"""Strategy DAG experiments: hash-consed vs unshared, symmetry quotients.

Model (docs/problem.md, docs/upper-bound.md, SoringP1/Minimax.lean):
  A state is the strict partial order (transitive closure) induced by the
  comparisons made so far, stored as successor bitmasks: succ[i] has bit j
  set iff i < j.  The remaining minimax cost is

      F(P) = 0                                                   if P is total,
      F(P) = 1 + min_{x,y incomparable} max(F(P+x<y), F(P+y<x))   otherwise,

  and S(n) = F(empty poset).

  An *optimal policy* is a strategy achieving the minimax value.  We study
  the size of a hash-consed DAG representation versus an unshared tree.

Experiments:
  1. Build the full minimax DAG (all optimal moves kept) for n <= 5.
  2. Count: unshared tree nodes, hash-consed DAG nodes, leaves.
  3. Quotient the DAG under S_n relabelling (canonical posets).
  4. Compare: DAG for ONE optimal policy vs union of ALL optimal strategies.
  5. Test whether DAG size is polynomial or exponential in n.

This is an experiment, not a proof.  It uses no external libraries.
"""

import argparse
import itertools
import time
from functools import lru_cache


# --------------------------------------------------------------------------
# Labelled partial orders as successor bitmasks.
# --------------------------------------------------------------------------

def extend(succ, i, j):
    """Transitive closure after adding i < j to an already closed state."""
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


def is_total(succ, n):
    return all(
        (succ[i] >> j & 1) or (succ[j] >> i & 1)
        for i in range(n) for j in range(i + 1, n)
    )


# --------------------------------------------------------------------------
# Minimax value computation (reference, from scripts/evaluate.py).
# --------------------------------------------------------------------------

def minimax_values(n):
    """Return dict mapping every reachable poset to its F value."""
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


# --------------------------------------------------------------------------
# Hash-consed DAG construction.
# --------------------------------------------------------------------------

class StrategyDAG:
    """Hash-consed DAG for optimal policies.

    Each node is a poset state.  Edges are (pair, yes_child, no_child).
    Hash-consing means identical posets share the same node.
    """

    def __init__(self, n, values, keep_all_optimal=True):
        """Build the strategy DAG.

        keep_all_optimal=True: union of ALL optimal strategies.
        keep_all_optimal=False: ONE optimal policy (first optimal move).
        """
        self.n = n
        self.values = values
        self.keep_all = keep_all_optimal
        self.nodes = {}       # succ -> node_id
        self.edges = []       # (node_id, pair, yes_id, no_id)
        self.leaves = set()   # node_ids that are total orders
        self._build()

    def _get_node(self, succ):
        if succ not in self.nodes:
            self.nodes[succ] = len(self.nodes)
        return self.nodes[succ]

    def _build(self):
        empty = (0,) * self.n
        self._build_node(empty)

    def _build_node(self, succ):
        nid = self._get_node(succ)
        if nid < len(self.edges):
            return  # already built
        if is_total(succ, self.n):
            self.leaves.add(nid)
            self.edges.append(None)
            return

        f_val = self.values[succ]
        optimal_moves = []
        for (i, j) in incomparable_pairs(succ, self.n):
            a = extend(succ, i, j)
            b = extend(succ, j, i)
            if 1 + max(self.values[a], self.values[b]) == f_val:
                optimal_moves.append(((i, j), a, b))
                if not self.keep_all:
                    break

        # For the DAG, we need to handle the case where we keep all optimal
        # moves: each node can have multiple outgoing edge-sets.
        # We represent this as a list of edge-sets per node.
        if nid >= len(self.edges):
            self.edges.append([])
        for (i, j), a, b in optimal_moves:
            yes_id = self._build_node(a)
            no_id = self._build_node(b)
            self.edges[nid].append(((i, j), yes_id, no_id))

    @property
    def num_nodes(self):
        return len(self.nodes)

    @property
    def num_leaves(self):
        return len(self.leaves)


class SinglePolicyDAG(StrategyDAG):
    """DAG for ONE optimal policy (single move per node)."""

    def __init__(self, n, values):
        super().__init__(n, values, keep_all_optimal=False)


# --------------------------------------------------------------------------
# Unshared tree (for comparison).
# --------------------------------------------------------------------------

def count_unshared_tree(n, values):
    """Count nodes in the unshared tree (no hash-consing)."""
    empty = (0,) * n
    count = [0]

    def build(succ):
        count[0] += 1
        if is_total(succ, n):
            return
        f_val = values[succ]
        for (i, j) in incomparable_pairs(succ, n):
            a = extend(succ, i, j)
            b = extend(succ, j, i)
            if 1 + max(values[a], values[b]) == f_val:
                build(a)
                build(b)
                break  # one optimal policy

    build(empty)
    return count[0]


def count_unshared_tree_all_optimal(n, values):
    """Count nodes in the unshared tree keeping ALL optimal moves."""
    empty = (0,) * n
    count = [0]

    def build(succ):
        count[0] += 1
        if is_total(succ, n):
            return
        f_val = values[succ]
        for (i, j) in incomparable_pairs(succ, n):
            a = extend(succ, i, j)
            b = extend(succ, j, i)
            if 1 + max(values[a], values[b]) == f_val:
                build(a)
                build(b)

    build(empty)
    return count[0]


# --------------------------------------------------------------------------
# Symmetry quotient: canonical form under S_n.
# --------------------------------------------------------------------------

def refine_colors(succ, n):
    """2-dimensional colour refinement."""
    color = [bin(succ[i]).count("1") for i in range(n)]
    while True:
        sig = []
        for i in range(n):
            down = tuple(sorted(color[j] for j in range(n) if succ[i] >> j & 1))
            up = tuple(sorted(color[j] for j in range(n) if succ[j] >> i & 1))
            sig.append((color[i], down, up))
        order = {v: k for k, v in enumerate(sorted(set(sig)))}
        comp = [order[v] for v in sig]
        if comp == color:
            return color
        color = comp


def _encode(succ, perm, n):
    new = []
    for a in range(n):
        bits = succ[perm[a]]
        m = 0
        for b in range(n):
            if bits >> perm[b] & 1:
                m |= 1 << b
        new.append(m)
    return tuple(new)


def make_refined_canon(n):
    cache = {}

    def canon(succ):
        if succ in cache:
            return cache[succ]
        color = refine_colors(succ, n)
        groups = {}
        for i, c in enumerate(color):
            groups.setdefault(c, []).append(i)
        gs = [groups[c] for c in sorted(groups)]
        best = None
        for combo in itertools.product(*(itertools.permutations(g) for g in gs)):
            perm = [x for p in combo for x in p]
            e = _encode(succ, perm, n)
            if best is None or e < best:
                best = e
        cache[succ] = best
        return best

    return canon


def quotient_dag_nodes(n, values, keep_all_optimal=True):
    """Count nodes in the DAG after quotienting by S_n symmetry."""
    canon = make_refined_canon(n)
    empty = (0,) * n
    seen = set()

    def build(succ):
        c = canon(succ)
        if c in seen:
            return
        seen.add(c)
        if is_total(succ, n):
            return
        f_val = values[succ]
        for (i, j) in incomparable_pairs(succ, n):
            a = extend(succ, i, j)
            b = extend(succ, j, i)
            if 1 + max(values[a], values[b]) == f_val:
                build(a)
                build(b)
                if not keep_all_optimal:
                    break

    build(empty)
    return len(seen)


# --------------------------------------------------------------------------
# Polynomial certificate test.
# --------------------------------------------------------------------------

def test_polynomial_bound(max_n=5):
    """Test whether DAG size grows polynomially or exponentially.

    We check if log2(DAG_nodes) / n is bounded (polynomial) or grows
    linearly (exponential in n).
    """
    print("Polynomial bound test: log2(nodes) vs n")
    print("If log2(nodes) ~ c*n, DAG is exponential. If ~ c*log(n), polynomial.")
    print()
    results = []
    for n in range(1, max_n + 1):
        values = minimax_values(n)
        empty = (0,) * n
        dag = SinglePolicyDAG(n, values)
        log_nodes = dag.num_nodes.bit_length() - 1
        ratio = log_nodes / n if n > 0 else 0
        results.append((n, dag.num_nodes, log_nodes, ratio))
        print(f"  n={n}: nodes={dag.num_nodes}, log2={log_nodes}, "
              f"log2/n={ratio:.3f}")
    return results


# --------------------------------------------------------------------------
# Main experiment driver.
# --------------------------------------------------------------------------

KNOWN = {0: 0, 1: 0, 2: 1, 3: 3, 4: 5, 5: 7, 6: 10, 7: 13, 8: 16, 12: 30}
A001035 = {0: 1, 1: 1, 2: 3, 3: 19, 4: 219, 5: 4231, 6: 130023}
A000112 = {0: 1, 1: 1, 2: 2, 3: 5, 4: 16, 5: 63, 6: 318, 7: 2045}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-n", type=int, default=5,
                    help="largest n for full experiment (default 5)")
    args = ap.parse_args()

    print("=" * 70)
    print("STRATEGY DAG vs UNSHARED TREE EXPERIMENTS")
    print("=" * 70)
    print()

    print("Reference: S(n) values and OEIS sequences")
    print(f"  Known S(n): {KNOWN}")
    print(f"  A001035 (labelled posets): {A001035}")
    print(f"  A000112 (unlabelled posets): {A000112}")
    print()

    print("-" * 70)
    print("Experiment 1: DAG vs unshared tree node counts")
    print("-" * 70)
    print()

    header = ("n | S(n) | unshared(1) | unshared(all) | DAG(1) | DAG(all) "
              "| DAG(1)/n! | DAG(all)/n!")
    print(header)
    print("-" * len(header))

    for n in range(1, args.max_n + 1):
        values = minimax_values(n)
        empty = (0,) * n

        tree1 = count_unshared_tree(n, values)
        tree_all = count_unshared_tree_all_optimal(n, values)

        dag1 = SinglePolicyDAG(n, values)
        dag_all = StrategyDAG(n, values, keep_all_optimal=True)

        import math
        fact = math.factorial(n)

        print(f"{n} | {KNOWN[n]} | {tree1} | {tree_all} | "
              f"{dag1.num_nodes} | {dag_all.num_nodes} | "
              f"{dag1.num_nodes/fact:.4f} | {dag_all.num_nodes/fact:.4f}")

    print()
    print("Note: DAG(1) = hash-consed DAG for ONE optimal policy.")
    print("      DAG(all) = hash-consed DAG for union of ALL optimal strategies.")
    print("      unshared(1) = tree nodes for ONE optimal policy (no sharing).")
    print("      unshared(all) = tree nodes keeping ALL optimal moves.")

    print()
    print("-" * 70)
    print("Experiment 2: Symmetry quotient (S_n canonical forms)")
    print("-" * 70)
    print()

    header2 = "n | DAG(1) nodes | quotient(1) | DAG(all) nodes | quotient(all)"
    print(header2)
    print("-" * len(header2))

    for n in range(1, args.max_n + 1):
        values = minimax_values(n)
        dag1 = SinglePolicyDAG(n, values)
        dag_all = StrategyDAG(n, values, keep_all_optimal=True)
        q1 = quotient_dag_nodes(n, values, keep_all_optimal=False)
        qall = quotient_dag_nodes(n, values, keep_all_optimal=True)

        print(f"{n} | {dag1.num_nodes} | {q1} | {dag_all.num_nodes} | {qall}")

    print()
    print("Quotient = number of isomorphism classes of posets in the DAG.")

    print()
    print("-" * 70)
    print("Experiment 3: Polynomial bound test")
    print("-" * 70)
    print()

    test_polynomial_bound(args.max_n)

    print()
    print("-" * 70)
    print("Experiment 4: Verifier complexity")
    print("-" * 70)
    print()
    print("A polynomial-in-DAG-size verifier would:")
    print("  1. Check each node is a valid poset (transitive closure).")
    print("  2. Check each edge (pair, yes_child, no_child) is valid.")
    print("  3. Check the DAG has no cycles (topological order).")
    print("  4. Check the root reaches a total order within k steps.")
    print()
    print("This is O(DAG_size * n^2) = poly(DAG_size, n).")
    print("BUT: this only verifies a GIVEN DAG. It does NOT prove S(n) <= k")
    print("without a polynomial-size DAG existing.")
    print()

    print("-" * 70)
    print("Experiment 5: Concrete no-go for naive polynomial certificates")
    print("-" * 70)
    print()
    print("If a polynomial-size DAG certificate existed for S(n) <= k,")
    print("then SORT-BOUND-U would be in NP (unary encoding).")
    print()
    print("But SORT-BOUND-U is sparse (Lemma 3.1 of research-encoding-consequences.md).")
    print("By Mahaney's theorem, a sparse set is not NP-hard under many-one")
    print("reductions unless P = NP.")
    print()
    print("This is a CONDITIONAL barrier, not a proof that no poly DAG exists.")
    print("It shows: IF a poly-size DAG certificate exists AND SORT-BOUND-U is")
    print("NP-hard, THEN P = NP. So the naive route to NP-hardness is blocked.")
    print()
    print("The DAG approach does NOT claim NP membership without a size bound.")


if __name__ == "__main__":
    main()
