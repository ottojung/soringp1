#!/usr/bin/env python3
"""Experimental individualization/refinement canonicalizer for finite posets.

No symmetry pruning is used: every vertex in the selected color cell is
branched on. Exhausted budgets raise CanonicalizationUnknown.
"""
import argparse
import importlib.util
import itertools
import time


class CanonicalizationUnknown(RuntimeError):
    pass


def encode(succ, order):
    n = len(succ)
    return tuple(sum(1 << b for b, old_b in enumerate(order)
                     if succ[old_a] >> old_b & 1) for old_a in order)


def normalized(signatures):
    table = {sig: i for i, sig in enumerate(sorted(set(signatures)))}
    return tuple(table[sig] for sig in signatures)


def refine(succ, colors):
    n = len(succ)
    while True:
        sigs = []
        for v in range(n):
            down = tuple(sorted(colors[u] for u in range(n) if succ[v] >> u & 1))
            up = tuple(sorted(colors[u] for u in range(n) if succ[u] >> v & 1))
            sigs.append((colors[v], down, up))
        new = normalized(sigs)
        # Refinement never merges cells; compare partitions, not raw ids.
        if all((colors[i] == colors[j]) == (new[i] == new[j])
               for i in range(n) for j in range(n)):
            return new
        colors = new


def make_ir_canon(n, node_cap=1_000_000, time_cap=30.0):
    cache = {}

    def canon(succ):
        if succ in cache:
            return cache[succ]
        started = time.monotonic()
        nodes = 0

        def visit(colors):
            nonlocal nodes
            nodes += 1
            if nodes > node_cap or time.monotonic() - started > time_cap:
                raise CanonicalizationUnknown(
                    f"IR budget exceeded (nodes>{node_cap} or time>{time_cap}s)")
            colors = refine(succ, colors)
            cells = {}
            for v, c in enumerate(colors):
                cells.setdefault(c, []).append(v)
            nonsingle = [(c, vs) for c, vs in sorted(cells.items()) if len(vs) > 1]
            if not nonsingle:
                order = tuple(v for _, v in sorted((c, vs[0]) for c, vs in cells.items()))
                return encode(succ, order)
            # Smallest color id is chosen canonically, hence equivariantly.
            cell = min(nonsingle, key=lambda item: item[0])[1]
            best = None
            fresh = max(colors, default=-1) + 1
            for v in cell:
                individualized = list(colors)
                individualized[v] = fresh
                leaf = visit(tuple(individualized))
                if best is None or leaf < best:
                    best = leaf
            return best

        result = visit(tuple(0 for _ in range(n)))
        cache[succ] = result
        return result

    return canon


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--n', type=int, default=7)
    ap.add_argument('--nodes', type=int, default=1_000_000)
    ap.add_argument('--seconds', type=float, default=30.0)
    args = ap.parse_args()
    path = __file__.replace('ir_poset_canon.py', 'state_compression.py')
    spec = importlib.util.spec_from_file_location('state_compression', path)
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    n = args.n
    ir = make_ir_canon(n, args.nodes, args.seconds)
    brute = old.make_refined_canon(n)
    # Every labelled poset via the existing recurrence's reachable state set.
    states = old.labelled_solve(n)[3]
    reps = {}
    for s in states:
        ref = brute(s)
        value = ir(s)
        if ref in reps and reps[ref] != value:
            raise SystemExit(f'IR not invariant at n={n}: {s}')
        reps[ref] = value
    if len(set(reps.values())) != len(reps):
        raise SystemExit(f'IR collision between brute-force classes at n={n}')
    print(f'PASS all {len(states)} labelled posets n={n}; known S={old.labelled_solve(n)[0]}')


if __name__ == '__main__':
    main()
