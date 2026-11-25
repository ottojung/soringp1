"""Finite checks supporting the asymptotic winning-frontier counting proof.

These checks do NOT establish the asymptotic theorem (see the paper proof).
No large poset enumeration occurs.
"""

import math
import unittest


def successors_for_one_step(s, indices):
    return {(2*x + bit) % s for x in indices for bit in (0, 1)}


class WinningFrontierSkeletonTests(unittest.TestCase):
    def test_de_bruijn_layers_become_universally_comparable(self):
        for r in range(1, 5):
            s = 1 << r
            for x in range(s):
                reachable = {x}
                for depth in range(1, 2 * r + 2):
                    reachable = successors_for_one_step(s, reachable)
                    if depth >= r:
                        self.assertEqual(len(reachable), s)

    def test_extra_adjacent_edges_define_distinct_relations(self):
        s, layers = 8, 4
        edges = {(i*s+x, (i+1)*s+(2*x+bit) % s)
                 for i in range(layers-1) for x in range(s) for bit in (0, 1)}
        missing = {(i*s+x, (i+1)*s+y)
                   for i in range(layers-1) for x in range(s) for y in range(s)} - edges
        additions = set(sorted(missing)[::7])
        edges |= additions
        adjacency = {v: [] for v in range(s*layers)}
        for u, v in edges:
            adjacency[u].append(v)
        for i in range(layers-1):
            for x in range(s):
                start = i*s+x
                reached = {start}
                stack = [start]
                while stack:
                    u = stack.pop()
                    for v in adjacency[u]:
                        if v not in reached:
                            reached.add(v)
                            stack.append(v)
                for y in range(s):
                    finish = (i+1)*s+y
                    # All paths from layer i to layer i+1 have length one.
                    self.assertEqual(finish in reached, (start, finish) in edges)

    def test_eventual_winning_budget_inequality(self):
        # Check a few *representative* parameters, not the general proof.
        for r in (16, 20, 24):
            s = 1 << r
            n = s*s
            t = 2*s*(s-1) + (r*n)//2
            log2_factorial_lower = n*(2*r - math.log2(math.e))
            w = r*s
            tournament_upper = (w-1) + (n-1)*(r + math.ceil(math.log2(r)))
            self.assertGreater(log2_factorial_lower - t, tournament_upper)

    def test_isomorphism_quotient_lower_bound(self):
        for r in (16, 20, 24):
            s = 1 << r
            n = s*s
            m = r*n//2
            M = (s-1)*(s*s-2*s)
            self.assertGreaterEqual(M, m)
            # log_2 binom(M,m) >= m*log_2(M/m) and log_2 n! <= n*log_2 n.
            log2_classes_lower = m*math.log2(M/m) - n*(2*r)
            self.assertGreater(log2_classes_lower, 0)


if __name__ == "__main__":
    unittest.main()

