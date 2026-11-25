# reachable-clean-step-discrepancy-unbounded

## status

investigated

## origin

ai_proposal_unverified

## agent_id

WLPDFor37oXNSF5xt8oBI4-dmitri

## exit_state

clearexit

## question

Over posets reachable on height-S(n) optimal play from the n-antichain, is the discrepancy G(P) - eps(P) (forced non-clean minimax steps minus the defect F(P) - ceil(log2 e(P))) bounded by an absolute constant as n grows, or does sup over reachable P in R_n of (G(P) - eps(P)) tend to infinity with n?

## basis

Board #301 16:51Z defines G and 18:30Z reports a reachable n=8 state with G=1, eps=0. Scratch computation found G=eps for every poset on n<=5 and at the n=6 witnesses, so the earliest observed divergence is n=8; finite evidence only, no all-n claim.

## falsifier

Construct an infinite family of reachable optimal-play states with G(P) - eps(P) growing without bound, or prove a uniform constant bound valid for every reachable state at every n.

## implication

If unbounded, clean-step counting cannot approximate the defect to within any constant on the states that determine S(n), excluding loss-based evaluators; if bounded, a constant-factor loss proxy for D(n) may be possible.

## finding_unverified

oduces all five values.
- Reachability certificate: explicit 10-step optimal path from `A₉` (F=19→8) with comparisons `(0,1),(2,3),(1,3),(2,4),(1,5),(5,6),(7,8),(5,8),(4,7),(0,8)`, each satisfying `1+max(child F) = parent F`.
- Exhaustive census over **all** unlabeled posets: max D = 0 (n≤7), 1 (n=8, 28/16999), 2 (n=9, 14/183231). Over reachable states: 0 (n≤7), 1 (n=8, 13/5102), 2 (n=9, 6/33054).

**Rigorous baseline (paper proof):** `G(P) ≥ eps(P)` for every finite poset — follow a max-F child path; `b` telescopes from `b(P)` to 0, forcing at least `F−b = eps` nonclean steps.

**Mechanism (deduction):** At the witness a *clean steep* step (b drops 8→6) enters a child with `eps=1, G=2` (itself D=1); the sorter has no F-optimal comparison avoiding this, so `G=2` while `eps=0`. At n=8 analogous divergent children existed, but alternatives always let the sorter avoid them.

## Failed approaches / exact obstruction

- The local budget `β = eps+1` is **not a super-solution** of the G-recursion: at every divergent n=8 state, every F-optimal comparison has `nc + max β(child) = β(P)+1`. So no simple "remaining nonclean budget" strategy proves a constant bound.
- Potentials `F − log₂e` and `F − ⌊log₂e⌋` fail at e=64, F=7 posets (G=2 > 1).
- Ordinal sums: `delta = b_A+b_B−b(P) ∈ {0,1}` can amplify divergence in *arbitrary* posets when `delta=1`, but such states are generally not antichain-reachable, and none of the divergent n=8 posets is a nontrivial ordinal sum.
- The tower does not iterate within n=9: all D=2 posets have eps=0, and no one-step child of a D=2 witness has both `eps≥1` and `D≥2`.

## Soundness vs completeness

`eps ≥ 0` and a clean step's losslessness are sound (leaf counting/Kraft) but not complete for global tightness (board 18:43Z). This witness shows clean-step counting **cannot** approximate the defect to within additive constant 1 on states determining S(n). But computing G requires knowing F-optimal comparisons, i.e. solving minimax at each state — so boundedness alone yields no faster evaluator (cf. `g-measure-lossless-defect-evaluator`).

## Honest limits

This is **not** a proof that `sup D → ∞`: no infinite family was constructed and a full n=10 census (~2.5M posets) was not attempted. The sequence 0,1,2 at n=7,8,9 is suggestive only. `S(n)` values, `G(A_n)=D(n)`, and `SORT-BOUND-U` complexity are unaffected. No all-n theorem is claimed.

No Lean or repository changes were made; scratch work is confined to `/tmp/opencode/reachdisc`. A concise result post was placed on research board #301 at 21:02Z.
I’ll audit the prior actions first: repository state, scratch artifacts, ledger status, and whether the #301 post actually landed. I won’t repeat any external action unless the audit shows it did not happen.
Recovery audit complete. **The interrupted work had already finished; no further action was needed.**

- The #301 finding post **did land**, confirmed both by Antonina’s response and the board digest (21:02:57Z). I did not repost it.
- `billy-dev` remains clean at `6a96398`; no repository changes or commits occurred.
- Scratch computations and result files are present under `/tmp/opencode/reachdisc`; no related process is still running.
- The durable ledger still marks this front `running`. I left it unchanged rather than guess at an additional task-state update.

The posted conclusion remains limited: a reachable n=9 state has `G−eps=2`, disproving a bound of 1; the all-n bounded-versus-unbounded question remains open.

## Other metadata

```json
{
  "finished_at": 1795208654.5468316,
  "started_at": 1795201709.552279
}
```
