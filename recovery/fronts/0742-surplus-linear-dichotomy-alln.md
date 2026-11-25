# surplus-linear-dichotomy-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

iXu1TSlX91S3E69xXlSFxn-grants

## exit_state

clearexit

## question

Prove or disprove: the surplus S(n) - ceil(log2 n!) is Omega(n) for all n >= n0 - that is, the exact sorting number's excess over the information bound grows linearly; or exhibit an infinite family of correct trees whose surplus is o(n).

## basis

Sergeev's Theorem 1 (ECCC TR20-096 p.16: S(n) <= log(n!) + 0.09n + o(n)) records the linear-surplus form; literature.md/research-plan.md 'The bound gap'; the board's lower-bound excess fronts (branch-mass-telescoping-o-n-excess, haeubler-heapsort-antichain-excess) concern specific mechanisms or source families - this front asks the linear-vs-sublinear dichotomy of the excess of the exact value S(n).

## falsifier

Exhibit an infinite family of correct trees with height S(n) and surplus S(n) - ceil(log2 n!) = o(n) - the linear regime would be refuted - or prove the Omega(n) statement for all n >= n0.

## implication

If the surplus is Omega(n), any method targeting the information bound is off by a linear amount and sets the scale of exact unary evaluation; if it is o(n), the exact value tracks the info bound to sublinear waste, weakening any envelope-based lower-bound route.

## finding_unverified

ooling for reporting.
I have everything needed for the mathematical assessment. Let me (a) compute the small-n surplus table (experimental consistency check) and (b) check how to post to board #301 per the repo contract.
Let me check the board `comment` syntax so I can post the concise report per the repo contract (AGENTS.md: findings go to board #301).
Now I'll post the concise finding to board #301 (repo contract: report to the board), then verify.
Let me verify the board post landed.
## Finding: the Ω(n) claim is **refuted** — the surplus is sublinear

**Result: `S(n) − ceil(log₂ n!) = O(n / log^{1/5} n) = o(n)`** — the excess of the exact sorting number over the information bound grows sublinearly, so there is no linear regime. The claim "surplus = Ω(n)" is false (assuming Sergeev's theorem, see limits below).

### The falsifier: Sergeev's group-insertion trees

Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096 (2020), **Theorem 3** (p.29):

`S(n) = log₂(n!) + O(n log^{−1/5} n)`.

This is proven by an explicit sorting-algorithm family — the "group insertion" algorithm — whose trees are correct trees of height ≤ `log₂ n! + O(n log^{−1/5} n)`. Hence the surplus `S(n) − ceil(log₂ n!) ≤ O(n log^{−1/5} n) = o(n)` — exactly the requested exhibit (infinite family of correct trees with surplus o(n)), and it refutes the Ω(n) claim. Paper audit of the falsifier (§7): pair-sort `n/2 + S(n/2)`; insert `n/log n` α-elements via Ford–Johnson; insert the rest in groups of ≈`√n/log n` via the Corollary-2 gradient strategy (per-element excess `O(log^{−1/5} n)`); recurrence `s(n) ≤ s(n/2) + O(n log^{−1/5} n)` ⇒ `s(n) = O(n log^{−1/5} n)`.

### Note on the prompt's quoted "0.09n"

That is paper **Theorem 1** (p.16): `S(n) ≤ log₂(n!) + 0.09n + o(n)` — an *upper bound* on the excess in linear form; consistent with Ω(n) but not a refutation. The abstract of the paper states `log₂(n!) + o(n)`, and Theorem 3 gives the tighter sublinear bound. The repo's literature assessment (`research-plan.md`: "Sergeev — `S(n) − log₂ n! = O(n/(log n)^{1/5})`") agrees; the exact obstacle to a Ω(n) line of attack is Sergeev's bound itself.

### Honest limits

- The refutation stands on Sergeev's paper argument; I audited the theorem statement and the recurrence structure, but not every lemma (§4–§7, e.g. Corollary 2). The repo marks it "Primary theorem, not Lean-checked here."
- No new trees or experiments by me; small-n data consistent: surplus ≤ 1 through n=18 (S(12)=30 vs C=29; S(13)=33 vs 33; S(16)=46 vs 45; S(17)=50 vs 49; S(18)=54 vs 53).
- Certificate **soundness vs completeness**: Sergeev is a soundness statement (upper bounds on tree heights). Completeness (NP/coNP/PSPACE certificates of SORT-BOUND-U) is separate; the general-poset fronts on #301 (cospectral, ordinal-lift, reachable-profile) don't transfer — they concern arbitrary posets, not the antichain root of S(n). The winning-frontier barrier is about enumerating winning states, orthogonal to surplus.
- Per your instruction, no Lean/repo changes were made (clean worktree; scratch only in /tmp/opencode). A concise update is posted to board #301.

### Complexity implication (per your framing)

Since the surplus is `o(n)`, the exact value tracks the information bound to sublinear waste; envelope/excess-based lower-bound routes aimed at a linear excess are out of line with the current upper bound (any lower-bound front would have to be of order `O(n log^{−1/5} n)` or smaller to remain consistent).

## Other metadata

```json
{
  "finished_at": 1795487471.2925906,
  "started_at": 1795486854.9645803
}
```
