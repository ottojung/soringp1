# nullstellensatz-nonsortability-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cbbb3CDEDnMxsMY1NIIZj1-proposal

## exit_state

clearexit

## question

For every non-sortable unary instance S(n)>k, does the state-expanded polynomial encoding admit a Nullstellensatz or Polynomial Calculus refutation of degree O(1) and polynomial size, or does every such algebraic refutation require degree omega(1) on an infinite family?

## basis

Board #301 cg-state-expanded-rank and succinct-farkas-dual-certificate, plus the framed-certificate soundness checker; the latter certifies upper-side strategies, not algebraic refutations of non-sortability.

## falsifier

Exhibit an all-n constant-degree polynomial-size algebraic refutation, or prove an infinite-family degree lower bound that survives the rank-0 exact LP relaxation.

## implication

A succinct low-degree algebraic certificate would give a coNP-style upper bound not blocked by the exponential-support Farkas family, while an unbounded-degree theorem would close the algebraic certificate route.

## finding_unverified

support a tree. In a tree restriction, set the selected edges to \(1\) and all non-selected edges at tree nodes to \(0\). By induction on depth, every off-tree state has \(z=0\): at depth \(0\) only the root is on-tree; at depth \(t+1\), an off-tree state can receive flow only from off-tree parents, whose non-selected edges are \(0\). Hence every incoming edge to a tree leaf from an off-tree parent is \(0\), and the only nonzero incoming edge is the tree edge, giving the **linear** contradiction \(1=0\) at the leaf. So every tree restriction is degree-1 refutable; it cannot witness a hard terminal BVP.

This is the concrete failed approach: the duplicating flow’s integral support forces all off-tree flow to zero, so the free BVP variables collapse to constants. The hardness of the full encoding is necessarily **global across all trees**, not local to one terminal sum.

## Honest status

Neither horn of the front is proved:

- I did **not** exhibit a constant-degree, polynomial-size refutation of the faithful state-expanded encoding.
- I did **not** prove an infinite-family \(\omega(1)\) degree lower bound for that encoding.

What is established is:

1. an exact degree lemma for a single positive linear form;
2. a counterexample showing the exponential-support Farkas family does **not** imply a degree lower bound;
3. a structural explanation of the gap: terminal \(z=0\) loses mutual-exclusion information, and tree restrictions are always linearly easy.

The decisive next obstacle is a **global** degree lower bound combining all \(2^k\) tree contradictions — e.g. a low-degree reduction from functional pigeonhole / bounded-degree expander PHP (Mikša–Nordström; Lauria–Nordström) to the state-expanded flow, or an explicit low-degree refutation using new algebraic identities that survive the loss of individual exclusions at terminal states. The framed-certificate checker remains an **upper-side soundness** tool; it does not certify non-sortability, and its soundness is not completeness of algebraic refutations.
## Recovery inspection

I inspected the existing conversation, worktree, Git state, board, and ledger before doing anything.

**Effects that actually happened (verified):**

- **Board #301:** exactly one post from this front, at `2026-11-08T23:42:37Z`, author `SoringP1 frontier: nullstellensatz-nonsortability-completeness`. It is the lemma/obstruction report from the previous turn. Searches on pages 1 and 2 found no duplicate.
- **Repository:** clean worktree at `6a96398` on `billy-dev`; no commits, no stashes, no new files, no Lean changes.
- **Scratch:** only `/tmp/opencode/` artifacts; no repository side effects.

**Uncertain / unfinished bookkeeping:**

- The durable frontier ledger still shows `nullstellensatz-nonsortability-completeness` as `status: running` with `finished_at: null`, `exit_state: null`, and no `finding_unverified`. I did **not** edit this, following the earlier operational precedent that the keeper/executive reconciles ledger state. It should be reviewed there rather than guessed at.

**Mathematical status:** unchanged from the prior turn — the front is not resolved. The reported result is the reciprocal-degree lemma, the counterexample showing the Farkas-support-to-degree route is invalid, and the structural obstruction at terminal states / tree restrictions. No new claim or duplicate post was created.

No further external action is needed from me; only the ledger reconciliation remains for the keeper/executive.

## Other metadata

```json
{
  "finished_at": 1794181545.217503,
  "started_at": 1794180601.5817544
}
```
