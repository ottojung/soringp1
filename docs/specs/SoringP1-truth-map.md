# SoringP1 truth map (S0, scoped draft)

**Status:** scoped draft, docs-only. Labels per `AGENTS.md` evidence vocabulary.
No new theorem is claimed here. Completeness for all-`n` exact-optimal
strategy programs and framed certificates is **OPEN**.

## R0 provenance (recorded, not proved)

- Remote: `https://github.com/ottojung/soringp1.git` (verified via `git remote -v` in isolated clone).
- Base: `origin/main` `f89f6d034a5f4bf36eac5f3c420b1e9a9a1b39c2`.
- Pinned reviewed fragment: `27afe9ef6f0b526c4127381b27b57e91e80f92e0`
  (tree `8c36f049bf6554b489a2297cfd4024ccfd93ff26`),
  single-file note SHA-256 `3fb731106208914f686ec1bb83dea3e3434be7e03f497bcd8df665447d89e02f`.
- Main strategy sketch: `docs/research-fo-tc-strategy-programs.md`
  at `f89f6d0` (SHA-256 recorded in S4 ledger).
- This spec directory does not replace any of the above; it indexes them.

## Objects

| Object | Meaning | Evidence |
|---|---|---|
| `S : ℕ → ℕ` | sorting number, `sInf {k \| HasBudget n k}` (`SoringP1/Model.lean`) | **[kernel-checked]** existence/attainment/minimality (`exists_hasBudget`, `hasBudget_S`, `S_le_iff`) |
| `SORT-BOUND-U` | `{1^n#1^k : S(n) ≤ k}`; input length `N = n+k+1` (`docs/problem.md`) | **[definition]**; unary scope per `AGENTS.md` |
| `ComparisonTree n` | `leaf` / `compare i j yes no`; `height`; `run ranking`; `Correct` (`SoringP1/Model.lean`) | **[kernel-checked]** model definitions |
| `adv` | partial-order minimax value, computable by recursion on card (`SoringP1/Minimax.lean`) | **[kernel-checked]** `S_eq_adv_univ : S n = adv univ`; mathematical equivalence only, **not** a machine-time bound |
| Strategy program `p` | byte string run by fixed interpreter `U`; charged `Ask`, `Emit`, `Halt` (see S2) | **[definition]** pinned to reviewed `FO(TC)_v` note; no kernel-checked correspondence to `HasBudget` |
| Framed certificate | DAG of comparisons with frames/joins/terminals, depth `≤ k` (see S3) | **[paper proof + implemented checker]** soundness only; exact all-`n` completeness **OPEN** |
| `QWIN_{v,d,c}` | restricted `∃p∀X Verify` predicate with fixed `v,d,c` (see S2) | **[paper proof]** conditional `Σ₂^P` characterization of the representable subclass only |

## Evidence labels used here

`definition`, `literature`, `deduction`, `conjecture`, `experiment`,
`paper proof`, `kernel-checked` — exactly the `AGENTS.md` vocabulary.
A passing test suite does not establish spec truth (see S4 R5).

## Unary input length

Measure against `N = n+k+1` for `SORT-BOUND-U` (or `N = n` for `S_unary`).
A bound exponential in numeric `n` is not `EXPTIME` in binary length.
`SORT-BOUND-U` is sparse; per `docs/problem.md` + `AGENTS.md`:
many-one `NP`-hardness would imply `P = NP` (Mahaney), and it cannot be
many-one `EXPTIME`-hard. `S(n) ≥ ⌈log₂ n!⌉` is a sorting lower bound,
not a lower bound for computing `S(n)`.

## May / cannot-claim matrix

| Claim | Allowed here? |
|---|---|
| `SORT-BOUND-U ∈ PSPACE` (documented bound) | May cite as **[literature/deduction]** via `docs/problem.md`; not re-proved here |
| Fixed-`FO(TC)_v` combined evaluation in `O(\|φ\|·N^(2v))` under explicit-table model | May cite as **[paper proof]** from pinned note `27afe9e`; state model assumptions |
| `QWIN_{v,d,c}` soundness + conditional `Σ₂^P` for the representable subclass | May cite as **[paper proof]** conditional; fixed `v,d,c`, explicit encoding required |
| Explicit optimal tree has `Ω(n!)` leaves; scoped barriers (explicit `e(P)` counting, full-frontier listing) | May cite as **[paper proof / literature + deduction, scoped]**; not general hardness |
| `SORT-BOUND-U ∈ NP` or `∈ Σ₂^P` (unrestricted) | **Cannot claim** — completeness OPEN (R4) |
| `SORT-BOUND-U ∉ P` / `∉ NP` | **Cannot claim** — would separate `PSPACE` classes (`AGENTS.md`) |
| Lean `S_eq_adv_univ` implies a Turing-machine time bound | **Cannot claim** — mathematical equivalence only (S1) |
| An explicit sorting tree is an `NP` certificate | **Cannot claim** — may be exponentially large (`AGENTS.md`) |
| Passing `python3 -m unittest discover -s tests` proves spec correctness | **Cannot claim** — validation boundary (R5) |

## Drift hazards (why this map exists)

Tree vs program vs DAG conflation; hidden quantifiers/costs/encodings;
completeness laundering (subclass soundness presented as full membership);
provenance confusion (main sketch `f89f6d0` vs reviewed fragment `27afe9e`);
over-formalization before the all-`n` theorem exists. S2 pins one fragment;
S4 gates translation.
