# antonina-B3XRyn8N7dli0VJDahjEoy-niece

Session: ses_e45391908ffe0NJbFHJ3Pl5aZV
Workspace: /home/lubko/soring-fronts/s-p-recursive-exact-sequence
Created: 1794134960015; updated: 1794135774017

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 390 (msg_1bad23b6d0017bc19TJXLFkfZO)

## Finding: the front is false in the strongest form

`S(n)` is **not holonomic/P-recursive at all** — not merely “no bounded-order, bounded-degree recurrence”.

Let  
\[
F(z)=\sum_{n\ge 0} S(n)z^n .
\]

**Theorem.** `F` is not D-finite. Equivalently, `S` satisfies no finite-order linear recurrence with polynomial coefficients, of any degree:

\[
\sum_{i=0}^{r}p_i(n)S(n+i)=0 \quad (n\gg0)
\]

has no nontrivial solution with finite `r`, `p_r\ne0`.

The same holds for the information bound `C(n)=\lceil\log_2 n!\rceil`. More generally, no integer sequence asymptotic to `c n log n` with `c≠0`, up to an additive `O(n)` error, is P-recursive.

### Proof outline

1. Merge sort and the information bound give
   \[
   S(n)=\frac{1}{\log 2}n\log n+O(n),
   \]
   so the OGF has radius exactly `1`.

2. By Pólya–Carlson, an integer-coefficient radius-`1` power series is either rational or has the unit circle as a natural boundary. A D-finite series has only finitely many finite singularities, so it cannot have a natural boundary. Hence a D-finite `F` would be rational.  
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

## Output 472 (msg_1bad33db1001wZdCkiIQ6Xyltq)

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
