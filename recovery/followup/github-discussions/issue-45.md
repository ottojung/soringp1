# Issue #45: Independent proof review for PR 44

Upstream: https://github.com/ottojung/soringp1/issues/45
State: closed
Created: 2026-10-22T19:46:02Z

Independently audit the new unary AC0 bound and diagonal surrogate theorem in PR #44. Check the machine enumeration, density of insertion-slack indices, all small cases of the merge recurrence, and polynomial-time recovery from unary threshold queries. Report any counterexample. This is not a theorem about hardness of the actual sorting function. No Lean work unless it directly advances its uniform complexity classification.

## Comments

### None — ottojung
Comment ID: 6352377875
Upstream: https://github.com/ottojung/soringp1/issues/45#issuecomment-6352377875

Independent research audit completed (2026-10-22); **no counterexample found**.

1. **Unary AC⁰:** For each length L, the cutoff property n+S(n) strictly increasing yields a DNF of ≤L exact delimiter-position tests, each O(L) literals. This is nonuniform: the cutoff bit pattern is advice, not a uniform algorithm. Any fixed-output-length AC⁰ reduction from PARITY would compose with it, contradicting the standard lower bound.
2. **Diagonal tally witness:** Repeated machine numbering M_i=N_j via i+1=2^r(2j+1) makes each polynomial-time machine appear at arbitrarily high i. For n with v₂(n)=i, the n^(i+2) simulation eventually outruns any fixed n^d runtime. Since i≤log₂ n and coding/decoding lengths are logarithmic, the universal simulation stays inside 2^O((log n)^2). Thus it gives a genuine decidable tally set outside uniform P, without assuming P≠NP.
3. **Insertion slack:** d_n=ceil(log₂n)−(I(n)−I(n−1)) lies in {0,1}. Telescoping produces sum d_j = Σ(ceil log₂j−log₂j)+log₂(N!)−I(N). On the first half of each dyadic block the summands exceed 1−log₂(3/2), giving a positive lower density for T. Consequently its mth index t_m=O(m), enumerable in polynomial time for unary m.
4. **Merge slack:** max_a binom(9,a)=126≤2^7, and max_a binom(N,a)/2^N is nonincreasing by Pascal's identity. Therefore binom(N,a)≤2^(N−2) for N≥9 and I(N)≤I(a)+I(c)+N−2. With b_N=0 for N≤8 this absorbs every b_N∈{0,1} in the merge recurrence.
5. **Threshold reduction:** Query U_G at (n=t_m, k=I(n)); it is accepted iff b_{t_m}=0, recovering the diagonal tally membership in polynomial time, contradicting U_G∈P.

**Independent numerical falsification checks:** computed T through n=300 and the merge baseline through n=49, then tested 25 independent arbitrary 0/1 placements on T∩[9,120]; all insertion and merging inequalities held for every relevant pair (a,c). These checks supplement, not replace, the all-n algebra above.

**Scope:** These statements do NOT show hardness of actual sorting S(n); G is explicitly artificial, and no Lean formalization is warranted. PR #44 already merged with successful CI. This completes the narrow proof-review assignment.

---

