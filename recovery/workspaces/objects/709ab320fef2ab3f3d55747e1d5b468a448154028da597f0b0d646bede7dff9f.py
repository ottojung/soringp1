"""Regression tests for the framed sorting-DAG verifier.

These test concrete certificates, not all-n completeness or optimality.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_framed_strategy import (
    InvalidCertificate, check_certificate, triangular_bubble_certificate
)


class FramedCertificateTests(unittest.TestCase):
    def test_bubble_cases(self):
        for n in range(13):
            with self.subTest(n=n):
                c = triangular_bubble_certificate(n)
                self.assertEqual(check_certificate(c), n * (n - 1) // 2)

    def test_too_small_budget(self):
        c = triangular_bubble_certificate(5)
        c["budget"] -= 1
        with self.assertRaises(InvalidCertificate):
            check_certificate(c)

    def test_unsound_permutation(self):
        c = triangular_bubble_certificate(2)
        c["nodes"][0]["gt"]["perm"] = [0, 1]  # missing comparison-dependent swap
        with self.assertRaises(InvalidCertificate):
            check_certificate(c)

    def test_non_sorting_program(self):
        c = triangular_bubble_certificate(3)
        c["nodes"] = c["nodes"][:1] + [{"leaf": True}]
        with self.assertRaises(InvalidCertificate):
            check_certificate(c)

    def test_cycle_rejected(self):
        c = triangular_bubble_certificate(3)
        c["nodes"][1]["lt"]["next"] = 0
        with self.assertRaises(InvalidCertificate):
            check_certificate(c)

    def test_invalid_frame_rejected(self):
        c = triangular_bubble_certificate(3)
        c["nodes"][0]["lt"]["perm"] = [0, 0, 1]
        with self.assertRaises(InvalidCertificate):
            check_certificate(c)


if __name__ == "__main__":
    unittest.main()
