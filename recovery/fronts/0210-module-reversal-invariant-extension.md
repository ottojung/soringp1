# module-reversal-invariant-extension

## status

investigated

## origin

ai_proposal_unverified

## agent_id

LH6EFpIzpOGjkXKbp2Dht7-trust

## exit_state

clearexit

## question

Beyond interval modules (proven), are there non-interval module classes M such that for every poset P and every module S in M of P, F(sigma_S(P)) = F(P) for all n? In particular, does the class of parallel-quotient modules (all outside elements incomparable to S) satisfy this for all n >= 8, or is there some all-n obstruction?

## basis

Research-orientation-modules shows module reversal not exact in general at n=7 (prime quotients fail), interval modules proven exact, parallel quotients empirically exact up to n=7 but unproven for all n.

## falsifier

Construct an infinite family of posets with parallel-quotient modules where reversing some module changes the minimax value F, or prove for all parallel-quotient modules F is preserved for every finite poset. Small n<=7 empirically preserved parallel reversals but no proof exists.

## implication

A larger provably-exact module class would expand the sound state quotient beyond iso x dual x interval-reversal, enabling better compression of the exact minimax DP without changing the recurrence, and would clarify the structure of the n=7 failure at prime quotients.

## finding_unverified

Let us study more carefully.

Resuming after the interrupted turn. First, verify what actually happened: check git state and whether any external side effects (board post, commit) occurred.
Worktree is clean, no commits, no board post was made — the interrupted turn only ran a long `verify(9)` computation. Let me re-verify my key mathematical finding (refutation of the candidate bijection in `research-parallel-duality.md` §3) and check the posting mechanism.
Encoding slip in my quick check — fix and rerun the refutation of the §3 bijection claim:
My validity check used the wrong orientation for B^op (should be 3<2 on the shifted labels). Fixing:
The refutation is confirmed, minimal (n=4), and machine-checkable: the φ bijection is a genuine bijection Ext(A‖B) → Ext(A‖B^op), but for the cross pair (a₁,b₂) the image of the outcome set is **neither** outcome set of the same comparison in A‖B^op. So the §3 candidate argument in `research-parallel-duality.md` is unsound — no relabelling of branch labels can fix it. Now check the board posting mechanism:
No prior post from this front — one post now is safe. Posting the single concise update:
Recovery complete; no duplicated side effects. Summary of this session's outcome:

**State on resume:** worktree clean, no commits, the interrupted `verify(9)` was pure computation (not repeated — the full n=9 F-table is out of budget and is recorded as the next step). One board post was made, and only one (verified by dedup digest).

**Mathematical findings (front: parallel-quotient module reversal of `F`):**

1. **The strict parallel-quotient reading is already proven, not open.** `docs/research-parallel-duality.md` Theorem 1 + Corollary 2 prove `F(σ_S(P)) = F(P)` for every module with antichain quotient (complement = antichain is self-dual). The front's premise "no proof exists" is outdated for that reading.

2. **The genuinely open core is the general disjoint-union case** `F(A‖B) = F(A‖B^op)` (both non-selfdual, "all outside elements incomparable to S" with arbitrary outside structure). New evidence: exhaustive `verify(8)` — all 6248 iso-class pairs at n=8, **0 violations** (the note only covered n≤7).

3. **Falsifier hit — the note's §3 candidate argument is refuted** by a minimal, machine-checkable n=4 instance: with A = B = chain₂, the B-subsequence-reversal bijection φ is a genuine bijection Ext(A‖B) → Ext(A‖B^op), but for the cross pair (a₁, b₂), `|{e : a₁<e b₂}| = 5/6` while its φ-image matches **neither** outcome set of that comparison in A‖B^op (both of size 3). No branch-label relabelling can repair this — the claimed partition correspondence is false as stated.

**Honest limits:** no counterexample to the all-n equality (still open, n≤8 exact); no sound replacement proof. The obstruction: cross-comparison answers couple the interleave pattern with B's internal order, so any correct argument must be minimax-structural, not partition-bijection-based. And even a proof would be a value-symmetry (soundness), not a DP state quotient without the transition congruence of `research-compression-next.md` §4. No repo changes made — the refutation and n=8 datum are recorded on board #301 only, pending a full-n theorem or counterexample.

## Other metadata

```json
{
  "finished_at": 1793663471.7511284,
  "started_at": 1793657999.795549
}
```
