"""Tests for the FO(TC) combined-complexity lemma pair probe."""

from scripts.fo_tc_combined_probe import (
    check_lemma_a_cases,
    check_leaf_bound,
    lemma_a_cost,
    leaf_lower_bound,
)


def test_lemma_a_bound_dominates_simulation():
    rows = check_lemma_a_cases()
    assert len(rows) == 4
    for num_sub, n, v, bound, sim in rows:
        assert bound == num_sub * (n ** (2 * v))
        assert sim <= 2 * bound


def test_lemma_a_grows_with_formula_text():
    assert lemma_a_cost(10, 4, 2) == 2 * lemma_a_cost(5, 4, 2)


def test_leaf_bound_factorial():
    assert leaf_lower_bound(5) == 120
    rows = check_leaf_bound()
    assert [n for n, _ in rows] == [3, 5, 8, 10]
