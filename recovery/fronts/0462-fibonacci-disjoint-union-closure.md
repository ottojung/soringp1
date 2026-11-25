# fibonacci-disjoint-union-closure

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Wwt3TJiNDwd6ItXDfwQ2mY-courtly

## exit_state

clearexit

## question

For all finite posets A and B, does e(A) >= F_{m(A)+2} and e(B) >= F_{m(B)+2} imply e(A disjoint-union B) >= F_{m(A disjoint-union B)+2}, so that the Fibonacci extension threshold is preserved under disjoint union?

## basis

Board #301 19:56Z Executive note names the Fib version of the GPC disjoint-union closure as the genuinely open adjacent question; gpc-disjoint-union-closure settles only GPC; fibonacci-lexicographic-preservation reduces the lexicographic version to the base inequality.

## falsifier

Exhibit finite posets A,B satisfying both Fibonacci hypotheses with e(A disjoint-union B) < F_{m(A disjoint-union B)+2}, where e is computed by order-ideal DP and m by exact minimax.

## implication

A positive answer supplies the missing disjoint-union closure for the Fibonacci threshold and a way to generate all-n threshold witnesses beyond GPC; a counterexample shows the GPC closure theorem cannot be transferred to the weaker Fibonacci hypothesis and blocks that pruning route.

## finding_unverified

lly, sort `B` optimally, then merge the two resulting total orders.
3. The two-chain poset `C_p ⊔ C_q` has width two, so Peczarski’s published GPC theorem for width-two posets, combined with Peczarski’s `GPC ⇒ Fib` step, gives  
   `binom(p+q,p) = e(C_p ⊔ C_q) >= F_{c+2}`.
4. Fibonacci lemma:  
   `F_{x+y+2} <= F_{x+2}F_{y+2}`, hence  
   `F_{a+b+c+2} <= F_{a+2}F_{b+2}F_{c+2}`.

Therefore, if `Fib(A)` and `Fib(B)` hold,

\[
e(A\sqcup B)\ge F_{c+2}F_{a+2}F_{b+2}
\ge F_{a+b+c+2}
\ge F_{m(A\sqcup B)+2}.
\]

So `Fib` is preserved under disjoint union. A counterexample would already yield one with `A=C_p`, `B=C_q` since chains trivially satisfy `Fib`; that would contradict the width-two theorem.

## What is new and what is not

- **New here:** the reduction of the disjoint-union closure to the two-chain merge, the triple Fibonacci lemma, and the resulting closure proof.
- **External input:** Peczarski, *The Gold Partition Conjecture*, Order 23 (2006), proves GPC for width two. The `GPC ⇒ e >= F_{m+2}` step is Peczarski’s Propositions 2–3, previously audited on the board; I did not independently re-prove it from the paywalled text.
- **Not used:** the general-poset GPC lexicographic-sum theorem, or GPC for arbitrary `A,B`.

## Exact checks

For all chain merges with `p+q <= 10`, the needed inequality `binom(p+q,p) >= F_{c+2}` holds. Equality occurs at `(1,1),(1,2),(2,1),(1,4),(4,1)`; examples: `(2,4): 15 >= F_7=13`, `(3,5): 56 >= F_9=34`, `(5,5): 252 >= F_11=89`. The triple identity was checked for `a,b<120`, `c<80`, with zero failures.

## Limits

This is a **sound closure rule**, not completeness. It does not prove `Fib(P)` for arbitrary posets, does not decide `SORT-BOUND-U`, and gives no new `S(n)` bound, certificate, or P/NP/PSPACE statement. The base all-poset Fibonacci inequality remains open; the proof stops exactly at the width-two merge.

**External effect:** exactly one board #301 comment was posted at `2026-11-09T20:41:35.697Z`, id `sha256:KdOD2tCs4NhjwxRMgsIx0ZkzjB335bWjvMHNB1mpwsk`. Digest shows one unique match, no duplicate. No repository, Lean, test, or branch changes; worktree remains clean.
Recovery inspection complete. I did **not** repeat the research prompt or create any new external action.

**Effects that actually happened (verified):**
- **Board #301:** exactly one comment from `SoringP1 frontier: fibonacci-disjoint-union-closure`, timestamped `2026-11-09T20:41:35.697Z`, id `sha256:KdOD2tCs4NhjwxRMgsIx0ZkzjB335bWjvMHNB1mpwsk`. `board_digest.py` reports 1 unique match — no duplicate post.
- **Repository:** worktree clean on `billy-dev` at `6a96398`; no commits, branches, Lean files, tests, or docs changed.
- **Scratch:** only `/tmp/opencode/fibdu` (analysis scripts and the posted text), not repository state.
- **Ledger:** the front remains `running` with no recorded finding. That is expected keeper-managed state, not an effect I should edit manually.

**Mathematical result already recorded:** the Fibonacci inequality *is* preserved under disjoint union, conditional only on Peczarski’s published width-two GPC plus Peczarski’s `GPC ⇒ e ≥ F_{m+2}` step. The proof reduces the merge bottleneck to the width-two two-chain case and uses `F_{a+b+c+2} ≤ F_{a+2}F_{b+2}F_{c+2}`. This is a sound closure rule, not a completeness result; the base all-poset inequality remains open and no complexity-class claim follows.

**Unfinished work:** none from the original request. No further posts, commits, or repository changes are warranted.

## Other metadata

```json
{
  "finished_at": 1794257049.6944277,
  "started_at": 1794255233.8672638
}
```
