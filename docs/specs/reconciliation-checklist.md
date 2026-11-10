# Reconciliation checklist / ledger (S4)

**Status:** checkable ledger for gates R0–R6. Docs-only increment.
Check a box only with owner + evidence hash + date; uncheck on drift.

## Claim ledger (claim, object, encoding, resource model, evidence, status, owner, next)

| # | Claim | Object / encoding | Resource model | Evidence | Status | Owner | Next |
|---|---|---|---|---|---|---|---|
| C1 | `S`, `ComparisonTree`, `HasBudget`, `S_le_iff`, `S_eq_adv_univ` as in S1 | Lean `SoringP1/*` | mathematical (no machine cost) | `docs/kernel-results.md`; S1 | accepted (kernel-checked) | repo | none (do not reopen) |
| C2 | `SORT-BOUND-U ∈ PSPACE`; unary `N=n+k+1`; sparsity constraint | unary `1^n#1^k` | TM time/space in `N` | `docs/problem.md`, `AGENTS.md` | accepted as documented bound | repo | none here |
| C3 | `FO(TC)_v` combined `O(\|φ\|·N^(2v))` + `QWIN` soundness + conditional `Σ₂^P` | explicit tables, `L=n+k+\|p\|+2`, fixed `v,d,c`, `∃p∀X Verify` | paper-model clocks `L^d`/`L^c` | pinned `27afe9e` (note SHA-256 `3fb73110…89e02f`) | accepted as **scoped/conditional** (S2) | fragment pin | prove/refute completeness |
| C4 | Framed-DAG soundness + polytime checker | explicit graph + `n` | polytime in explicit length | frontier note + `scripts/check_framed_strategy.py` | accepted as sound/checkable (S3) | repo | exact all-`n` completeness |
| C5 | All-`n` exact completeness (programs at `S(n)`; DAGs at `S(n)`) | `HasBudget n (S n)` target | poly size + uniform polytime | — | **OPEN** | this issue | all-`n` proof or refuting family |
| C6 | Unrestricted `SORT-BOUND-U ∈ NP` / `∈ Σ₂^P` | unary threshold | uniform polytime verifier | — | **NOT CLAIMED** (needs C5) | — | blocked on C5 |

## Gates R0–R6

- [x] **R0 identity/provenance.** Remote `https://github.com/ottojung/soringp1.git`;
  base `f89f6d034a5f4bf36eac5f3c420b1e9a9a1b39c2`;
  pinned fragment `27afe9ef6f0b526c4127381b27b57e91e80f92e0` /
  tree `8c36f049bf6554b489a2297cfd4024ccfd93ff26` /
  note SHA-256 `3fb731106208914f686ec1bb83dea3e3434be7e03f497bcd8df665447d89e02f`;
  main sketch `docs/research-fo-tc-strategy-programs.md` SHA-256 recorded below.
  Owner: agent-RGr10Dxu9qJSCRf7uZxgbi-asia. Evidence: `git rev-parse`, `sha256sum`.
- [x] **R1 truth-map freeze / independent review.** S0 frozen + no-overclaim
  review recorded with verdict + artifact hashes. Owner: author + reviewer
  (subagent `ses_e3c667e43ffeTeGEtI9P7uZh4V`). Evidence: APPROVE verdict
  below + board comment; artifact hashes in Review record.
- [x] **R2 fragment pinning.** S2 pins `FO(TC)_v` / `QWIN_{v,d,c}` to `27afe9e`;
  main sketch `f89f6d0` explicitly superseded for complexity citation.
  Owner: agent-RGr10Dxu9qJSCRf7uZxgbi-asia.
- [x] **R3 correspondence target.** S1 names `HasBudget n k` / `S_le_iff`
  (`S_eq_adv_univ` as math bridge, no machine-time reading). Owner: author.
- [x] **R4 no-overclaim.** S0 matrix + S2/S3 OPEN markers; no `NP`/`Σ₂^P`
  for unrestricted `SORT-BOUND-U`; no `∉ P`/`∉ NP`; no tree-as-certificate.
- [ ] **R5 validation boundary.** Tests cited as regression only
  (`python3 -m unittest discover -s tests`); Lean re-check required before any
  Lean integration (`lake build --wfail`, `leanchecker`, axioms). Not run for
  Lean in this docs-only increment by design.
- [ ] **R6 translation gate.** No implementation/translation before
  R0–R5 recorded with owner/reviewer/rollback. This branch adds `docs/specs/`
  only; no compiler, no version bump, no Lean edits.

## Review record (independent no-overclaim review)

- Reviewer: subagent `ses_e3c667e43ffeTeGEtI9P7uZh4V` (independent pass,
  strict overclaim/fidelity/scope checks against `27afe9e` note, `f89f6d0`
  sketch, `SoringP1/*`, `docs/problem.md`, `docs/kernel-results.md`,
  frontier note, `AGENTS.md`).
- Verdict: **APPROVE** — no unrestricted `NP`/`Σ₂^P` membership claim, no
  completeness claim at `S(n)`, no machine-time reading of `S_eq_adv_univ`,
  no tree-as-certificate, no test-as-proof; sketch/fragment not confused;
  OPEN markers present in all five files; docs-only scope confirmed
  (`git status`: only `?? docs/specs/`).
- Artifact hashes (recomputed by author at commit; reviewer hashes match
  except two transcription typos in the reviewer message for S1/S3, resolved
  by re-hash to the values below):
  - `docs/specs/SoringP1-truth-map.md`:
    `fd94942481d7e719294eafdf5040fef9a2dd9166547fbf09f0cce041c5669356`
  - `docs/specs/S1-kernel-model-contract.md`:
    `f0037bcee757e0ab8e35e145bdf4f805e89b5518af1d74c40ab7298482f929d9`
  - `docs/specs/S2-strategy-program-fragment.md`:
    `4ce70071bedbf5a3ef61bd6aaabb4c4de920b07f79151ec8d36642f4f73996a1`
  - `docs/specs/S3-framed-certificate-contract.md`:
    `3640b8e4574f95f907b149420a35303bfbb9b43f3ce9882cfc37a45c5dcccfea`
  - `docs/specs/reconciliation-checklist.md`: hash at commit (see commit stat).
- Validation: `python3 -m unittest discover -s tests` → 182 tests OK
  (skipped=1) in ~37s on this branch; `git diff --check` clean.

## Base file hashes (at branch creation)

Recorded at commit time; reviewer re-hashes:

- `docs/research-fo-tc-strategy-programs.md` (main `f89f6d0`):
  `5d80e704e1dded1408ee0a4acd86a271f91c6d5f67206deb7382cb61799137e4`
- Reviewed note `27afe9e:docs/research-fo-tc-combined.md`:
  `3fb731106208914f686ec1bb83dea3e3434be7e03f497bcd8df665447d89e02f`

## Rollback

Revert `docs/specs/` to `f89f6d0` (directory did not exist there) if review
fails. No other paths touched by this increment.
