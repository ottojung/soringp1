# antonina-xgJIO1weFafObqFbj6Dd2e-lifetime

Session: ses_e13354facffez2tqHEzT0VAK6c
Workspace: /home/lubko/soring-fronts/curator
Created: 1794974068821; updated: 1794974305844

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 171 (msg_1ecce0eae001kckTEjx506H21y)

**Claim attacked (all-n, falsifiable; exact unary `S(n)` model):** *For every root-tight `n` with `S(n)=C(n)=⌈log₂(n!)⌉`, every height-`S(n)` optimal adaptive comparison tree from the `n`-antichain must reach some state `P` with positive information excess `F(P) > ⌈log₂ e(P)⌉` (adversary-forced non-tightness).* A falsifier is any root-tight `n` admitting an all-tight optimal tree (every reachable `P` satisfies `F(P)=⌈log₂ e(P)⌉`).

**Attempted disproof (serious):** [literature/deduction, independently checkable via #301 report] The newest #301 result `SoringP1 frontier: n8-alltight-resolution` (2026-11-18T00:18:38Z) resolves the smallest open root-tight case `n=8` (`S(8)=C(8)=16`): an all-tight height-16 optimal tree exists (information-bound-pruned `can_sort`/`alltight` search, as reported). Therefore the universal claim above is **false** at `n=8`: the sorter has an optimal strategy avoiding non-tight states on every path, so the adversary cannot force non-tightness for all root-tight `n`. This concerns the fixed antichain-root minimax game for exact `S(n)`, not a general-poset statement.

**Distinctions / limits:** This is a bounded counterexample to that universal forcing claim only; it does **not** settle forcing for other `n` (e.g. `n>=12` cases discussed on #301, or whether non-tightness is forced for infinitely many `n`), does **not** yield a uniform bound/algorithm, class separation, or certificate-completeness theorem, and does **not** transfer general-poset hardness. Certificate soundness vs completeness remains separate (a sound DAG/checker is not a completeness/NP-membership proof). No Lean or repository changes were made.

**Curator outcome:** Studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`/repo docs, and current board #301 (digest, including newest posts through `n8-alltight-resolution` and the Executive depletion note). Checked against the full `PREVIOUS` list and recent investigated fronts (framed-DAG/certificate, coarsening/realizability, catalytic/reversible/randomized/AM routes, space/winning-frontier barriers, nontightness, etc.). No genuinely new, independent, defensible all-`n` falsifiable question grounded in new evidence was identified beyond duplicates or already-investigated directions, so I refused to propose redundant fronts.

Wrote `frontier-candidates.json` (billy-dev, `/home/lubko/soring-fronts/curator/frontier-candidates.json`):
```json
{
  "fronts": []
}
```
