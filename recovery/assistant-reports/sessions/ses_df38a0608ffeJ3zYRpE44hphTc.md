# antonina-JZSHn06b0CnTBRoG5hkMl0-rejoined

Session: ses_df38a0608ffeJ3zYRpE44hphTc
Workspace: /home/lubko/soring-fronts/sergeev-framed-dag-exact-budget-alln
Created: 1795505388222; updated: 1795505766229

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20c75fe48001CvyyqhtIi5Dlb8)

I'll start by understanding the environment, the current branch, and the key documents.

## Output 25 (msg_20c76168d001aaBOFAvOwjHx1n)

I'm on `billy-dev` as required. Let me read the board digest, literature, and check for any earlier work in this front (in case of resume).

## Output 44 (msg_20c762aa30011izpa6sekiwwD7)

This front has substantial prior context. Let me read the most relevant documents on framed certificates, Sergeev's construction, and the exact FJ no-go.

## Output 63 (msg_20c763f81001bbNVODSyBSiFsD)

Let me get the full text of the key #301 post and check the front definition plus the framing checker.

## Output 82 (msg_20c764f3b001u8BNsT8cHkqm9x)

Let me read the full newest #301 post and find how to query the board directly.

## Output 97 (msg_20c765e44001KViH03VhWIyznG)

The digest truncates at 2000 chars. Let me extract just the single key post's full body via a targeted query (not dumping the board).

## Output 108 (msg_20c7673af001u3xsU4noFRMEqZ)

Let me check for any prior work specific to this front (resume check) and fetch Sergeev's paper.

## Output 123 (msg_20c775ec70018DWqEyC6BDqVoq)

Let me check whether this exact front has prior work and read the most relevant prior notes (Sergeev grammar lower bound, rank-envelope completeness, framed-DAG lower bound).

## Output 138 (msg_20c77912b001pjEyWF7iALtCDf)

This front is already in the ledger. Let me read its full entry and the most relevant prior findings to avoid repeating work.

## Output 149 (msg_20c77a47c001tf4Q2uWbrMuZYr)

This front is currently "running" (this session). There's extensive prior work concluding a structural "coupled containers vs local envelopes" obstruction but no all‑n proof. Let me read the primary source and a couple of the sharpest prior board findings so I can attack a genuinely new angle rather than repeat.

## Output 164 (msg_20c787007001mngVre6bwv6CPP)

Let me download the paper and extract its text locally.

## Output 202 (msg_20c78f065001wC2wyqcJsgBP4I)

A stale `inspect.py` in `/tmp/opencode` is shadowing the stdlib. Let me work in a clean directory and use a venv for pypdf.

## Output 229 (msg_20c795031001hcRZKlGn3qe3Ak)

I have the full paper. Let me study the group-insertion algorithm and its surplus analysis.

## Output 274 (msg_20c79c704001A8GidgyTozgkUN)

Let me check the board for any prior post making the "reduction to open surplus problem / no-transfer" point, so I don't duplicate.

## Output 285 (msg_20c7a42b0001s2LH4lzlYvAxZN)

I have the primary source and a clear picture. Let me verify worktree cleanliness and learn the Antonina posting interface before writing up the finding.

## Output 303 (msg_20c7af5aa001uzlI9f07bdmRBV)

I have everything I need. Let me write a durable note (outside the repo) with the full analysis, then post a concise finding to #301.

## Output 314 (msg_20c7b393e001lr8KY91gNx9feJ)

Now let me post the concise finding to board #301.

## Output 332 (msg_20c7b7e59001IU08o0cdcNobiO)

Let me verify the post landed on the board and confirm the worktree is still clean.

## Output 343 (msg_20c7b97c7001CJL9G9CoNnS9Hq)

Done. Here is the research report.

## Front: `sergeev-framed-dag-exact-budget-alln`

**Environment:** `billy-dev`, clean worktree at `6a96398`. I studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-framed-certificate-frontier.md`, `docs/research-sergeev-asymptotic.md`, the full text of Sergeev's ECCC TR20‑096 (downloaded and read), the exact FJ no‑go post on #301, and checked for prior work on this front in the ledger/digest so as not to repeat it.

**Claim attacked (all‑n, falsifiable):** P — for every n there is a polynomial‑size sound permutation‑framed DAG (checker grammar, antichain root) of height *exactly* `S(n)`, obtained by compiling Sergeev's group insertion; hence `SORT-BOUND-U ∈ NP`. Falsifier: (F1) superpolynomial size, or (F2) an exact height formula exceeding `S(n)` infinitely often.

**Result: OPEN — no theorem, no counterexample, no repository/Lean/CI/ledger changes.** One #301 post landed, plus one note in my durable workspace (my only external writes). The concrete finding is a rigorous *no‑transfer + reduction* obstruction:

1. **Model‑fidelity correction.** Any correct sorter has comparison count `C_A(n) ≥ S(n)`. Sergeev gives only `C_A(n) = log₂(n!) + o(n)`, an upper bound with a non‑effective constant. So a successful framing has height `o(n)`-above-`S(n)` and is an NP witness for `1ⁿ#1ᵏ` only when `C_A(n) ≤ k`; for the tight yes‑instance `k = S(n)` that forces `C_A(n) = S(n)`. **The front's implication holds only for exact height — an `o(n)`-surplus compilation does *not* yield NP membership.** Earlier fronts blurred this; Sergeev's asymptotic algorithm alone cannot supply the witness.

2. **FJ no‑go does not transfer.** That no‑go used an explicit linear surplus *lower* bound `F_FJ(n) − log₂(n!) ≥ 0.01n`. Sergeev's Theorem 3 provides no surplus lower bound at all, so the “height exceeds S(n) eventually” deduction has no analogue.

3. **F2 reduces to two open problems.** It needs both an explicit surplus lower bound for a fixed schedule and a computable surplus upper bound on `S(n)` (the still‑blocked effective‑finite‑Sergeev problem), with the former exceeding the latter infinitely often. Even granting `C_A(n) ≥ ⌈log₂ n!⌉+1` eventually, it additionally needs `S(n)=⌈log₂ n!⌉` infinitely often — open (surplus known in `{0,1}` only through n=22).

4. **F1 is beyond counting.** Permutation frames encode all `n!` inputs in poly size (checker accepts a 19‑node, depth‑13 exact‑height certificate for n=7 funnelling 5040 paths into one leaf), so leaf/path/level counting cannot prove a size lower bound; and `SORT-BOUND-U` is tally/in `P/poly`, so circuit lower bounds cannot apply. F1 is the general open completeness question. The coupled‑containers‑vs‑rank‑envelopes obstruction remains the best structural candidate but is not a proof — the one concrete #301 counterexample was retracted, and the join condition `e(P∩Q) ≤ 2^{k−d}` is only necessary (sufficiency open, no reachable witness for n≤6).

**Honest limits:** no all‑n theorem, no explicit constant, no exhaustive join counterexample. I kept general‑poset results and certificate *soundness* strictly separate from completeness. The productive next steps are (i) an effective finite Sergeev bound plus an explicit surplus lower bound for a fixed schedule, or (ii) a reachable information‑gap join witness beyond n≤6 — neither achieved here. I did not mark the ledger front complete, since a process exit is only a recorded investigation, not a proof.
