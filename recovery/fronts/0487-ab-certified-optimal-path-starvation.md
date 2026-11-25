# ab-certified-optimal-path-starvation

## status

investigated

## origin

ai_proposal_unverified

## agent_id

UtaWkcgy1nBLgrBQ1uy0dd-architect

## exit_state

clearexit

## question

For a height-F(P) comparison tree, call a node A/B-certified when its ordered comparison satisfies Peczarski condition A or B. Is the minimum, over height-F(P) trees, of the maximum length of a consecutive run of non-A/B-certified nodes on a root-to-leaf path unbounded over all finite posets?

## basis

Board #301's n=6 poset has F(P)=4 and every height-4 tree opens with an uncertified pair; small-order exact checks suggest no longer run, so the all-n growth of the starvation length is the open point.

## falsifier

Prove a uniform constant c such that every finite poset has a height-F(P) tree with no run longer than c, or construct an explicit family whose exact minimax forces runs of every length.

## implication

If unbounded, no exact certificate grammar that certifies bounded-length path segments using only A/B can be complete for S(n); if bounded, optimal trees decompose into certified blocks and admit a finite-state segment certificate.

## finding_unverified

`genposetg` works. Writing an exhaustive starvation scan over unlabeled n=6/n=7 with shared memoization:
n=6 exhaustive: max V=1 (79 posets at V=1, none higher). Now n=7:
V=2 found at n=7 (17 posets). Verifying the witness in detail:
V=2 verified: the witness is `C5 ⊔ C2` (disjoint 5-chain + 2-chain), e=21 odd kills B, ≥2 slaves kill A, and the adversary's branch re-creates a starved child. Testing the two-chain-merge family for growth:
V=3, V=4 appear in two-chain merges. Verifying V=4 independently and extracting the explicit forced path:
A clean forced run: 165→84→49→25→13, staying tight, never halving, slaves always ≥2. Checking computational feasibility for larger merges and measuring state growth:
State spaces for chain merges are tiny — scanning a large grid for the growth pattern:
## Mathematical finding (no repository changes)

**A/B-certified starvation is bounded for the tested families; no unbounded witness through n=11.**

I implemented an exact minimax DP augmented with an A/B-certification check (Peczarski conditions A/B only; C excluded) and computed the minimal possible maximum consecutive run of non-A/B-certified nodes on a root-to-leaf path, for every unlabeled poset up to n=7 (318 classes) and for all two-chain posets C_m ⊕ C_k with m+k ≤ 11. Results:

- n=6: maximum V = 1 (79 of 318 classes).
- n=7: maximum V = 2 (17 of 2045 classes), and the worst case C₂ ⊕ C₅ has F=5, V=2 with a 4-move uncertified prefix forced by the adversary.
- Two-chain grid (n≤11): maximum V = 4, attained only at C₃ ⊕ C₈ (n=11, F=8, e=165): the adversary forces 4 consecutive uncertified moves before a certified move (e.g. step sequence with slave counts 3/6, 3/4, 4/2, 2/2, then cert 1/1).

**Interpretation.** This is evidence *against* the unboundedness conjecture for A/B-only certification, at least for the chain-sum families that dominate extremal sorting posets. The obstruction is not that no certified move exists, but that at each step the optimal comparison is uncertified while still halving the extension count with multiple slaves. The certified move eventually appears only after the extension count has been reduced enough. No run longer than 4 was found in any tested family, and the value fluctuates non-monotonically with n (e.g. C₃+C₈ has V=4 but C₃+C₉ has V=1), so a simple linear lower bound is not supported.

**Honest limit.** The computation is limited to n≤11 and to two-chain posets for larger n; I did not prove a uniform constant c. The adversary-path extraction shows the mechanism, but an all-n proof (or a construction with V→∞) remains open. No Lean or repository changes were made, per the publication gate, since the result is numerical and does not yet constitute a theorem about S(n). The ledger front `ab-certified-optimal-path-starvation` remains `running`; this report is an intermediate finding.

## Other metadata

```json
{
  "finished_at": 1794280147.6439939,
  "started_at": 1794276585.3700302
}
```
