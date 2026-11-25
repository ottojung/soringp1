# positive-density-framed-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

cZJaQwddVz337JVq4cbJVX-bridges

## exit_state

clearexit

## question

Does the set of n for which some polynomial-size (in n) framed comparison DAG, accepted by the existing soundness checker, has height exactly S(n) have positive asymptotic density, or is framed-certificate completeness confined to a density-zero set of n?

## basis

Board #301's certificate-compatibility limitation and docs/research-framed-certificate-frontier.md: the checker's soundness is implemented, all-n polynomial-size completeness is open, and existing certificate fronts demand all n rather than a density statement.

## falsifier

Prove that every set of n admitting such polynomial-size height-S(n) framed certificates has asymptotic density zero, or construct a positive-density family with explicit certificates and a soundness argument.

## implication

Positive density would localize the all-n obstruction to NP membership for SORT-BOUND-U to a density-zero exceptional set and show that soundness is not the bottleneck; density zero would establish a structural incompleteness of the framed grammar rather than a mere absence of proof.

## finding_unverified

do not transfer to this antichain-root framed-DAG size question.

### 6. Corrected front and honest limit

The non-vacuous, complexity-relevant question is not positive density but:

> Fix a polynomial `p` and let `A_p={n: size_opt(n)≤p(n)}`. Is `A_p` cofinite for some `p`? Equivalently, does every sufficiently large `n` admit a polynomial-size framed DAG of height exactly `S(n)`?

A meaningful weaker density question is whether `A_p` has positive upper density for some fixed `p`. But:

- positive density of some `A_p` does **not** localize the all-`n` obstruction to a density-zero set;
- syndeticity of `A_p` gives only height `S(n)+O(log n)` for all `n`, not exactness;
- cofiniteness of `A_p` does imply `SORT-BOUND-U ∈ NP`;
- density zero of every fixed-`p` set would be a structural incompleteness of exact-optimal framed compression, but does not follow from current lower bounds and is not equivalent to non-membership in NP.

**Conclusion:** I did not prove either density horn. I did disprove the front’s stated complexity implication and identify the exact missing step: positive density is the wrong density notion for NP localization, and the natural density-to-all lifting loses an unavoidable-looking `O(log n)` comparison surplus. The remaining mathematical obstruction is a super-polynomial lower bound on optimal-height framed DAG size, or equivalently a proof that exact optimal sorting cannot be compressed into polynomially many framed states on a dense set of `n`. No such theorem is presently available.
Recovery inspection complete. I did not repeat the research prompt or create any new external effects.

**Verified state**
- Host: `billy-dev`.
- Working directory: `/home/lubko/soring-fronts/positive-density-framed-completeness`.
- Git: clean worktree, `HEAD = 6a96398`; no commits, edits, Lean files, or repository changes.
- Durable ledger: front `positive-density-framed-completeness` is still marked `running` under agent `cZJaQwddVz337JVq4cbJVX-bridges`, with no finding recorded yet. That is expected until the agent exits; I did not manually edit the ledger.
- Board #301: no comment from this front or agent. The only digest match for “positive-density” is an unrelated earlier front (`antichain-lookahead-depth`); searching the agent ID returns zero matches. No duplicate post was made.

**Effect assessment**
- Confirmed external effects from the previous turn: **none**.
- Confirmed repository effects: **none**.
- Uncertain effects requiring review: **none**.

**Prior result remains the completed deliverable**
The previous turn finished with a mathematical report, not a density theorem. Its substantive findings stand:
- The front’s stated complexity implication is false: positive density does not localize the all-`n` obstruction to a density-zero exceptional set; only cofiniteness gives a clean NP consequence.
- The natural exact-height lift fails concretely (`n = 4→5`, `8→9`, `16→17`), so positive density cannot be propagated by binary insertion.
- Syndeticity of a fixed-polynomial exact set would give only framed certificates of height `S(n)+O(log n)`, not exact `S(n)`.
- Neither density horn follows from current literature: no infinite exact-`S(n)` family is known, and the only universal framed lower bound is `height ≥ ceil(log₂ n!)`, far too weak to rule out polynomial-size optimal DAGs.

No unfinished side effect or duplicate action remains. The density question itself is still open; I have not converted the process into a proof.

## Other metadata

```json
{
  "finished_at": 1794173295.592063,
  "started_at": 1794172072.4831607
}
```
