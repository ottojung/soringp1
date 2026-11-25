# antonina-KNoBRAo0LE79o7Nco4SXiI-shilling

Session: ses_e0ed50842ffeJ3o4DhrKlLmqjf
Workspace: /home/lubko/soring-fronts/curator
Created: 1795047487431; updated: 1795047733596

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f12af7ec001Loy46x4hzS8VHN)

I'll start by understanding the repository state, the contract documents, and how to access board #301.

## Output 25 (msg_1f12b0bf1001IoROKarsCbY0K0)

I'm currently on `main`, but the task requires `billy-dev` ONLY. Let me check branches and operational details before doing anything.

## Output 44 (msg_1f12b1a4f001W72t1edjQ3W2lA)

`billy-dev` is the execution host (not a git branch), so I'm in the right place — I must not switch branches or make repo/Lean changes. Let me read the board #301 digest and the existing frontier definitions to avoid duplicates.

## Output 63 (msg_1f12b32ae001ubyPkN7WpbQMfM)

Let me look at the frontier definitions and get fuller board content by redirecting to files.

## Output 122 (msg_1f12ba769001N5e5Xk5NT1VjOk)

Let me extract all 540 ledger front questions to a searchable file so I can precisely avoid duplicates.

## Output 169 (msg_1f12c280b001HLFRzjUO86p64L)

The frontier is heavily saturated. Let me read the full newest posts and the research plan to find any genuinely new angle before deciding.

## Output 213 (msg_1f12c77bd0017f1G4Y6B5QPNdz)

Let me read the full newest lookahead posts to find any new structural fact not yet fronted.

## Output 231 (msg_1f12cd1af001YaBVu9LMyZntyH)

Let me verify precisely which "lookahead" and "equal-extensions" questions are already fronted, so I don't duplicate.

## Output 260 (msg_1f12d90b80019u0XKXOULT9dwu)

Let me check the height-two / star-family fronts to see if the newest n=12 star structure is already covered.

## Output 280 (msg_1f12e3fab001VjcPJsrc4O5Bp9)

Let me confirm the keeper's expected schema for the curator file (including the empty case) before writing.

## Output 291 (msg_1f12e66d2001aLxABuQ7oX9kDn)

I've completed a thorough review. Let me write the required curator output file.

## Output 311 (msg_1f12e8636001UGS8ldKFjX4f0V)

Done. Here is my honest report.

## Setup
`billy-dev` is the **execution host** (`docs/operations.md`), not a git branch; the checkout stays on `main` at `6a96398`. I made **no** commits, Lean files, tests, board posts, or ledger edits. The only working-tree change is the required deliverable `frontier-candidates.json` (untracked).

## What I studied
`AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, the 540-entry frontier ledger, and board #301 pages 1 (full newest posts through 2026‑11‑19 00:11Z). Primary-literature anchors checked against `literature.md`: Ford–Johnson, Knuth TAOCP §5.3.1, Peczarski (2012), Stober–Weiß (ALENEX 2023), Mahaney (1982). I did not rediscover exact values or the sparsity barrier.

## Precise all‑n claim attacked, and serious disproof attempt
**Candidate claim C:** there is a universal constant `c` with `L_{c·n}(A_n) = S(n)` for all `n` (equivalently `t(n) ≤ c·n` for every information‑loose `n`), where `L_t` is the extension‑count lookahead hierarchy and `t(n)=min{t : L_t(A_n)=S(n)}`.

Disproof routes tried:
- **(deduction, #301)** Barrier `L_t(A_n)=C(n)` for `2t≤n` and finite convergence `L_t(A_n)=S(n)` for `t≥n(n−1)/2` give only `⌊n/2⌋+1 ≤ t(n) ≤ n(n−1)/2`.
- **(deduction, ledger finding `lookahead-convergence-depth`)** The 2‑adic obstruction gives `t*(n) > v₂(n!) = n − s₂(n)` on any loose family; this refutes the *stronger* fronted claim “`t*(n)−⌊n/2⌋` is bounded” (already investigated) but not C.
- **(experiment/#301, reported not re‑run by me)** `t12-lookahead-strong` gives `t(12) ∈ [18,66]`, i.e. `t(12)/12 ∈ [1.5,5.5]` — compatible with C, not a counterexample.

**Outcome: C survives; I could not disprove it.** A genuine counterexample needs an infinite family with `t(n)/n → ∞`, which requires both “`S(n)>C(n)` infinitely often” and a superlinear lower bound on `t(n)` — both explicitly open on #301. No new theorem, no counterexample.

## Soundness vs completeness; general posets vs root
- **(deduction)** Framed‑DAG local checks and `L₀ = ⌈log₂ e⌉` are *sound* and poly‑time checkable; *completeness* (a polynomial‑size all‑`n` certificate reaching `S(n)`, hence `SORT-BOUND-U ∈ NP`) is open. Soundness alone yields no class membership.
- **(deduction)** Height‑two excess unboundedness, arbitrary‑poset `F` hardness and Fredman/Kahn–Saks are general‑poset results; without a reduction to the antichain root they do not change `S(n)` (`AGENTS.md` model‑fidelity).

## Curator decision
`frontier-candidates.json` = `{"fronts": []}`. I found no defensible, non‑duplicate all‑n direction: the 540 ledger fronts (all investigated/blocked), the board investigations through 11‑19 (`t12-*`, `fr-n12-persistent`, lookahead convergence), the Executive’s 23:16Z saturation audit, and a prior empty curation already cover lookahead growth, the 2‑adic barrier, height‑two/star families, certificates, space/time bounds, FO‑definability, and hardness/barrier angles. Every fresh angle I generated reduced to an existing front or to a question blocked by “`S(n)>C(n)` infinitely often.” Per the contract, no speculative filler is warranted; research remains open — saturation is not completion.
