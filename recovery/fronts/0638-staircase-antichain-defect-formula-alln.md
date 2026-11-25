# staircase-antichain-defect-formula-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ctahUF2K5HzSXNWQ9HfrAS-defeated

## exit_state

clearexit

## question

For every a,b >= 1 with a+b >= 3, let Z_b be the staircase poset on b elements (i<j iff j>=i+2) that board #301 identifies as attaining the maximum local information excess R(b), let A_a be the a-antichain, and let delta(a,b)=F(Z_b disjoint-union A_a)-F(A_a)-F(Z_b) be the exact minimax disjoint-union defect. Is delta(a,b) >= min(a,b)+1 for all such a,b, and can delta be given by a closed form, in particular for each fixed a where does the surplus delta-(min(a,b)+1) first become positive?

## basis

Board #301 2026-11-21T08:02Z/08:05Z reports that R(n)=max local excess grows linearly via Z_n (e=Fib(n+1), F=n-1) and that the global R-table sufficient condition fails; Viche reports F(Z_b sqcup singleton)=b+1 for b<=5 and b+2 from b=6. My scratch bitmask minimax (no repo change) computed delta(a,b) for a<=3,b<=5: delta>=min+1 in every case except the known excluded (1,1), with zero surplus for small b and a positive surplus appearing at b=4 for a=2,3 and at b=6 for a=1.

## falsifier

Exhibit a,b with a+b>=3 and an independently checkable exact-minimax computation giving F(Z_b disjoint-union A_a) <= F(A_a)+F(Z_b)+min(a,b), i.e. a defect violation; or exhibit two pairs (a,b) whose exact delta values refute a proposed closed form or surplus-boundary rule.

## implication

Z_b attains the maximal local excess, so it is the hardest component for the defect inequality; an all-(a,b) formula or bound for delta settles the extremal case of F(A disjoint-union B)>=F(A)+F(B)+min+1, the lower-bound recursion underlying S(n)=F(A_n)=F(A_a disjoint-union A_b), and thereby constrains uniform exact evaluation of the unary sorting-number function.

## finding_unverified

 option 2):** the pairs `(3,4)` and `(3,5)` refute the rule `delta(3,b)=b+1` (predicts 5 and 6; actual 5 and 5), the "surplus = b−3" boundary rule, and the composite `⌊(a−1)b/2⌋+a−S(a)+1`. More generally, the sort-then-binary-insert strategy gives the rigorous bound `delta(a,b) ≤ Σ_{i=1}^a ⌈log₂(b+i)⌉ = O(a log b)` for fixed `a`, so **any** linear-in-`b` closed form is false for large `b` (e.g. `(2,14)`: bound 8 < predicted 9; `(3,20)`: bound 15 < predicted 21). Any true closed form must be merge/logarithmic in shape, and the surplus thresholds are only computationally verified, not proved for all `b`.

## Soundness ≠ completeness

- The staircase lemma `e=Fib(n+1), F=n−1, r≈0.3058n` is a **sound lower bound** — and precisely why the R-table sufficient condition fails for every fixed-`a` large-`b` split. A sound certificate does not make that method complete.
- General-poset SUPI results (Kahn–Saks; Cardinal et al. STOC'10; van der Hoog–Rutschmann FOCS'24) give `Θ(c·log e(P))` *approximate* query bounds with preprocessing — sound upper bounds on `F`, **not** exact `F` and not a uniform polynomial-time evaluator; they imply nothing about `SORT-BOUND-U ∈ P/NP`.
- The defect recursion is a sound lower-bound tool for `S(a+b)`, but its all-`n` proof remains open; exact minimax is sound but finite.

## Honest limits

No violating pair was found (so the inequality's option 1 is not delivered), no all-`n` proof or closed form was established, and the surplus-boundary rules are unverified beyond the computed range. `S(n)` and `SORT-BOUND-U` remain open. I did not attempt a further exhaustive enumeration or new Lean formalization, as neither would change what is known here.
Let me inspect the durable state to confirm what actually happened and avoid duplicating anything.
Confirmed. Let me also check the durable task ledger entry to report its state accurately.
Inspection complete. No duplication needed — the previous turn's external action had already landed exactly once.

## What actually happened

- **Git:** `billy-dev`, worktree clean, HEAD `6a96398` unchanged. No commits, no repo/Lean/CI/test/main/ledger/bill/ballot edits.
- **Board #301:** exactly **one** post by the required author tag `SoringP1 researcher: staircase-antichain-defect-formula-alln`, created `2026-11-21T09:01:10.754Z`. Confirmed by fetching the board twice after the backend recovered.
- **Scratch:** only `/tmp/opencode/front_defect/` (minimax scripts, board JSON captures, post draft). No repository files were touched.
- **Ledger:** the front entry `staircase-antichain-defect-formula-alln` still reads `status: running`, agent `ctahUF2K5HzSXNWQ9HfrAS-defeated`, started 08:42:29. This is a stale durable record, not something I modified (the contract forbids agents changing the ledger). Flagging it for the keeper/review rather than editing it.

## Uncertainty noted

One intermediate board fetch (`board_after2.json`) returned a 0-byte file during the backend failure; the retry (`board_after3.json`, 137,997 bytes) confirms a single post and no duplicate. So the empty file was a transient fetch failure, not a missing or repeated action.

## Unfinished work

None. The single board post (falsifier delivered: pairs `(3,4)`/`(3,5)` refute the `delta(3,b)=b+1` closed form; asymptotic merge upper bound `O(a log b)` refutes linear-in-`b` forms; no defect-violation counterexample found; soundness-vs-completeness distinction recorded) was already delivered and confirmed. I did not repeat it.

## Other metadata

```json
{
  "finished_at": 1795251785.4166086,
  "started_at": 1795250549.8818018
}
```
