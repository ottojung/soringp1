# minimax-equals-info-only-large-n

## status

investigated

## origin

ai_proposal_unverified

## agent_id

tbdgId5Cb4MrzqSjZopn8r-blazed

## exit_state

clearexit

## question

Prove or disprove for all sufficiently large n that the equality S(n)=ceil(log2(n!)) holds iff every minimax-optimal first move produces two subproblems with log2(e(P1))+log2(e(P2)) within o(1) of log2(n!) and the information bound is tight recursively under all optimal strategies (the 'information-theoretic closure' property), or find a counterexample family where information bound is tight globally but no strategy achieves recursive tightness for all n.

## basis

Known equality at {1..11,20,21} and gaps elsewhere (docs/research-certificates-barriers.md, literature); e(P) gives necessary log2(e) bound but not sufficient and not determining of minimax (research-plan notes).

## falsifier

Construct an infinite family where S(n)=ceil(log2(n!)) but for every minimax-optimal strategy at some level the split gives imbalance forcing S(n) > ceil(log2(n!)) in a way not visible from total e alone, or prove recursive closure is automatic.

## implication

Clarifies when equality cases are 'fragile' to strategy choices versus strategy-independent; bears on whether the exact-reset/divisibility obstructions can only hit in tight information-bound regimes.

## finding_unverified

 power of two). The meaningful discriminator: do optimal trees exist that visit only *individually info-tight* states (m = ⌈log₂ e⌉, slack allowed)? This decides whether recursive-tightness failure is avoidable by strategy choice at all:
Clean and dirty optimal trees *coexist* at n=6 while n=5 forces clean trees everywhere — recursive info-tightness is strategy-dependent at n=6. Sharpening the instance data (max local gap, depth distribution, spare-bit exactness):
The printed "violations" is a bug in my checker's comparison (it compared the gap against the spare count rather than the mass inequality). Correct Theorem-1 check — for every reachable state, L0(P) ≤ C−d, and for loose ones the strengthened e ≤ 2^(C−d−1):
The theory and instance are verified. Before reporting, one attempt to check the phenomenon persists at n=7 (bounded), to see whether "loose states reachable in tight trees" is a persistent pattern or an n=6 artifact:
n=7 (tight, S(7)=13=C(7)) shows the same phenomenon — 64k loose states reachable at budget, again with exactly one spare bit (e=420=2^9 at depth 3). The mechanism is persistent, not an n=6 artifact. I have a complete, independently checkable result. Per the research contract (findings go to board #301, no repo changes), let me post the report:
Report posted to board #301 exactly once (verified at 19:56:49Z; no duplicates — the interrupted turn never posted). Worktree clean, no repo/Lean changes.

## Result summary

**The front's biconditional is refuted under both readings; the salvageable all-n content is a new "one-bit slack rule".**

**Theorem (paper proof, all n, any tree).** If a depth-d reachable state P in a correct height-h tree is locally loose (m(P) > ⌈log₂ e(P)⌉), then e(P) ≤ 2^(h−d−1). Corollary: in any height-C(n) tree, every *critically loaded* reachable state (e > 2^(C−d−1)) is exactly info-tight — m(P) = ⌈log₂ e(P)⌉ = C−d, strategy-independent.

**Refutations (verified computationally):**
- **First-move condition vacuous:** every antichain comparison splits e exactly n!/2 : n!/2 (swap-involution symmetry; checked n≤11). Literal reading — sum within o(1) of log₂ n! — unsatisfiable for all n ≥ 4 (sum = 2log₂(n!/2) = log₂ n! + (log₂ n! − 2) → diverges), so the iff fails at literature-tight n=20, 21 by published values alone.
- **Recursive tightness not necessary at tight n:** n=6 (S=C=10) has 1440 locally-loose states reachable in some optimal height-10 tree — all with gap exactly 1 and mass exactly 2^(C−d−1) (rule attained at zero margin) — plus independently existing clean optimal trees: **clean and dirty optimal trees coexist**. n=7 (S=C=13) reproduces this (64k loose states in the explored subset, again zero-margin). n=5 by contrast forces clean trees. So the property is strategy-dependent at tight n, not forced by equality, and not uniform across equality cases.
- **Falsifier mechanism impossible:** local split imbalances can never force S(n) > C(n) — by the theorem they cost ≤ 1 level, absorbed by one spare bit; only *global tree non-existence* (Wells' slack exhaustion at n=12) produces gaps. So exact-reset/divisibility-type obstructions can only bite where slack is exhausted, never inside tight regimes' critical states.

**Honest limits:** exhaustive only through n=7 (n=7 capped at 400k states); no tight n ≥ 22 known, so "all sufficiently large n" can't be instantiated computationally today; sufficiency direction ("conditions imply tightness") remains equivalent to the original hard problem.

## Other metadata

```json
{
  "finished_at": 1793735843.0963705,
  "started_at": 1793729827.3322585
}
```
