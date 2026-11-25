# antonina-RyqzZxGylCT2EfURmtBZpl-treasure

Session: ses_e00f8e97fffear3mEAAbLMnVUv
Workspace: /home/lubko/soring-fronts/curator
Created: 1795280017031; updated: 1795280711412

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ff0716a2001lxm5Ey1kkynuxH)

I'll start by understanding the environment — locating the `billy-dev` worktree, studying the repository docs, and figuring out how to access board #301.

## Output 34 (msg_1ff0733c9001o6S606HRbyJnyH)

I'm on the correct host. Let me study the core documents and access board #301 via the digest tool.

## Output 49 (msg_1ff074f6e0012DTMqJsQKAlDIu)

Now let me access board #301 and examine the frontier infrastructure.

## Output 90 (msg_1ff07917d001YG2CKcdqyXSY9J)

Let me read the current frontier candidates file, the research plan, and some recent docs to understand what's already covered.

## Output 105 (msg_1ff07e211001zETrZUu56YEbTJ)

Let me examine the fresh board findings more deeply and run an independent minimax computation to ground a new research question. First, let me set up a scratch working area.

## Output 180 (msg_1ff0ead50001YEe0NAb4h7DHEO)

I found a concrete refutation and need to check novelty against the 648 existing fronts. Let me search the ledger and docs for related keywords.

## Output 227 (msg_1ff10178e001R5cZCAjmod7sY5)

I have a concrete refutation and three candidate non-duplicate directions. Let me verify the refutation numbers cleanly once more, then write the JSON.

## Output 238 (msg_1ff1111bb0015zO2L8jhs3eZ22)

The refutation is confirmed. Now I'll write the JSON with three genuinely new, non-duplicate fronts grounded in the freshest board findings and my independent computation.

## Output 267 (msg_1ff118f3a001f1gH01DSB9zNyJ)

Done. Here is the honest report.

## What I studied
- `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-frontier.json`, `docs/research-plan.md`.
- Antonina board #301 (digest through the newest 16:48Z postings), plus the 648-entry frontier ledger to refuse duplicates.

## Claim attacked and disproved
I took the **freshest** board result — the 16:31Z non‑potential theorem that any sort of `C_a ⊔ B` makes at least `ceil(log2 C(a+b,a))` cross comparisons on some path — and attacked its natural **additive strengthening**:

> `F(C_a ⊔ B) ≥ F(B) + ceil(log2 binomial(a+b,a))` for all chains `C_a` and posets `B`.

Using a fresh from‑scratch exact minimax evaluator (validated against `S(n)=0,1,3,5,7,10` and `F(C_n)=0`), I found **finite counterexamples with deficit 1**:
- `(a,b,B)=(1,4,A_4)`: `F=7` vs additive target `5+3=8`
- `(2,3,A_3)`: `F=6` vs `3+4=7`
- `(3,4,A_4)`: `F=10` vs `5+6=11`

So the cross‑comparison count and `F(B)` are **not additive**. This is a **general‑poset** result about `C_a ⊔ B`, not about the antichain root `S(n)`; and it refutes a **sound lower‑bound route**, not completeness of any certificate. It does **not** touch the defect inequality D, which survives these cases.

## Curator decision
Three genuinely new, all‑n, falsifiable fronts, each grounded in the newest board evidence or the computation above, and checked absent from all 648 ledger fronts:
1. `cross-cost-additivity-ceiling-alln` — is the cross‑cost deficit bounded or unbounded?
2. `balanced-fj-sufficiency-alln` — does info+FJ certify the antichain defect on every balanced split?
3. `defect-refinement-monotonicity-scope-alln` — for which `a` does defect monotonicity under refinement fail?

## Honest limits
- These are proposed questions with finite/structural evidence, **not theorems, proofs, or verifications** — the JSON makes no such claim.
- No Lean file, test, commit, PR, ledger edit, or board post was made. The only worktree change is the required deliverable `frontier-candidates.json`; scratch computations live in `/tmp/opencode/curator-research/`.
- `S(n)`, `SORT-BOUND-U`, and the defect inequality D remain open; no complexity‑class separation is claimed.
