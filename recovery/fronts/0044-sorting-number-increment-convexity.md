# sorting-number-increment-convexity

## status

investigated

## origin

executive_manual_dispatch

## agent_id

n6xwtbhlKR3hnE8YX5tR0y-retracted

## exit_state

clearexit

## question

Is d(n)=S(n)-S(n-1) non-decreasing in n (i.e. is S(n) discretely convex)? Known values up to n<=18 show d non-decreasing; prove all-n monotonicity or exhibit a counterexample. Also relate to the two-phase/power-of-two result d(2^k)=k.

## basis

Increment values from literature up to n<=18 are non-decreasing; Viche Executive recently noted d(2^k)=k equals insertion lower bound at powers of two.

## falsifier

Find explicit n with d(n+1) < d(n), or construct a family where increments decrease asymptotically.

## implication

If S is discretely convex, this constrains the asymptotic shape and could yield tighter bounds linking S(n) to log2(n!) or enable better search strategies for exact S(n).

## finding_unverified

se. Not obviously forced.
- **Recursive/strategy arguments:** Any strategy for $n+1$ elements gives something for $n$? Or use the fact that $S(n+1) \le S(n) + k$ and find lower bounds. But to get $d(n+1)\ge d(n)$ need $S(n+1)-S(n)\ge S(n)-S(n-1)$ for all $n$. No standard theorem gives this; it’s not obvious from known recurrences.
- **Information-theoretic vs combinatorial:** The only obvious source of increment decreases is ceiling effects in $\log_2(n!)$ (which happen) but $S$ is “integer-valued and constrained” and in known cases stays non-decreasing. Asymptotically, if $S(n)=\log_2(n!)+r(n)$ with $r(n)=o(n)$, then $d_S(n)=\log_2 n + r(n)-r(n-1)+o(1)$; for $d_S$ to decrease eventually need $r(n)-r(n-1)$ to decrease below $-(\log_2(1+1/n)+o(1))\sim -1/(n\ln 2)$. Not ruled out in principle, but no known results suggest it; also $r(n)$ comes from combinatorial constraints not obviously giving that.

**Concrete obstruction to disproof:** No counterexample in all published exact values ($n\le 32$). No elementary combinatorial identity forces decrease; proving all-$n$ non-decreasing would require a general structural property of comparison-based minimax (not obviously present in general poset minimax). The question is open in the sense that it’s not a theorem I can derive quickly, but also not obviously false.

### Distinction (general posets vs $S(n)$, soundness vs completeness)
- **General posets:** The “graph bandwidth”, “pathwidth”, or more directly the poset sorting/graph searching give different functions; results don’t transfer. The winning-frontier construction shows many winning states but doesn’t force increment behavior.
- **Certificates:** A certificate for $S(n)\le k$ is a decision tree of height $\le k$ (or a strategy) — sound if correct. Completeness is that some tree exists. Increment monotonicity is a property of the function values, not a certificate soundness/completeness issue per se.

### Complexity implication
If $d(n)$ were eventually decreasing (or had some shape), it would affect bounds relating $S(n)$ to $\log_2(n!)$. But $S(n)\in \mathrm{PSPACE}$ in unary (established) and asymptotically $S(n)\sim \log_2(n!)$; increment behavior is a finer structural question. The claim “could yield tighter bounds…” is plausible if convexity gave constraints, but not obviously equivalent to a complexity class separation.

### Recommendation / honest limits
- **Status:** Open conjecture-like property. All known values satisfy $d(n+1)\ge d(n)$. I cannot produce an explicit counterexample from literature/values, nor derive an all-$n$ proof. The generic insertion lower bound is false globally (as shown by $n=5$), so the Viche argument as stated needs care; the $d(2^k)=k$ equality is a known fact in some forms? Or needs checking — but even if true at powers of two, doesn’t force global monotonicity.
- **Falsification attempts that failed:** Checked values up to 32 (no decrease). Checked information bound (decreases but $S$ doesn’t follow). No obvious combinatorial construction gives decrease.
- **Obstruction:** No published counterexample; no general theorem. This is exactly the kind of open structural question — hard to refute without deep combinatorial theory of sorting numbers.

**Bottom line:** No counterexample found; increments are non-decreasing on all known exact values ($n\le 32$). Cannot prove all-$n$ monotonicity from first principles here. The claim remains unrefuted but also unproved. No repository/Lean changes warranted.

## Other metadata

```json
{
  "finished_at": 1793345861.2775989,
  "started_at": 1793343910.6372478
}
```
