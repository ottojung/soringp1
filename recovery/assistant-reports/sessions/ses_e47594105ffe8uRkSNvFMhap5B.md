# antonina-WNPEmQSIrmEDWCVTNyH3AB-alien

Session: ses_e47594105ffe8uRkSNvFMhap5B
Workspace: /home/lubko/soring-fronts/shallow-state-fibonacci-hardness
Created: 1794099298097; updated: 1794101358305

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 52 (msg_1b8a6fc99001IvHsJ3XhGAK1Eb)

The front and prior state are clear so far. The width-two note is merged; the *unrestricted* LV PP-hardness post is on the board. Now I need the original reduction's details to test whether its instances are shallow at all. Let me find it.

## Output 100 (msg_1b8a81a6d001VQW7D02lFYZYgm)

No prior scratch work exists for this front: the worktree is clean, and there is no branch for it. Let me check whether the previous turn posted anything to the board for this front.

## Output 173 (msg_1b8a880ee001vwvv8fSFpGDtBP)

The board picture is clear. The front is running (agent id `WNPEmQSIrmEDWCVTNyH3AB`, this checkout), but no prior work from this front exists on disk or on the board — the previous turn evidently failed before doing anything. So the work itself is still undone. I'll start from the model analysis. First, let me look at the cached literature in /tmp/opencode and `docs/problem.md`.

## Output 213 (msg_1b8ab3b9e001adWSojJGlBLUHR)

The cached PDFs are only about merging, not relevant. Let me fetch the primary sources needed for this front: Kravitz–Sah (arXiv:1906.06036) and Brightwell–Winkler.

## Output 242 (msg_1b8ab62010016U2Yc2x4B0HUOg)

Kravitz–Sah's construction is **width-two** — that's good news for the sparseness of the gadget `M`. Now the decisive question is whether the #LE-hard source instances can be chosen sparse (few cover/Hasse relations), since `Q = P(+)M` inherits the cover count of `P`. Let me check the literature on restricted #LE hardness.

## Output 328 (msg_1b8ac6c6d001BiFZJUVaMFjXqF)

The reduced question is now sharp. Let me lay out the model analysis and then verify it computationally.

**Key derivation (the reachability lemma).** A state `P` on n labelled keys is reached by a consistent comparison sequence iff every cover relation of `P` was directly compared: comparing pairs builds the transitive closure, a cover pair `(x,y)` of the final poset can never be derived transitively (an intermediate `w` with `x<w<y` would make it not a cover), so comparing exactly the covers of `P` suffices and is necessary. Hence **reachable-in-≤k comparisons ⟺ |cov(P)| ≤ k**, and the states explored by an exact unary evaluator (minimax DFS with budget S(n)) are exactly the n-posets with at most S(n) covers.

So the front's shallow class = posets with O(n log n) cover relations. The existing LV reduction maps `(P,K)` to `Q = P(+)M` with `e(Q) = c·e(P)`. The catch was: if `P` is dense, `cov(Q)` ≈ n²/2 could exceed S(|Q|). But `M` (a width-two Kravitz–Sah/Stern–Brocot poset, ≤2 minimal elements) can be **pumped** below by a chain `C_L` of fresh all-bottom elements: `e` unchanged, `|Q|` grows by `L`, covers grow only linearly. With `L = n⁴` and `|Q| = Θ(n⁴)`, `cov(Q) ≈ n⁴ + n² ≪ S(|Q|) ≥ log₂(|Q|!) ≈ |Q|·log₂|Q|`. Let me test both parts.

## Output 394 (msg_1b8b0ad76001lJEn6IbVbx41TZ)

Part (a) verified on all 1,099 labelled posets through n=5. Fixing the call signatures for part (b).

## Output 442 (msg_1b8b17d2e001ZixSaI9RqsZ9dS)

Bug found in my cover formula (must use `|min(Q1)|`, not final-Q mins), and part (c)'s gadget bound was dishonest (I asserted covers ≤ |M0| for width-two; needs justification). Let me debug (b) and read the KS construction in detail for an honest cover bound.

## Output 453 (msg_1b8b27ff6001V1d0E5kNdcq1nf)

Found it: `chain_below` with L=0 adds phantom negative-label edges. Fixing, and also fixing the (c) bound to be honest about the gadget.

## Output 478 (msg_1b8b36bdd001tjExXOS5BNbDqj)

The math is fine; the script compared against mins of the **final** poset instead of the middle part. Fixing both (b)'s formula and making (c) parametric in the (unaudited) KS gadget constant.

## Output 535 (msg_1b8b6d905001U46H6plpi37CJO)

Exhaustive check (all P n≤4, all M n≤3, L≤5): zero mismatches. The earlier random violation involved L=6 — let me test whether larger L breaks the cover formula.

## Output 546 (msg_1b8b7a308001un3dRN9y4RLaft)

The exhaustive test is authoritative (zero mismatches everywhere), but I want to reproduce and explain the random-trial discrepancy rather than ignore it. Let me print full details of any failing random trial.

## Output 614 (msg_1b8badf2100153F3wtkH8OcV0r)

Found the real script bug: `_, mQ1part = mins_maxs(...)` unpacked **maxs**, not mins. The math is right; the test was wrong. Fixing and rerunning.

## Output 632 (msg_1b8bbc38e001mdIoPh9iq1Xlxt)

All three model-theory parts pass. Now the end-to-end toy check of the complete reduction (interval arithmetic + multiplicative ordinal sum + cover budget) at small scale.

## Output 726 (msg_1b8c4b257001yWGi87degjSQGp)

End-to-end check passes (33 toy reduction instances, zero mismatches; `e(Q) = c·e(P)` asserted throughout). Now let me record evidence hashes and post the finding to the board.

## Output 804 (msg_1b8c5d353001yC8bhK7jdCPibf)

Posted exactly once (`sha256:pXM8mkIC8DWr6YLb5cXvjxjn6ZWwKegcjZwJddW0tsc`). Final state check:

## Output 815 (msg_1b8c5e543001JX60T0cnl7cRqy)

## Summary

**Context recovered.** The prior turn completed nothing for this front: worktree clean, no branch, no scratch files, and no board post mentioning the shallow front — so no side effects could be duplicated. I verified that before doing anything.

**The finding (mathematical, conditional): the reachable-state restriction does NOT rescue extension-threshold pruning.** Two self-contained results carried it:

1. **Reachability lemma** [deduction, machine-checked]: a poset state is reachable from the antichain by `k` admissible comparisons iff `|cov(P)| ≤ k` — every cover relation must be compared directly, since transitive derivation of a cover is impossible. Hence the exact unary evaluator explores exactly `{P : |cov(P)| ≤ S(n)}`, i.e. posets with O(n log n) cover relations. Verified against BFS over comparison sequences on all 1,099 labelled posets n ≤ 5.

2. **Bottom-chain pumping** [deduction]: the board's Las Vegas PP-hardness reduction `Q = P(+)M` fails the shallow restriction only because a dense source instance `P` contributes Θ(n²) covers. Inserting an L-chain strictly below everything (`L = 2|M|² + n²`) leaves `e` unchanged, gives a single minimal element, and `cov(Q) ≈ 2|M|² ≪ S(N) ≥ log₂N!` — so the target lands inside the comparison-reachable class anyway. Verified numerically robust to the (unaudited) Kravitz–Sah gadget constants (up to C = 10⁶, n up to 2·10⁵), plus 33 end-to-end toy reduction instances with `e(Q) = c·e(P)` and correct interval arithmetic.

**Consequence**: the falsifier's first branch is refuted — a poly-time predicate `e ≤ T(b)` on comparison-reachable states would put `L_bin` in ZPP (→ `PP=NP`, `PH=NP`), with the reduced instance genuinely a visited (state, remaining-budget) pair of the unary DFS. The "hardness is an artifact of unreachable larger posets" objection is refuted, *modulo* the same unverified effective-Kravitz–Sah deduction the unrestricted post already carries — I state that inherited caveat explicitly.

**Honest limits.** Soundness of the Fibonacci threshold conjecture and completeness of the base are untouched; the blow-up grows to Θ(n⁴); a genuinely separate residual question (intrinsic #LE-hardness for naturally sparse-Hasse posets, without the pump) is identified and explicitly left open.

**Actions**: exactly one board comment on #301 (`sha256:pXM8mkIC8DWr6YLb5cXvjxjn6ZWwKegcjZwJddW0tsc`), no commits, no Lean files, worktree clean — per the publication gate, the conditional nature doesn't warrant a repository note before the KS audit closes. Check scripts are hashed in the post for independent replay.

## Output 836 (msg_1b8c62610001blwpJjDPc8z8PN)

Recovery check complete. The single external effect — the board #301 comment `sha256:pXM8mkIC8DWr6YLb5cXvjxjn6ZWwKegcjZwJddW0tsc` — is present exactly once. Worktree is clean and no further action is outstanding.

**Final state of the `shallow-state-fibonacci-hardness` front:**
- One board post recorded (the reachability lemma + bottom-chain pumping result + caveats).
- No repository changes, commits, or Lean files.
- No duplicate posts or side effects.

The front's substantive question is answered (conditionally): the shallow/reachable-state restriction does not rescue extension-threshold pruning, because any reduction target can be pumped into the comparison-reachable class via a fixed bottom chain. The result's validity inherits the existing unaudited effective-Kravitz–Sah step; the reachability and pumping lemmas are independently self-contained and small-scale verified. No unfinished work remains.
