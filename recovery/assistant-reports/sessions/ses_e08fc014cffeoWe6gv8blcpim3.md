# antonina-BC7wpbTyXoL5kmDtlyZM8f-event

Session: ses_e08fc014cffeoWe6gv8blcpim3
Workspace: /home/lubko/soring-fronts/curator
Created: 1795145596607; updated: 1795145846580

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f703feea001WWwY704xj5IET7)

I'll start by understanding my environment and the relevant documents. Let me explore in parallel.

## Output 29 (msg_1f70410580019F7Mb0DQ3C93B2)

I'm on `main` in the curator worktree. Let me verify the host and gather the board digest, current frontier files, and research-frontier definitions in parallel.

## Output 52 (msg_1f7042945001x5ZEIXbGCnP17y)

On billy-dev. Let me locate the frontier definition and read the recent board digest.

## Output 67 (msg_1f7043a3300139u8lPphnfET6n)

Let me read the frontier definition, the current ledger state, more board pages, and the key recent research notes.

## Output 86 (msg_1f70450b8001I8ywHj8JTup0PC)

Let me read the newest research notes and inspect the ledger's full front inventory to avoid duplicates.

## Output 105 (msg_1f70466cf001nM1qpHWNEyRimy)

Let me dump all existing front IDs and the newest board content to understand what's covered and what's genuinely new.

## Output 125 (msg_1f7048a26001tt6D74hF8r8Ala)

Let me examine the newest FO(TC) result in detail — the assigned issue and the commits — so I don't duplicate the running front and can find a genuinely new angle.

## Output 171 (msg_1f704fd9700158a862rvy3qLth)

Let me read the detailed FO(TC) strategy-program note — the main new mathematical development.

## Output 182 (msg_1f7050dd7001Gzjo7ORxzQwnEZ)

Let me read the founder's assigned "fervor" issue and the two-phase barrier note it references.

## Output 206 (msg_1f705534f0012oJQKFT5Yaxq8z)

Let me examine the very recent two-phase characterization commit and check which FO(TC)-themed fronts already exist in the ledger.

## Output 221 (msg_1f705ab30001tldhEUXUyIZvQh)

Let me search the full ledger text (questions + findings) for candidate themes to ensure genuine novelty.

## Output 232 (msg_1f705ed7e0011TcWUkD32S2ShU)

Let me inspect the closest existing fronts to make sure a "hitting set / universal-quantifier elimination for program verification" front is genuinely new.

## Output 243 (msg_1f7066d52001oBP6gpxeWPVVsw)

Let me do a concrete, independent computation to ground the analysis (leaf slack at tight budget, and the loose-budget disproof).

## Output 272 (msg_1f70726d1001OzvygZ131Fxjt5)

Let me verify the exact schema the keeper expects for curator candidates, then write the file.

## Output 292 (msg_1f7076796001Q2tJyby4zPx9QV)

Schema confirmed. Now I'll write the JSON file with two genuinely new fronts, then validate it.

## Output 303 (msg_1f7078b940015tO71BuS9ZuRIT)

Now let me validate the file against the exact schema and check for duplicate fingerprints against the ledger.

## Output 321 (msg_1f707af80001ei4N3hM6KPJo1m)

Done. Here's what I did and the honest limits.

## What I studied
AGENTS.md, `docs/problem.md`, `operations.md`, `literature.md`, the recent #301 digest, the founder's "fervor" issue `JTsW4AnxTLzN18IBQibXea-fervor`, and the newest SoringP1 `origin/main` artifacts (`research-fotc-strategy-programs.md`, `research-fo-tc-split-schema.md`, publication record). I confirmed I'm on **billy-dev** and enumerated all **585** ledger fronts to refuse duplicates.

## The claim I attacked (and its status)
**Claim:** the `∀X` over input orders in the FO(TC) verifier `QWIN = ∃p ∀X Verify(p,X)` can be replaced by a polynomial-size set of representative orders, placing the representable subclass in NP rather than Σ₂ᵖ.

- **[deduction]** At a loose budget `k = n(n−1)/2` this is refuted: a sort-all-but-one-order program forces any hitting set to contain all `n!` orders.
- **[experiment/deduction]** At the tight budget `k = S(n)` the disproof needs a poly-size *optimal* program and a separately addressable leaf — i.e. it leans on Conjecture C, which is open. An independent computation gave `2^(S(n)−log₂ n!) ∈ [1, 3.4]` for `n ≤ 22`, so leaf-cones are tiny and single-order isolation looks feasible, but I did **not** prove it.

So the all-n question is genuinely open. **No proof, verification, class separation, or S(n) value is claimed.** General-poset hardness and certificate *soundness* (Σ₂ᵖ for the subclass) are kept strictly separate from *completeness* (unrestricted membership), as required.

## Novelty check
Searched all 585 fronts: **zero** coverage of hitting sets, teaching dimension, universal-quantifier elimination, minimal `v`, or transitive-closure context width. Both proposed fronts are non-duplicate by ID and by question fingerprint.

## Deliverable
Wrote only `frontier-candidates.json` (validated against the exact `research_frontier.py` schema and duplicate checks): two new all-n falsifiable fronts — one on the universal-order hitting set / NP-vs-Σ₂ᵖ collapse, one on the minimal FO(TC) variable bound for optimal programs. Git remains clean at `f89f6d0` (only the requested JSON is untracked); no Lean, commits, CI, ledger, or board changes.
