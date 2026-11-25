# excess-band-diagonal-decision-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

VcykfpPyCqWJVlstW6MxvL-stifle

## exit_state

clearexit

## question

For every fixed constant c >= 0 and all n, is the unary diagonal band language BAND_c = {1^n : S(n) <= ceil(log2(n!)) + c} decidable in time polynomial in n (and c), and if one uniform algorithm decides every band in poly(n,c), does that put S_unary in FP by scanning c up to the explicit polynomial bound n(n-1)/2?

## basis

docs/problem.md records SORT-BOUND-U in P iff S_unary in FP via binary search on k, and kernel-checks S(n) <= n(n-1)/2, supplying a polynomial excess scan; ceil(log2(n!)) is computable in poly time from unary n. Board #301 (2026-11-22) has extensive excess/tightness results (info-tightness-set-complexity, cheap-zone excess, tightness density), but the complexity of the shifted diagonal BAND_c itself is not among the 694 audited ledger IDs.

## falsifier

Either exhibit a uniform poly(n,c) band decider for all c, or prove that deciding BAND_1 is polynomial-time Turing-equivalent to full SORT-BOUND-U / exact S(n) evaluation, so that no constant-excess diagonal is easier than the whole threshold problem on infinitely many input lengths.

## implication

A uniform poly(n,c) band decider would, by the elementary scan c = 0..n(n-1)/2, compute S(n) in polynomial time and hence place SORT-BOUND-U in P; an equivalence result would be a new barrier showing that even a one-bit-excess diagonal keeps the full difficulty of exact evaluation. No separation or class membership is claimed here.

## finding_unverified

ng matters.

**2. [conditional, rigorous] The FALSIFIER's `BAND_1 ≡_T S(n)` arm is a conjecture, not a deduction.** Exact data for `n≤22` (OEIS A036604): `D=0` on `{1..11,20,21}`, `D=1` on `{12..19,22}` — so all known `n` lie in `BAND_1`. Sergeev (ECCC TR20-096) proves only the **upper** bound `S(n)≤log₂(n!)+o(n)`, which does **not** refute `D(n)≤1` for all `n`. Under that unrefuted hypothesis, `BAND_1` is trivial (∈FP), while `S(n)=C(n)+[n∉BAND_0]` gives `BAND_0 ≡_T S(n)` — so `BAND_1` is **not** Turing-equivalent to `S(n)` unless `S ∈ FP`. Precisely: `BAND_1 ≡_T S(n)` implies (`D` not bounded by 1) **or** (`S ∈ FP`); an unconditional refutation needs `S ∉ FP`, which is out of scope (would give `P≠PSPACE`).

## Serious disproof attempt — exact obstruction
I tried to build a poly-time Turing reduction from `S(n)` to a `BAND_1` oracle. Every query yields only the single bit `D(m)≤1` for `m≤poly(n)`. When `D(n)≥2` the "no" answer says nothing about the *value* `D(n)` (up to `Θ(n²)`), and no structural relation is known between the level set `{m : D(m)≤1}` and the values `D(n)` — in the bounded-`D` scenario that set is constant. **No reduction found; the equivalence remains unproved and appears false in the `D≤1` scenario.**

**Model fidelity:** general-poset hardness and `#P`-hard counting of `e(P)` do not transfer to the fixed antichain root without a reduction; certificate *soundness* (checking a supplied tree) is not *completeness* (existence of a short tree). Sparsity/Mahaney is a many-one barrier and does not rule out a tally Turing-oracle equivalence; `P/poly` blocks circuits, not Turing reductions.

## Honest limits
Neither falsifier horn was achieved. No improved uniform bound/algorithm for `S(n)`, no separation, no class membership, no counterexample. The front is unresolved but the gap is now precise: **uniform band decider ⟺ `SORT-BOUND-U ∈ P`; and the `BAND_1`-equivalence arm requires first resolving both the boundedness of `D` and whether `S ∈ FP`.** No repository, Lean, test, or ledger changes were made — a clean worktree is the normal outcome here.
I'll re-verify the durable state read-only before doing anything — no new posts, commits, or edits.
Recovery audit complete — **nothing remains unfinished, and I took no new actions.**

| Check | Result |
|---|---|
| Git worktree | Clean on `billy-dev` at `6a96398`; reflog = clone only; stash empty |
| Repo/Lean/test/CI/ledger changes | None |
| Ledger front `excess-band-diagonal-decision-alln` | `running`, `finding=null` — untouched by me (keeper owns transition) |
| Board #301 posts by this front | **Exactly one** (`16:24:59Z`), confirmed by four distinct filters, each returning 1 match |
| Prior-turn side effects | All accounted for: the single #301 comment was the only external write; JSON redirect saved at `/tmp/opencode/band_post_result.json` |

The previous turn's work is complete:
- One board post reporting the finding: uniform poly(n,c) band decider ⟺ `SORT-BOUND-U ∈ P` (one query at `c = k−C(n)`, no scan needed); `BAND_1 ≡_T S(n)` is an unproved conditional claim; neither falsifier horn achieved; exact obstruction and honest limits stated.
- No duplicated post, commit, purchase, or other external action — I did not re-run the posting command despite the repeated recovery warning.

If anything remains uncertain, it is only the keeper's eventual `running → investigated` ledger transition, which is an operational step outside this session and should not be forced manually.

## Other metadata

```json
{
  "finished_at": 1795364793.3703723,
  "started_at": 1795363870.3352768
}
```
