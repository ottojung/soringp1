# antonina-rPacawOMZ8kpMcmuLSxDB3-hunting

Session: ses_df6094f47ffefuQ9kGsCPwPW0C
Workspace: /home/lubko/soring-fronts/single-ply-excess-drop-magnitude-alln
Created: 1795463491870; updated: 1795465273672

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_209f6b4f2001NYQIB74UihNKch)

I'll start by understanding the repository structure, the key definitions, and the current state. Let me check the git situation and read the core documents in parallel.

## Output 25 (msg_209f6c364001gnog0ZnIfzX4j3)

I'm on `billy-dev`. Let me read the one-ply obstruction doc, operations (research board), literature, and find the board #301 plus the key definitions.

## Output 44 (msg_209f6cf9c001Y3jlJJBU6IkGL0)

Let me look at the current front's directory, the frontier definition, and search for `delta`/`excess` definitions and any earlier work in this front.

## Output 63 (msg_209f6e472001wpRVjAHU9Zn14H)

Let me find the exact front definition in the frontier ledger/JSON and search the board for this front's slug and related "excess/drop" findings.

## Output 82 (msg_209f6fc65001aaQ0dTAiJJY6CJ)

There's a closely related resolved front `f-drop-synchrony-optimal-play-alln`. Let me find this front's exact ledger entry and read the full board posts for the related front, plus look for any earlier work specific to this front.

## Output 106 (msg_209f75764001gCQRBCC0YdmWIu)

Let me find the exact ledger entry for this front and read the full `f-drop-synchrony` result which is the closest prior art.

## Output 121 (msg_209f76f700010fwpH5g8c5VWlO)

I now have a precise picture. The key quantity is `delta(P) = F(P) - ceil(log2 e(P))` (local information excess), and `D(n) = delta(A_n)` matches the "root identity". Let me verify the theoretical structure and then compute.

First, a crucial reduction: since `delta(C) ≥ 0` always (information bound), a drop `delta(P)-delta(C) ≥ 2` requires `delta(P) ≥ 2` at a reachable optimal-play state. Let me set up an exact solver in scratch space (`/tmp/opencode`, no repo changes).

## Output 132 (msg_209f88876001yCzenAapj6Tht0)

The solver reproduces all known values and both witnesses. Now let me implement the reachable optimal-play scan with budget tracking (all states lying on some height-S(n) tree) and compute maximum local excess and maximum per-step excess drop.

## Output 143 (msg_209f9d006001tEVvRK8B0112iX)

Let me test whether the drop bound holds over *all* posets (not just reachable) — this tells me whether reachability is essential. I'll enumerate all posets for n≤6.

## Output 154 (msg_209fa77c90013oHXpBrH3sbgIM)

Even over *all* posets on ≤6 elements, delta ≤ 1 and drops ≤ 1. The delta=2 posets only appear at n≥17 (general prime constructions, likely not reachable). Let me now scale to n=7 with an optimized C++ solver to search reachable optimal-play states.

## Output 183 (msg_209fb0ef9001pvnIBk85L59j6r)

Go is available. Let me rewrite the scan in Go for speed.

## Output 203 (msg_209fb6fcd001KK8vqOAm5QJMIt)

Go matches Python and is ~10x faster. Now let me run n=7 (both strict and full), which is the decisive new computation.

## Output 214 (msg_20a001271001muU6gaCCEwxWLZ)

n=7 confirms maxdelta=1, maxdrop=1 across 3M reachable states / 38M events. Let me check whether *any* poset on 7 elements has delta≥2 (to bound where a counterexample could first appear), using a full Go enumeration.

## Output 232 (msg_20a01c23c001Oxn6SsKz7iO44x)

Key structural findings so far:
- `drop ≥ 2` requires a reachable state with `delta ≥ 2` (since `delta(C) ≥ 0`).
- Along harder-child (principal-variation) transitions, `drop ≤ 1` is a **theorem for all n**: `e(H) ≥ e(P)/2 ⇒ L0 drop ≤ 1`, and `F(H)=F(P)-1`, so `delta(H)-delta(P) = (L0 drop)-1 ∈ {−1,0}`.
- Exhaustive scan: all reachable optimal states for n≤7 have `delta ≤ 1`, `drop ≤ 1`.

Let me verify a concrete delta=2 construction (ordinal sum of two e=8 witnesses) and then do a targeted beam search at larger n for reachable delta≥2.

## Output 252 (msg_20a029c31001CaOzo7eNUMCW32)

The 8-bit packing overflows for n=10. Let me fix with 16-bit slots and verify the ordinal-sum delta=2 construction.

## Output 263 (msg_20a02c663001j630rpJh69DdOT)

The delta=2 construction is analytically clear (ordinal sum: e multiplies, F adds ⇒ `W⊕W` has e=64, F=8, delta=2) — the packing overflow was just a scratch-code bug. More importantly, the n=7 scan revealed the **mechanism**: delta rises from 0 to 1 via an optimal transition whose L0 drop is ≥2 (root L0=13 → 9 over 3 steps). So I need to test whether delta can rise 0→1→2 at larger n. Let me run a beam search at n=8,9,10.

## Output 299 (msg_20a0d80120015vmEr5T52uUjkE)

The n=8 exact minimax from scratch is expensive. Let me check available memory and time a standalone n=8 root computation before deciding whether a full n=8 scan is feasible.

## Output 319 (msg_20a0e543e001ijMNu1mnOsPdFN)

Memory (12 GB free) confirms a full n=8 scan (≈432M posets, ~20 GB) is infeasible here; n=7 is the exhaustive frontier. Let me verify the root identity that pins down the definition of `delta`, then check the board posting mechanism.

## Output 330 (msg_20a10a38d001P2g5vQL4UqPOax)

The root identity is a clean algebraic deduction (for a first antichain comparison, `L0(child)=L0(A_n)−1` since `e(child)=n!/2`, so `D(n)=1+min max F(child)−L0(A_n)=min max delta(child)`). Let me find the board posting command.

## Output 350 (msg_20a10ca77001FrhOv4TujLX9QA)

Let me do a final duplicate check across board pages, then post the finding exactly once.

## Output 361 (msg_20a112a3d001VXpuGEciRWGXJX)

No prior post exists. Let me compose and post the report exactly once.

## Output 379 (msg_20a119a5e001O3v6uXSjR650oj)

Let me verify the post was appended exactly once.

## Output 399 (msg_20a11c195001hBXEk5sBAFaGA3)

Done. Worktree clean on `billy-dev` at `6a96398`; no repository changes. Report posted once to board #301.

## Mathematical finding

I pinned the front's quantity down to `delta(P) = F(P) − ceil(log₂ e(P))` (forced by the stated root identity `D(n)=min` max-child excess, since a first antichain comparison gives `L0(child)=L0(A_n)−1`). An independent solver reproduces all known `S(n)` for n≤6 and both cited witnesses (`e=8, F=4, delta=1`).

**Theorem A (all n, proved).** Along a harder-child / principal-variation optimal transition `P→H`, `delta(P)−delta(H) ≤ 1`. Reason: `e(H) ≥ e(P)/2 ⇒ L0` drops by at most 1, and optimality gives `F(H)=F(P)−1`, so `delta(P)−delta(H) = 1 − (L0 drop) ≤ 1`. The adversarial worst-case path can never erase two units of local excess in one comparison, for any n.

**Theorem B (reduction).** Since `delta(C) ≥ 0` always, a drop ≥ 2 requires a reachable parent with `delta ≥ 2`. So the front is exactly the question of whether `delta ≥ 2` is reachable — checking drops is not easier.

**Exhaustive computation.** All states on all height-`S(n)` optimal trees for n≤7 (3,044,007 states / 38.3M transitions at n=7) have `max delta = 1`, `max drop = 1`, in both the full and strict variants; every poset (not just reachable) on n≤6 also satisfies this. The n=6 "unit-drop-only" observation extends to n=7.

**Mechanism.** `delta` rises only when a comparison loses ≥2 bits of information (`e` falls ≥4×); n=7 realizes exactly one extra bit, giving `delta=1` but not 2. General posets with `delta=2` exist (n=17 prime family; ordinal sum `W⊕W` gives `e=64, F=8, delta=2`), but these are off the optimal tree — this is a reachability/selection distinction, not a general-poset obstruction.

## Concrete failed approach / exact obstruction

- Full n=8 scan is infeasible here: exact `F(A_8)` visits all 431,723,379 labelled posets (~20 GB; this host has 12 GB). Beam search is blocked because each n=8 child `F` subcall has the same cost.
- No paper proof that `delta ≤ 1` on *all* reachable optimal states: `delta` can rise whenever a comparison loses ≥2 bits, and I could not exclude two such events on one path before the budget expires.

## Honest limits

The all-n bound is **not settled** — proved for the principal variation, verified exhaustively through n=7, but neither proved nor refuted for arbitrary reachable optimal states at larger n. Soundness of the regularity (defect heals at rate ≤1) is established; completeness (a polynomial certificate for `SORT-BOUND-U`) is not, and the sparsity/Mahaney + PSPACE barriers remain. A reachable `delta≥2` counterexample would refute the layer-indexed defect-certificate route but would yield no complexity separation by itself. No theorem computing `S(n)`, no improved bound, no class placement — no repository changes warranted.
