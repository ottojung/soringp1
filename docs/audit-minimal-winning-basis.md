# Independent audit — "Minimal winning-state bases can be superpolynomial"

Auditor: Viche Executive (direct referee audit; managed appointments failed with backend quota errors, so this audit was executed directly).
Date: 2026-11-06T23:20Z.
Subject: `/home/lubko/soring-fronts/minimal-winning-basis-20261106/docs/research-minimal-winning-basis.md` (read-only; not modified by this audit).
Companion executable checks: `scripts/minimal_winning_basis.py`, `tests/test_minimal_winning_basis.py` (both in the author worktree).

## Verdict

**VALID as labelled, with one strengthened consequence and one phrasing caveat.**

Every quantified step of the deduction was checked and passes. The
computational claims reproduce: `python3 -m unittest
tests.test_minimal_winning_basis` in the author worktree → `OK` (2 tests:
known antichain counts for `n=4,t=1` → 12 and `n=8,t=2` → 840; equality-size
antichain property for small families), and the script independently prints
the same counts. These checks were executed by the auditor, not merely cited
from the note.

## Step-by-step verification

1. **Counting** (`[deduction]`): `choose(n,2t)·(2t)!/(2^t t!)·2^t =
   n!/((n-2t)! t!)`. Partition count of the selected `2t` labelled elements
   into `t` unordered pairs is `(2t)!/(2^t t!)`; each pair orients in two
   ways. Every choice yields a distinct labelled poset (the chains identify
   the matching). Verified numerically: `n=4,t=1` gives 12, `n=8,t=2` gives
   840, both reproduced by the checked script.
2. **Exactly-`t` reachability** (`[deduction]`): from the antichain, the `t`
   disjoint pairs are initially incomparable; running one comparison per pair
   is legal and performs exactly `t` comparisons. Each comparison makes
   exactly one unordered pair comparable, so every `t`-comparison history has
   at least `t` comparable unordered pairs. The constructed `P` has exactly
   `t`. Hence any `Q` whose relation set is contained in `P`'s relation set
   has at most `t` comparable pairs, and therefore exactly them, so `Q=P`.
   Inclusion-minimality inside `W[n,t,r]` (when a member is winning)
   follows. The note is right that pairwise incomparability alone would NOT
   give this; the exact `t`-relation count is the essential ingredient.
3. **Linear extensions** (`[deduction]`): independent 2-chains multiply the
   extension count by 2 each, so `e(P) = n!/2^t`.
4. **Fredman premise** (`[literature]`): the theorem needed is
   `F(P) <= log2 e(P) + c n` uniformly in `P` for an absolute constant `c`.
   **Verified from an accessible authoritative source**: M. L. Fredman, *How
   good is the information theory bound in sorting?*, Theor. Comput. Sci.
   1(4) (1976) 355–361, DOI 10.1016/0304-3975(76)90078-5, as restated in
   Cardinal, Fiorini, Joret, Jungers, Munro, *Sorting under Partial
   Information (without the Ellipsoid Algorithm)*, STOC 2010 /
   arXiv:0911.0086v3, "Previous Results" paragraph (full text inspected by
   the auditor): *"He showed that there exists an algorithm that performs
   `log e(P) + 2n` additional comparisons between elements of V."*
   The additive constant is therefore **explicit**, `c = 2` under the natural
   reading (total = `log2 e(P) + 2n`), rather than merely existential.
   Caution: the word "additional" is most naturally read as the excess over
   the `log e(P)` lower bound, i.e. total = `log2 e(P) + 2n`; the primary
   full text (paywalled at Elsevier for this environment) should be
   re-checked before any formal use of the numerical value of `c`.
5. **Budget inequality** (`[deduction]`): with `c = 2`,
   `F(P) <= log2(n!) - t + 2n`. Since `t = floor(n/4)`, the requirement
   `F(P) <= H(n) - t` reduces to `n·ceil(log2(n+1)) >= 2n`, which holds for
   every `n >= 2` (in fact `>= 3n` for `n >= 3`). So the note's "for all
   sufficiently large n" hedge can realistically be replaced by
   **`n >= 2`** once the explicit reading of Fredman's constant is confirmed
   against the primary text.
6. **Validity of `H` as a sorting upper bound** (`[deduction]`): mergesort
   uses at most `n·ceil(log2 n)` comparisons, and
   `H(n) >= n·ceil(log2(n+1)) >= n·ceil(log2(n))`. Correct.
7. **Asymptotic count**: with `t = floor(n/4)`,
   `log2(n!/((n-2t)! t!)) = log2(n!/((n/2)!(n/4)!)) = (1/4 + o(1)) n log2 n`
   by Stirling. Correct.

## Strengthening permitted by the verified premise

With the cited secondary statement total = `log2 e(P) + 2n`, the note's
"Stronger existential-slack corollary" no longer needs its existential `D`:
the additive slack can be taken **explicitly `2n`** (budget
`H_2(n) = ceil(log2(n!)) + 2n`), provided `H_2` is separately validated as a
sorting upper bound for all `n` (merge-sort excess over
`ceil(log2(n!))` must be `<= 2n`; plausible since
`log2(n!) >= n(log2 n - log2 e)` with `log2 e ≈ 1.44`, but small `n` should
be tabulated before asserting). The author matter for a v2 of their note,
not a change this audit makes.

## Remaining limits (unchanged, correctly labelled by the note)

- The result covers only **relation-inclusion dominance bases** at fixed
  explicit budgets. It implies nothing for arbitrary exact evaluators,
  symbolic representations, or the exact-optimal budget `S(n)`
  (whose surplus over `ceil(log2(n!))` is `o(n)` by Sergeev, so the
  superpolynomial-basis argument cannot execute at `S(n)`).
- The all-`n` conclusion rests on the literature theorem, which above is
  verified through a peer-reviewed secondary citation of the primary; the
  primary PDF was not directly retrievable (Elsevier paywall) in this
  environment. This is adequate for research status `[literature]`-verified
  but should be flagged for final-archive completeness.

## Execution notes

- Author worktree untouched; no source or note file modified.
- Management note: managed appointments for this audit
  (`jYExL5LXiNvRT453Qeb3Gl-pleased`, `Bal16zUzmqFyytNdwQbnCY-them`) both
  failed with
  backend quota errors without output; this document is the first
  successful audit output of this front.
