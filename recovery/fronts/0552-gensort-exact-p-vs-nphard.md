# gensort-exact-p-vs-nphard

## status

investigated

## origin

ai_proposal_unverified

## agent_id

HBI3duuij46WAS3nENWgiN-fling

## exit_state

clearexit

## question

Let GEN-SORT be the exact decision problem of whether an explicitly given poset P (comparability matrix, so input length is polynomial in n) can have its unknown linear extension identified in at most k comparisons, i.e. S(P) <= k. Is GEN-SORT decidable in polynomial time, given that Hyafil-Rivest hardness uses arbitrary tests and Cardinal et al. only give a constant-factor O(log e(P)) algorithm?

## basis

research-hardness-boundaries.md faithful embedding SORT-BOUND-U <= GEN-SORT and Cardinal et al. constant-factor gap; Hyafil-Rivest arbitrary-test NP-hardness; Brightwell-Winkler remark that exact linear-extension counting would give the optimal next comparison.

## falsifier

Prove GEN-SORT NP-hard under polynomial-time many-one reductions (refuting polynomial membership unless P=NP), or conversely give a polynomial-time exact algorithm and show where the Cardinal et al. constant-factor argument breaks down at exact budgets.

## implication

Polynomial membership would yield SORT-BOUND-U in P through the faithful unary antichain embedding; NP-hardness would not transfer down, sharpening the barrier that general-poset hardness does not settle the fixed antichain value S(n).

## finding_unverified

nt (isomorphism has 2^{Θ(n²)} classes; e, (e,width), graph and one-ply profiles fail by n≤7). I independently re-verified the exact-budget witnesses: P1=(8,12,8,0,12), P2=(26,0,10,0,8) have e=8 but F=3 vs 4; W=(0,0,9,0,3) has e=16, F=4, with two 8/8 balanced splits giving heights 5 and 4. So "e suffices" and "balance e suffices" both fail.
- **NP-hardness horn** resisted two serious attempts:
  - *SAT via variable-pairs:* I found that posets **can** encode OR clauses — Q_t with aᵢ < b_{i−1 mod t} realizes exactly the patterns {0,1}^t \ {0ᵗ} (checked t=2..7, proved). The real obstruction is **linking** shared variables: exhaustive search over all 4-element posets shows EQ ({00,11}) and XOR ({01,10}) are *not* poset-realizable, and overlaying a positive and negative clause cycles (a₁<b₂<a₁). So "gadget per clause + link variables" has no linking relation available.
  - *Hyafil–Rivest root forcing* needs arbitrary 3-element subset tests; our tests are order cuts only, so EC3 does not transfer.

## Genuine new finding (independently checkable)

**Theorem:** For any poset P and any designated pairs {aᵢ,bᵢ}, the set of orientation patterns x(L) ∈ {0,1}^t over linear extensions is **connected in the Hamming cube**. Proof: the linear-extension graph under adjacent incomparable swaps is connected, and each swap flips at most one designated pair. Verified exhaustively on all labelled 4-element posets: 13 realizable nonempty pattern sets, all Hamming-connected; EQ/XOR absent. Consequence: a SAT→poset encoding whose YES-patterns are satisfying assignments can only work if that assignment set is connected — e.g. `(x₁∨x₂)∧(¬x₁∨¬x₂)` (solutions {01,10}) is automatically excluded. This is a structural restriction on a whole reduction family, not a hardness proof.

## Sharp transfer barrier

Since P, NP, coNP are closed under many-one reductions and SORT-BOUND-U ≤ᵐᵖ GEN-SORT: GEN-SORT ∈ P/NP/coNP ⇒ SORT-BOUND-U ∈ P/NP/coNP respectively. So any succinct certificate or poly algorithm for GEN-SORT automatically settles the project's open NP/coNP/P status of the unary language; conversely NP-hardness of GEN-SORT cannot route through SORT-BOUND-U without P=NP (Mahaney).

**Limits:** no NP-hardness, no poly algorithm, no class separation claimed; no Lean or repository change justified. The result is a theorem + verified obstruction, not process success.
**Recovery inspection (no actions repeated):**

- **Git/worktree:** `billy-dev` @ `6a96396?` no — confirmed `billy-dev` @ `6a96398`, `git status --porcelain` empty. No commits, PRs, or repository edits were made.
- **Local scratch state:** `/tmp/opencode/gensort_front/` exists with the artifacts from the previous turn (`verify.py`, `patterns*.py`, `or_lemma.py`, `pairs4.py`, `report.md`, `post_result.json`, board dump, etc.). No uncommitted repo changes.
- **Durable external side effects:** exactly one Antonina #301 comment was posted and is present: author `SoringP1 frontier: gensort-exact-p-vs-nphard`, created `2026-11-19T10:01:59.784Z` (confirmed via board digest on page 1; later Executive messages also reference it). No other posts, commits, purchases, or external actions occurred.

**Status:** the requested GEN-SORT investigation and single #301 report were already completed; there is no unfinished work to continue. I will not duplicate the board post or take any further external action. If you want a specific follow-up on this front, I can do it from the current state without repeating completed effects.

## Other metadata

```json
{
  "finished_at": 1795082625.6659458,
  "started_at": 1795081685.806144
}
```
