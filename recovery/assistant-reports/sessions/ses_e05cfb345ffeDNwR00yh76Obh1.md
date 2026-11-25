# antonina-J3cLWb8OOWAIvWPdeVIr6J-tenderly

Session: ses_e05cfb345ffeDNwR00yh76Obh1
Workspace: /home/lubko/soring-fronts/curator
Created: 1795198831812; updated: 1795199560813

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fa304d3e001R1NLfnL6qwDTzt)

I'll start by understanding the repository state, the docs, and board #301. Let me explore in parallel.

## Output 42 (msg_1fa30a8d9001yguSrntDHJX3Aw)

I'm on billy-dev as required. Let me gather the fuller board context and research docs.

## Output 122 (msg_1fa31c08c001ob2kogj9dhOJKx)

I have a thorough picture of the docs and ledger. Now let me do the actual research: attack a precise all-n falsifiable claim about exact unary S(n) that I don't see in the ledger, and try hard to disprove it computationally. Let me first check whether my candidate claim is already covered.

## Output 133 (msg_1fa32b1460018GeA4eYZnrqYuv)

No ledger front covers "power-of-two extension count ⟹ perfectly sortable". Let me attack that precise all-n claim from scratch with an independent enumerator.

## Output 151 (msg_1fa335890001HKOpGDvS3NveK7)

I found genuine counterexamples. Let me verify one independently with a completely different representation (sets of permutations), and check reachability from the antichain root.

## Output 169 (msg_1fa3439b9001TLsJ1Br9Fj3IZP)

Independently confirmed: e=8 but F=4, and **no root comparison splits 8 into 4+4** — exact halving is impossible. Now let me check near-duplicate coverage before deciding on new fronts.

## Output 184 (msg_1fa345f8c001wjSemwxG0SS81w)

Let me check the board more broadly for near-duplicate coverage of my candidate directions.

## Output 202 (msg_1fa35bb76001Vuc2zDbz1nSxEG)

The halving direction is genuinely new (no board/ledger match). Let me characterize the counterexample family a bit more for a solid basis, then finalize.

## Output 213 (msg_1fa36422f001RhivNrT5FqTBgA)

Let me quickly check a few ledger-adjacent fronts to avoid any accidental duplication, then write the JSON.

## Output 233 (msg_1fa378257001oqUwwN3ydaoCxE)

The board shows an important overlap: a "loose e=8 witness at n=5" is referenced. Let me check that doc before claiming novelty.

## Output 248 (msg_1fa37b3dd001vxo9aCh9swhG8D)

My "counterexample" is already a known repository datum (docs/research-n12-nontightness.md line 192). I must not claim novelty for it. Let me read the newest board posts in full to find genuinely open, unclaimed directions.

## Output 268 (msg_1fa3824e7001ueuGS6FLCTlkhr)

The freshest open thread involves the Ford–Johnson gap. Let me check whether the "gap growth" question is already claimed before proposing it.

## Output 288 (msg_1fa3ae383001jwXPoEtY8iWmaW)

I've confirmed my finite counterexample is a documented datum (docs/research-n12-nontightness.md), so I won't claim novelty for it. The genuinely unclaimed directions are the all-r infinitude of the halving obstruction, its survivability under antichain reachability, and the recognition complexity of information-tightness. Let me write the JSON.

## Output 306 (msg_1fa3b4b4c001muDqgnCPsG0MZL)

Done. I worked on billy-dev (host confirmed), studied AGENTS.md, docs/problem.md, docs/research-plan.md, docs/research-core-threshold.md, docs/research-width-two-threshold.md, the frontier ledger (611 investigated/blocked fronts), and board #301 across all pages.

## Research attack and honest outcome

**Claim attacked (all-n, falsifiable):** "Every finite poset with `e(P) = 2^r` is perfectly sortable, i.e. `F(P) = log₂ e(P) = r`."

I derived the *exact-halving necessity* condition: if `e(P) = 2^r`, then `F(P) = r` requires a comparison tree in which every node splits its extension count into two equal halves (since `e₀ + e₁ = 2^r` and both children need `≤ 2^{r-1}`). From a from-scratch enumerator I found n=5 posets with `e = 8` but `F = 4`, whose root splits are only `5+3` and `2+6`, never `4+4`; n=4 had none. I independently re-verified one (`succ=(26,0,10,0,8)`) with a second representation (explicit sets of surviving permutations): sortable in 4 but not 3 comparisons.

**Honest limits — I am not claiming a new theorem:**
- The e=8, cost-4 witness is already a documented datum at `docs/research-n12-nontightness.md:192`, used there to show `m` is not a function of `e`. My contribution is only the halving framing, not a new counterexample or new S(n) value.
- This is a **general-poset** result. It does not transfer to the antichain root without a reachability argument: the witness is not reachable at n=5 (its 5 covers exceed the window depth `S(5)−F = 3`). No class separation, no SORT-BOUND-U consequence, and no general-poset→S(n) bridge is supplied.
- A sound Kraft-clean witness is not a completeness certificate for tightness; I kept that distinction explicit.
- No Lean, repository, CI, ledger, or main changes were made; worktree is clean apart from the required output file.

## Curator output

I wrote three genuinely new, non-duplicate fronts to `/home/lubko/soring-fronts/curator/frontier-candidates.json` (schema and all field-length constraints validated):

1. `halving-obstruction-infinitude-allr` — whether power-of-two halving obstructions exist for all r and how `m(r)` grows.
2. `antichain-reachable-power2-halving-obstruction` — whether that obstruction survives the reachability filter inside the actual height-S(n) game.
3. `information-tightness-recognition-complexity` — complexity and certificate completeness (vs mere soundness) of recognizing `F(P) = ⌈log₂ e(P)⌉`.

I avoided the actively dispatched (#301 18:03Z) fronts: Kraft-clean converse at n=7,8, the tight-tree constructor grammar, FJ arithmetic gap, and the many greedy/e-index and certificate fronts in the ledger.
