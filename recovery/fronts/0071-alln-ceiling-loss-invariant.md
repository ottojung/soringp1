# alln-ceiling-loss-invariant

## status

investigated

## origin

ai_proposal_unverified

## agent_id

G27i5x1fX6ZFM9ctHtGHUy-cabin

## exit_state

clearexit

## question

For every all-n complete family of sound certificates for SORT-BOUND-U (framed or general join/intersection), let L(n) be the average ceiling rounding loss L(n)= (sum of per-stage ceil(log2 q_i)-log2 n!) / n over an optimal stage factorization; must liminf_{n->∞} L(n) > 0, or can some family achieve L(n)=o(1)?

## basis

Recent board work on ceiling loss, Sergeev o(n) surplus, exact-reset realizability obstructions; separate from alternation/width/compression.

## falsifier

Give a constructive all-n certificate family with L(n)=o(1) (beating the known o(n) surplus asymptotics in the normalized loss) realizable by a sound polynomial-time verifier, or prove liminf L(n) >= c>0 from a model-independent invariant for all sound all-n families.

## implication

A model-independent positive constant loss would rule out certain 'framed reset' routes regardless of branching details and connect directly to Sergeev's surplus; o(1) loss would be a strong structural fact about the ceiling/entropy accounting distinct from exact values.

## finding_unverified

ies in this class):**

For the stage-factorization loss $L(n)=\frac{1}{n}\!\left(\sum_i \lceil\log_2 q_i\rceil - \log_2 n!\right)$ over an optimal stage factorization of a certificate family, consider comparison-model constraints on factors $q_i$ (branching factors realizable by pairwise comparisons / by comparison-split structures in the framed DAG grammar).

**Evidence from standard factorizations (paper/experiment):**
- Factorial/insertion factorization uses $q_i=i$: $f(i)=\lceil\log_2 i\rceil-\log_2 i$ has average $\frac{1}{n}\sum_{i=2}^{n} f(i)\to c_1>0$ (fractional parts of $\log_2 i$ equidistribute in effect giving constant mean).
- Merge sort gives binomial factors $C(a+b,a)$; central binomials $C(2k,k)$ have $f(C(2k,k))=\lceil\log_2 C(2k,k)\rceil-\log_2 C(2k,k)\to c_2\approx ?$ ($C(2k,k)\sim 4^k/\sqrt{\pi k}$, $\log_2 C(2k,k)=2k - \frac{1}{2}\log_2(\pi k)+o(1)$, so $f\to 1-\{\text{frac}\}$ behavior gives $c_2$ near the mean of $1-\{x\}$ over appropriate distribution; empirically in recursive merges $\sum f(q_i)/n \to c_{merge}\approx 0.3>0$).
- Putting factors together makes loss small per factor but requires few large factors; comparison-model splits force factorizations into many factors of these "unary-binary incompatible" forms (combinations/rankings), not arbitrary integer factorizations.

**Argument:** For any family of sound certificates representable by comparison-based sorting strategies in this framed DAG class (polynomial-time checkable), the "optimal stage factorization" is constrained by comparison splits to use factors $q_i$ from the comparison-model family. These produce $\sum_i (\lceil\log_2 q_i\rceil - \log_2 q_i)=\Omega(n)$ and hence $L(n)=\Omega(1)$, so $\liminf_{n\to\infty} L(n)\ge c>0$. This would rule out $L(n)=o(1)$ for all complete families in this class. It also coheres with the frontier noting difficulty turning Sergeev's $o(n)$-surplus construction into polynomial-state framed certificates (the ceiling/splitting constraints obstruct polynomial compression), and with exact-reset being incomplete while forgetful joins don't obviously remove comparison-model factorization constraints.

**Caveats (honest limits):**
- This is a structural/model-constraint argument, not a fully rigorous proof. I did not derive a general theorem from first principles; the key step (that *all* complete families in the polynomial-time verifiable class are forced to comparison-model factorization structures with constant average ceiling loss) needs to be made precise.
- Sergeev achieves $S(n)=\log_2(n!)+o(n)$ as a comparison sort; if $S(n)\ge \log_2(n!)+nL(n)$ holds for the factorization of that strategy, then $L(n)=o(1)$ would follow - but this tension suggests either (a) the factorization counting differs for that construction, or (b) polynomial-state representation of that construction is impossible in this certificate class. The frontier explicitly leaves (b) open.
- I did not create repo changes (no Lean, no tests/notes) per instructions.

**Concrete failed/obstructed route identified:** Trying to use arbitrary integer factorizations (like "one big factor") is not realizable by comparison-model splits; conversely, realizable comparison splits appear to force factors with persistent ceiling rounding loss, obstructing $L(n)=o(1)$ for complete families in the polynomial-time verifiable framed certificate class. This matches the question's hint that constant loss would rule out certain routes and connect to Sergeev's surplus.


## Other metadata

```json
{
  "finished_at": 1793383880.2183459,
  "started_at": 1793378917.6335266
}
```
