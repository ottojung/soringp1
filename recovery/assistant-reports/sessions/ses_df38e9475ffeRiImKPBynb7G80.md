# antonina-MAoURI5aksRG8CYf0wou3k-ilium

Session: ses_df38e9475ffeRiImKPBynb7G80
Workspace: /home/lubko/soring-fronts/curator
Created: 1795505089453; updated: 1795505348162

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20c716be00017weT3hINh6KWwQ)

I'll start by getting oriented: checking the git branch/state and reading the key documents.

## Output 25 (msg_20c717b5b001ieI6fp7G5SzWTj)

I'm on `main` but need to work on `billy-dev ONLY`. Let me check branches and read the operations/literature docs.

## Output 44 (msg_20c718857001dFovuyOWETnUVS)

`billy-dev` is the execution host (per operations.md), not a git branch. Let me confirm the host and read the research board digest #301.

## Output 59 (msg_20c71a5a1001W8EFSVYsFaB42v)

Let me read more board pages and the existing frontier definitions to avoid duplicates.

## Output 74 (msg_20c71c5b5001c9jeQnRNQsOsYG)

Let me survey the research docs and the full recent board to ground new directions.

## Output 89 (msg_20c71fc7b001rxbiJx7HLFltLa)

Let me read the full newest FJ post and key research docs to understand the frontier.

## Output 131 (msg_20c729142001u0a0goT5cC5k6v)

Let me fetch the full newest FJ post and scan more board pages to map what's open.

## Output 142 (msg_20c72a8d8001LdvP84IaQMf5ur)

Let me read a few investigated posts in full to precisely avoid duplication.

## Output 153 (msg_20c731ac5001Q5gx2b9KpiftMl)

Let me scan several board pages for key candidate topics to avoid duplication.

## Output 173 (msg_20c73a639001b6X5mxEdbXD8Vi)

Let me compute the Ford–Johnson height at n=28 and check it against the literature interval S(28)∈{99,100,101}.

## Output 184 (msg_20c742903001aRswG9ZvqQ76q4)

Let me check a couple of directly-related prior posts (framed DAG polynomiality, ESO certificate, adversary/coNP) to position new fronts precisely.

## Output 195 (msg_20c7470190014LmlcqRz1GyhEA)

Let me run a clean scratch analysis of an incremental (first-difference) invariant of exact S(n) using literature values, as a concrete attack target.

## Output 215 (msg_20c74c430001518qBEMO1apdoD)

I've grounded the analysis. Let me validate the candidate front field lengths before writing.

## Output 226 (msg_20c7504b4001PImtZyLdF5J4Vo)

All field constraints pass. Now I'll write the JSON object to the required path.

## Output 246 (msg_20c753c160012zzQ9pkmk8z4e8)

## Summary

Host confirmed as `billy-dev`; working directory clean on `main` at `f89f6d0` (no commits, branches, Lean, tests, CI or ledger changes). I studied `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-plan.md`, the certificate/barrier/Sergeev/winning-frontier notes, primary literature leads (Ford–Johnson, Sergeev TR20-096, Mahaney, Stober–Weiß), and the newest board #301 posts through the `fj-exact-barrier-20261124` result (2026-11-24T06:36Z), plus a scan of the prior front slugs and the 20-item PREVIOUS list to avoid duplicates.

### Attack performed (and honest limits)

I attacked two all-n claims about exact unary `S(n)` and tried to refute them:

1. **"SORT-BOUND-U ∈ coNP via a succinct adversary certificate."** I could **not** disprove it. The winning-frontier barrier (`2^{Ω(n log² n)}` nonisomorphic winning states) rules out *enumerating* winning states, but not a succinctly represented adversary strategy, and no unconditional size lower bound for any fixed certificate grammar is available; a general refutation would approach PSPACE vs coNP territory. Crucially I kept the distinctions straight: a *sound* local forcing invariant (admissible child ⇒ correct certificate) is not *complete* (must force an obstruction from the antichain root against every sorter), and general-poset adversary hardness does not transfer to `S(n)` without an encoding-preserving reduction.

2. **First-difference invariant** `d(n)=S(n)−S(n−1) ∈ {⌊log₂n⌋,⌈log₂n⌉}` and the related surplus structure. A fresh scratch computation over known `S(1..22)` is consistent with it; the only surplus drop is at n=20, and `F_FJ(28)=101` vs `S(28)∈{99,100,101}` gives no explicit FJ-crossover witness (FJ non-optimality remains ineffective). A concrete potential falsifier is a surplus drop 1→0 at a "dangerous" n (e.g. 25 or 28) where the information increment equals `⌊log₂n⌋`; `S(23+)` is open, so this is **unresolved**, not a theorem. This is distinct from the investigated surplus≥2/density fronts.

No genuine new theorem or counterexample met the publication gate, so no Lean/repository/board/ledger changes were made.

### Output

Wrote ONLY the required JSON object to `/home/lubko/soring-fronts/curator/frontier-candidates.json` (valid JSON, 3 new nonredundant fronts; all field-length constraints satisfied):

- `succinct-adversary-copnp-sortboundu-alln` — coNP/adversary-succinctness angle (no prior dedicated front).
- `sergeev-framed-dag-exact-budget-alln` — fills the concrete architecture gap the newest FJ no-go explicitly leaves open.
- `first-difference-info-bound-increment-alln` — local-update structure of exact `S(n)` with a concrete dangerous-n falsifier.

The only filesystem side effect is the required `frontier-candidates.json` (untracked); the worktree has no other changes.
