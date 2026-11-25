# antonina-X3lacfmfuBEYBYcEVjmwk1-streaks

Session: ses_dff05ac3cffejH1OGWIIHLYSxj
Workspace: /home/lubko/soring-fronts/curator
Created: 1795312737694; updated: 1795314744664

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 27 (msg_20106a3e2001WUcBlI1kLns1Zc)

I'll start by orienting myself carefully, given the recovery warnings. Let me check the host, git state, existing task records, and the key docs in parallel.

## Output 46 (msg_201077add001G1rCh0udFIEgjM)

I'm on `billy-dev`, git is clean, and the deliverable `frontier-candidates.json` does not exist yet. There's substantial prior scratch work in `/tmp/opencode` from an interrupted turn. Let me read the core docs and locate board #301.

## Output 65 (msg_201083e69001o2x1cHOdBXstG9)

Now let me read the latest board #301 digest and the literature notes.

## Output 80 (msg_20108836c001b5JZF1Jz8GvANK)

Let me capture the full board digest to a file and read the barrier docs to understand what's already been investigated.

## Output 113 (msg_20108b2c1001b02hNSPMFlbKKK)

Let me read the remaining barrier docs and check the durable ledger state to map what's been covered.

## Output 128 (msg_201094222001raWHB2da0Pv3hc)

The ledger shows 675 already-investigated fronts — an extremely dense coverage. Let me examine the existing scratch solvers (from the interrupted turn) so I can do independent grounding work without reinventing them, then probe a genuinely fresh claim.

## Output 143 (msg_2010a203d001fdFZvombnPgsU5)

I have solid independent solvers from the prior turn. Now let me mount a fresh, substantive attack: a claim not in the 675-front ledger, grounded in today's `t5` uniform-base result. I'll test whether the antichain extremizes the minimax value among all posets with at most `n!` linear extensions.

## Output 161 (msg_2010b201e001Iss6B5P1ph7LzA)

A genuine counterexample appeared at `n=5`: a 6-element poset with exactly `5!=120` linear extensions but minimax `m=8 > S(5)=7`. This refutes the claim. Let me verify it independently with two different representations and methods before relying on it.

## Output 179 (msg_2010b770b001LUG7tbXQBEI0oR)

Three independent methods confirm the counterexample. Let me probe one more layer — whether the gap persists at `n=6` (7-element posets with `e ≤ 720`) — to sharpen the research question, with a bounded timeout.

## Output 208 (msg_20117e4330015clKaPa90J8cKO)

The `n=6` probe is computationally blocked (6.1M posets; enumeration didn't finish in the time budget) — an honest limit. My verified `n=5` counterexample is sufficient grounding. Let me check the keeper's exact schema before writing the deliverable.

## Output 219 (msg_201184afc001AhLkG7hDT4Y1pJ)

I have a verified, non-duplicate finding. Now I'll write the curator deliverable with two sharply scoped, all-n falsifiable fronts grounded in it.

## Output 232 (msg_201189f2f0012dyg8KUB3aHkMO)

Now let me validate the JSON against the exact keeper schema and confirm it's a single clean external effect.

## Output 241 (msg_20118bf8b001nLgMMe4XQsOlv7)

## Report — curator run on `billy-dev` (2026-11-22)

**Recovery check.** Host is `billy-dev`; git clean at `f89f6d0`. The deliverable `frontier-candidates.json` did **not** exist, so the interrupted turn never completed it. Board #301 already contains the `t5`, frontier-peak, and tightness posts from prior turns — I did **not** re-post, re-commit, or repeat any external side effect. The only effect this turn is writing `frontier-candidates.json` (schema-validated, duplicate-checked against all 675 ledger IDs).

**Grounding attack — claim disproved.** I attacked an all-`n` claim not present in the ledger: *the antichain `A_n` extremizes the exact minimax comparison count among all posets with at most `n!` linear extensions*, i.e. `T(n):=max_{e(P)≤n!} m(P) = S(n)`. I **refuted** it at `n=5` with a 6-element poset (relations `0<1, 5<3, 5<4`) having `e=120=5!` but `m=8 > S(5)=7`, cross-checked by three independent methods (brute permutation count, frozenset minimax, depth-bounded DP); exhaustive search confirmed no ≤5-element poset with `e≤120` has `m>7`, so `g(5)=6` sharply. Scratch only: `/tmp/opencode/uniform_base_{attack,verify,n6}.py`.

**Honest limits.**
- This is a **constraint on one family of evaluator approaches**, not a class result: optimizing `m(P)` under an `e≤n!` cap yields `T(n)>S(n)`, so it cannot be an exact route to `S(n)`. It says nothing about `SORT-BOUND-U ∈ P/NP/PSPACE` (the sparse/PSPACE facts are unchanged).
- **General-poset vs antichain:** the witness is a *general* poset; it gives **no reduction to the antichain root**, no hardness transfer, and no lower bound for computing `S(n)`. It distinguishes certificate **soundness** (the gadget is checkable) from **completeness** (it does not cover the antichain).
- The `n=6` extension probe (7-element posets, `e≤720`) was **computationally blocked** (6.1 M posets; enumeration did not finish within 150–420 s) — recorded as a limit, not an obligation.
- No new `S(n)` value, no Lean/repository/CI change, no board post.

**Deliverable.** `/home/lubko/soring-fronts/curator/frontier-candidates.json` contains two genuinely new, non-duplicate all-`n` fronts grounded in the verified witness and today's board #301: `near-antichain-excess-gadget-size` (is `g(n)=n+1` for all `n≥5`?) and `uniform-extension-base-gap-growth` (is `T(n)−S(n)` bounded or unbounded?). Both pass the keeper's exact id/slug, field-length, and duplicate-fingerprint checks.
