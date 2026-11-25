# sergeev-framed-dag-exact-budget-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

JZSHn06b0CnTBRoG5hkMl0-rejoined

## exit_state

clearexit

## question

Can Sergeev-style group-insertion sorting be compiled into a polynomial-size permutation-framed DAG whose height equals the exact optimum S(n) for all n, given that the newest #301 FJ no-go excludes the Ford-Johnson architecture but explicitly leaves this one open?

## basis

The 2026-11-24T06:36Z #301 post fj-exact-barrier-20261124 proves FJ height has Theta(n) surplus versus Sergeev's o(n) and states the polynomial-size exact-budget certificate question stays open.

## falsifier

Prove that any framed-DAG representation of Sergeev's group insertion has superpolynomial size, or that its exact height formula strictly exceeds S(n) for infinitely many n.

## implication

A positive compilation would give SORT-BOUND-U in NP; a negative result would identify the main surviving constructive architecture as incapable of exact optimal-height certification.

## finding_unverified

earch report.

## Front: `sergeev-framed-dag-exact-budget-alln`

**Environment:** `billy-dev`, clean worktree at `6a96398`. I studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-framed-certificate-frontier.md`, `docs/research-sergeev-asymptotic.md`, the full text of Sergeev's ECCC TR20‑096 (downloaded and read), the exact FJ no‑go post on #301, and checked for prior work on this front in the ledger/digest so as not to repeat it.

**Claim attacked (all‑n, falsifiable):** P — for every n there is a polynomial‑size sound permutation‑framed DAG (checker grammar, antichain root) of height *exactly* `S(n)`, obtained by compiling Sergeev's group insertion; hence `SORT-BOUND-U ∈ NP`. Falsifier: (F1) superpolynomial size, or (F2) an exact height formula exceeding `S(n)` infinitely often.

**Result: OPEN — no theorem, no counterexample, no repository/Lean/CI/ledger changes.** One #301 post landed, plus one note in my durable workspace (my only external writes). The concrete finding is a rigorous *no‑transfer + reduction* obstruction:

1. **Model‑fidelity correction.** Any correct sorter has comparison count `C_A(n) ≥ S(n)`. Sergeev gives only `C_A(n) = log₂(n!) + o(n)`, an upper bound with a non‑effective constant. So a successful framing has height `o(n)`-above-`S(n)` and is an NP witness for `1ⁿ#1ᵏ` only when `C_A(n) ≤ k`; for the tight yes‑instance `k = S(n)` that forces `C_A(n) = S(n)`. **The front's implication holds only for exact height — an `o(n)`-surplus compilation does *not* yield NP membership.** Earlier fronts blurred this; Sergeev's asymptotic algorithm alone cannot supply the witness.

2. **FJ no‑go does not transfer.** That no‑go used an explicit linear surplus *lower* bound `F_FJ(n) − log₂(n!) ≥ 0.01n`. Sergeev's Theorem 3 provides no surplus lower bound at all, so the “height exceeds S(n) eventually” deduction has no analogue.

3. **F2 reduces to two open problems.** It needs both an explicit surplus lower bound for a fixed schedule and a computable surplus upper bound on `S(n)` (the still‑blocked effective‑finite‑Sergeev problem), with the former exceeding the latter infinitely often. Even granting `C_A(n) ≥ ⌈log₂ n!⌉+1` eventually, it additionally needs `S(n)=⌈log₂ n!⌉` infinitely often — open (surplus known in `{0,1}` only through n=22).

4. **F1 is beyond counting.** Permutation frames encode all `n!` inputs in poly size (checker accepts a 19‑node, depth‑13 exact‑height certificate for n=7 funnelling 5040 paths into one leaf), so leaf/path/level counting cannot prove a size lower bound; and `SORT-BOUND-U` is tally/in `P/poly`, so circuit lower bounds cannot apply. F1 is the general open completeness question. The coupled‑containers‑vs‑rank‑envelopes obstruction remains the best structural candidate but is not a proof — the one concrete #301 counterexample was retracted, and the join condition `e(P∩Q) ≤ 2^{k−d}` is only necessary (sufficiency open, no reachable witness for n≤6).

**Honest limits:** no all‑n theorem, no explicit constant, no exhaustive join counterexample. I kept general‑poset results and certificate *soundness* strictly separate from completeness. The productive next steps are (i) an effective finite Sergeev bound plus an explicit surplus lower bound for a fixed schedule, or (ii) a reachable information‑gap join witness beyond n≤6 — neither achieved here. I did not mark the ledger front complete, since a process exit is only a recorded investigation, not a proof.

## Other metadata

```json
{
  "finished_at": 1795505820.6821158,
  "started_at": 1795505386.4100227
}
```
