# antonina-T18bTtMhS03IJk769fWyC7-scarlet

Session: ses_e42d1f9a2ffeXUxDAF3MH5YUSL
Workspace: /home/lubko/soring-fronts/cutting-plane-nonsortability-refutations
Created: 1794175272753; updated: 1794176058358

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1bd2e09f7001sFg3OF8XmZluab)

I'll start by studying the contract, problem docs, and the current board state.

## Output 525 (msg_1bd36c1bf0014mcClSsUKsJBDL)

I found the key structural point. Let me record the precise argument in scratch and then verify it against small cases before posting.

## Output 581 (msg_1bd38328a001p3YyWWv3eheGqF)

I need to correct one overreach in the posted complexity interpretation. The rank-0 theorem stands, but system size alone does not bound a Farkas certificate's support. Let me post a scoped correction.

## Output 610 (msg_1bd38d359001jAo6y6bzJPVDVp)

## Result

I studied `AGENTS.md`, `docs/problem.md`, the certificate/barrier note, board **#301**, and the sorting-number literature (Stober–Weiβ, arXiv:2206.05597v2; Kleitman–Rothschild for poset counts; standard Chvátal–Gomory sources). I fixed the “faithful state-expanded” encoding explicitly, because the term is not canonical.

**Main finding: for the faithful state-expanded duplicating-flow 0-1 IP, the LP relaxation is feasibility-exact. Therefore the Chvátal–Gomory infeasibility rank is 0 on every non-sortable instance.** The unbounded-rank horn is impossible for this encoding.

### Encoding and proof

States are transitively closed partial orders on `[n]`. With `z_{P,t}` (“state `P` occurs at depth `t`”) and `x_{P,t,e}` (“comparison `e` is selected at `P`, depth `t`”), the constraints are:

- `z_{A_n,0}=1`;
- for non-total `P`, `t<k`: `z_{P,t}=Σ_e x_{P,t,e}`;
- for every `Q`, `t<k`: `z_{Q,t+1}=Σ_{P,e,o:P+o(e)=Q} x_{P,t,e}`;
- `z_{Q,k}=0` for non-total `Q`.

The key is that selecting a comparison sends mass to **both** adversary outcomes. Hence if an LP solution has `z_{P,t}>0`, some `x_{P,t,e}>0`, and both children have positive `z`. Closing the support gives an actual deterministic strategy:

> **Lemma (support closure).** For every root `P` and budget `d`, the LP relaxation is feasible iff the minimax height `F(P) ≤ d`.

No integrality is needed in the forward direction; only the support of the fractional solution matters. Thus for every `k<S(n)`, the LP itself is infeasible. A Farkas certificate using only the original inequalities already refutes it, so the CG rank is **0**, not merely bounded.

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

## Output 699 (msg_1bd39edd6001LvVe40YJh4FRmm)

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
