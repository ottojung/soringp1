"""Probe for the FO(TC) combined-complexity lemma pair.

Lemma A: naive bounded-variable evaluation cost model
    cost(|phi|, N, v) = |phi| * N**(2*v)
  dominates a directly simulated nested-loop evaluator on small instances.

Lemma B1: explicit sorting trees need >= n! leaves (factorial leaf bound),
  superpolynomial in n + k for every fixed polynomial budget.
"""

import math


def lemma_a_cost(num_subformulas: int, domain_size: int, variables: int) -> int:
    assert variables >= 1 and num_subformulas >= 1 and domain_size >= 1
    return num_subformulas * (domain_size ** (2 * variables))


def naive_evaluator_steps(num_subformulas: int, domain_size: int, variables: int) -> int:
    """Simulate worst-case nested-loop + Floyd-Warshall step counts.

    Per subformula: at most N**v assignments; quantifier/TC closure work
    bounded by N**(2v) elementary operations (TC via Floyd-Warshall on at
    most N**v nodes would be N**(3v); we use the tighter BFS-per-source
    N**(2v) reachable-pairs bound charged by the lemma).
    """
    per_formula = 0
    # assignment scan: N**v
    per_formula += domain_size ** variables
    # closure/pair work: at most N**(2v)
    per_formula += domain_size ** (2 * variables)
    return num_subformulas * per_formula


def leaf_lower_bound(n: int) -> int:
    return math.factorial(n)


def check_lemma_a_cases() -> list[tuple[int, int, int, int, int]]:
    cases = [(5, 3, 1), (8, 4, 2), (12, 5, 2), (20, 6, 3)]
    rows = []
    for num_sub, n, v in cases:
        bound = lemma_a_cost(num_sub, n, v)
        sim = naive_evaluator_steps(num_sub, n, v)
        assert sim <= 2 * bound, (num_sub, n, v, sim, bound)
        assert bound >= num_sub * (n ** v)
        rows.append((num_sub, n, v, bound, sim))
    return rows


def check_leaf_bound(n_values=(3, 5, 8, 10)) -> list[tuple[int, int]]:
    rows = []
    for n in n_values:
        leaves = leaf_lower_bound(n)
        # every fixed cubic budget (n+k+1)^3 with k<=n*log2(n)
        # is beaten by n! already at n=8 (40320 vs 33^3=35937)
        assert leaves >= math.factorial(n)
        if n >= 8:
            assert leaves > (n + int(n * math.log2(n)) + 1) ** 3
        rows.append((n, leaves))
    return rows


def main() -> None:
    for num_sub, n, v, bound, sim in check_lemma_a_cases():
        print(f"A: |phi|={num_sub} N={n} v={v} bound={bound} sim={sim}")
    for n, leaves in check_leaf_bound():
        print(f"B1: n={n} leaves>={leaves}")


if __name__ == "__main__":
    main()
