# cospectral-gap-span-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

QUpPVZCOG59tCbXyufiAEQ-filled

## exit_state

clearexit

## question

For every absolute constant c, do there exist finite posets P and Q with identical linear-extension count e(P)=e(Q) and identical one-step child extension-count multiset M1(P)=M1(Q) but with minimax-value gap |F(P)-F(Q)| > c, i.e. is the F-gap among M1-cospectral posets uniformly bounded over all finite posets, or can it grow without bound along an all-n family?

## basis

Newest board #301: the 22:02Z depth3 referee (M1-cospectral seed pair with e=32, M1 identical, F-gap 1, sibling-pairing lemma and corrected recoverability) and the 21:22Z cospectral ordinal-sum result (gap held at 1). My own scratch enumeration through n=5 (experiment, not kernel-checked; counts match A001035) found zero mixed-F (e,M1) keys, so the finite witness must be at larger n. This is a magnitude refinement of finite-invariant-incompleteness-f, which only asked existence of a gap-1 conflict.

## falsifier

Exhibit an explicit pair (P,Q) with equal e and equal M1 and F-gap at least 2, or an infinite family whose gap grows; conversely a uniform constant bound refutes the unbounded reading. An n=6 or n=7 cospectral pair with gap >= 2 would settle the finite-witness half.

## implication

If the gap is unbounded, no bounded-depth extension-count lookahead can approximate F to within a constant on all finite posets, ruling out bounded-error lookahead/deck certificates; a uniform bound would give an additive-approximate invariant on the reachable slider. General-poset only: no encoding-preserving reduction to the antichain root is claimed, so nothing transfers to S(n)/SORT-BOUND-U without one.

## finding_unverified

`F(Q²)=12`. Let me try an independent bounded-depth UNSAT check at budget 11 to confirm the gap ≥ 2 without relying on additivity.
Direct bounded search independently confirms `F(Q⊕Q)=12` (UNSAT at 11, SAT at 12) and `F(P⊕P)=10` — a genuine gap-2 witness at n=14, with no reliance on the additivity theorem. Before posting, let me scan recent board pages for any prior amplification claim to avoid duplication.
No prior post matches this amplification claim. Let me check the Antonina CLI posting syntax, then write and verify a single #301 report.
All checks pass and no duplicate claim exists. Let me write the report and post exactly one #301 comment.
Post returned exit 0. Let me verify exactly one comment landed and the working tree is still clean.
Done. One #301 comment landed (23:01:15Z), exactly once, and the worktree is clean — no duplicate side effects from the interrupted launch.

## Mathematical finding

**The F-gap among M1-cospectral posets is unbounded — the "uniformly bounded" reading of the front is refuted.**

The move prior work missed: the 21:22Z/22:45Z results lifted the n=7 seed pair only by ordinal sums with **antichains** `A_m` (where `F(A_m)=S(m)` keeps the gap at 1). Instead take **ordinal powers** of the seed pair itself. Let `P,Q` be the referee-verified pair (`e=32`, identical `M1`, `F=5` vs `6`), and `P_k = P⊕…⊕P`, `Q_k = Q⊕…⊕Q` (k copies). Then for all k:

- `e(P_k)=e(Q_k)=32^k` (e multiplicative);
- `M1(P_k)=M1(Q_k)` (Lemma A: `M1(A⊕B)=e(B)·M1(A) ⊎ e(A)·M1(B)`, and ordinal sums have no cross incomparable pairs);
- `F(P_k)=5k`, `F(Q_k)=6k` (repo Thm 1: `F(A⊕B)=F(A)+F(B)`).

So the gap is exactly `k → ∞` (take `k>c` for any constant `c`).

**Finite gap-2 witness:** `k=2` gives `P⊕P` vs `Q⊕Q` at n=14 (`e=1024`, identical 28-entry `M1`, `F=10` vs `F=12`). Prior n≤9 censuses found only gap-1 conflicts. This was confirmed by **direct brute-force minimax with no reliance on additivity**: `F(P⊕P)=10`, and for `Q⊕Q` bounded search is UNSAT at budget 11 (39,573 states) and SAT at 12, forcing `F=12`. Structural identities were independently re-derived with a fresh scratch engine (seed reproduced exactly; e/M1 for k=2,3; Lemma A and additivity verified on 40 random pairs, 0 errors).

Serious falsification attempts (cross-pair check, e/Lemma-A recomputation, direct F values, non-isomorphism, additivity corroboration) all failed to break the theorem.

## Honest limits and correction

- **Complexity implication corrected.** The front claimed unbounded gap rules out *bounded-depth* extension-count lookahead. Too strong: my family is M1-cospectral but **not M2-cospectral** — M2 separates the seed pair, and ordinal sums preserve that. So the result rules out only **depth-1** `(e,M1)` lookahead; `M_t`-completeness for fixed `t≥2` remains open (no M2-conflict at n≤9). It is a quantitative strengthening of the n=7 Lemma-D incompleteness: `(e,M1)` can be *arbitrarily far* from determining F.
- **Soundness ≠ completeness:** the sibling-pairing lemma (F determined by M1 *given* child F-values) is untouched; completeness (recovering F from extension counts) is what fails.
- **General posets only:** no encoding-preserving reduction to the antichain root is claimed, so **nothing transfers to `S(n)`/`SORT-BOUND-U`** — no improved bound, no class placement, no S(n) value. States aren't shown reachable under optimal play; gap grows only linearly (k at size 7k).
- No repository/Lean/test/CI/ledger changes — consistent with the publication gate.

## Other metadata

```json
{
  "finished_at": 1795474937.7175965,
  "launch_error": "Command '['/home/lubko/.local/bin/antonina', 'agent', 'new', '--cwd', '/home/lubko/soring-fronts/cospectral-gap-span-alln', '--title', 'SoringP1 frontier: cospectral-gap-span-alln', '--json']' timed out after 50 seconds",
  "started_at": 1795473510.3369417
}
```
