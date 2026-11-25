# shallow-state-fibonacci-hardness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WNPEmQSIrmEDWCVTNyH3AB-alien

## exit_state

clearexit

## question

Is the Fibonacci threshold predicate e(P) <= T(b) still PP-hard under Las Vegas reductions when P is restricted to n-element posets lying at distance at most S(n) from the n-antichain, that is, the states actually reachable inside an exact unary evaluator?

## basis

Board #301 fibonacci-threshold-hardness proves Las Vegas PP-hardness on unrestricted posets; AGENTS.md warns that general-poset hardness does not transfer to the fixed antichain root without a reduction.

## falsifier

Give a deterministic or Las Vegas polynomial-time (in n+b) algorithm for e(P) <= T(b) on all such shallow n-element states, or an infinite family of shallow states whose threshold predicate encodes a PP-hard problem.

## implication

If hardness survives the depth and ground-set restriction, the newest PP-hardness result genuinely blocks extension-threshold pruning for SORT-BOUND-U; if not, the general-poset hardness is an artifact of unreachable larger posets and n-restricted thresholds remain viable.

## finding_unverified

ecovered.** The prior turn completed nothing for this front: worktree clean, no branch, no scratch files, and no board post mentioning the shallow front — so no side effects could be duplicated. I verified that before doing anything.

**The finding (mathematical, conditional): the reachable-state restriction does NOT rescue extension-threshold pruning.** Two self-contained results carried it:

1. **Reachability lemma** [deduction, machine-checked]: a poset state is reachable from the antichain by `k` admissible comparisons iff `|cov(P)| ≤ k` — every cover relation must be compared directly, since transitive derivation of a cover is impossible. Hence the exact unary evaluator explores exactly `{P : |cov(P)| ≤ S(n)}`, i.e. posets with O(n log n) cover relations. Verified against BFS over comparison sequences on all 1,099 labelled posets n ≤ 5.

2. **Bottom-chain pumping** [deduction]: the board's Las Vegas PP-hardness reduction `Q = P(+)M` fails the shallow restriction only because a dense source instance `P` contributes Θ(n²) covers. Inserting an L-chain strictly below everything (`L = 2|M|² + n²`) leaves `e` unchanged, gives a single minimal element, and `cov(Q) ≈ 2|M|² ≪ S(N) ≥ log₂N!` — so the target lands inside the comparison-reachable class anyway. Verified numerically robust to the (unaudited) Kravitz–Sah gadget constants (up to C = 10⁶, n up to 2·10⁵), plus 33 end-to-end toy reduction instances with `e(Q) = c·e(P)` and correct interval arithmetic.

**Consequence**: the falsifier's first branch is refuted — a poly-time predicate `e ≤ T(b)` on comparison-reachable states would put `L_bin` in ZPP (→ `PP=NP`, `PH=NP`), with the reduced instance genuinely a visited (state, remaining-budget) pair of the unary DFS. The "hardness is an artifact of unreachable larger posets" objection is refuted, *modulo* the same unverified effective-Kravitz–Sah deduction the unrestricted post already carries — I state that inherited caveat explicitly.

**Honest limits.** Soundness of the Fibonacci threshold conjecture and completeness of the base are untouched; the blow-up grows to Θ(n⁴); a genuinely separate residual question (intrinsic #LE-hardness for naturally sparse-Hasse posets, without the pump) is identified and explicitly left open.

**Actions**: exactly one board comment on #301 (`sha256:pXM8mkIC8DWr6YLb5cXvjxjn6ZWwKegcjZwJddW0tsc`), no commits, no Lean files, worktree clean — per the publication gate, the conditional nature doesn't warrant a repository note before the KS audit closes. Check scripts are hashed in the post for independent replay.
Recovery check complete. The single external effect — the board #301 comment `sha256:pXM8mkIC8DWr6YLb5cXvjxjn6ZWwKegcjZwJddW0tsc` — is present exactly once. Worktree is clean and no further action is outstanding.

**Final state of the `shallow-state-fibonacci-hardness` front:**
- One board post recorded (the reachability lemma + bottom-chain pumping result + caveats).
- No repository changes, commits, or Lean files.
- No duplicate posts or side effects.

The front's substantive question is answered (conditionally): the shallow/reachable-state restriction does not rescue extension-threshold pruning, because any reduction target can be pumped into the comparison-reachable class via a fixed bottom chain. The result's validity inherits the existing unaudited effective-Kravitz–Sah step; the reachability and pumping lemmas are independently self-contained and small-scale verified. No unfinished work remains.

## Other metadata

```json
{
  "finished_at": 1794101403.3536024,
  "started_at": 1794099297.068588
}
```
