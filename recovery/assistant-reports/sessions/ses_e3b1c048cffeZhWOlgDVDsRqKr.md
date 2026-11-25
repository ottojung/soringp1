# antonina-kl32a7q084HChQ0tmsqt0c-fathom

Session: ses_e3b1c048cffeZhWOlgDVDsRqKr
Workspace: /home/lubko/soring-fronts/height-two-prime-excess-boundedness
Created: 1794304637832; updated: 1794318964794

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1768 (msg_1c5bc149c001Ahv0mQl62wYw15)

Recovering — checking what already happened before continuing.

## Output 1788 (msg_1c5bc54eb001c7pVYTPOEgLlkl)

No duplicate side effects — worktree clean, no prior post from this front. I'll verify the remaining load-bearing facts, then report.

## Output 1837 (msg_1c5be7863001Z8xvoS26woIHmw)

Done. Recovery check first: worktree was clean, no prior post from this front existed, all previous work was scratch-only in `/tmp/opencode/primeh2` — nothing duplicated.

**Finding (posted to #301 at 13:55:47Z, no repo/Lean changes):** the front's question stays OPEN, with two sharp new pieces:

1. **One-direction hardness [deduction]:** a uniform bound over all height-two prime posets would imply `E(n)`-boundedness (via the board-verified single-deletion interval `E(a)+E(b)−1 ≤ d ≤ E(a)+E(b)+2`). So a uniform-bound proof is out of reach — it would settle a major open sorting-theory statement.
2. **Precise obstruction:** writing `e(P) = m!k!·avg_s` gives `d ≤ E(m)+E(k)+log2(max_s/avg_s)+O(1)`. Any falsifier must grow `max_s/avg_s` *and* defeat cross/within integration savings — which needs exact `F` at `n≥11` or new `S` values, both currently infeasible.

**Failed approaches with exact blockers:** exhaustive `n≤7` (max excess 0); `n=8` non-isomorphic reps (max excess 1, genuine `eta=2` cases); single-deletion/pattern/band/tree-complement families (all excess ≤1); new glued prime family `R_t` with exact counts to `n=26` — but `F(R_3)` (`19≤F≤24`) resisted poset-state Minimax, 48-element symmetry reduction, budgeted DFS with orbits+Hanamura–Iwata+cutoff, and the extension-set solver. Literature SUPI `O(log e)` results are multiplicative, not additive-constant bounds; soundness ≠ completeness distinguished; no `SORT-BOUND-U` consequence claimed.
