"""Regression cases for the strategy DAG probe."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from strategy_dag_probe import (
    StrategyDAG,
    SinglePolicyDAG,
    minimax_values,
    count_unshared_tree,
    count_unshared_tree_all_optimal,
    quotient_dag_nodes,
    make_refined_canon,
    extend,
    incomparable_pairs,
    is_total,
)


class StrategyDAGTests(unittest.TestCase):
    def test_small_values_match_known(self):
        known = {1: 0, 2: 1, 3: 3, 4: 5, 5: 7}
        for n, expected in known.items():
            with self.subTest(n=n):
                values = minimax_values(n)
                empty = (0,) * n
                self.assertEqual(values[empty], expected)

    def test_dag_single_policy_size(self):
        expected_nodes = {1: 1, 2: 3, 3: 11, 4: 47, 5: 239}
        for n, expected in expected_nodes.items():
            with self.subTest(n=n):
                values = minimax_values(n)
                dag = SinglePolicyDAG(n, values)
                self.assertEqual(dag.num_nodes, expected)

    def test_dag_all_optimal_size(self):
        expected_nodes = {1: 1, 2: 3, 3: 19, 4: 181, 5: 1551}
        for n, expected in expected_nodes.items():
            with self.subTest(n=n):
                values = minimax_values(n)
                dag = StrategyDAG(n, values, keep_all_optimal=True)
                self.assertEqual(dag.num_nodes, expected)

    def test_unshared_tree_single_policy(self):
        expected = {1: 1, 2: 3, 3: 11, 4: 47, 5: 239}
        for n, exp in expected.items():
            with self.subTest(n=n):
                values = minimax_values(n)
                self.assertEqual(count_unshared_tree(n, values), exp)

    def test_unshared_tree_all_optimal(self):
        expected = {1: 1, 2: 3, 3: 55, 4: 1957, 5: 26541}
        for n, exp in expected.items():
            with self.subTest(n=n):
                values = minimax_values(n)
                self.assertEqual(count_unshared_tree_all_optimal(n, values), exp)

    def test_quotient_counts(self):
        expected_q1 = {1: 1, 2: 2, 3: 4, 4: 7, 5: 11}
        expected_qall = {1: 1, 2: 2, 3: 5, 4: 12, 5: 19}
        for n in range(1, 6):
            with self.subTest(n=n):
                values = minimax_values(n)
                q1 = quotient_dag_nodes(n, values, keep_all_optimal=False)
                qall = quotient_dag_nodes(n, values, keep_all_optimal=True)
                self.assertEqual(q1, expected_q1[n])
                self.assertEqual(qall, expected_qall[n])

    def test_dag_smaller_than_unshared_all(self):
        for n in range(3, 6):
            with self.subTest(n=n):
                values = minimax_values(n)
                dag = StrategyDAG(n, values, keep_all_optimal=True)
                tree = count_unshared_tree_all_optimal(n, values)
                self.assertLess(dag.num_nodes, tree)


class DistinctPosetsTheorem(unittest.TestCase):
    """Theorem 2.6: distinct nodes have distinct labelled posets in a tree."""

    def test_all_nodes_distinct_posets_single_policy(self):
        for n in range(1, 7):
            with self.subTest(n=n):
                values = minimax_values(n)
                dag = SinglePolicyDAG(n, values)
                posets = list(dag.nodes.keys())
                self.assertEqual(len(posets), len(set(posets)),
                                 f"n={n}: duplicate posets in single-policy DAG")

    def test_hash_consing_saves_zero_single_policy(self):
        import math
        for n in range(1, 7):
            with self.subTest(n=n):
                values = minimax_values(n)
                dag = SinglePolicyDAG(n, values)
                tree = count_unshared_tree(n, values)
                self.assertEqual(dag.num_nodes, tree,
                                 f"n={n}: hash-consing changed node count")
                self.assertEqual(dag.num_nodes, 2 * math.factorial(n) - 1)


class QuotientCertificate(unittest.TestCase):
    """Quotient certificate size with relabelling maps."""

    def test_quotient_edge_counts(self):
        expected_qedges = {1: 0, 2: 1, 3: 7, 4: 23, 5: 35, 6: 415}
        for n, expected in expected_qedges.items():
            with self.subTest(n=n):
                values = minimax_values(n)
                canon = make_refined_canon(n)
                empty = (0,) * n
                seen = set()
                qedges = [0]

                def count_qedges(succ):
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
                            qedges[0] += 1
                            count_qedges(a)
                            count_qedges(b)

                count_qedges(empty)
                self.assertEqual(qedges[0], expected)


if __name__ == "__main__":
    unittest.main()
