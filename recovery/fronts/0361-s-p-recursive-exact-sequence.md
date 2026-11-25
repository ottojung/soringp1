# s-p-recursive-exact-sequence

## status

investigated

## origin

ai_proposal_unverified

## agent_id

B3XRyn8N7dli0VJDahjEoy-niece

## exit_state

clearexit

## question

For every n, does the exact sorting number S(n) admit an explicitly given fixed-order P-recursive (holonomic) representation, i.e. polynomials p_0,...,p_r with r and total degree bounded by absolute constants and p_r nonzero, such that sum_{i=0}^{r} p_i(n) S(n+i) = 0 for all n >= 0?

## basis

OEIS A036604/A003070 exact values through n=22 (Peczarski 2012; Stober-Weiss 2023), Sergeev's o(n) excess, and docs/research-plan.md; no holonomic, D-finite, or generating-function front occurs in the 360-entry ledger.

## falsifier

Prove non-holonomy of the generating function of S via a modular, singularity, or asymptotic obstruction that survives the known S(n) = log2(n!) + o(n) regime, or exhibit an explicit bounded-order candidate recurrence together with a certified exact value at which it provably fails.

## implication

An explicitly given fixed-order holonomic recurrence with polynomial-time computable coefficients would yield a polynomial-time evaluator for S(n), placing SORT-BOUND-U in P; a non-holonomy theorem would exclude every finite-order recurrence as an exact-evaluation route, a barrier not implied by the winning-frontier enumeration bound.

## finding_unverified

By Pólya–Carlson, an integer-coefficient radius-`1` power series is either rational or has the unit circle as a natural boundary. A D-finite series has only finitely many finite singularities, so it cannot have a natural boundary. Hence a D-finite `F` would be rational.  
   Equivalently, Bell–Chen–Nguyen–Zannier (arXiv:2306.02590) gives rationality directly, since `S(n)` is an integer of height `O(log n)=o(n)`.

3. If `F` were rational, partial fractions give
   \[
   S(n)=\sum_\alpha P_\alpha(n)\alpha^{-n}.
   \]
   Radius `1` forces every `|\alpha|\ge1`. Writing `\lambda=1/\alpha`, the unit-modulus terms give
   \[
   S(n)=n^d q(n)+O(n^{d-1}),
   \]
   where `q(n)` is a nonzero finite sum of unit-modulus exponentials. Comparing with `c n log n+O(n)`:
   - `d=0` makes `S` bounded;
   - `d=1` makes `S/n` bounded;
   - `d\ge2` makes `S/n^d\to0`, while `q(n)` cannot tend to `0`.

   Contradiction.

### Honest correction

A first attempt used “rational coefficients have polynomial growth, but `n log n` is super-polynomial”. That is false: `n log n=O(n^2)`. An independent audit caught this. The proof was repaired to use the **finite exponential-sum shape** of rational coefficients, not growth alone. The repaired argument was re-audited.

### What this does and does not establish

- **Does:** kills every fixed-order P-recursive exact-evaluation route, and also every algebraic generating function. This closes the algebraic-recurrence family that the winning-frontier barrier explicitly left open.
- **Does not:** show `SORT-BOUND-U ∉ P`, or any class separation. Non-holonomic integer sequences can be trivially computable. It says nothing about nonlinear recurrences, variable-order recurrences, general-poset minimax values, or certificate soundness/completeness.
- No exact OEIS value or finite computation is used.

### Artifacts

- Note: `docs/research-nonholonomy.md`
- Barrier row added to `docs/research-plan.md` and `docs/README.md`
- Commit on `billy-dev`: `73b1272`
- Board #301 post: author `SoringP1 frontier: exact-sortnumber-nonholonomy`

No Lean changes: the proof depends on an external analytic theorem and was not kernel-checked.
Recovery inspection complete. I did not repeat the prompt and created no new external effects.

**Verified state**
- Host: `billy-dev`.
- Working directory: `/home/lubko/soring-fronts/s-p-recursive-exact-sequence`.
- Git: clean worktree, `HEAD = 73b1272` (`Document non-holonomy barrier for exact sorting numbers`).
- Files present in that commit:
  - `docs/research-nonholonomy.md`
  - barrier row in `docs/research-plan.md`
  - index entry in `docs/README.md`
- Board #301: the finding **was posted exactly once** at `2026-11-08T11:01:19.559Z` by `SoringP1 frontier: exact-sortnumber-nonholonomy`. The digest reports one matching post. I did not post again.

**Durable ledger**
- `s-p-recursive-exact-sequence` is still marked `running` with no finding recorded yet. This is expected until the agent exits and the keeper records the returned result. I did not edit the ledger directly.

**Effect assessment**
- Confirmed side effects: one local commit and one board #301 comment.
- No duplicate post, no additional commit, no Lean changes.
- No uncertain external effects requiring review.

The mathematical result from the previous turn stands as reported: an unconditional non-holonomy barrier for `S`, not a complexity-class separation. The only remaining process step is the keeper recording this agent’s result in the ledger.

## Other metadata

```json
{
  "finished_at": 1794135786.4012575,
  "started_at": 1794134958.8606696
}
```
