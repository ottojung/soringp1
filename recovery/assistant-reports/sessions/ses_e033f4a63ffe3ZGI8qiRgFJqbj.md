# antonina-MHJR3O1Ez0RPfcQN4QebgA-concluded

Session: ses_e033f4a63ffe3ZGI8qiRgFJqbj
Workspace: /home/lubko/soring-fronts/t4-uniform-tightness-threshold
Created: 1795241850341; updated: 1795242808401

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 375 (msg_1fccd69d2001W3XQshpziYK3jr)

## Finding (front `t4-uniform-tightness-threshold`)

**Claim tested.** \(T(4)=12\) for all \(n\): every finite poset \(P\) with \(e(P)\le 12\) linear extensions satisfies \(m(P)\le 4\). Equivalently, no poset has \(e(P)\le 12\) and minimax depth \(\ge 5\).

**Disproof attempt.** A poset with \(e\in\{11,12\}\) and \(m\ge 5\) would have to have *no* comparison whose two outcomes both have \(\le 7\) extensions (since \(T(3)=7\) all-\(n\) is certified by Hanamura–Iwata). I searched for such “unbalanced” posets:

- Chain-plus-one insertion posets for \(n\le 12\): all good splits exist, \(m\le 4\).
- Multi-chain merge posets with \(e\le 12\): only \((2,1,1)\) (\(e=12\)) occurs, and it has \(m=4\) with a good split.
- Almost-total posets (≤6 missing comparabilities) for \(n\le 8\): 614 cases with \(e\in\{11,12\}\), all with a good split.
- Random posets on 6–10 elements: 1037 cases with \(e\in\{11,12\}\), none lacking a good split.
- Width check: no width-\(\ge 4\) poset with \(e\le 12\) was found in any of the above families (width \(\le 3\) appears forced).

**Result.** No falsifier was found. The claim \(T(4)=12\) is unrefuted in all tested families and sizes up to \(n=10\).

**Exact obstruction to proof.** Kahn–Saks gives, for \(e=11\) or \(12\), a comparison with both branches in \([3e/11,\,8e/11]\), i.e. a max branch of **8**, one short of the needed \(\le 7\). To close the all-\(n\) proof one needs a stronger balance lemma for posets with exactly 11 or 12 linear extensions: exclude the case where every comparison is a \(3/8\) or \(4/8\) split. The computation above supports that such posets do not occur, but I did not establish the lemma.

**Limits.** No all-\(n\) proof or counterexample is produced; no Lean/repository changes were made. If \(T(4)=12\) does hold, the certified small-extension base for exact minimax evaluation extends from \(e\le 7\) to \(e\le 12\), but that consequence remains conditional.

## Output 479 (msg_1fcce509e0015ZxcDxyMNT0JMT)

I now have a clear picture of the state. Let me verify there's no existing t4 finding on the board, and check how posts are made.


## Output 494 (msg_1fcce6e300019SLU1wcfwdM0NX)

A t4-uniform-tightness-threshold finding was **already posted on Nov 17**. Let me read it to avoid duplicating prior work.


## Output 523 (msg_1fcce986c001Er6oCFahpoXZ1i)

I now have a complete picture of the state. Let me summarize what I've found:

**What actually happened (no guesswork):**
- Git working tree is clean at `6a96398` on `billy-dev` — **no repo/commit/Lean changes**
- A `t4-uniform-tightness-threshold` finding was **already posted to #301 on Nov 17** (page 10, author "SoringP1 frontier: t4-uniform-tightness-threshold") — it reports exhaustive `n≤6` (0 counterexamples), partial `n=7`, the Kahn–Saks balance blocker, and concludes all-n is open
- **My previous turn did NOT post anything new to the board** — no t4 finding in my style exists on #301
- Two worktrees exist with identical content: `t4-uniform-tightness-threshold` (my CWD) and `exec-t4-uniform-tightness-20261121` (dispatched by curator)

Let me verify my extended research is sound before reporting.


## Output 543 (msg_1fccf1c9f0012b2J442vXVNjla)

My research is verified. Here is my honest report on the state of the `t4-uniform-tightness-threshold` front.

---

## Status report: `t4-uniform-tightness-threshold` (T(4) = 12?)

### What actually happened (verified, no guessing)

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
