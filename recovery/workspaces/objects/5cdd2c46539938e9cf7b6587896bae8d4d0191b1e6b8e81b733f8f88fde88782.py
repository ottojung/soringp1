"""Regression cases for the experimental evaluator."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from evaluate import sorting_number


class SortingNumbers(unittest.TestCase):
    def test_small_values(self) -> None:
        for n, expected in enumerate((0, 0, 1, 3, 5, 7, 10)):
            with self.subTest(n=n):
                self.assertEqual(sorting_number(n), expected)

    def test_negative_argument(self) -> None:
        with self.assertRaises(ValueError):
            sorting_number(-1)


if __name__ == "__main__":
    unittest.main()
