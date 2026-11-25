# antonina-GvuhNBX7BCnQreaok9Hz5R-expected

Session: ses_df38a0d0cffey2bvY1EdrQNZy0
Workspace: /home/lubko/soring-fronts/succinct-adversary-copnp-sortboundu-alln
Created: 1795505386552; updated: 1795505778481

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20c75faa300107ysgNKVX2aG2B)

I'll start by understanding the repository structure and the key documents.

## Output 21 (msg_20c760f23001HoNazcpJ0uVAD4)

I'm on `billy-dev`, working tree clean. Let me read the key documents.

## Output 44 (msg_20c762323001tQO6wntkF9xwD6)

Let me read the directly relevant research docs and the board digest.

## Output 67 (msg_20c7631050010tuJeDnlqiptr9)

Let me check the research board #301 and look for any prior work on this specific front (possible infrastructure failure).

## Output 95 (msg_20c765f16001MLUU0GYl9IjWQp)

Let me check related prior work on coNP certificates in the repo history and the board, to avoid rediscovery.

## Output 161 (msg_20c780a48001qqWtX6dypCqYC3)

Let me check what's known about lower bounds on the surplus `S(n) − ⌈log₂ n!⌉`, since that affects the exact-budget family.

## Output 176 (msg_20c790a590013Ibizix7Tnrixz)

Let me check how to post to the board and verify a few key facts independently.

## Output 214 (msg_20c79b309001WrDkaWnrM0vnxN)

I have enough context. Let me independently verify the key arithmetic/structural facts with a scratch script (no repo changes).

## Output 241 (msg_20c7b1254001OmET3maS4aZo6g)

I've completed the analysis. Let me post a single finding to board #301 (the established reporting channel).

## Output 293 (msg_20c7bc1f3001osyngc3vChdiaO)

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
