# antonina-mHqRBJZfWEfxjULwWQawTA-front

Session: ses_e0eb570afffeWhTSo5coBHGxES
Workspace: /home/lubko/soring-fronts/curator
Created: 1795049557850; updated: 1795049820636

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f14a8f80001765S95ivKSWgIi)

I'll start by understanding the repository structure, confirming I'm on `billy-dev`, and reading the key documents and board #301.

## Output 21 (msg_1f14aa7ce001SurZMYKTL0vW5T)

I'm currently on `main`, but the task requires `billy-dev`. Let me check available branches and switch.

## Output 32 (msg_1f14ab41a0014QLW2pqC1K2O0T)

There's no `billy-dev` branch visible. Let me check worktrees and all refs.

## Output 43 (msg_1f14ac273001ptlZ7XDtYdl8wb)

No `billy-dev` branch exists in this repo. Let me look at the broader workspace — the task mentions `billy-dev` specifically, which may be a branch in another worktree/repo.

## Output 54 (msg_1f14ad1a9001Q2yCp7u570Z95M)

Let me search specifically for `billy-dev` across all these directories.

## Output 65 (msg_1f14aeb1e0016rmz2NqPtDvz3G)

`billy-dev` is the active branch in `/home/lubko/soring301`. Let me examine that repo (board #301) and read the core docs in the curator repo.

## Output 80 (msg_1f14b265d001j4C0iiThX5DOvT)

Let me find board #301 — checking MCP resources and the soring301 repo docs.

## Output 95 (msg_1f14b48d6001qswi0lWFHNYKso)

Let me read operations.md to learn how to access board #301 (Antonina).

## Output 106 (msg_1f14b56fe001UNBXf8h51M7P3B)

I'm on billy-dev (the execution host). Let me read the current board #301 digest.

## Output 117 (msg_1f14b6f59001MIi4hSmAgWDDAG)

Let me check the digest script options so I can read full posts of the newest findings.

## Output 137 (msg_1f14b94dd001e42FYlJNODPQ77)

Let me examine the ledger of all investigated fronts (to refuse duplicates) and the literature, plus the newest dispatched fronts.

## Output 152 (msg_1f14baecb001UZuojkKiUh99uA)

Let me read the full newest reports directly from Antonina (beyond the digest truncation) and the ledger details for the newest fronts.

## Output 163 (msg_1f14bfd54001sLW9pixugW9HSf)

Let me inspect the exact questions of related ledger fronts to avoid duplicating them.

## Output 174 (msg_1f14c7f37001rA0rfn4v3s1UZa)

Let me check the ledger structure properly.

## Output 194 (msg_1f14ca80c001bqYfybStM34qOR)

Let me verify key numerical facts myself and check a few more ledger entries for overlap with my candidate fronts.

## Output 205 (msg_1f14dba32001ZBc4iarM05GCYT)

Let me check the winning-frontier fronts to ensure my admissible-frontier front is distinct.

## Output 216 (msg_1f14de236001yR0dhtdPbPFA2T)

I have enough grounding. Let me verify my drafted fields meet the schema constraints and that IDs are novel, then write the file.

## Output 254 (msg_1f14e5e4e001Xn0pXh19gLZPn0)

I worked on the billy-dev host, studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, and the newest #301 posts (Viche's 00:51Z verification, `abc-tree-completeness-antichain`, `t12-decide-symbolic`/`t12-lookahead-strong`). I confirmed the 540-front ledger is saturated and checked every candidate ID against it (no overlaps).

## Claim attacked and disproof attempt

**Claim (lookahead-to-strategy extraction):** for all `n`, if the extension-count relaxation first reaches `L_t*(A_n) = S(n)` at minimal depth `t*(n)`, then a height-`S(n)` sorting tree exists whose every node `P` satisfies `L_{t*(n)-1}(P) = F(P)`.

What I established:
- **Deduction:** `L_t ≤ F` always (`L_0 = ⌈log₂ e⌉ ≤ F`, inductively). At `n=12`, `C(12)=29`, `S(12)=30`, and `L_1(A_12)=1+⌈log₂(12!/2)⌉=1+28=29 < 30` — arithmetic I rechecked directly. So constant-depth lookahead is refuted at `n=12`.
- **Structural obstruction:** root equality `L_t*(A_n)=S(n)` only forces the minimizing move's *max of children's relaxed values* to equal `S(n)−1`. A child can have `L_{t−1}(child)=S(n)−1` while `F(child)>S(n)−1`, so root tightness need not propagate one level down. Extraction can fail in principle.
- **Honest limit:** the full claim is **not decided**. Deciding it needs `t*(12)` (known only in `[18,66]`) and child values; the admissible frontier grows from `S10=250310` to an extrapolated `~9·10¹⁰` at depth 18, which blocks the computation. The claim "`t*(n)≤n`" is refuted only by the cross-validated-but-not-independently-re-run engine result `t(12)≥18>12`, so I label that **experiment/deduction**, not a theorem.

## Soundness vs completeness, and general posets

The Peczarski A/B/C conditions are **sound** sufficient conditions for an optimal comparison, but the n=7 node (chain-of-6 plus isolate; FJ move `{3,6}` optimal yet uncertified, with certified pivot `{2,6}`) and the n=9 starved state show they are **incomplete as a node-local grammar for optimal trees**. That is a barrier to one certificate format only — it yields no NP/coNP/P result for `SORT-BOUND-U`. Likewise, the general-poset refutations (recursive-abc at n=6, the `C_m ⊔ {z}` lower-middle lemma, the n=9 reversal defect) are not antichain-root theorems and do not transfer without a reduction. I created no Lean or repository artifacts and posted nothing to #301.

## Output

Wrote `frontier-candidates.json` with 3 genuinely new, non-duplicate all-`n` questions — all schema-validated (slug 6–63 chars; question ≥75; falsifier/implication ≥40; basis ≥35):

1. `lookahead-tightness-strategy-extraction` — whether root-level lookahead tightness is extractable into a uniformly tight optimal strategy (distinct from `lookahead-convergence-depth`, which asks about the value of `t*`).
2. `sublinear-window-lookahead-attainment` — whether a `c<1` induced-subposet window can attain `S(n)`, versus an Ω(n)-window barrier (sharpens the flatness theorem; distinct from the blocked unrestricted-invariant front).
3. `admissible-frontier-growth-alln` — all-`n` growth of the budget-`C(n)` *admissible relaxation frontier* (distinct from the winning frontier at budget `S(n)`).

No theorem or verification is claimed for any of them; they are proposed falsifiable questions for independent challenge.
