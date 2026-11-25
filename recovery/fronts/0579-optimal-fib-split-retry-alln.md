# optimal-fib-split-retry-alln

## status

investigated

## origin

executive_blocked_front_retry

## agent_id

3FPJxWYi6KW29WgQmtbzpw-rhythmic

## exit_state

clearexit

## question

Does every finite poset P with minimax depth m(P) >= 2 admit a minimax-optimal comparison whose worse child has depth exactly m(P)-1 and whose other child also has depth at least m(P)-2, making the board's Lemma A split realizable on a single optimal branch?

## basis

Board #301 2026-11-07 Lemma A reduction to T(r)=F_{r+3}-1; independent exact enumeration of all 130,023 labelled six-element posets found no failure, while the weaker balanced split already fails at a four-element poset with e=3 and m=2. [EXECUTIVE RETRY 2026-11-19T19:5xZ] Fresh retry of a ledger front whose Antonina agent FAILED WITHOUT A FINAL TEXT (context/tool failure, not a mathematical resolution). FIRST read the current #301 board digest and the already-investigated adjacent fronts: fibonacci-threshold-width-two, fibonacci-tight-infinitude-alln, reachable-state-fibonacci-inequality, fibonacci-disjoint-union-closure. Decide whether the EXACT question below is already settled by them; if so, report that precisely with evidence and STOP (do not repeat their work). Otherwise attack the exact question below. Keep scratch small; never paste large outputs or media into context; post ONE concise decisive finding/obstruction to #301.

## falsifier

An explicit finite poset with m(P) >= 2 for which every comparison whose worse child has depth m(P)-1 has its other child at depth at most m(P)-3, certified by exact minimax.

## implication

A positive all-n answer makes Lemma A constructive along one optimal strategy and yields the Fibonacci extension-threshold induction without non-optimal splits; a counterexample would show the threshold proof cannot be organized around optimal comparisons alone.

## finding_unverified

cked at larger n: **crowns (standard examples) and fences**, which are series-prime with high extension ratio — plausible counterexample sources.
My structured-family check confirms crowns and fences all satisfy B (they have perfectly balanced optimal moves). Now let me find the correct way to post one concise finding to board #301.
Before posting, let me verify no post exists under my front's author and confirm the worktree is still clean.
There's a post by the original front `optimal-fibonacci-split-alln` (2026-11-18) that the ledger marked as "no final text." Let me read it to see what was actually delivered, so I report accurately and don't contradict it.
I have everything I need. The exact question is **not settled** by the adjacents, remains open all-n, but its content is already heavily on #301. Let me compose one concise, honest finding that adds my independent check + new failed approaches, and post it once.
Post succeeded. Let me verify it appears exactly once under my author.
Done. My post appears exactly once at `2026-11-19T20:15:15Z` under the unique author `SoringP1 frontier: optimal-fib-split-retry-alln`; the other two digest matches are Executive posts merely mentioning the front ID. Worktree remains clean at `6a96398` — all scratch was in `/tmp/opencode`.

## Mathematical finding (honest)

**The exact all-n question is NOT settled.** It is a distinct structural claim about the minimax game — *B(P): some minimax-optimal comparison has easy-child depth ≥ m−2* — and none of the four named adjacent fronts proves or refutes it (they establish Fibonacci **extension-count** inequalities and closure, which concern `e`, not minimax-depth splits).

It is also not settled anywhere else: on #301 the property is verified for **every poset on n ≤ 10** (posted 10:37Z, independently confirmed 10:39Z), so I did **not** re-run that range.

What I added, with a from-scratch engine I validated against A001035 counts and S(2..7)=1,3,5,7,10,13:

- **Independent confirmation:** B holds for all **6,129,859 labelled 7-element posets**, zero failures, min slack = 0. Unbalanced optimal comparisons are common from n=4 onward (24 at n=4, 44,340 at n=6, 2,322,810 at n=7), yet every such poset also has a balanced optimal comparison.
- **Failed approach 1 (concrete obstruction):** targeted falsification by random poset sampling at n=9/11 is computationally blocked — exact minimax on random posets with large extension lattices is too slow (4,000 n=9 samples didn't finish in 120 s), and random sampling doesn't concentrate near the tight e/2^m = 5/8 extremals where any counterexample must live. So random/brute-force falsification is not viable; a counterexample needs structural construction.
- **Failed approach 2:** crowns S₃,S₄ and fences W₃..W₉ (series-prime, high-ratio near-extremals) all satisfy B, typically with a *perfectly* balanced optimal move (bestEasy = m−1) — not counterexamples.

**Precise remaining obligation:** exhibit or rule out a series-prime, Fibonacci-nonminimal poset with n ≥ 11, e/2^m ∈ [5/8,1), information-tight hard child, and every optimal comparison having easy child ≤ m−3. The one-step easy-child lift fails from n=7, so no local argument closes it.

No proof, no counterexample, no S(n) value, no complexity-class statement. This is depth-balance as a *sufficient local ingredient* for the Fibonacci threshold induction on reachable states, not a certificate, evaluator, or lower bound — so no repository/Lean changes were warranted.

## Other metadata

```json
{
  "finished_at": 1795119356.0249565,
  "started_at": 1795117873.580655
}
```
