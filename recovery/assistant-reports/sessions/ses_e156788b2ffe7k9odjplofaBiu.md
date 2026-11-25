# antonina-wskjPMvJzSzNI7OurdXUvz-belonged

Session: ses_e156788b2ffe7k9odjplofaBiu
Workspace: /home/lubko/soring301-exec-quantified-root-adversary-proof-20261117e
Created: 1794937223008; updated: 1794937338215

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 78 (msg_1ea9a166d001ZXOPxwdOSnUug4)

Wrote `exec-report.md` in this worktree.

- **Question addressed:** sound, polynomial-time checkable adversary invariant forcing a comparison obstruction from the initial `n`-element antichain under every sorting strategy (root quantifier, issues #47/#48 context per frontier/docs).
- **Candidates examined:** baseline information invariant `C(n)=ceil(log2 n!)` (sound, root-valid, efficiently checkable, non-strengthening); one-ply `L1(P)>d` lift (sound locally, not unconditionally poly-time checkable in `n`, and **no root strengthening** since antichain first comparisons split `n!/2,n!/2` so `L1(A_n)=L0(A_n)`; maintainability under every sorter not established); “no balanced split” budget invariant (unsatisfiable at root above baseline / same symmetry falsifier); forced reachability of known hard reachable gadgets (structural/merge/same-`e` witnesses sound for reachable states but root-transfer/maintainability under every strategy not established).
- **Findings:** positive for baseline only; negative for examined strengthening candidates as root-forcing polynomial-time-checkable invariants; overall **inconclusive** on existence of any non-baseline such invariant.
- **Included:** soundness checks, falsification attempts (antichain symmetry, reachable-to-root transfer gap, checkability-vs-power), obstacles, decisive next question (poly-time computable predicate + proved adversary reply rule initialized at `A_n` with certified super-information deficit / concrete sorter counterstrategy falsifier), and explicit claim-type labels throughout. No new experiments run; analysis grounded in cited repo docs. No repository code/tests/Lean/build changes beyond the report.
