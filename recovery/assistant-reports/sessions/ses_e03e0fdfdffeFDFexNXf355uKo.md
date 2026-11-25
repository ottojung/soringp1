# antonina-Qqj0KfPn3n7ERx9HdjO1RY-opportune

Session: ses_e03e0fdfdffeFDFexNXf355uKo
Workspace: /home/lubko/soring-fronts/excess-at-most-one-alln
Created: 1795231253015; updated: 1795234345718

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fc1f0250001rYU75Jww78pH8G)

I'll start by reading the context documents as instructed.

## Output 55 (msg_1fc1f2183001T890laA8eVZvr2)

Board #301 is fetched via the local `antonina` CLI. Let me read the board pages and the other context files.

## Output 87 (msg_1fc1f99ba0016xKCQQG6eA6GYX)

The board context is clear. Now let me gather the remaining context: compute C(n), check for Ford–Johnson code, look at the frontier definition, and read the reusable search machinery.

## Output 106 (msg_1fc217e71001HRg9Ser57mlE3G)

C(25)=84 confirmed. Now let me check the ledger for this front, read the FJ implementation in `upper_witness.py`, and the budgeted DFS machinery.

## Output 121 (msg_1fc21928e001S30oUzBFXE5KyI)

Let me examine the ledger for the excess-at-most-one front's full history, and check prior scratch in /tmp/opencode.

## Output 136 (msg_1fc2248b3001jHlTuLsxbNDP6J)

The first attempt's scratch is in `/tmp/opencode`. Let me scan it for prior work on n=25 / minimax to design a genuinely different method.

## Output 164 (msg_1fc22ca590011A98wRa2JLIEy4)

The first attempt used the full poset enumeration DP. My retry will use different methods. Let me check machine resources, then build the toolkit in /tmp/opencode.

## Output 175 (msg_1fc25107a0012sjBD2LUaxRJh6)

4 cores, 15GB RAM, numpy available. Now I'll build the research toolkit in `/tmp/opencode/excess25/`:

- **Method A**: memoized decision DP `feasible(P, h)` — decides `S(n) ≤ h` directly (different from the first attempt's full poset enumeration).
- **Method B**: Wells admissible forward search (canonical set-based search).
- **Method C**: heuristic tree search (witness families).

First, the poset toolkit with an exact extension-count DP.

## Output 211 (msg_1fc27f20a0012rkZgrSVcFQcZY)

Bug: `((sel >> x) & 1)` is an int array, not boolean, so `sel[cond]` uses integer indexing. Fix:

## Output 229 (msg_1fc2821d8001pnISaM4J05sg0k)

`ext_count` validated. Now the Method A decision DP:

## Output 848 (msg_1fc4e1619001YySNCXdcHawF8O)

## Honest report — Front `excess-at-most-one-alln` (retry, 2026-11-21)

**Outcome: OBSTRUCTION written and posted to board #301 (no counterexample, no window advanced).**

### What I attempted
I retried the front as an independent researcher, pushing on the n=25 window (FJ(25)=86=C(25)+2, C(25)=84, so S(25)∈{84,85,86}; a certified S(25)≥86 would falsify the front). I built from-scratch tools in `/tmp/opencode/excess25/` (no repo changes) and validated them first:

- **`ext_count`** (2ⁿ-subset DP for linear extensions): matches brute force for n≤7 and n! for n≤18.
- **Decision DP** `feasible(P,h)` (memoized minimax decision, sound & complete: D(Aₙ,h) ⇔ S(n)≤h): matches `evaluate.py` S(n) for n=2..6 (feasible(S−1)=False, feasible(S)=True).
- **Wells admissible forward search**: validated on n=5,h=7 (nonempty through level 7, S(5)=7=C(5)).

Methods tried on n=25,h=85 (different methods / witness families):
- **Method A** — memoized decision DP, lexicographic pair order.
- **Method C** — decision DP with balanced-pair ordering (most balanced split first) — a different witness family.
- **Method B** — Wells admissible forward search (calibrated on n=12,h=29).

### Measured evidence
- `ext_count` at n=25 costs **29.2s/poset** (antichain) / 11.2s (total). At n=22: 1.33s.
- **Method A**: after 4 min → 10 calls, 5 memo states (~0.04 calls/s ≈ 25s/call). Level 1 alone ≈ 300 pairs × 2 children × 29s ≈ 4.8 h; full depth-85 ≈ 85×4.8h ≈ 17 days even if a height-85 tree exists and ordering is lucky.
- **Method C**: after 90s → 1 call, 2 ecache entries; same bottleneck.
- **Method B**: n=12,h=29 level-2→3 transition took ~12 min (2365 posets, ~156k pairs), confirming exponential frontier growth; at n=25, level 1 alone ~2.4 h.

### Precise obstruction (posted to #301)
To certify the front false at n=25 one must certify **S(25)≥86**, i.e. that no decision tree of height ≤85 sorts 25 distinct keys — equivalently D(A₂₅,85)=False. The only known exact methods (memoized minimax decision DP and Wells admissible forward search) both reduce to enumerating posets on 25 elements with e(P)≤2^(85−depth); each such enumeration requires computing e(P) via a 2²⁵-subset DP costing ~29s/poset, and the frontier at level 2 already exceeds 10⁵ posets (projected from n=12). No polynomial-size certificate or transfer theorem is known that avoids this enumeration. Structural reasons: S(23) itself is open; the winning-frontier barrier (2^(1/4−o(1)) n log² n states at optimum); no succinct certificate known; general-poset excess does not transfer to the antichain root (sortability is not a function of e(P)). Hence the n=25 window resists certified falsification: **the window remains {84, 85, 86}**.

### What did NOT happen
- No counterexample found at any n; no S(n) value determined.
- No window advanced (S(25) still in {84,85,86}).
- No repo/Lean/commit/PR changes (worktree clean at 6a96398).

The deliverable — obstruction with its exact formulation — is posted to board #301 (author tag `excess-at-most-one-alln-retry-20261121`, createdAt 2026-11-21T04:12:10Z). Scratch and measurements are under `/tmp/opencode/excess25/`.
