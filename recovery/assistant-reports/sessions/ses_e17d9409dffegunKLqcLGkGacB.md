# antonina-Hz3m5rcrUC5OFtc8gkKKnt-guess

Session: ses_e17d9409dffegunKLqcLGkGacB
Workspace: /home/lubko/soring-fronts/sergeev-gap-effective-uniform-bound
Created: 1794896215981; updated: 1794896781092

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 97 (msg_1e82eba54001bp35mSs6e6XAJ4)

**Recovery/state check (billy-dev):** Inspected `/home/lubko/soring-fronts/sergeev-gap-effective-uniform-bound` on branch `billy-dev...origin/billy-dev`, clean working tree at `6a96398` (`git status --short --branch` empty). No local repo changes, no task artifacts, and no evidence of external side effects from this turn. Antonina CLI and board access were available (`python3 scripts/board_digest.py --recent 7` succeeded); recent board #301 activity includes `info-bound-gap-invariant-alln` (gap-window/invariant angle, no theorem) but not this exact “explicit `(C,alpha)` finite strengthening of Sergeev’s `O(n/(log n)^(1/5))`” question. I did not post, commit, or modify the repository.

**Sources studied:** `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/research-plan.md`, `docs/research-sergeev-asymptotic.md`, board #301 excerpts, ECCC TR20-096 metadata/abstract (Sergeev 2020; full constructive proof text/PDF not retrieved here), and known exact values/gaps for `n<=22` (as recorded in repo/docs/OEIS literature baseline).

## Front
**Claim (all `n`, unary/exact `S` model):** Is there an explicit constant `C > 0` and exponent `alpha > 0` such that for all `n >= 2`,
`S(n) <= ceil(log2(n!)) + C*n/(log(n+2))^alpha`?
**Complexity implication:** a constructive, explicit `(C,alpha)` would give an effective finite additive-gap window above the information bound for all `n`, narrowing the exact threshold/search window for evaluating `S(n)` / deciding `SORT-BOUND-U` in terms of the known gap (it does not by itself imply `P`, `NP`, or a separation). A robust impossibility for this shape would indicate a real limit of current asymptotic upper-bound techniques as finite uniform bounds.

## Mathematical finding (paper deduction, conditional on Sergeev)
**Status: the falsifier direction is refuted in the existential sense by Sergeev’s asymptotic theorem; a fully explicit numerical `(C,alpha)` is not extracted here. No independently checkable new all-`n` theorem/counterexample is established beyond this standard finiteness consequence, so no repo/Lean change is warranted (per AGENTS publication gate).**

1. **[literature]** Sergeev (ECCC TR20-096, 2020, Thm. 3) gives
   `S(n) = log2(n!) + O(n/(log n)^(1/5))`.
   Hence there exist `C0 > 0` and `n0` with
   `S(n) - ceil(log2(n!)) <= S(n)-log2(n!) <= C0*n/(log n)^(1/5)` for all `n >= n0`.

2. **[deduction]** Fix any `alpha` with `0 < alpha <= 1/5`. Since `log(n+2) ~ log n`, there is `C1 >= C0` and `n1 >= n0` with
   `S(n) - ceil(log2(n!)) <= C1*n/(log(n+2))^alpha` for all `n >= n1`.
   The initial segment `{2, ..., n1-1}` is finite, and `S(n)` is finite for each `n`, so
   `M_alpha := max_{2 <= n < n1} ((S(n)-ceil(log2(n!))) * (log(n+2))^alpha / n)` is finite.
   Therefore for `C := max(C1, M_alpha, 1)`,
   `S(n) <= ceil(log2(n!)) + C*n/(log(n+2))^alpha` for **all** `n >= 2`.

3. **Consequence for the asked front/falsifier.** Assuming Sergeev’s theorem, **no fixed `(C,alpha)` can be falsified by infinitely many `n` for every proposed choice, and no uniform all-`n` impossibility of this functional shape follows**: in fact some `(C,alpha)` (e.g. any `alpha <= 1/5` with sufficiently large finite `C`) must hold for all `n`. The finite-prefix absorption is automatic once an asymptotic `o(n)`/`O(n/(log n)^(1/5))` upper bound is known; Sergeev’s method is not obstructed from yielding a uniform bound of this shape in principle (the obstruction is only to *reading off* constants from the proof as stated).

4. **Small-`n` sanity (known data, `n<=22`):** `g(n)=S(n)-ceil(log2(n!))` is `0` except `n in {12..19}` where `g(n)=1` (max of `g(n)*(log(n+2))^(1/5)/n` over `n<=22` is about `0.101` at `n=12`), giving no finite counterevidence and trivially absorbable.

## Limits / what is not shown
- **Not an explicit constant extraction:** I did **not** derive a concrete numerical `C` or verify `n0`/constants inside Sergeev’s group-insertion construction (full proof details unavailable in this session). So the claim in the fully constructive sense “here is an explicit written-down `(C,alpha)` proved from Sergeev’s proof” remains open from this investigation.
- **No stronger form proved:** this does not give a better exponent than `1/5`, no improvement to `S(n)`, and no complexity-class classification.
- **Model note:** this concerns the additive gap above `ceil(log2(n!))` for the exact sorting number function `S(n)` (adaptive worst-case comparisons), not a runtime/certificate lower bound for computing `S(n)`, and not general-poset hardness. No claim of NP/P/separation is made.
- **Attempted disproof:** I looked for an all-`n` or infinite-family obstruction/counterexample route to “no fixed `(C,alpha)`”; given the asymptotic theorem, such a falsifier cannot exist except by contradicting Sergeev, and I found no independent evidence against Sergeev or any finite counterexample in known values. Honest outcome: **no counterexample/finitization-impossibility found; existential finiteness follows from literature, but explicit constants require a separate audit/extraction of Sergeev’s proof.**
