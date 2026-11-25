# halving-obstruction-infinitude-allr

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cNxP3OS9hattGQHCcbTPgk-bland

## exit_state

clearexit

## question

For every r at least 3, does there exist a finite poset P whose number of linear extensions is exactly 2^r and for which no comparison at the root splits the extension set into two parts of size 2^(r-1) each, forcing the exact minimax continuation cost to exceed log2(e(P))? Determine the smallest element count m(r) of such a poset and whether m(r) grows without bound.

## basis

A counting argument makes exact halving necessary for cost log2(e) whenever e is a power of two; a finite enumeration found e=8, cost-4 posets at n=5 whose root splits are only 5+3 and 2+6, while n=4 had none. The n=5 example is a documented datum in docs/research-n12-nontightness.md; all-r infinitude and m(r) are not recorded in the ledger.

## falsifier

Exhibit some r for which every poset with exactly 2^r linear extensions admits an exact-halving comparison at the root, or determine m(r) exactly and show it is bounded by a constant over all r.

## implication

An infinite family of power-of-two obstruction states would make local looseness a structural feature of the minimax game rather than a sporadic small-case datum, and would bound what evaluators relying on halving-style tight subproblems can assume; it does not by itself give a complexity-class separation for SORT-BOUND-U.

## finding_unverified

 the post landed on the board and confirm the worktree remains clean.
The investigation is complete. The board post landed at 18:45:24Z and the worktree remains clean on `billy-dev`.

## Summary

I attacked the front `halving-obstruction-infinitude-allr` by trying to refute it. **It survived** — I could not disprove it, and I established it positively.

### Mathematical finding

**Necessity (deduction).** If `e(P)=2^r` and the exact minimax cost `F(P)=r`, a height-`r` tree has `2^r` leaves, so it must be complete: the root splits `2^(r−1)/2^(r−1)`. Contrapositive: *no* root halving ⟹ `F(P)>r`. This is a sound lower-bound direction; the existing 18:43Z board post proves the converse (halving exists yet children loose), so root halving is **necessary but not sufficient** for tightness at power-of-two `e`.

**Primitive obstructions (experiment, brute-force extension counts + two independent minimax engines)** — all with `F−log₂e = 1` and no `2^(r−1)+2^(r−1)` split:

| r | e | n | successor masks | F | example root splits |
|---|---|---|---|---|---|
| 3 | 8 | 5 | `(0,0,1,3,7)` | 4 | 3+5, 2+6, 2+6, 3+5 |
| 4 | 16 | 6 | `(16,40,57,32,0,0)` | 5 | 4+12, 10+6, 14+2, …, 9+7 |
| 5 | 32 | 7 | `(16,64,121,113,0,64,0)` | 6 | 11+21, 17+15, …, 18+14 |

Exhaustive enumeration gives **m(3)=5, m(4)=6, m(5)=7** (no obstruction at `n≤4`; 120 at `n=5`; 1440+1440 at `n=6`, none with `r≥5` there).

**Infinite family (deduction + check for k≤3).** Ordinal sum `P⊕Q` multiplies `e`, adds `F`, and takes incomparable pairs from the union — so non-halving is preserved. `R3^{⊕k}` has `e=2^{3k}`, `F=4k`, gap `k→∞`, no halving. Since `{3,4,5}` generates every `r≥3`, **every `r≥3` has an obstruction**, with unbounded minimax gap.

### Honest limits

- **Falsifier's first alternative refuted** (obstructions exist at r=3,4,5); **second impossible**: `m(r) ≥ min{n : n!≥2^r} = Ω(r/log r) → ∞` by trivial counting. Upper bound `m(r) ≤ 5⌈r/3⌉+O(1)`; exact `m(r)` for `r≥6` not determined.
- **Soundness ≠ completeness, and no transfer to S(n).** These are general-poset states. Repo Lemma 1.3 makes every labelled poset reachable in the broad state graph, but optimal-path reachability from the antichain under budget `S(n)` (the separate `antichain-reachable-power2-halving-obstruction` front) is not addressed. Hence **no bound, hardness, or nonmembership for `SORT-BOUND-U` or unary `S(n)` follows** — no complexity-class separation.
- No Lean, repository, test, ledger, commit, or PR changes; scratch work only under `/tmp/opencode`; worktree clean. Process success here is a reported finding, not a proof about `S(n)`.
Inspected (billy-dev, `/home/lubko/soring-fronts/halving-obstruction-infinitude-allr`, branch `billy-dev`, `6a96398`):
- `git status`: clean (no staged/unstaged/untracked files), nothing to do.
- Board #301 (digest, page 1, contains `halving-obstruction-infinitude-allr`): one post, 2026-11-20T18:45:24.195Z by `SoringP1 researcher: halving-obstruction-infinitude-allr` (finding posted). No duplicate post found.
- No commits/PR/ledger/repo/Lean changes were made (and none should be). Scratch analysis was done under `/tmp/opencode` (ephemeral), not repeated.

Effect status: the requested external side effect (one board comment) **already happened once** (verified). No unfinished work remains from the prior interrupted prompt; nothing else to continue or to duplicate.

If anything else in that prior turn felt unfinished in your view, tell me what and I’ll address it directly.

## Other metadata

```json
{
  "finished_at": 1795200392.341649,
  "started_at": 1795199572.1961472
}
```
