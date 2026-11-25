# minimax-witness-family-size-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

8hKKDwUVLnTrXjKzFSxGgT-english

## exit_state

clearexit

## question

For every n, is there a set H_n of total orders on [n] of size 2^{o(n log n)} (ideally poly(n)) such that the minimum height of an adaptive pairwise comparison decision tree correctly sorting every order of H_n equals S(n), so that H_n alone forces the full worst-case comparison number, or must every such S(n)-complete witness family have size 2^{Omega(n log n)} (a constant fraction of all n! orders)?

## basis

Independent from-scratch minimax DP (this curation pass, experiment not proof): h(S_n)=S(n) computed for n=2,3,4, with minimum witness-family sizes 5 (n=3), 12 (n=4, strictly below the trivial 2^{S-1}+1=17 cardinality bound), and <=60 (n=5 sampled), i.e. roughly n!/2; plus 2026-11-20 #301 hitting-set impossibility for FO(TC) programs at k>=S(n) and docs/problem.md open upper-bound frontier.

## falsifier

Either exhibit an all-n family H_n of size 2^{O(n)} with minimum sorting-tree height exactly S(n), or prove that for some c>0 and all large n every H_n with |H_n| < c*n! is sortable within S(n)-1 comparisons, so no subexponential witness family exists.

## implication

A subexponential S(n)-complete witness family would allow a faster exact evaluator for S_unary by taking the minimax only over H_n instead of all n! orders, directly targeting the open shrink-the-exponent goal for SORT-BOUND-U; a matching 2^{Omega(n log n)} lower bound would be a new barrier showing the full order set is essentially necessary.

## finding_unverified

udied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, the relevant #301 posts (including the 03:44Z FO(TC) hitting-set barrier), then built a **from-scratch minimax solver** for `h(H)` (verified `h(S_n)=1,3,5,7` for `n=2..5`) and attacked the witness-family question.

## Mathematical finding (not a theorem completion)

For `τ(n) = min{|H| : h(H) = S(n)}`:

- **Rigorous lower bound** (`h(H) ≤ |H|−1`): any two orders differ at some pair; comparing it leaves both sides nonempty, induct on the larger side. Hence `τ(n) ≥ S(n)+1 = Ω(n log n)`. The bound is attained by "comb" families (≈`n` orders forcing `h≈n`), so it alone does not settle the question.
- **One-sided reformulation**: `τ(n) ≥` minimum hitting set of `{D(T)}`, where `D(T)` is the set of orders at depth exactly `S(n)` in an optimal sorter. The converse needs an extension lemma I could not prove.
- **The exact obstruction**: the whole front reduces to whether the defect `D(n)=max_H(h(H)−log₂|H|)` is `O(n)`. If yes, `τ(n) ≥ 2^{S(n)−O(n)} = 2^{Ω(n log n)}` (no subexponential witness family); a `2^{O(n)}` witness family would require defect `Θ(n log n)`, for which no construction exists.

## Concrete failed approach

I tried to prove `D(n)=O(n)` via per-step balanced splits / potential functions. This fails structurally: comb families have min-side 1 at every pair. The only general structural fact I could establish is that for `|H|≥4` the majority tournament is transitive (a 3-cycle forces 3 distinct exception orders, contradicted by a 4th), bounding pure-comb families but saying nothing about the balanced-split regime needed for `h=S(n)`. Both horns remain open; I did not prove or disprove either.

## Consistency and honesty

- My computation (τ(3)=5, τ(4)=12 with an explicit witness, τ(5)≤49) matches the Executive's independent exhaustive check posted at 05:47Z (τ(3)=5, τ(4)=12 exhaustive; n=4 strictly below the pigeonhole bound 17).
- I explicitly distinguished this from the FO(TC) hitting-set barrier (different statement; leaf-corruption doesn't apply to a minimax tree chosen after `H`) and from general-poset hardness (their large defect comes with exponentially large `|H|`, so it doesn't transfer).
- Complexity caveat recorded: even an existing subexponential witness family helps exact `S_unary` evaluation only if uniformly constructible.

No new `S(n)` value, class separation, Lean file, or repository change. `S(n)` and `SORT-BOUND-U` remain open.
Recovery inspection (no actions repeated):

- **Git / repo state:** `billy-dev...origin/billy-dev`, HEAD `6a96398d937d20977a91b9afa8619cb27feab269`, working tree clean (`git status --short --branch` empty except branch). No commits, PRs, Lean files, or other repository changes were made.
- **Durable external side effect (board):** #301 already contains the front report `SoringP1 frontier: minimax-witness-family-size-alln` at **2026-11-20T05:56:36.427Z** (confirmed via `board_digest.py --contains "minimax-witness-family-size-alln"`). A 05:47Z Executive commissioning/verification note and the 05:56Z post are both present; I did **not** repost.
- **Local/scratch artifacts:** `/tmp/opencode/witness/` contains the from-scratch solver/scripts and `post_result.json` from that pass only; no uncertain external actions remain.

**Status:** the prior turn’s work is complete and all intended effects already occurred. No unfinished work to continue and no external actions duplicated. Uncertain effects: none identified.

## Other metadata

```json
{
  "finished_at": 1795154268.5186772,
  "started_at": 1795153047.3226128
}
```
