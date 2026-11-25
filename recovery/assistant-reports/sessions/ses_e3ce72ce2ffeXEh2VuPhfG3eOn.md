# antonina-PVDw5nVW1Gqy9v204NjImd-more

Session: ses_e3ce72ce2ffeXEh2VuPhfG3eOn
Workspace: /home/lubko/soring-fronts/upper-inequality-structural
Created: 1794274546583; updated: 1794277255262

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 16 (msg_1c318e8db001Lm94K2ixmrTULx)

I'll start by inspecting what already happened (git state, scratch, board) before doing any new work.

## Output 113 (msg_1c31a12e4001yA1h1x7WOEfWWl)

No prior post from this front exists; git is clean and `/tmp/opencode/upineq` is absent, so this is a fresh start. Now I'll set up exact computation.

## Output 146 (msg_1c31e6617001EWZuCvPT1IZ2CS)

The hypothetical tight family is `C_a ⊔ C_b` (merging two sorted lists). Let me compute its exact minimax with a dedicated interval-of-lattice-paths DP, and cross-check on brute force.

## Output 310 (msg_1c329c8a90011i5Lb1mU4iMBcp)

The clean proof route is an induction needing a "good comparison" lemma. I'll test that lemma exactly over all small posets.

## Output 361 (msg_1c32d8d3a001y4I9rFa2qaeyjw)

The induction route needs cover monotonicity, which can fail. A more promising decisive family is multiway merge: `(3,3,3)` is near the threshold. I'll compute it exactly with chain-permutation symmetry.

## Output 474 (msg_1c333a5cc00135rDIfaxgbOBa3)

I'll run an exact symmetry-reduced solver for the multiway-merge family, starting with validation sizes.

## Output 880 (msg_1c341dd9f001LGj6kIUmLArp9f)

Recovery check first: the worktree was clean at `6a96398`, `/tmp/opencode/upineq` did not exist, and issue #301 had **no prior `upper-inequality-structural` comment**. So the interrupted turn had produced no external effect; I did the work fresh and posted exactly once.

**Outcome (acceptance case (c): honest precise blocker — no proof, no counterexample).**

- **Proof attempt.** I reduced a proof of `(U)` to an explicit induction condition using `D = covers + psi`. Two facts are easy: adding a relation creates one new cover and may destroy old ones, so `covers` increases by at most 1; and `psi` never increases under adding a relation. The induction then requires a “D-balanced comparison lemma” (GC): a globally balanced pair whose majority branch does not increase `D`. Kahn–Saks' `3/11`–`8/11` pair is **not enough** for that majority branch. GC holds for all 399 non-total posets of size ≤6, but I cannot prove it in general. That is the precise missing step.

- **New finite evidence beyond size 9.** A rigorous infinite-parameter family: `k` disjoint 2-chains plus `r` isolates. Ford–Johnson can use the `k` given pairs as its initial comparisons, giving `F ≤ H(2k+r) − k`; this beats the `(U)` line for all `0≤k,r≤100`. In particular the `n=10` five-pair near-antichain has `F=17` exactly by the two-sided FJ/information sandwich, with a wide `(U)` margin. I also checked that the newly reported unbounded prime-excess gluing family does **not** threaten `(U)`: its covers grow exponentially while excess grows linearly.

- **Task 3.** `psi=mM` whenever `min(m,M)=1`, and `psi=m+M` when `m,M≥2`; so the strengthening is active exactly when `(m−1)(M−1)>1`. The extremal block `Merge(2,4)` has `(m,M)=(2,2)`, so any admissible replacement must keep `phi(2,2)≥4`.

The single post is on **#301 at 02:20Z** under `SoringP1 frontier: upper-inequality-structural`. No repo, Lean, PR, or scratch-directory changes outside `/tmp/opencode/upineq`; the worktree remains clean.

## Output 892 (msg_1c3421087001fG4x7dewTvOb8k)

Recovering — verifying existing effects before acting.

## Output 907 (msg_1c34220ff001Wdpz4aK5xJgz39)

Recovery check complete. No further action taken; no duplicate post.

- Worktree: clean detached at `6a96398`, `git status --short` empty.
- Scratch `/tmp/opencode/upineq/` exists with prior turn's scripts and `post.md`.
- Board #301 already contains the single `SoringP1 frontier: upper-inequality-structural` post at `2026-11-10T02:20:18.276Z` (acceptance case (c): `(U)` open, GC blocker, matching-plus-isolates family, `F=17` five-pair value).
- No commits, no Lean/PR changes, no pending solver processes found.

All effects from the interrupted prompt already happened. Nothing unfinished; posting again would duplicate.
