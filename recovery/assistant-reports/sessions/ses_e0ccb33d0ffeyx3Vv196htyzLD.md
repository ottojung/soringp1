# antonina-HBI3duuij46WAS3nENWgiN-fling

Session: ses_e0ccb33d0ffeyx3Vv196htyzLD
Workspace: /home/lubko/soring-fronts/gensort-exact-p-vs-nphard
Created: 1795081686086; updated: 1795082590855

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f334d11f001JA506OX90kvePV)

I'll start by understanding my environment, the current branch, and the key documents.

## Output 43 (msg_1f334fbb3001f8T80FYeqkCIrL)

Now let me check the research board #301 digest and the key research document on hardness boundaries.

## Output 54 (msg_1f3350b18001sgIYWN3QwmcaSs)

Let me search the board for prior work on this specific front and read the key research document.

## Output 83 (msg_1f33535d50011oLJ0ki524wURq)

Let me dump the full board to a scratch file so I can search all pages for prior work on this front.

## Output 110 (msg_1f3361270001NYhP6Ao2kPh4Ak)

Let me look at prior board posts most relevant to this exact front to avoid duplicating work.

## Output 153 (msg_1f336a03f001YmlgIm1z2vLQk1)

I now have a good picture of prior work. Let me study the primary literature on the exact complexity of generalized sorting, since the repository note says it's open.

## Output 337 (msg_1f33b1459001M95Rpk2ADIT451)

I have a thorough picture of prior work. Let me independently verify the key finite witnesses with my own from-scratch evaluator before writing anything.

## Output 373 (msg_1f33c110c001F8zXuEBzRh51HL)

I found a potentially new structural angle. Let me test it computationally: which Boolean constraints on "orientation patterns" of independent pairs are realizable by a poset.

## Output 432 (msg_1f3403776001NNe1uBfqkgWQ84)

This is a genuinely new structural angle. Let me characterize which Boolean constraints on orientation pairs a poset can enforce.

## Output 450 (msg_1f3408368001Qz3NvfNdM7Mv2t)

I've found a genuine new theorem. Let me write up the report carefully.

## Output 477 (msg_1f34154540010PdcSu4ZxjkE7y)

The theorem checks out. Let me post the single report to board #301.

## Output 515 (msg_1f341e53a001veMAXOmNdvJfli)

Done. I worked only on `billy-dev`, kept the worktree clean, and posted one report to Antonina #301 (author `SoringP1 frontier: gensort-exact-p-vs-nphard`, confirmed as exactly one comment). No Lean, repo, test, or ledger changes.

## What I attacked

The claim **GEN-SORT ∈ P** (explicit comparability matrix, matrix length N = Θ(n²)), with the two falsifier horns: prove many-one NP-hardness, or give a poly exact algorithm and locate Cardinal et al.'s exact-budget breakdown.

## Honest outcome: neither horn proved — GEN-SORT remains unclassified

- **Poly-algorithm horn** is not a short target: `SORT-BOUND-U ≤ᵐᵖ GEN-SORT`, so GEN-SORT ∈ P would put `S_unary ∈ FP` (a stated open problem). The minimax recursion has no known sound polynomial state quotient (isomorphism has 2^{Θ(n²)} classes; e, (e,width), graph and one-ply profiles fail by n≤7). I independently re-verified the exact-budget witnesses: P1=(8,12,8,0,12), P2=(26,0,10,0,8) have e=8 but F=3 vs 4; W=(0,0,9,0,3) has e=16, F=4, with two 8/8 balanced splits giving heights 5 and 4. So "e suffices" and "balance e suffices" both fail.
- **NP-hardness horn** resisted two serious attempts:
  - *SAT via variable-pairs:* I found that posets **can** encode OR clauses — Q_t with aᵢ < b_{i−1 mod t} realizes exactly the patterns {0,1}^t \ {0ᵗ} (checked t=2..7, proved). The real obstruction is **linking** shared variables: exhaustive search over all 4-element posets shows EQ ({00,11}) and XOR ({01,10}) are *not* poset-realizable, and overlaying a positive and negative clause cycles (a₁<b₂<a₁). So "gadget per clause + link variables" has no linking relation available.
  - *Hyafil–Rivest root forcing* needs arbitrary 3-element subset tests; our tests are order cuts only, so EC3 does not transfer.

## Genuine new finding (independently checkable)

**Theorem:** For any poset P and any designated pairs {aᵢ,bᵢ}, the set of orientation patterns x(L) ∈ {0,1}^t over linear extensions is **connected in the Hamming cube**. Proof: the linear-extension graph under adjacent incomparable swaps is connected, and each swap flips at most one designated pair. Verified exhaustively on all labelled 4-element posets: 13 realizable nonempty pattern sets, all Hamming-connected; EQ/XOR absent. Consequence: a SAT→poset encoding whose YES-patterns are satisfying assignments can only work if that assignment set is connected — e.g. `(x₁∨x₂)∧(¬x₁∨¬x₂)` (solutions {01,10}) is automatically excluded. This is a structural restriction on a whole reduction family, not a hardness proof.

## Sharp transfer barrier

Since P, NP, coNP are closed under many-one reductions and SORT-BOUND-U ≤ᵐᵖ GEN-SORT: GEN-SORT ∈ P/NP/coNP ⇒ SORT-BOUND-U ∈ P/NP/coNP respectively. So any succinct certificate or poly algorithm for GEN-SORT automatically settles the project's open NP/coNP/P status of the unary language; conversely NP-hardness of GEN-SORT cannot route through SORT-BOUND-U without P=NP (Mahaney).

**Limits:** no NP-hardness, no poly algorithm, no class separation claimed; no Lean or repository change justified. The result is a theorem + verified obstruction, not process success.

## Output 544 (msg_1f3425f43001Hd9XUUvSNhEloY)

**Recovery inspection (no actions repeated):**

- **Git/worktree:** `billy-dev` @ `6a96396?` no — confirmed `billy-dev` @ `6a96398`, `git status --porcelain` empty. No commits, PRs, or repository edits were made.
- **Local scratch state:** `/tmp/opencode/gensort_front/` exists with the artifacts from the previous turn (`verify.py`, `patterns*.py`, `or_lemma.py`, `pairs4.py`, `report.md`, `post_result.json`, board dump, etc.). No uncommitted repo changes.
- **Durable external side effects:** exactly one Antonina #301 comment was posted and is present: author `SoringP1 frontier: gensort-exact-p-vs-nphard`, created `2026-11-19T10:01:59.784Z` (confirmed via board digest on page 1; later Executive messages also reference it). No other posts, commits, purchases, or external actions occurred.

**Status:** the requested GEN-SORT investigation and single #301 report were already completed; there is no unfinished work to continue. I will not duplicate the board post or take any further external action. If you want a specific follow-up on this front, I can do it from the current state without repeating completed effects.
