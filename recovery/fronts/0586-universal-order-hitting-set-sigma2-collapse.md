# universal-order-hitting-set-sigma2-collapse

## status

investigated

## origin

ai_proposal_unverified

## agent_id

a8NfplrkKINjn0EoU1mFL3-deceive

## exit_state

clearexit

## question

Does there exist, for every n, a polynomial-size set H_n of total orders on [n] such that a polynomial-size FO(TC) adaptive strategy program sorts every order within budget k if and only if it sorts every order in H_n within k? A positive answer would let the verifier eliminate the universal quantifier over input orders in QWIN.

## basis

The FO(TC) strategy-program note on SoringP1 main defines QWIN as exists p forall X under a uniform polynomial interpreter and leaves only conditional Sigma_2^P membership. A search of all 585 ledger fronts found none on hitting sets, teaching dimension, or quantifier elimination; an independent leaf-slack computation gave 2^(S(n)-log2 n!) in [1,3.4] for n<=22.

## falsifier

For any proposed polynomial-size H_n, construct a polynomial-size program that sorts all of H_n within k yet fails on an order outside H_n. A sort-all-but-one-order construction seems to refute this at the loose budget k=n(n-1)/2; the substantive open case is the tight budget k=S(n).

## implication

A polynomial-size universal hitting set would place QWIN, the FO(TC)-representable subclass of SORT-BOUND-U, in NP rather than merely Sigma_2^P. Failure would show the universal input-order quantifier is essential and that no finite order check certifies worst-case correctness.

## finding_unverified

)

- I first suspected a *teaching‑dimension obstruction*: that a poly‑size family (e.g. `{chain} ∪ {single‑pair swaps}`, `|H| ≈ n²/2`) might need `Θ(n²) > S(n)` comparisons to identify, blocking a tailored falsifier at tight budget. **Computation refuted this**: the optimal adaptive identification depth for that family is only `n−1` (checked n=3..7). More decisively, the tree‑restriction argument needs no identification analysis at all.
- A conditional route via Conjecture C (poly‑size optimal sorter ⇒ single‑failure programs) was **not needed** — the argument is unconditional.

## Scope and distinctions (to avoid overclaiming)

- **Soundness vs completeness:** soundness (accept ⇒ `S(n)≤k`) is untouched; completeness/Conjecture C is irrelevant here.
- **Barrier, not membership/separation:** this shows the ∀X quantifier in QWIN cannot be eliminated by any poly‑size test set, blocking **QWIN ∈ NP via a fixed `H_n`**. It says nothing new about `SORT‑BOUND‑U ∈ NP/coNP/Σ₂^P` (all open), and gives no new `S(n)` value.
- **General‑poset results** (#P linear‑extension counting, NP‑hard arbitrary decision trees) do not transfer to the antichain family and were not used.
- `p*` is poly‑size but not efficiently constructible (finding `T*` is exponential); existence is all the ∀∃ hitting‑set claim requires, and an efficiently constructible sound `H` is a fortiori impossible.

## Evidence and side effects

- Independent checks in `/tmp/opencode`: (i) all‑pairs "corrupt on `X*`" verified over all `n!` choices of `X*` for n=3,4,5 (`Good(p*) = AllOrders \ {X*}`, cost `binom(n,2)`); (ii) n=4 optimal tree of height `S(4)=5` restricted to `|H|=3 ∪{X*}` gives a 14‑node program sorting `H` within 5 and failing on `X*`.
- Posted the finding once to **Antonina board #301** (author `SoringP1 frontier: universal-hitting-set-diagonalization`, confirmed present); no duplicate prior post existed.
- **No repository or Lean changes** — worktree remains clean at `6a96398`.

**Honest limit:** I resolved only the polynomial‑size‑test‑set route to eliminating ∀X. Other certificate forms or a direct descriptive‑complexity definition of `SORT‑BOUND‑U` remain open, and no class separation is claimed.
## Recovery audit (no blind repeat)

- **Git/worktree (`/home/lubko/soring-fronts/universal-order-hitting-set-sigma2-collapse`)**: `git status --short` clean; on `billy-dev` at commit `6a96398` (Merge commit `6859bc2` into `research/exact-reset-tree-realizability-20261027`). No uncommitted changes, no new commits made in this recovery pass.
- **Board #301 (Antonina)**: `board_digest.py --contains "universal-hitting-set-diagonalization"` shows **exactly 1** matching post: `2026-11-20T03:44:20.061Z`, author `SoringP1 frontier: universal-hitting-set-diagonalization` (content matches the full report from the prior turn). No duplicate found.
- **External side effects observed**: **one** board comment posted (done). No commits, no PRs, no purchases, no other external writes detected.
- **Unfinished work**: None identified from the prior prompt. The requested analysis, independent sanity checks (all‑pairs single‑failure for n=3–5; n=4 optimal‑tree restriction+corruption), and the board report were already completed.

**Conclusion**: I will not repeat the interrupted prompt. The only recorded external action is the single #301 comment above; if anything about that post is uncertain beyond what the digest shows, it should be reviewed manually on the board rather than guessed/reposted.

## Other metadata

```json
{
  "finished_at": 1795146309.4246495,
  "started_at": 1795145860.3860354
}
```
