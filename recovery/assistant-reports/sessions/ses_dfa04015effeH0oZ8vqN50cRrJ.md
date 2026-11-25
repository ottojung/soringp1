# antonina-9xMjEJtKEB5BMvUgaLomq0-halted

Session: ses_dfa04015effeH0oZ8vqN50cRrJ
Workspace: /home/lubko/soring-fronts/curator
Created: 1795396730619; updated: 1795397599076

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_205fc0740001Gjh4KTLuO6kwgm)

I'll start by studying the repository docs, the research board, and the contract. Let me explore first.

## Output 29 (msg_205fd10a80014bQueqZiIxT3jY)

Let me check the host, branches, and pull the board #301 digest.

## Output 44 (msg_205fd8294001lomp189CEl1Stm)

We're on the `billy-dev` host (the required host). Now let me get the full board #301 digest and the literature review.

## Output 76 (msg_205fe1227001Iq1HqN1IF8sWD9)

Let me get the full newest board entry, the ledger state, and the obstruction-next doc referenced by the executive.

## Output 95 (msg_205fed29a001mhepx27sg5K7b5)

Let me get the full newest board entry (with larger excerpts) and properly query the frontier ledger.

## Output 127 (msg_205ff51dd001CTRP3XJ63kV0eT)

The board digest is truncated at 850 chars per message. Let me read the full newest entry, and the key research docs to ground new candidate fronts.

## Output 223 (msg_206091305001ECLipl7130ZidG)

The curator deliverable is complete.

**What I did (on billy-dev, branch main):**
- Read `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-obstruction-next.md`, `docs/research-structural-lower-bounds.md`, `docs/research-sergeev-asymptotic.md`, the newest board #301 (Viche Executive pass 2026-11-23T01:10Z, listing the six freshly dispatched fronts), and the 697-front ledger.
- Studied the primary sources cited (Peczarski, Stober–Weiss, Wells, Mahaney, Ford–Johnson, Knuth, Sergeev, Hanamura–Iwata).
- Attacked the falsifiable all-n claim **“D(n) = S(n) − ⌈log₂ n!⌉ ≤ 2 for all n”** (the gap-2 analogue of the open P1). A small read-only computation (`/tmp/opencode/attack_excess_two.py`) checked n ≤ 22: all D(n) ∈ {0,1}, so no counterexample to D ≤ 2. A structural attempt over certified merge costs found that gap 2 *does* occur for general posets (`Merge(6,10): F = 15 = ⌈log₂ C(16,6)⌉ + 2`), but this does **not** transfer to the antichain root — D(16) = 1 there. Honest obstruction: no method exists to prove F(antichain_n) ≥ C(n)+3 for n ≥ 23 (those values are open); the claim remains unrefuted and unproved.

**Honest limits:**
- n ≥ 23 exact values are open, so falsification of the gap-2 claim is computationally infeasible; the attack is inconclusive, not a theorem.
- Certified merge gaps are general-poset results; they do not imply antichain-root excess (D(16)=1 vs. Merge(6,10) gap 2), so I kept them distinct from the root questions, per the model-fidelity rules.
- Soundness (a 3-probe scheme never false-accepts) is already achievable; **completeness** (deciding the width-2 band without computing D(n)) is the open part — I made that distinction explicit in the third front rather than conflating it with general-poset lower bounds.

**Deliverable:** `/home/lubko/soring-fronts/curator/frontier-candidates.json` — a valid JSON object with 3 genuinely new, non-duplicate fronts:
1. `excess-gap-two-alln` — universal D(n) ≤ 2 bound.
2. `excess-two-realization-alln` — whether gap 2 is ever realized by the antichain for n ≥ 23.
3. `excess-two-soundness-completeness-alln` — whether the width-2 band has a sound *and* complete O(1)-size certifier.

Worktree is otherwise clean (only the requested untracked `frontier-candidates.json`); no Lean, tests, commits, PRs, or board posts were created by this session.
