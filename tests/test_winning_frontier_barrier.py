"""Exact finite checks of the paper-level frontier-count theorem."""
import math
import unittest

def matching(s):
    assert s >= 4 and (s & (s - 1)) == 0
    return [2*x if x < s//2 else (2*x+1) % s for x in range(s)]

def budget(r):
    s=1<<r
    n=s*s
    factorial=math.factorial(n)
    k=(factorial-1).bit_length()  # exact ceil(log_2(n!))
    t0=2*s*(s-1)
    b=s-1+(n-1)*r
    m=k-t0-b
    M=(s-1)*(s*s-2*s)
    return factorial,k,t0,b,m,M

class WinningFrontierTests(unittest.TestCase):
    def test_matching(self):
        for r in range(2,9):
            s=1<<r
            f=matching(s)
            self.assertEqual(set(f),set(range(s)))
            for x,y in enumerate(f):
                self.assertIn(y,((2*x)%s,(2*x+1)%s))

    def test_exact_1024_witness(self):
        fac,k,t0,b,m,M=budget(5)
        self.assertEqual((k,t0,b,m,M),(8770,1984,5146,1640,29760))
        self.assertEqual(t0+m+b,k)
        self.assertLess(m,M//2)
        self.assertGreater(math.comb(M,m),(1<<381)*fac)

    def test_exact_4096_witness(self):
        fac,k,t0,b,m,M=budget(6)
        self.assertEqual((k,t0,b,m,M),(43251,8064,24633,10554,249984))
        self.assertGreater(math.comb(M,m),(1<<19831)*fac)

    def test_smaller_r_has_no_positive_quotient_bound(self):
        fac,k,t0,b,m,M=budget(4)
        self.assertEqual((k,t0,b,m,M),(1684,480,1035,169,3360))
        self.assertLess(math.comb(M,m),fac)

if __name__=="__main__":
    unittest.main()
