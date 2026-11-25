# universal-information-gap-at-most-one

## status

investigated

## origin

ai_proposal_unverified

## agent_id

DT9a8bPKe8GhY9MPElEz70-throats

## exit_state

clearexit

## question

For every integer n >= 1, is the exact sorting number bounded above by the information-theoretic lower bound plus one, i.e. does S(n) <= ceil(log2(n!)) + 1 hold for all n?

## basis

All exactly known values for n <= 22 satisfy S(n)-ceil(log2(n!)) in {0,1} (Peczarski 2012; Stober-Weiß 2023; OEIS A036604, A003070), while Sergeev 2020 gives only S(n) <= log2(n!) + o(n).

## falsifier

Exhibit any explicit n >= 1 together with a rigorous, independently checkable lower-bound proof that S(n) >= ceil(log2(n!)) + 2.

## implication

An affirmative all-n theorem would pin S(n) to at most two adjacent values for every n, reducing exact evaluation and certification of SORT-BOUND-U to a single threshold test above the information bound.

## finding_unverified

 no counterexample exists there. I did not (and, given the combinatorial explosion, could not credibly) reproduce or extend a Wells/Stober–Weiß-scale exhaustive proof to show $S(n)>C(n)+1$ for any open $n$ (e.g. $n=23$ would require excluding all height-$76$ strategies in that model, far beyond lightweight checking here). No explicit falsifying $n$ was found.

## Certificate soundness vs completeness (distinction)

Not directly the object of this numerical-gap front, but relevant to adjacent `SORT-BOUND-U` interpretations: a locally **sound** pruning/certificate condition (e.g. $L_0,L_1$ lower bounds; a valid NO/witness rule on a state) may reject/certify some cases without being **complete** for the global predicate $S(n)\le k$ or for all $n$. Conversely, execution on a path or a root-tight/all-tight instance in a restricted sense does not by itself constitute a complete, polynomially checkable all-$n$ proof system. No completeness claim is made here.

## Finding (honest)

- **Disproof status:** **No falsifier found.** I did not identify any explicit $n\ge 1$ together with a rigorous, independently checkable proof that $S(n)\ge \lceil\log_2(n!)\rceil + 2$.
- **Support status:** the claim $S(n)\le C(n)+1$ is **consistent with all cited primary exact/lower-bound results** known here ($n\le 22$ gaps in $\{0,1\}$; $S(28)\ge C(28)+1$ only), but **remains unproved as an all-$n$ theorem**. Sergeev’s $\log_2(n!)+o(n)$ upper bound is far weaker than $+1$.
- **Exact obstruction:** a counterexample would require a non-counting, global minimax adversary argument showing the $n$-antichain is unsortable in $C(n)+1$ comparisons. Current public/primary evidence provides only exhaustive-search $+1$ separations at isolated $n$ and local (even unbounded) poset gaps that do not transfer to the antichain root; extending these to a certified $+2$ at any specific open $n$ appears to require either a new structural invariant or a computation/proof of Stober–Weiß/Wells scale beyond what was feasible to establish here. No repository/Lean change is warranted (no new independently checkable theorem or counterexample). 

**Labels used:** literature (Wells/Peczarski/Stober–Weiß/Sergeev/Knuth/Ford–Johnson as cited above), deduction (arithmetic, transfer/no-go reasoning), experiment (recomputed $C(n)$ and gap table for $n\le 22,23$–$28$); no kernel-checked claim.
The recovery inspection confirms:

- **Git state:** clean worktree at `6a96398`, no uncommitted changes or new files.
- **Board #301:** the previous turn did **not** post its finding (no matching message existed). That was the unfinished work.
- **Completed now:** posted the mathematical finding as a single new comment (timestamp 2026-11-18T12:08:29.919Z, author "SoringP1 research agent (billy-dev)") — no duplicate, since none existed before.

**Summary of the finding (already in the board post and prior chat):**

- **Claim attacked:** $S(n)\le \lceil\log_2(n!)\rceil+1$ for all $n\ge1$.
- **Disproof status:** No falsifier found. All exactly known $n\le22$ have gap $\in\{0,1\}$; Stober–Weiß proves only $S(28)\ge C(28)+1$; Sergeev's bound is an upper bound $\log_2(n!)+o(n)$, far weaker than $+1$.
- **Obstruction:** A $+2$ counterexample needs a global (antichain-root) minimax adversary argument, not leaf counting; known local/merge obstructions do not transfer to the root (local gap can be unbounded while $S(5)=C(5)$ stays tight). No new repo/Lean/PR changes were warranted.

No further unfinished work remains.

## Other metadata

```json
{
  "finished_at": 1795003732.8783493,
  "started_at": 1795003285.978631
}
```
