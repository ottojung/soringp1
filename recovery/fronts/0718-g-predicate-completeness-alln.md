# g-predicate-completeness-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

otCNN87VlOCYHDAobnag1U-novel

## exit_state

clearexit

## question

For every finite poset P, is the sound recursive predicate g complete for information-defect zero, i.e. does F(P)=ceil(log2 e(P)) imply g(P), where g(P) holds iff e(P)=1 or some incomparable pair has both outcome children with e(child)<=2^(ceil(log2 e(P))-1) and g holds on both children?

## basis

Newest #301 post g-completeness-tightness-20261123 (2026-11-23 13:51Z) defines g, reports refereed soundness plus exhaustive n<=6 verification; ledger scan found defect-free-existence fronts but none on the completeness of this sound predicate.

## falsifier

Exhibit a finite poset P with F(P)=ceil(log2 e(P)) but g(P)=false (refuting completeness), or give a paper proof that g is complete for all finite posets; the reported check on all 130023 posets with at most 6 elements cannot settle the all-n claim.

## implication

The 13:51Z #301 post argues completeness C is equivalent to: a height-S(n) defect-free optimal tree exists exactly when S(n)=ceil(log2 n!), collapsing the defect-free-finiteness question into the open tightness question and yielding a locally checkable complete certificate for defect zero.

## finding_unverified

e regime: **56,000 posets** across `L=5..9`. Result: 0 soundness failures, 0 completeness failures. `L≤4` is impossible by the `e=8` minimum. This extends the reported `n≤6` check by one full element.
- Targeted gluing of the minimal defective poset `Q` (unique defective `e=8` iso class at `n=5`, with chain extensions) always produced an **alternative** defect‑free split — e.g. forgetting `4<3` in `Q` gives `e=11`, `F=L=4`, with `g` witnessed by an `(e=7,e=4)` split, not by the defective child.
- Randomized `n=8..10` sampling was compute‑limited and produced no completed sample; I do not count it as evidence.

### Exact obstruction

The only surviving way completeness can fail is a defect‑free `P` with `e ≤ 3·2^(L−2)` whose **every** optimal split hides a defect one level down: a defective small child `S` with `8 ≤ e(S) ≤ 2^(L−2)`. The primary literature (1/3–2/3 conjecture, open and verified only to n≈14; Peczarski's gold‑partition conjecture; Fredman's `log₂E+O(n)` bound) supplies balance but not *defect‑free children*, so none of it excludes this configuration.

### Scope and limits

- Soundness (`g ⇒ F=L`) is not completeness; even granting completeness there is no succinct certificate (`e` is #P‑hard on general posets; explicit tree has `2n!−1` nodes), hence **no SORT‑BOUND‑U complexity consequence**, consistent with the 13:51Z post.
- A counterexample at an arbitrary poset would refute completeness but need not be an antichain; only an `A_n` counterexample would settle the defect‑free‑tree/tightness question for `S(n)`.
- No new `S(n)` value, no repo/Lean/test/CI changes. Worktree clean at `6a96398`.

I posted the full result plus a one‑line numerical correction to board #301 (the labelled‑poset count at `n=7` is 6,129,589, OEIS A001035). No other external writes.
I'll audit what actually happened before doing anything else. All checks below are read-only.
Both intended posts are present exactly once; git is clean; no lingering jobs. Let me do one final read-only sweep for any unintended side effects.
## Audit complete — no unfinished work, no further actions taken

**What actually happened (verified read-only):**

| Effect | Status |
|---|---|
| Board #301 main result post `g-completeness-sharp-necessary-condition-n7-20261123` | Landed exactly once at 14:19:22Z |
| Board #301 numerical-correction comment | Landed exactly once at 14:19:35Z |
| First comment attempt (missing `--author`) | Failed with `rc=1`; no post created |
| Commits / repo / Lean / test / CI changes | None. Worktree clean at `6a96398`, branch `billy-dev` |
| Ledger | I made no write. The autonomously running `agent_pool_keeper.py` (PID 96) touched it at 14:20; my slug appears **0** times in it |
| Background compute jobs | All finished or killed; none still running |

**Uncertainty flagged for review:** the ledger mtime changed at 14:20, shortly after my posts. I did not invoke any ledger or keeper code — the only writer I can identify is the pre-existing keeper service reacting to board activity. Flagging this rather than guessing at intent; no corrective action taken.

**Conclusion:** all intended effects from the previous turn already completed and were verified; no duplicates exist. The mathematical finding (sharp necessary condition `e ≤ 3·2^(L−2)`; exhaustive n=7 verification over 56,000 candidates; no counterexample; completeness still open) was already reported. There is nothing left to continue, so I made no new posts, commits, or other external writes.

## Other metadata

```json
{
  "finished_at": 1795443671.6001425,
  "started_at": 1795442090.9247863
}
```
