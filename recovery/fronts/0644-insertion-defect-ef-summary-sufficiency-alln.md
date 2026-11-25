# insertion-defect-ef-summary-sufficiency-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

znXQTP5RiFXZOmsexRw6ud-neuralgic

## exit_state

clearexit

## question

For every b >= 1 and every pair of b-element posets B and B' with the same linear-extension count and the same exact minimax value, e(B)=e(B') and F(B)=F(B'), must their one-key disjoint-union insertion defects delta(A_1,B)=F(B disjoint-union A_1)-F(B) also be equal for all n, or does some b admit an (e,F)-collision with different insertion cost?

## basis

Newest board #301 12:09Z reports zero same-(b,e,F) splits at b=4,5 and that the information gap is not a predictor; my independent scratch minimax (not a proof), validated on S(n)=0,0,1,3,5,7,10, found at b=5 exactly 24 (e,F) classes with 4230 posets in collided classes and zero defect splits; ledger has equal-extensions-equal-height (e alone, refuted) and defect-a1-universal-floor (a lower floor), neither asking (e,F) sufficiency.

## falsifier

Find two b-element posets with identical (e,F) but different exact one-key insertion defect, witnessed by an independent minimax computation and a matching upper strategy and lower bound; an extensible family would refute the (e,F)-summary claim for all larger b.

## implication

If the summary suffices, insertion cost is a function of three numbers and a compact exact evaluator becomes plausible; a collision shows any e- or (e,F)-indexed compression is sound but incomplete for exact unary S(n).

## finding_unverified

---|---|---|---|---|---|
| `B_short` | `A₁ ⊔ C₂ ⊔ C₃` (isolated key + 2-chain + 3-chain) | `(0,8,48,0,32,0)` | 60 | 7 | **9** | **2** |
| `B_long` | `C₂ ⊔ K₂,₂` (2-chain + "2 minima below 2 maxima") | `(4,24,0,0,0,24)` | 60 | 7 | **10** | **3** |

Here `e(B⊔A₁) = 420`, `⌈log₂ 420⌉ = 9`, `c = ⌈log₂ 7⌉ = 3`. So `B_short⊔A₁` is information-tight (`δ=2=c−1`), while `B_long⊔A₁` acquires one unit of excess (`δ=3=c`).

### Verification (three independent methods, scratch only)

1. **From-scratch transitive-closure minimax**, validated first on `S(n)=0,0,1,3,5,7,10` and `F(C_b)=0`.
2. **`e=60` two ways**: subset DP *and* brute force over all `6! = 720` permutations.
3. **Structurally independent extension-set minimax** (surviving-linear-extension sets, no transitive closure): `F=7` for both, `F(B⊔A₁)=9` vs `10`.
4. **Explicit certificates**: a height-9 tree with 420 singleton leaves for `B_short⊔A₁` with height-8 *infeasible*; a height-10 tree with 420 singleton leaves for `B_long⊔A₁` with height-9 *infeasible* (budget DP).

An **exhaustive census of all 318 iso classes at b=6** (three independent runs agreeing) finds exactly two `(e,F)` splits — `(60,7)` and `(120,8)` — both with `δ∈{2,3}` and **all split members information-excess**. This is precisely why prior tight-host searches at b=4,5 (which I reproduce: 24 `(e,F)` classes, zero splits) missed it. Ordinal-summing each witness with a 4-chain gives b=10 posets still with `(e,F)=(60,7)` but `δ=3` vs `4`, so the collision is not isolated to b=6.

### Complexity implication (and its limit)

`δ` is not a function of `(e,F)` nor of `(b,e,F)`. Hence any state compression that records only `(e,F)` is **sound as a bound index but incomplete for exact insertion cost** — it cannot underwrite an exact unary `S(n)` evaluator via `F(A_a⊔A_b) ≥ F(A_a)+F(A_b)+min(a,b)+1`. This is a method-family soundness/completeness point, **not** a new `S(n)` bound or a complexity-class separation (`SORT-BOUND-U` is sparse and in PSPACE; general-poset minimax does not transfer to the antichain root without a reduction).

### Honest limits

No all-`n` theorem, no faster evaluator, no P/NP/PSPACE consequence. The result is one fully certified counterexample plus an exhaustive b=6 census and one b=10 extension; a clean infinite family is **not** established. `S(n)` and `SORT-BOUND-U` remain open.

Reported once to board #301; worktree clean at `6a96398` on `billy-dev`, no Lean/repository changes.
No unfinished work to continue.

I inspected the durable state:

- **Board #301**: exactly **1** post authored `SoringP1 researcher: insertion-defect-ef-summary-sufficiency-alln` containing the falsifier result (`total matching posts: 1`). No duplicate post.
- **Git**: `/home/lubko/soring-fronts/insertion-defect-ef-summary-sufficiency-alln` is clean at `6a96398` on `billy-dev...origin/billy-dev` (`git status --short --branch` empty). No commits, no repo files changed.
- **Scratch only**: computations live under `/tmp/opencode/efsplit/` (not a repository side effect). `search7.py` seen in `/tmp/opencode/p2hostscratch` belonged to another cwd/process, not this front’s claimed result.
- **External effects**: only the single board comment is confirmed. Nothing uncertain.

The result stands as reported: the `(e,F)`-summary sufficiency claim is **refuted** at `b=6` by certified `(e,F)=(60,7)` witnesses with `δ=2` vs `3` (and a second `(120,8)` split), independently verified and exhaustively censused; `S(n)`/`SORT-BOUND-U` remain open.

## Other metadata

```json
{
  "finished_at": 1795269866.7624269,
  "started_at": 1795267974.7596555
}
```
