# antonina-BucnyzQG7H4wQJhIZPMIBk-clutching

Session: ses_df4d3e8f3ffedUM9s1RmJCkcil
Workspace: /home/lubko/soring-fronts/curator
Created: 1795483768596; updated: 1795485062715

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 48 (msg_20b30330b001g40uP2FJ2cj7dW)

Let me gather the facts: compute the information-bound values exactly, fetch the OEIS sequence of exact sorting numbers, and read the relevant docs.

## Output 79 (msg_20b32a3a5001YAgOnC7qp1eJC3)

Now let me check the board for related fronts (duplicate screening), the research plan, and the ledger IDs.

## Output 98 (msg_20b34b8180012EHmYt2jsu40Xg)

The ledger contains some excess/gap-themed fronts. Let me inspect their questions to screen for duplicates before finalizing anything new.

## Output 122 (msg_20b35048c001sC4dA8UxNSVh7m)

The code tool is misbehaving; I'll use the shell with python3 instead.

## Output 137 (msg_20b35251b001QPHytcF0JI9vvF)

Now let me look at the findings of the closest excess/gap fronts in the ledger to see what is open vs. done (to avoid duplicates).

## Output 148 (msg_20b37c1a9001yM1W6Xrn3Fna25)

Now let me screen for novelty: check the ledger and current board for any front asking about zero-excess after 22 or excess at n ≥ 23.

## Output 159 (msg_20b3d74970017JXg9iPYWVUkdF)

One final novelty check on the proposed new front's exact claim against the ledger and board.

## Output 170 (msg_20b3e998e001yW0e7s7vTwMBmC)

Novelty confirmed — none of the ledger or board fronts ask "is the excess zero for every n ≥ 23?" Now I'll write the new frontier candidates to `frontier-candidates.json`.

## Output 190 (msg_20b3f044f001qpSH8JsglwlGZ2)

The keeper checks for textual duplicates — mentioning other fronts' slugs in the question could trip it. Let me rewrite the question/implication without any ledger slugs and re-validate.

## Output 210 (msg_20b3f8b710010w9bXmDhOn3Mp4)

`frontier-candidates.json` is written and validated (id `excess-zero-after-22-alln`; lengths: question 273 ≥ 75, falsifier 113 ≥ 40, implication 462 ≥ 40, basis 575 ≥ 35; unique in the 739-front ledger).

## What I studied and what I attacked

**Sources read:** AGENTS.md, docs/problem.md, docs/literature.md, docs/operations.md, README.md, docs/research-n12-nontightness.md, plus board #301 (digest, newest posts), the durable ledger (~/.local/state/soringp1/frontier-ledger.json), and primary literature data (OEIS A036604/A003070 b-files).

**Attack — claim:** the information-bound excess cap `D(n) = S(n) − ⌈log₂ n!⌉ ≤ 1` for every n (this is the ledger front `excess-at-most-one-alln`). **Disproof attempt:** (a) exact data through n = 22 (OEIS A036604 + A003070, cross-checked against literature.md): D ∈ {0,1}, D=0 for n ≤ 11, D=1 at {12,…,19, 22}, D=0 at {20, 21}; (b) paper attempt: no mechanism producing D ≥ 2 anywhere; the n=12 gap (Wells) is the smallest global gap, and repo docs mark "the information bound can be off by more than 1 … is open"; (c) computation: S(23) is open (Stober–Weiß: exact values through n = 22; S(23) open; their S(17) run took ~115 h on a 48-thread machine) — infeasible to extend here. **Verdict: disproof inconclusive; no counterexample through n = 22; the claim stays open (consistent with data).**

## New frontier proposed (in `/home/lubko/soring-fronts/curator/frontier-candidates.json`)

**`excess-zero-after-22-alln`** — *Is the information-bound excess D(n) = S(n) − ⌈log₂ n!⌉ equal to zero for every n ≥ 23, i.e., does the unary sorting number return to the information bound after the excess-1 values at n ∈ {12,…,19, 22}? All-n claim: ∀n ≥ 23, S(n) = ⌈log₂ n!⌉.*
- **Falsifier:** exhibit n ≥ 23 with D(n) ≥ 1 (S(n) ≥ ⌈log₂ n!⌉ + 1).
- **Basis:** OEIS tables through n = 22 (C(12)=29, S(12)=30, …, S(22)=71 vs C(22)=70); README.md; literature.md; Stober–Weiß (S(28) ≥ 99, n = 23 open).
- **Novelty:** checked against all 739 ledger fronts and board #301 — nothing asks "excess = 0 for every n ≥ 23" (distinct from `excess-at-most-one-alln`, `excess-two-realization-alln`, `post22-gap-growth-alln`).

**Honest limits:** the falsifier is unverified through n = 22 (data is consistent with D=0); S(23+) is uncomputed, so even a positive verification of D(n)=0 for 23, 24, … lacks a theorem/mechanism reason; nothing here is claimed proved, verified, or trans-completeness-positive. No Lean/repo changes were made, per the publication gate.
