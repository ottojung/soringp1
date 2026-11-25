# cross-cost-additivity-ceiling-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

JBM9oMcOCQhcrDkatBgKZw-duties

## exit_state

clearexit

## question

For the exact adaptive minimax F, how far can the additive cross-cost lower bound fail? Determine whether the deficit D(a,b,B)=F(B)+ceil(log2 binomial(a+b,a))-F(C_a disjoint-union B) is bounded by a constant over all a,b>=1 with a+b>=3 and all b-element posets B, or grows without bound; here C_a is a chain and the fresh board theorem only gives a cross-comparison count on some path, not additivity with F(B).

## basis

Fresh #301 non-potential theorem (16:31Z) gives cross comparisons at least ceil(log2 binomial(a+b,a)); an independent from-scratch minimax computation yields deficit-1 candidate witnesses (a,b,B)=(1,4,A_4),(2,3,A_3),(3,4,A_4), which are finite checks and not an all-n theorem. No ledger front treats cross-cost additivity with the binomial bound.

## falsifier

Exhibit a chain C_a and poset B with F(C_a disjoint-union B) at most F(B)+ceil(log2 binomial(a+b,a))-2, from an independent exact minimax computation, or prove the deficit is unbounded above over all a,b.

## implication

Fixes the exact reach of additive 'internal cost plus cross-cost' lower bounds for disjoint unions: a bounded deficit would salvage a sharpened decomposition recursion for exact S(n), while unbounded growth rules out the whole additive family motivated by the board's cross-comparison theorem.

## finding_unverified

Let me fetch the exact known sorting numbers to analyze the excess Δ(n)=S(n)−⌈log₂ n!⌉.
I've found a clean exact decomposition of the deficit. Let me test the remaining criterion (Δ(B)=1, g=1, Δ(P)=0) on the best candidate posets.
I'll re-inspect state after the interruption before continuing.
State is clean — no external side effects from my front. Let me read the new board posts that reference this front before finalizing the analysis.
State is clean and I've completed the mathematical work. Let me find the correct board-post command, then make exactly one post.
I'll write the finding to a scratch file, then post exactly once to board #301.
The post command succeeded; let me verify exactly one comment landed.
Done. After the backend-failure interruption I re-inspected state: the repo was clean at `6a96398`, no commit/stash/board post from this front existed, and the ledger still showed it `running`. No effects were duplicated. I resumed the computation, finished the analysis, and made exactly one board post (verified: a single comment, 18:15:35Z).

## Mathematical finding

**Exact decomposition (deduction, all-n).** Let `F` be the exact adaptive minimax, `e(P)` the extension count, and define the information excess `Δ(Q) = F(Q) − ⌈log₂ e(Q)⌉ ≥ 0`. For `P = C_a ⊔ B`, with `C = binom(a+b,a)` and `e(P) = C·e(B)`:

```
D(a,b,B) = Δ(B) − Δ(C_a ⊔ B) + g(a,b,B),   g = ⌈log₂e(B)⌉ + ⌈log₂C⌉ − ⌈log₂(e(B)·C)⌉ ∈ {0,1}.
```

So `D ≤ Δ(B) + 1`, and **`D ≥ 2` forces all three of**: `Δ(B) ≥ 1` (B strictly beats its own information bound), `g = 1`, and `Δ(C_a ⊔ B) = 0` (the union is information-tight). Unbounded `D` therefore requires unbounded `Δ(B)`. For the antichain family this reduces further to `D(1,b,A_b) = −d(b+1) = Δ(b) − Δ(b+1) − [ceiling bracket]`.

**Falsification search (from-scratch minimax, validated on S(n) for n≤6 and all three stated deficit-1 witnesses).** Exhaustive over all 4231 labelled b=5 posets (a=1,2), all b≤4 with a+b≤7, all 130023 b=6 posets screened for Δ plus top candidates tested, and 13602 sampled b=7 posets: **maximum observed D = 1**. No `D ≥ 2` witness. Best near miss: b=7, F(B)=6, e=21, a=2 has `Δ(B)=1` and `g=1` but `Δ(P)=1`, giving D=1.

**Concrete failed approach.** A natural non-closed potential `Φ(Q)=F(B_Q)+log₂ I_min(Q)−1` on cross-augmented states is refuted: at root (a=1,b=3,A₃), `Φ=4` but both children of a cross comparison have `Φ=2` (interleaving count collapses 4→1). This is a different obstruction from the already-closed `m+1` potential no-go — here the interleaving-count term itself is not 1-Lipschitz under cross transitivity.

## Honest limits

I did **not** prove `D ≤ 1` for all a,b,B, nor exhibit `D ≥ 2`, nor prove unboundedness. The question reduces to the all-n behavior of the minimax excess `Δ`: it is 0/1 for antichains through n=22 (OEIS A036604) and ≤1 for every poset I checked up to size 7, but its all-n behavior is open. This concerns exact minimax only — no general-poset hardness transfer and no certificate-completeness claim is made. No repository, Lean, test, CI, or ledger changes; scratch work is in `/tmp/opencode/crosscost/`. S(n) and SORT-BOUND-U remain open.

## Other metadata

```json
{
  "finished_at": 1795284977.3934836,
  "started_at": 1795280737.6660671
}
```
