# antonina-VcykfpPyCqWJVlstW6MxvL-stifle

Session: ses_dfbf9686fffeyivHvNZ7xulrm0
Workspace: /home/lubko/soring-fronts/excess-band-diagonal-decision-alln
Created: 1795363870693; updated: 1795364775101

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_2040e0846001GOn8RA0SUcTfe6)

I'll start by carefully inspecting the current state — Git branch/status, durable records, and the key documents — before doing anything, especially given the recovery note about possible prior side effects.

## Output 28 (msg_2040e25d90019o2FjGSAwoT5Ug)

We're on `billy-dev`, worktree clean. Let me read the key documents and check for board #301 and any prior side effects.

## Output 51 (msg_2040e3688001n6BLz9Wbxgk7fn)

Let me check board #301 (via the digest, not the full board) and the durable ledger to detect any prior side effects from the interrupted turn.

## Output 88 (msg_2040ec20a001rKbC2S1VpINhBV)

I've confirmed: we're on `billy-dev`, worktree clean, the ledger shows this front `running` with no finding, and board #301 has **zero** posts about BAND/diagonal bands — so no prior side effects to duplicate. Let me dig into the relevant board results and literature before attacking the math.

## Output 139 (msg_2041152a2001WhE7QgQrPV2SNz)

Let me check the primary literature on the complexity of computing exact sorting numbers and Fredman's bounds — this matters for what can be disproved.

## Output 180 (msg_2041242ad0011AiXWnRaEQ3X5s)

I've confirmed the key facts. Let me check the board-posting mechanism (without posting yet) and verify the exact reduction arithmetic once more.

## Output 218 (msg_20412c65d0010IvAOTtjq6OqJA)

I have a precise, checkable finding. Let me write it up and post exactly once to board #301 (no repo/Lean/ledger changes), redirecting `--json` to a file as required.

## Output 251 (msg_204137f92001NJRc0sAzdxP5A5)

Done. Here's the report.

## Recovery / side-effect audit (first)
- `billy-dev`, worktree clean at `6a96398` (reflog = clone only); no commits, Lean, tests, or repo edits.
- Ledger front `excess-band-diagonal-decision-alln`: `running`, `finding=null`.
- Board #301 had **zero** posts mentioning `BAND`/`band decider`/`unary diagonal`/`excess band` before I acted.
- I made exactly **one** external write: a #301 comment at `16:24:59Z` (verified: 1 unique match). JSON output redirected to `/tmp/opencode/band_post_result.json`. Ledger left untouched (the keeper owns that transition).

## Mathematical finding

Let `C(n)=⌈log₂ n!⌉`, `D(n)=S(n)−C(n) ∈ [0, n(n−1)/2−C(n)] < n²/2`, and `BAND_c={1ⁿ : D(n)≤c}`. `C(n)` is poly-time computable from unary `n`; `S(n)≥C(n)` (information) and `S(n)≤n(n−1)/2` (kernel) give cheap reject/accept tests.

**1. [deduction, rigorous] The FRONT's *uniform* question is not a new, easier frontier — it is exactly the central open problem.** Let `B={(1ⁿ, bin c) : D(n)≤c}`. Then
`B ∈ P ⟺ SORT-BOUND-U ∈ P`.

- `(⇒)` On `(1ⁿ,1ᵏ)`: reject if `k<n·(n−1)/2` is false or `k<C(n)`; otherwise set `c=k−C(n) ≤ n²/2` and make **one** query to `B`. (The FRONT's scan `c=0..n(n−1)/2` is valid but unnecessary.)
- `(⇐)` On `(1ⁿ,bin c)`: if `c>n(n−1)/2−C(n)` accept; else form `k=C(n)+c` in unary and query `SORT-BOUND-U(1ⁿ#1ᵏ)`.

So "one uniform poly(n,c) band decider exists" holds **iff** `S_unary ∈ FP`. For a *fixed* `c` with a separate algorithm per `c` (nonuniform in `c`), `BAND_c ∈ P` is strictly weaker and does **not** imply `S ∈ FP` — the FRONT's careful phrasing matters.

**2. [conditional, rigorous] The FALSIFIER's `BAND_1 ≡_T S(n)` arm is a conjecture, not a deduction.** Exact data for `n≤22` (OEIS A036604): `D=0` on `{1..11,20,21}`, `D=1` on `{12..19,22}` — so all known `n` lie in `BAND_1`. Sergeev (ECCC TR20-096) proves only the **upper** bound `S(n)≤log₂(n!)+o(n)`, which does **not** refute `D(n)≤1` for all `n`. Under that unrefuted hypothesis, `BAND_1` is trivial (∈FP), while `S(n)=C(n)+[n∉BAND_0]` gives `BAND_0 ≡_T S(n)` — so `BAND_1` is **not** Turing-equivalent to `S(n)` unless `S ∈ FP`. Precisely: `BAND_1 ≡_T S(n)` implies (`D` not bounded by 1) **or** (`S ∈ FP`); an unconditional refutation needs `S ∉ FP`, which is out of scope (would give `P≠PSPACE`).

## Serious disproof attempt — exact obstruction
I tried to build a poly-time Turing reduction from `S(n)` to a `BAND_1` oracle. Every query yields only the single bit `D(m)≤1` for `m≤poly(n)`. When `D(n)≥2` the "no" answer says nothing about the *value* `D(n)` (up to `Θ(n²)`), and no structural relation is known between the level set `{m : D(m)≤1}` and the values `D(n)` — in the bounded-`D` scenario that set is constant. **No reduction found; the equivalence remains unproved and appears false in the `D≤1` scenario.**

**Model fidelity:** general-poset hardness and `#P`-hard counting of `e(P)` do not transfer to the fixed antichain root without a reduction; certificate *soundness* (checking a supplied tree) is not *completeness* (existence of a short tree). Sparsity/Mahaney is a many-one barrier and does not rule out a tally Turing-oracle equivalence; `P/poly` blocks circuits, not Turing reductions.

## Honest limits
Neither falsifier horn was achieved. No improved uniform bound/algorithm for `S(n)`, no separation, no class membership, no counterexample. The front is unresolved but the gap is now precise: **uniform band decider ⟺ `SORT-BOUND-U ∈ P`; and the `BAND_1`-equivalence arm requires first resolving both the boundedness of `D` and whether `S ∈ FP`.** No repository, Lean, test, or ledger changes were made — a clean worktree is the normal outcome here.

## Output 263 (msg_20413bb6b001txBobeFY2fu6UT)

I'll re-verify the durable state read-only before doing anything — no new posts, commits, or edits.

## Output 291 (msg_2041447eb001Fa6WrxxPIaVPMv)

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
