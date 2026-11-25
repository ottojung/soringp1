# antonina-tlMkWf7UhrpIL9Zpib8PVs-punctures

Session: ses_e10e938e0ffeyxoqX3Gityl7Si
Workspace: /home/lubko/soring-fronts/n12-obstruction-invariant-generalization-20261118
Created: 1795012609872; updated: 1795013453474

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 564 (msg_1ef2399ce001UJUmwMnPTCsZvW)

Done. Posted the research report to board issue #301 as author "SoringP1 frontier: n12-obstruction-invariant-generalization" (timestamp 2026-11-18T14:50:36Z). Worktree remains clean at 6a96398; no repo/Lean/test changes.

Summary of the report:
- **Question:** Can the n=12 obstruction S(12)=30>C(12)=29 be explained by a generalizing poset invariant (component reversal defect, Fibonacci split, or antichain reachability)?
- **Result:** No. None of the three families survives:
  - *Antichain reachability (#antichains):* computationally unsound (I>F for 18/182/2190 posets at n=3/4/5) and too weak on antichains (I_R(A_n)=n ≪ C(A_n)).
  - *Component reversal defect:* vanishes on antichains (comparability graph has no edges → defect 0), so it can never exceed C at A_12; only helps on already-covered decomposable posets.
  - *Fibonacci split:* on antichains any invariant is a function of n; no Zeckendorf predicate reproduces the irregular excess pattern (0 for 1–11, 1 for 12–19, 0 for 20–21, 1 for 22) without being unsound on tight n (e.g. n=11=8+3 has 2 terms).
- Extends the prior pair-split barrier: no surveyed family (L_k, merge-factor, scalars, or the three new candidates) is strictly above C at A_12; the +1 is a global routing property (Wells empties level S_24; Stober–Weiss sortable=no). Open obstacle: a compact checkable certificate of S(12)>29, or a family-specific barrier theorem.
