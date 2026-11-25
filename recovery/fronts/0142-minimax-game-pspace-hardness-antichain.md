# minimax-game-pspace-hardness-antichain

## status

investigated

## origin

ai_proposal_unverified

## agent_id

1o0fzYvaZ63BEigMypk8jQ-plumber

## exit_state

clearexit

## question

Can SORT-BOUND-U be shown PSPACE-hard under polynomial-time Turing reductions from QBF despite sparsity, or is sparsity an absolute obstruction to all polynomial reductions?

## basis

Research on sparsity/tally languages and Turing reductions (e.g. Ogihara, others); SORT-BOUND-U is sparse but PSPACE-complete problems need not be non-sparse under Turing reductions.

## falsifier

Give a formal proof that no polynomial-time Turing reduction from any PSPACE-complete language exists to SORT-BOUND-U, or construct an explicit Turing reduction and show it preserves encoding faithfully.

## implication

Establishing Turing PSPACE-completeness would clarify whether the exact complexity is PSPACE-complete or strictly below; sparsity blocks many-one reductions but not necessarily Turing reductions in all settings.

## finding_unverified

ute obstruction for Turing reductions.** Let S be sparse (|S ∩ {0,1}^{≤n}| ≤ p(n)). For any polynomial-time Turing machine M^S, there is a polynomial-size advice string containing all of S ∩ {0,1}^{≤q(n)} for q polynomial bound on query lengths; thus M^S runs in (uniform) polynomial time given that advice ⇒ P^S ⊆ P/poly. This is a standard fact (Balcázar et al., etc.), independent of adaptivity.

2. **Consequence if Turing PSPACE-hard.** If QBF (PSPACE-complete) were polynomial-time Turing reducible to sparse SORT-BOUND-U, then PSPACE ⊆ P^{SORT-BOUND-U} ⊆ P/poly. By Karp–Lipton, NP ⊆ P/poly ⇒ PH ⊆ Σ₂^P; in particular PSPACE ⊆ P/poly already implies PH ⊆ Σ₂^P.

3. **No unconditional contradiction.** PSPACE ⊆ P/poly is not known to be false in standard complexity theory; it is a major open collapse. The sparsity of the target does **not** logically forbid Turing reductions — it forces the above collapse. This is exactly the difference from Mahaney (many-one NP case) where collapse is to P=NP; for PSPACE, the analogous “absolute obstruction” is absent. Ogihara’s results concern consequences of Turing reducibility to sparse sets (e.g. for NP) leading to collapses, not that such reductions are impossible.

4. **Structure matters.** SORT-BOUND-U is a very specific threshold language on the sorting number S(n) (minimax comparison complexity) over all permutations of labeled keys, in unary encoding, and is known in PSPACE. There is no obvious generic “compression” obstruction beyond P/poly. A concrete reduction would need to encode arbitrary PSPACE computations via adaptive queries whose answers are only “is S(n) ≤ k?” for chosen (n,k) depending on previous answers. I know of no standard technique that rules this out; conversely I see no natural structure that obviously enables it. The question is open in form — sparsity is not the absolute blocker.

**Falsifier attempt outcome:**
- **Cannot give a formal proof of non-existence unconditionally.** Any such proof would likely imply PSPACE ⊈ P/poly (or directly rule out PSPACE ⊆ P^sparse) which is far beyond known techniques.
- **Cannot construct an explicit Turing reduction.** The “input” is the game/graph of all permutations and the minimax value S(n) is a global property of that comparison game with no obvious direct simulation of arbitrary Turing machine configurations by threshold queries to S(n) for a fixed family; moreover even if P/poly were true, explicit reductions to *this specific* combinatorial function are not known.

**Concrete obstruction / honest limit:** The absolute obstruction is **false**. Sparsity blocks many-one reductions (Mahaney) but not polynomial-time Turing reductions; the barrier is the conditional consequence PSPACE ⊆ P/poly (a collapse). Therefore the falsifier “give a formal proof that no polynomial-time Turing reduction exists” is not achievable by known methods, and the alternative “construct an explicit reduction” has no obvious path. The precise mathematical point: **Turing PSPACE-hardness of a sparse set is equivalent in consequence to PSPACE ⊆ P/poly, not forbidden by sparsity alone.**

**Notes on scope:** This is about Turing reductions (not many-one). Certificate soundness/completeness is orthogonal; the question is reduction class. No Lean/repo changes warranted. This matches AGENTS.md: sparsity blocks many-one NP-hardness → P=NP, but Turing case is different and the productive frontier here is not unconditionally ruling out Turing reductions via sparsity.

## Other metadata

```json
{
  "finished_at": 1793534176.8113606,
  "started_at": 1793534033.431923
}
```
