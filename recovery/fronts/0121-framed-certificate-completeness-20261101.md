# framed-certificate-completeness-20261101

## status

investigated

## origin

ai_proposal_unverified

## agent_id

ZzeXnn4nQxMlh94ySrJ1sH-names

## exit_state

clearexit

## question

For the framed/quotient certificate grammar in docs/research-framed-certificate-frontier.md, is there an all-n obstruction to polynomial-size sound+complete certificates for exact S(n)? Consider join-incompatibility, state growth across all root histories, and whether forcing soundness for all input orders prevents polynomial quotient classes for large n.

## basis

Framed-certificate frontier identifies completeness as open; join-incompatibility noted as obstruction for NP membership.

## falsifier

Construct an explicit infinite family of root-optimal strategies with no polynomial framed DAG certificate, or show that any sound complete framed grammar requires exponential size for some n via a proved obstruction (not just local examples).

## implication

An all-n obstruction would rule out NP membership via this certificate class; a constructive all-n polynomial family would be a major positive step.

## finding_unverified

s $P$ reachable at the same depth under budget $k=S(n)$ with $F(P)\le k-t$ (all winning). This is exponential in $n\log^2 n$.

### The obstruction (plausible, not yet fully proved)
The natural bar to polynomial-size *quotient* (class-based) certificates is **move-universality / join-incompatibility**:

1. **Pigeonhole:** Any quotient map to $\mathrm{poly}(n)$ classes merges exponentially many frontier states $P,P'$ into the same class $c$.
2. **Move-disjointness is the threat:** For a class $c$ to support a single local move of some root-optimal strategy (and have both outcomes winning from $c$), every state $P\in c$ on that strategy must admit that *same* comparison as part of *some* root-optimal completion, and both branches must remain feasible. If there is an infinite family where some class contains $P,P'$ with disjoint sets $M(P)\cap M(P')=\emptyset$ of minimax-optimal moves, no local rule on classes is valid for a root-optimal strategy covering both — forcing either (a) larger depth, (b) abandoning optimality, or (c) refusal to merge (killing polynomial quotient size).
3. **Joins compound it:** The framed grammar's join = intersection is sound but forgetful; forcing soundness for *all* input orders while trying to share common states across different root histories makes it hard to preserve admissible optimal moves for all merged states. This is the "join-incompatibility" noted in the frontier.

### Concrete status against the falsifier
- **For quotient certificates:** The obstruction is sharp in structure. What remains unproved is (a) an explicit infinite family with $M(P)\cap M(P')=\emptyset$ for *every* coarser quotient merging some pair, and (b) ruling out a nontrivial alternative quotient invariant that is weaker than isomorphism but still move-universal. The winning frontier is the right candidate; move-disjointness is a concrete falsifiable claim but not yet a theorem.
- **For general framed DAGs (non-quotient):** Pigeonhole on arbitrary isomorphism classes doesn't directly apply. A general DAG might not use a single class system with uniform local rules — different paths might use different representations. The grammar is more general than relabeling quotients; ruling out *all* polynomial framed DAGs would require a stronger obstruction (e.g. path constraints that can't be shared even with arbitrary frame structure), which is not established.
- **Complexity implication:** If an all-n obstruction holds for *some* polynomial certificate class that is complete for NP-membership of $SORT\!-\!BOUND\!-\!U$, it would rule out NP membership via that class. However, NP membership of this sparse unary language is already heavily constrained by Mahaney; more directly, the question is whether the *framed/quotient* class can capture all root-optimal strategies. No general NP-completeness/NP-membership theorem is claimed either way.

**Bottom line:** There is a credible all-n obstruction route (winning frontier + move-disjoint/join-incompatible classes) for polynomial-size *quotient* framed certificates. A full proof requires showing move-disjointness for some infinite family under all coarser quotients. For *arbitrary* framed DAGs (the full grammar) the obstruction is weaker and not established. No new repository/Lean artifact is warranted by this analysis; the next decisive step is either constructing an explicit infinite family with provably disjoint $M(P),M(P')$ under merging, or a general argument ruling out non-quotient sharing.


## Other metadata

```json
{
  "finished_at": 1793496321.617816,
  "launch_error": "unowned path /home/lubko/soring-fronts/framed-certificate-completeness-20261101",
  "started_at": 1793494688.0894034
}
```
