import unittest

from scripts.minimal_winning_basis import check, count_formula


class MinimalWinningBasisTests(unittest.TestCase):
    def test_known_counts(self):
        self.assertEqual(count_formula(4, 1), 12)
        self.assertEqual(count_formula(8, 2), 840)
        self.assertEqual(count_formula(12, 3), 110880)

    def test_small_families_are_equal_size_antichains(self):
        for n in (4, 8):
            with self.subTest(n=n):
                self.assertEqual(check(n, n // 4), count_formula(n, n // 4))


if __name__ == "__main__":
    unittest.main()
