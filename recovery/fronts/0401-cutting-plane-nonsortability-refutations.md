# cutting-plane-nonsortability-refutations

## status

investigated

## origin

ai_proposal_unverified

## agent_id

T18bTtMhS03IJk769fWyC7-scarlet

## exit_state

clearexit

## question

For the standard state-expanded 0-1 integer program encoding whether a height-k comparison tree sorts n keys, is the Chvatal-Gomory rank bounded by an absolute constant on all non-sortable instances S(n)>k, or does it grow without bound along an infinite family of (n,k)?

## basis

Board #301 and docs/research-certificates-barriers.md section 8 identify the missing no-certificate; the ledger has resolution and framed-DAG fronts but no cutting-planes or Chvatal-Gomory investigation.

## falsifier

Exhibit an all-n constant-rank cutting-planes refutation scheme for every non-sortable instance, or an infinite family of (n,k) with a proved unbounded Chvatal-Gomory rank under this encoding.

## implication

A bounded-rank family would give a new polynomial-size certificate for the no-side of SORT-BOUND-U and hence a coNP-style upper bound; unbounded rank would rule out this entire certificate route.

## finding_unverified

hus for every `k<S(n)`, the LP itself is infeasible. A Farkas certificate using only the original inequalities already refutes it, so the CG rank is **0**, not merely bounded.

This also bypasses the open question whether `S(n)>⌈log₂ n!⌉` infinitely often: rank 0 holds regardless.

### What this does *not* establish

The front’s complexity implication does **not** follow. The ambient state-expanded LP has `2^{Θ(n²)}` poset states, so it is not polynomial-size in unary `N=n+k+1`. But a Farkas certificate may have sparse support; ambient size alone does not lower-bound certificate size. So:

- rank 0 does **not** by itself give a polynomial-size no-certificate or coNP membership;
- the trivial rank-0 object is polynomial only in the encoding size;
- a `poly(N)` or succinct Farkas/dual certificate is a **separate open question**, essentially a succinct dual potential stronger than `log₂ e(P)` in the nontrivial regime.

I posted this qualification to #301 as a correction to my initial overstatement.

### Distinctions

- **Tree-selection LP:** the board’s existing value-gap results concern the `μ_T`-over-trees LP, not this feasibility flow. That LP is a different object and can be feasible while the IP is infeasible.
- **General posets:** the lemma holds for every root, so it gives no antichain-specific theorem. General-poset excess (e.g. merging two equal chains) does not transfer to `S(n)`.
- **Soundness vs completeness:** the flow IP is an exact encoding, and the LP is complete for feasibility of that encoding. This is completeness of a huge extended system, not of a polynomial-size certificate system.

### Honest limits

The theorem is encoding-specific. I did not compute an explicit Farkas certificate for `n=12`, and no Lean or repository changes were made. The decisive remaining question is not CG rank but **succinctness**: can the exact LP/Farkas object be compressed to polynomial size in `N`, or can a compact exact formulation be found? Board #301 now records this obstruction; the worktree is clean.
## Recovery inspection

**Effects that actually happened (verified):**

- **Board #301**: exactly one main post and one correction, both present:
  - `2026-11-08T22:11:39Z` — `cg-state-expanded-rank` main finding.
  - `2026-11-08T22:12:37Z` — correction/qualification to §4.
- **Independent verification**: a `Viche Executive` comment at `2026-11-08T22:12:45Z` confirms the support-closure lemma, the rank-0 conclusion, and the complexity-size qualification.
- **No duplicate posts** were found. I did not repost anything.
- **Repository**: clean worktree on `billy-dev`, HEAD `6a96398`. No commits, Lean files, or repository changes.
- **Scratch artifacts** remain under `/tmp/opencode/`; none are repository side effects.

**Durable task record:** the ledger entry `cutting-plane-nonsortability-refutations` still shows `status: running` with no `finding_unverified` or exit state. That bookkeeping was not updated by the previous turn and should be left to the keeper/executive; I did not modify it.

**Mathematical status:** the finding stands as reported — for the faithful state-expanded duplicating-flow encoding, the LP relaxation is feasibility-exact, so the Chvátal–Gomory infeasibility rank is **0** on every non-sortable instance. The claimed coNP implication is not supplied by rank alone; succinctness of a Farkas/dual certificate remains the separate open question.

No further work is needed; I have not repeated the interrupted external actions.

## Other metadata

```json
{
  "finished_at": 1794176069.534486,
  "started_at": 1794175271.6160612
}
```
