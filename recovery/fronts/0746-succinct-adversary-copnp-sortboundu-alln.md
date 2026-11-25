# succinct-adversary-copnp-sortboundu-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

GvuhNBX7BCnQreaok9Hz5R-expected

## exit_state

clearexit

## question

Does SORT-BOUND-U admit a polynomial-size succinct adversary certificate certifying S(n)>k at the n-antichain against every sorter, thereby giving coNP membership without enumerating the exponentially many winning frontier states?

## basis

problem.md leaves NP/coNP membership open; research-winning-frontier-barrier.md rules out full winning-state enumeration; board #301 has no dedicated adversary-certificate or coNP-membership front.

## falsifier

Exhibit an infinite family of budgets (n,k) with S(n)>k for which every adversary-winning strategy needs superpolynomial description size under any fixed sound succinct scheme.

## implication

A sound and complete polynomial-size adversary certificate would place SORT-BOUND-U in coNP, a new uniform upper bound strictly below PSPACE unless coNP=PSPACE.

## finding_unverified

the board, to avoid rediscovery.
Let me check what's known about lower bounds on the surplus `S(n) − ⌈log₂ n!⌉`, since that affects the exact-budget family.
Let me check how to post to the board and verify a few key facts independently.
I have enough context. Let me independently verify the key arithmetic/structural facts with a scratch script (no repo changes).
I've completed the analysis. Let me post a single finding to board #301 (the established reporting channel).
## Result

I attacked the claim that a fixed polynomial-size, sound-and-complete succinct **adversary** certificate scheme exists for `SORT-BOUND-U` (equivalently, that `SORT-BOUND-U ∈ coNP`). I could not disprove it; the honest outcome is a precise obstruction plus two failed disproof routes. No repository or Lean changes were made — worktree is clean at `6a96398` on `billy-dev`, and one finding was posted to board #301.

### What I established

**F1 — the requested falsifier is unattainable unconditionally (exact obstruction).** `SORT-BOUND-U ∈ PSPACE` is already proved in the repo (`research-certificates-barriers.md`, Claim A: `APTIME = PSPACE` on the unary game). So proving that infinitely many no-instances have only superpolynomial adversary certificates would give `SORT-BOUND-U ∉ coNP`, hence **coNP ⊊ PSPACE** — a major open separation. The front as literally posed reduces an open complexity problem, rather than a tractable combinatorial target.

**F2 — implication sharpened.** A poly-size scheme would give not just `coNP` membership but `S_unary ∈ FP^NP` (binary search on `k ∈ [0, n⌈log₂n⌉]` with `O(log n)` P^NP queries). Unless `Δ₂ᵖ = PSPACE` (PH collapse), this is a strict uniform improvement over `FPSPACE`.

**F3 — soundness ≠ completeness.** Sound verifiers are easy (explicit adversary tree + local checks); determinacy guarantees a winning strategy exists. Completeness — a poly witness for *every* no-instance — is the entire open content.

**F4 — counting certificates refuted (rigorous, independently checked).** Any certificate whose soundness uses only the number `m` of surviving permutations requires `m > 2^k` (a height-`k` tree has ≤ `2^k` leaves), hence works only for `k < ⌈log₂ n!⌉`. Exact arithmetic confirms `⌈log₂ 12!⌉ = 29 < S(12) = 30`, so the hard instance `k = 29 = S(12)−1` admits **no counting certificate**; likewise for every known surplus-1 `n` (12–19, 22, and `S(28) ≥ 99` vs `⌈log₂ 28!⌉ = 98`).

**F5 — the winning-frontier barrier does not transfer.** It counts *sorter-winning states reachable under some outcome sequence*; a certificate lower bound needs states *forced against every sorter*. Reachability ≠ forcing, and that note explicitly excludes selective/compressed methods. The front's motivation conflates the sorter's YES direction with the adversary's NO direction.

**F6 — general posets do not transfer.** Kahn–Saks and the `n=7` `(e, M1)`-cospectral counterexample concern arbitrary posets; Sergeev gives only `S(n) = log₂(n!) + o(n)`, and whether surplus is positive infinitely often is open — so even the family `k = S(n)−1` is not known to be infinite.

### Honest limits
The general coNP question remains **open**. Both serious disproof attempts failed for general schemes, and the literal falsifier would resolve `coNP` vs `PSPACE`. The decisive next obstacle is to name a certificate grammar strictly stronger than counting and prove either completeness or an unconditional grammar-specific size lower bound. Process success here is not a proof.

## Other metadata

```json
{
  "finished_at": 1795505819.7892709,
  "started_at": 1795505385.1102335
}
```
