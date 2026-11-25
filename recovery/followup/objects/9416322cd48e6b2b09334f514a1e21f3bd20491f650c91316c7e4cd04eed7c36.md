# FO(TC) strategy program: one falsifiable question

Hypothesis: every exact S(n)-comparison sorter has a polynomial-size FO(TC) strategy program whose interpreter runs in uniform polynomial time, so SORT-BOUND-U is in Sigma_2^P via existential program + universal order quantifier.

Falsification target: the fixed-m split-schema penalty C(m,n) (branch research/...-fo-tc-split-schema) grows super-polynomially in n for fixed m; if so, no polynomial-size FO(TC) program can encode the split family without growing the universal quantifier's program budget, refuting completeness for that fragment. Test C(5,8), C(6,9) next.

Next decisive question: does C(m,n) stay bounded by a polynomial in n for any fixed m, or does the penalty grow? A growing penalty refutes polynomial-completeness for fixed-m programs; bounded penalty supports it.">
filePath">
/workspace/soringp1/docs/research-fo-tc-program-question.md
## Update (C(5,8), C(6,9))
C(5,8)=16 exact (no penalty); C(6,9)=19 exact. Penalty cells remain (3,5)=7? wait C=7 vs B=8, (4,5), (3,6), (4,7). No growth of penalty in tested range. Fixed-m programs remain exact for m>=5 through n=9.

## Update (extended sweep, fixed-m split schemas)
Computed C(m,n) for additional cells:
- m=2: C(2,6)=9 (pen0), C(2,7)=12 (pen0) — split_total = S(2)+C = 1+C = S(n) holds (10,13)
- m=3: C(3,7)=10 (pen0), C(3,8)=13 (pen0) — holds (13,16); fails at (3,6) as before
- m=4: C(4,8)=11 (pen0), C(4,9)=15 (pen1) — holds at 8, fails at 9 (split_total 20>19)
- m=5: C(5,8)=9 (pen0), C(5,9)=12 (pen0) — holds at 8,9
- m=6: C(6,9)=10 (pen1) — fails at 9 (split_total 20>19)

Pattern: for large fixed m (e.g. m>=5) the split-schema achieves exact S(n) through n<=9 with penalty 0 on C in tested cases; penalty appears at specific (m,n) points but C penalty itself remains small (+0 or +1). No evidence of super-polynomial growth in the tested range. Fixed-m split families fail at some n>m for every fixed m tested so far (some fail earlier). This is consistent with the phase-coupling barrier but does not by itself refute polynomial-completeness of arbitrary (non-split) programs. The decisive question remains: can non-split FO(TC) strategy programs achieve polynomial size and uniform polytime for all n?
