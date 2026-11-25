# t4-uniform-tightness-threshold

## status

investigated

## origin

ai_proposal_unverified

## agent_id

MHJR3O1Ez0RPfcQN4QebgA-concluded

## exit_state

clearexit

## question

Is every finite poset with at most 12 linear extensions sortable in at most 4 adaptive comparisons, i.e. is the uniform tightness threshold T(4) equal to 12 for all n?

## basis

research-obstruction-next.md and research-core-threshold.md: T(3)=7 is certified all n by Hanamura-Iwata; the core census gives T(4)=12 only through n <= 6; all-n status remains open.

## falsifier

Exhibit a finite poset with e(P) <= 12 and minimax depth at least 5, or a poset with e(P)=13 and depth at most 4, either of which would move T(4) away from 12.

## implication

If T(4)=12 holds for all n, the certified small-extension base for exact minimax evaluation of S(n) extends from e <= 7 to e <= 12 without changing the antichain root.

## finding_unverified

tually happened (verified, no guessing)

| Item | State |
|------|-------|
| Git working tree | Clean at `6a96398` on `billy-dev` — **no commits, no Lean changes, no repo/test/CI changes** |
| Board post for t4 | **Already exists** — posted Nov 17 by "SoringP1 frontier: t4-uniform-tightness-threshold" (issue #301, page 10). Reports exhaustive `n≤6` (0 counterexamples), partial `n=7`, the Kahn–Saks balance blocker, concludes all-n open |
| My previous turn's board posting | **Did not happen** — no t4 finding in my style was posted to #301 |
| Worktrees | `t4-uniform-tightness-threshold` (my CWD) and `exec-t4-uniform-tightness-20261121` (curator-dispatched) — identical content at `6a96398` |

Since the Nov 17 post already reports the core negative result, I will **not** duplicate it with a new board post. My extended search is consistent with it and adds incremental evidence only.

---

## Mathematical finding (negative / inconclusive)

**Claim tested:** `T(4) = 12` for all finite posets — every poset `P` with `e(P) ≤ 12` has `m(P) ≤ 4` (sortable in ≤ 4 adaptive comparisons).

**Disproof attempt: failed.** No finite poset with `e(P) ≤ 12` and `m(P) ≥ 5` was found.

### Evidence gathered

1. **Exhaustive `n ≤ 6`** (all 1,3,19,219,4,231,130,023 labelled posets): **0** counterexamples with `e ≤ 12, m ≥ 5`. Confirms `T(4) ≥ 12` on this range (matches Nov 17 post).

2. **Extended structural families** (new beyond Nov 17's `n≤7` partial search), all with `e ∈ {11, 12}`:
   - **Chain-plus-one insertion posets**, `n ≤ 12`: 0 bad cases — every one has a comparison whose both outcomes have `e ≤ 7` (good split), `m ≤ 4`.
   - **Multi-chain merges** (all chain partitions, `n ≤ 9`): only `(2,1,1)` has `e=12`, `m=4`, good split. 0 bad cases.
   - **Almost-total posets** (≤6 missing comparabilities), `n ≤ 8`: 614 cases with `e ∈ {11,12}`, all have good splits. 0 bad.
   - **Random posets**, `n ≤ 10`: 1,037 cases with `e ∈ {11,12}`, all have good splits. 0 bad.
   - **Width**: no width-`≥4` poset with `e ≤ 12` found in any family; width `≤ 3` appears forced.

### Exact obstruction to an all-n proof

To prove `m(P) ≤ 4` for `e(P) ∈ {11, 12}` via the Hanamura–Iwata base (`e ≤ 7 ⇒ m ≤ 3`), one needs: from every such poset, a comparison whose **both** outcomes have `e ≤ 7` (so `1 + 3 = 4` suffices).

Kahn–Saks guarantees a comparison with balance ratio in `[3/11, 8/11]`. For `e = 12`, the heavier side is guaranteed at most `floor(8·12/11) = 8` — **one short of the needed `≤ 7`**. So the general balance theorem alone cannot prove `T(4) = 12`; an all-n proof requires a stronger splitting lemma specific to `e ∈ {11, 12}`, or a different invariant entirely.

### Conclusion

**All-n status: open.** No counterexample found (disproof not achieved), no all-n proof obtained (claim not established). The `e ≤ 12 ⇒ m ≤ 4` claim holds on all tested data but remains unproved for arbitrary `n`.

### No repository changes

Per the publication gate and AGENTS.md, no Lean file, test, commit, or PR was created — this is a negative/inconclusive result without a substantiated new theorem or counterexample, so nothing was integrated. The working tree remains clean at `6a96398`.

### Next decisive obstacle

A strengthening of the balance guarantee for posets with exactly 11 or 12 linear extensions: show that every such poset admits a comparison with both branches at `e ≤ 7`, or exhibit a counterexample. Until that lemma is proved or falsified, `T(4) = 12` for all `n` remains open.

## Other metadata

```json
{
  "finished_at": 1795242815.23543,
  "started_at": 1795241849.9331334
}
```
