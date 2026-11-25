# antonina-euaQLf1AlP7yDM7sysamhR-seated

Session: ses_e3ef62387ffeT8HAnDyVLS4qaE
Workspace: /home/lubko/soring-fronts/merge-block-ordinal-supremum-n9
Created: 1794240011438; updated: 1794240865910

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 591 (msg_1c116c55c001wD8FZ8Z6pJL77k)

**Finding (board #301 posted, 16:14Z).** No 9-element poset exceeds the constant. The exhaustive exact computation over all **183,231** unlabeled posets on 9 elements gives

\[
\max_{|B|=9}\frac{F(B)-\log_2 e(B)}{\operatorname{covers}(B)+M(B)m(B)}
=0.13637764662879948
< \frac{5-\log_2 15}{8}=0.13663867554893516,
\]

with zero violations. The maximum is attained by a dual pair:

- `succ=(0,1,1,3,3,5,11,19,183)`: \(e=181,\ F=9,\ \mathrm{covers}=9,\ (m,M)=(2,1)\);
- its dual `(0,0,1,1,2,5,9,55,255)`: \((m,M)=(1,2)\).

Both have denominator \(9+2=11\). The antichain value is \(F=19=S(9)\).

**Why n=9 does not rise.** The maximizer is a one-point extension of the n=8 maximizer. Adding the point changes \((\mathrm{covers},m,M)\) from \((7,2,2)\) to \((9,2,1)\), leaving the denominator and the alpha value unchanged. So the n=8 consistency value is structurally reproduced at n=9, not broken.

**Verification.** I reran `quotient_classes(9)` from the current worktree (`6a96398`), obtaining an output identical to the earlier exact `vals9` data. Extension counts came from an independent subset DP; covers, minima and maxima from direct definitions. The top 30 classes were rechecked with the independent plain labelled `structural_lower_bounds.minimax` and an independent linear-extension DP: 30/30 agree, 0 mismatches. Worktree remains clean; no Lean or repository changes.

**Failed falsifier attempt, and the concrete trap.** I tried to build an n=10 counterexample by one-point extensions of the top ten n=9 maximizers. Among all such extensions with denominator \(\le 12\), the maximum was still only `0.1250128427`; none exceeded the constant. An earlier apparent n=10 counterexample with ratio `0.1492` was spurious: the extension routine inserted \(d<x<u\) without adding the forced relations \(d<u\), so the state was not transitively closed. After adding the closure, the exact value dropped to \(F=7\), ratio `0.0659`. This was a bug, not a theorem.

**Honest limits.** This is an exhaustive finite theorem for n=9 about the fixed-block ordinal-sum ratio. It does **not** prove the inequality for all n, does not give an n=10 or all-n counterexample, and says nothing new about \(S(n)\), `SORT-BOUND-U`, or complexity classes. The leaf certificate \(C(P)=\lceil\log_2 e(P)\rceil\) is sound but not complete; the ratio measures its incompleteness. General-poset SUPI results give constant-factor approximations, not exact minimax, and do not transfer to the antichain root. An all-n inequality or an n≥10 counterexample remains open.
