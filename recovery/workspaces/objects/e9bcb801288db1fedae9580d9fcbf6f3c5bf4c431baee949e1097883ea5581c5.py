"""Standalone experiment: selection lower bounds as sorting-state pruning.

The evaluator intentionally implements only the research prototype; it does not
modify or import the production budgeted-pruning script.
"""
from functools import lru_cache
import importlib.util
from pathlib import Path
import math


def _baseline():
    path = Path(__file__).with_name("budgeted_pruning_experiments.py")
    spec = importlib.util.spec_from_file_location("baseline_pruning", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def selection_lb(succ, n, rank):
    """Cremer Cor. 7: max(ceil(log2 Phi*), KEY), directly enumerated."""
    # A down-set L and a minimal element e of its complement form a
    # compatible solution: L ∪ {e} is again a down-set, so an extension can
    # list L, then e, then the remaining elements.
    all_vertices = (1 << n) - 1

    def is_downset(A):
        return not any((succ[y] >> x) & 1
                       for x in range(n) if (A >> x) & 1
                       for y in range(n) if not (A >> y) & 1)

    solutions = []
    fg = 0
    fg_delta = 0
    for L in range(1 << n):
        if L.bit_count() != rank - 1:
            continue
        if not is_downset(L):
            continue
        outside = [x for x in range(n) if not (L >> x) & 1]
        mins = [x for x in outside if not any(
            (succ[y] >> x) & 1 for y in outside if y != x)]
        b = len(mins) - 1
        fg += 1 << b
        for e in mins:
            U = all_vertices ^ (L | (1 << e))
            solutions.append((L, e, U, b))
    # A is a size-rank down-set and its maximal elements are possible e.
    for A in range(1 << n):
        if A.bit_count() != rank:
            continue
        if not is_downset(A):
            continue
        maxima = [x for x in range(n) if (A >> x) & 1 and not any(
            (succ[x] >> y) & 1 for y in range(n) if (A >> y) & 1)]
        fg_delta += 1 << (len(maxima) - 1)
    c = len(solutions)
    phi = fg + fg_delta - c
    if phi < 1:
        raise AssertionError(f"Cremer Phi* must be positive, got {phi}")
    phi_lb = (phi - 1).bit_length()
    key = max((len([x for x in range(n) if (A >> x) & 1 and not any(
        (succ[x] >> y) & 1 for y in range(n) if (A >> y) & 1)]) - 1 + b
        for L, e, U, b in solutions
        for A in [L | (1 << e)]), default=0)
    return max(phi_lb, key)


def main():
    m = _baseline()
    checked = 0
    strict = 0
    maxima = {}
    for n in range(1, 7):
        exact = m.memoized_F(n)
        stronger = 0
        for P in m.all_posets(n):
            e = m.linear_extensions(P, n)
            info = (e - 1).bit_length()
            lb = max(selection_lb(P, n, i) for i in range(1, n + 1))
            if lb > exact[P]:
                raise AssertionError((n, P, lb, exact[P]))
            checked += 1
            if lb > info:
                strict += 1
                stronger += 1
        maxima[n] = (len(m.all_posets(n)), stronger)
        print(f"n={n}: posets={maxima[n][0]} strict={stronger}")
    print(f"checked={checked} strict_total={strict}")


if __name__ == "__main__":
    main()
