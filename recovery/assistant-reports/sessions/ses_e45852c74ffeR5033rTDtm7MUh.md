# antonina-igFfBo27iyyZwaPj04TKeV-singing

Session: ses_e45852c74ffeR5033rTDtm7MUh
Workspace: /home/lubko/soring-fronts/eventual-information-nontightness
Created: 1794129974452; updated: 1794130997574

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 352 (msg_1ba88b863001Wfi1mqrMv7DIMx)

Worked on `billy-dev`; worktree remains clean (no repository or Lean changes). Board #301 updated; durable note at `~/.local/state/soringp1/information-tightness-20261108.md`.

## Mathematical findings

**1. Ford–Johnson is never information-tight beyond n = 21 — for all n.**
Let `F(n)` be the merge-insertion comparison count and `C(n) = ceil(log2 n!)`.

- `F(n) > C(n)` for every `n >= 23`.
- The complete set of `n >= 23` with `F(n) = C(n)+1` is exactly `{23, 24, 40, 41, 42, 43}`.
- For `n >= 122`, `F(n) >= C(n)+3`.

This upgrades the earlier numerical check to `2·10^6` into an all-n theorem. The proof uses the exact formula
`F(n) = M n − (2^{M+2} − 4 − floor(3M/2))/3`, `M = ceil(log2(3n/4))`, an exact check for `23 <= n <= 121`, and a Stirling/concavity argument giving `F(n) − log2(n!) >= c0·n − O(1)` with `c0 = log2 3 − 3 + 1/ln 2 ≈ 0.0276575`.

**2. A linear-depth barrier for leaf-count lookahead at the antichain.**
For `L_0(P)=ceil(log2 e(P))` and the t-ply minimax relaxation `L_t` scored by extension counts, for every `n` and every `0 <= t <= floor(n/2)`:

    L_t(A_n) = C(n).

So the natural sound extension-count lower-bound hierarchy is exactly the information bound at the antichain for linear lookahead depth. If `S(n) > C(n)`, convergence of this hierarchy requires depth `> n/2`. This is a structural incompleteness result for that family of certificates, not a statement about all methods.

## Falsifier attempt

No explicit `n >= 23` with a height-`C(n)` strategy was found.

- The first possible cases are `n = 23, 24`, where Ford–Johnson is only one comparison above `C(n)`.
- Peczarski (2007) excludes beating Ford–Johnson by any split-and-merge algorithm for `n < 47`; this covers all six one-gap sizes but not arbitrary algorithms.
- An exhaustive height-75 search at `n = 23` is far beyond the state sizes of Wells–Peczarski–Stober–Weiss (`n = 18` already required days and large memory); it was not attempted.

## Soundness vs completeness

The Wells–Peczarski efficiency prune is sound: `e(P) > 2^r` rules out sorting in `r` comparisons, and an empty forward layer certifies non-tightness. It is not complete: one-sided search suffices at `n = 12` but not at `n = 13,14` (Stober–Weiss). The `L_t` theorem above gives a stronger structural version of this gap at the antichain.

## Honest limits

The front remains open. This proves neither `S(n) > C(n)` nor `S(n) = C(n)` for any `n >= 23`, and does not determine `S(23)` or `S(24)`. Theorem 1 concerns the Ford–Johnson upper bound, not `S(n)`; Manacher’s `F(n) > S(n)` infinitely often does not imply `S(n) > C(n)`. Theorem 2 rules out a natural lower-bound family, not all possible proofs or constructions.

## Output 428 (msg_1ba8a5763001CbSSAQqu4Ai8Ju)

Recovery inspection completed. I did **not** repeat the research prompt or any external action.

**Effects verified as already completed**
- Board #301 has exactly **one** matching post: `SoringP1 frontier: information-tightness-all-n`, created `2026-11-08T09:41:14Z` (3,849 body chars). No duplicate.
- Durable note exists: `~/.local/state/soringp1/information-tightness-20261108.md` (7,371 bytes).
- Temp artifacts from the prior turn exist under `/tmp/opencode/` (`soring301-post.md`, `soring301-comment.json`); they are local scratch files.

**Repository state**
- Host: `billy-dev`.
- Worktree is clean: `git status --short` produced no output.
- HEAD remains `6a96398`; no commits were created.

**Conclusion**
The prior turn's work was completed exactly once. There is no unfinished external action to resume, and I have not posted again, committed, or modified the repository. No effect remains uncertain.
