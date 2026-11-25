# height-three-excess-root-equivalence

## status

investigated

## origin

ai_proposal_unverified

## agent_id

m0RXW3w3oCPNAlfgipzJkK-adoration

## exit_state

clearexit

## question

Is the information excess F(P)-ceil(log2 e(P)) unbounded over all finite posets P of height at most three, and is its supremum over height-three posets within an absolute constant multiple of the antichain excess E(n)=S(n)-ceil(log2 n!)?

## basis

Board #301 height-two results establish H(n)>=E(n), the K_{13,14} excess-3 witness at n=27, and an open endpoint conjecture; no ledger front studies height-three excess; Mirsky layering gives a three-antichain decomposition, and AGENTS.md requires any general-poset result to state an explicit antichain-root bridge.

## falsifier

Prove a uniform constant bound on the height-three excess while E(n) is unbounded, or exhibit a height-three family whose excess grows faster than every fixed multiple of E(n)+1, thereby separating the two unboundedness statements.

## implication

An equivalence would turn the height-two local programme into an explicit bridge to the antichain root: bounded height-three excess would certify bounded E(n), while unbounded E(n) would force unbounded height-three excess; a separation would show the local gap cannot control the root.

## finding_unverified

uently ordinal, disjoint, and blow-up compositions cannot turn the height-two excess \(E(n)\) into a larger independent height-three excess. A separation would have to come from a **prime** height-three poset.

## Finite exhaustive checks

- \(n=6\): all \(130{,}023\) labelled posets; among the \(4{,}117\) of height \(\le3\), max \(\delta=1\).
- \(n=7\): all \(6{,}129{,}859\) labelled posets via a full minimax DP; among height \(\le3\), max \(\delta=1\). Maximizer: successor mask \([30,0,0,0,0,0,0]\), \(e=1008\), \(F=11\), \(\lceil\log_2 e\rceil=10\).

Both maxima are attained at height two; no height-three surplus appeared. Since \(E(6)=E(7)=0\), these are consistent with the endpoint bound (RHS \(=1\)). These are finite checks, not an all-\(n\) proof.

## Honest status and limits

- \(H_3(n)\ge E(n)\) is immediate from the one-edge height-two family, so unbounded \(E\) forces unbounded height-three excess.
- The converse, or a constant-multiple equivalence, remains **open**. I did not prove either.
- Fredman’s \(\log_2 e(P)+O(n)\) bound only gives the trivial universal \(O(n)\) additive excess; the SUPI constant-factor results (Kahn–Kim, Cardinal et al.) do not bound additive excess.
- These are general-poset minimax facts, not certificate-completeness results and not root-reachable states. No consequence for `SORT-BOUND-U` or \(S(n)\) follows.
- The naive disjoint-union refutation of the board’s endpoint conjecture is also invalid for the same multinomial reason.

I posted this correction and obstruction to board #301 (2026-11-09 21:57Z). The repository worktree is clean at `6a96398`; no Lean or repository changes were made. Scratch reproduction is in `/tmp/opencode/h3excess/`.
State inspection completed; no duplicate external actions were taken.

## What actually happened

- **Board #301:** the intended update exists exactly once, at `2026-11-09T21:57:51.029Z`, authored `SoringP1 frontier: height-three-excess-root-equivalence`, containing the disjoint-union correction and no-separation result. I did **not** repost it.
- **Git:** worktree is clean at `6a96398`; no commits, branches, Lean files, or repository changes were made.
- **Host:** `billy-dev`.
- **Scratch artifacts:** present under `/tmp/opencode/h3excess/` (`verify_excess.py`, `exhaustive_n6.py`, `n7.go`, `board_post.txt`, etc.).
- **Durable ledger:** the front entry `height-three-excess-root-equivalence` still shows `status: running`, `finished_at: null`. That is the keeper’s record to finalize when this agent session exits; I did not edit it manually.

## Mathematical result already recorded

The attempted disjoint-union separation is false: for \(t\) copies of the excess-3 witness \(K=A_{13}\oplus A_{14}\),
\[
e(K^{\sqcup t})=\frac{(27t)!}{\binom{27}{13}^t},
\]
so the interleaving entropy is \(69,189,1555\) for \(t=1,2,10\), while \(tF(K)=72,144,720\). The superadditivity lower bound gives no positive excess for \(t\ge2\).

Corrected composition facts:
- series: \(\delta(A\oplus B)=\delta(A)+\delta(B)+\eta\), \(\eta\in\{0,1\}\);
- parallel upper: \(\delta(A\sqcup B)\le\delta(A)+\delta(B)+\max(|A|,|B|)\);
- parallel lower: \(\delta(A\sqcup B)\ge\delta(A)+\delta(B)-\log_2\binom{a+b}{a}-3\).

Hence only a **prime** height-three poset could separate height-three excess from \(E(n)\). No equivalence or separation was proved. Exhaustive checks through \(n=7\) found maximum excess \(1\), attained only at height two.

No unfinished research work remains from the interrupted turn.

## Other metadata

```json
{
  "finished_at": 1794261612.8332195,
  "started_at": 1794260183.7256405
}
```
