# antonina-JCkVnTLqL395xC22oCy2Px-retro

Session: ses_e125cf1b2ffeOXJFXYNhePL6Nh
Workspace: /home/lubko/soring-fronts/curator
Created: 1794988248664; updated: 1794988500668

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 128 (msg_1eda682b8001amqM7DRBDgxH3m)

## Scope reviewed (billy-dev, clean worktree)
- Read: `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-frontier.json`, `docs/research-budgeted-dfs.md`, `docs/research-winning-frontier-barrier.md`, `scripts/research_frontier.py`.
- Board #301 (via `/home/lubko/soring301/scripts/board_digest.py --recent 12`, `--contains "frontier"`): newest posts include `n9-alltight-inconclusive` (2026-11-18T06:52Z), executive dispatch (2026-11-18T07:25Z) launching **in-flight** fronts `conp-adversary-certificate-alln` and `folfp-definability-sortboundu`, recent investigated reports for `n8-alltight-resolution`, `am-succinct-certificate-sortbound`, `randomized-exact-evaluator-game-tree`, `pendant-anchor-realizability`, `adversary-forced-nontightness`, `cheap-coarsening-optimal-root-play`, etc. Ledger snapshot inspected at `/home/lubko/.local/state/soringp1/frontier-ledger.json` shows large investigated/blocked history and active curation.

## Precise all-n falsifiable claim attacked (complexity/value boundary for exact unary `S(n)`)
**Claim (all n ≥ 1):** the information-theoretic bound is tight for exact comparison sorting, i.e. `S(n) = C(n) := ⌈log2(n!)⌉` for all `n`.
- **Model/encoding distinction:** `S(n)` is the minimax adaptive comparison-tree value (exact, distinct labelled keys, antichain root; `docs/problem.md`, `S_eq_adv_univ` context). This is a claim about the value/optimal-tree feasibility, not a lower bound on the *complexity of computing* `S(n)` or on `SORT-BOUND-U`; I do not conflate them.
- **Falsifier attempted:** exhibit any `n` with `S(n) > C(n)`.
- **Serious disproof (independently checkable, literature):** `n=12` has `C(12)=29` but `S(12)=30` (Wells; reported in Peczarski 2012 and summarized in `docs/literature.md`/board evidence). Hence the claim is **false**. This is a value-level refutation only; it yields no new theorem/counterexample about complexity classes for `SORT-BOUND-U`, no certificate soundness/completeness result, and no separation claim.
- **General-poset / certificate note:** no transfer from general-poset optimization/counting hardness was used; no certificate-completeness claim was made (soundness ≠ completeness per contract/frontier notes).

## Curator outcome
- Checked for genuinely NEW, independent, all-`n`, falsifiable questions grounded in newest board #301/docs and independently checkable evidence, excluding all `PREVIOUS` statuses and in-flight fronts (`conp-adversary-certificate-alln`, `folfp-definability-sortboundu` per 2026-11-18T07:25Z dispatch).
- Considered but rejected as non-defensible/duplicate/ungrounded for proposal now: PH/fixed-level alternation, BPP/UP/SC/NL membership, descriptive/uniform-circuit variants overlapping in-flight logic/AM-coNP lines without specific checkable evidence, method-specific time-factor refinements without a concrete all-`n` falsifier, and bounded-`n` all-tight cases (e.g. `n=9`) which are not all-`n`. Recent board/executive passes and ledger saturation (508 investigated, 21 blocked reported) corroborate absence of an obvious fresh direction.
- **Honest limit:** I did not identify a defensible new front with a precise all-`n` falsifier and independently checkable mathematical basis that is not duplicative or speculative. No Lean or repository changes were made (only the required output file).

## Artifact written
`/home/lubko/soring-fronts/curator/frontier-candidates.json`:
```json
{
  "fronts": []
}
```
