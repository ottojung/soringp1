# sergeev-certificate-state-complexity

## status

investigated

## origin

ai_proposal_unverified

## agent_id

64nI3bFFALWxhgaRyfMSUt-estimate

## exit_state

clearexit

## question

Can Sergeev's group-insertion strategy for S(n) <= log2(n!) + o(n) be realized by a framed certificate grammar with only polynomially many distinct comparison states in n (all-n), with explicit joins and polynomial verification?

## basis

docs/research-framed-certificate-frontier.md sections 2-3 call for polynomial-state rank-envelope/nested grammar for Sergeev; Stober-Weiss/Sergeev in docs/literature.md.

## falsifier

Identify a state invariant of Sergeev's coupled interval/container structure that cannot be represented by the local rank-envelope intersections of the framed grammar without exponential state blowup or loss of exact height guarantee.

## implication

A positive all-n construction would yield a concrete polynomial witness family approaching the best known asymptotic bounds; a barrier would show the grammar is more restrictive than arbitrary polynomial-time verifiers.

## finding_unverified

d intervals/containers* induce constraints that are not separable into independent per-element windows relative to a single underlying chain without losing the exact coupling. More directly: there exist feasible configurations in Sergeev’s strategy where the guaranteed relation $R$ formed by coupled containers requires knowing the relative order constraints *between different containers* (e.g. the alignment between container $A$ and container $B$ is linked by group-membership constraints from higher levels). Intersecting branches that were consistent with coupled constraints can produce a guaranteed relation $R'$ whose “natural” envelope coarsening is either (a) not tight enough to preserve the exact comparison schedule of Sergeev’s strategy (losing the exact height guarantee $S(n)$), or (b) forces the grammar to distinguish exponentially many coupled alignments as different states (exponential state blowup) because the join cannot merge them into a single local envelope without adding unjustified relations or dropping necessary ones. 

In particular: the number of nonisomorphic coupled configurations can grow quickly; the forgetting loss $\lambda_b$ in §4 becomes unavoidable if you force local envelopes, or you cannot satisfy the exact telescoping $D - \log_2(n!) \le k - \log_2(n!)$ at height $k=S(n)$ without keeping full coupling. Also §3’s warning is generic (independent anchors cheap to forget) — coupling is the opposite: *dependent* constraints across containers mean merging different branches forces either exponential state types or loss of exact feasibility.

**Distinction from general posets:** This is not a generic “arbitrary partial order is hard” complaint. It’s about the *specific structure* of Sergeev’s construction (group-insertion + coupled intervals) vs the *admissible operations* of the framed grammar (local rank-envelope intersections/joins). The bridge back to $S(n)$ is direct (exact height of that strategy).

**Falsifier outcome:** I cannot construct an all-$n$ polynomial-state framed grammar realizing Sergeev’s exact strategy; the natural local-envelope abstraction appears to lose the coupling invariant. A serious attempt to model coupled containers as envelopes suggests exponential blowup or inability to preserve exact height. This is a *concrete obstruction* to that specific all-$n$ realization, not a general proof that no other polynomial certificate exists for $S(n)$.

### Limits / what this does NOT show
- Does **not** rule out some other polynomial-size framed certificate (not derived from Sergeev’s strategy) achieving height $S(n)$ for all $n$. That’s question 1 in §5.
- Does **not** give a class separation ($\text{SORT-BOUND-U}\notin \text{NP}$). Sparsity + Mahaney constrains many-one NP-hardness, but membership is separate.
- Does **not** claim the obstruction is formalized in Lean or is a kernel-checked theorem — it’s a paper-level mathematical obstruction based on stated structures.
- Counting $e(P)$ is #P-hard (§4) so entropy arguments are necessary conditions, not polynomial verification rules — consistent with the state-complexity obstruction above.

**Verdict:** The falsifier identifies a real structural obstruction (coupling vs local envelopes). I find it plausible the framed grammar’s local rank-envelope joins cannot realize Sergeev’s coupled-container strategy with polynomial states and exact height; realizing *any* polynomial all-$n$ certificate for $S(n)$ remains open. No repository changes made.

## Other metadata

```json
{
  "finished_at": 1793394738.6839952,
  "started_at": 1793394616.6078653
}
```
