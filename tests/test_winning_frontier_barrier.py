"""Exact finite checks of the rectangular winning-frontier theorem."""
import math
import unittest

def params(columns, levels):
    s, L = columns, levels
    n=s*L
    factorial=math.factorial(n)
    k=(factorial-1).bit_length()  # exact ceil(log2(n!))
    t0=s*(L-1)
    h=(s-1).bit_length()         # exact ceil(log2(s))
    B=(s-1)+(n-1)*h
    m=k-t0-B
    M=(L-1)*s*(s-1)
    return factorial,k,t0,B,m,M

class WinningFrontierTests(unittest.TestCase):
    def test_224_exact(self):
        fac,k,t0,B,m,M=params(16,14)
        self.assertEqual((k,t0,B,m,M),(1431,208,907,316,3120))
        self.assertEqual(t0+m+B,k)
        self.assertGreater(math.comb(M,m),fac*(1<<39))

    def test_256_symmetric_exact(self):
        fac,k,t0,B,m,M=params(16,16)
        self.assertEqual((k,t0,B,m,M),(1684,240,1035,409,3600))
        self.assertEqual(t0+m+B,k)
        self.assertGreater(math.comb(M,m),fac*(1<<148))

    def test_edge_independence_on_small_rectangles(self):
        # Closure cannot infer any unselected adjacent-layer edge:
        # paths of length >=2 necessarily advance >=2 levels.
        for s,L in ((3,4),(4,3),(5,4)):
            skeleton={(i*s+x,(i+1)*s+x)
                      for i in range(L-1) for x in range(s)}
            missing={(i*s+x,(i+1)*s+y)
                     for i in range(L-1) for x in range(s)
                     for y in range(s) if x!=y}
            selected=set(sorted(missing)[::3])
            edges=skeleton|selected
            adj={v:[] for v in range(s*L)}
            for a,b in edges: adj[a].append(b)
            for i in range(L-1):
                for x in range(s):
                    start=i*s+x;reached={start};stack=[start]
                    while stack:
                        a=stack.pop()
                        for b in adj[a]:
                            if b not in reached:
                                reached.add(b);stack.append(b)
                    for y in range(s):
                        end=(i+1)*s+y
                        self.assertEqual(end in reached,(start,end) in edges)

if __name__=="__main__":
    unittest.main()
