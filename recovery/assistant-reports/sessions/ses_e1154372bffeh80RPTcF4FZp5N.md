# antonina-HGSY3jKYLfsteKgx189XFW-hastily

Session: ses_e1154372bffeh80RPTcF4FZp5N
Workspace: /home/lubko/soring301-exec-t4-n7-complete-20261118
Created: 1795005597929; updated: 1795007036839

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 367 (msg_1eec1aa69001L3IBn2SqQvpVE0)

The task is complete. Here is a summary of what was done:

## Results

### n=7: Exhaustive certification ✅
- **Total labelled posets on 7 elements:** 6,129,859 (matches OEIS A001035(7))
- **Posets with e(P) ≤ 12:** 522,060
- **Counterexamples (e ≤ 12, m ≥ 5):** 0
- **Runtime:** 17 seconds (independent C reimplementation, `-O2`)
- T(4) ≥ 12 is now **exhaustively certified** for n ≤ 7.

### n=8: Partial search (time-limited)
- **Total labelled posets on 8 elements:** 431,723,379
- **Visited:** 56,142,924 (≈13%)
- **Posets with e ≤ 12 found:** 2,208,749 (all pruned: m ≤ 4)
- **Counterexamples:** 0
- **Runtime:** 300 seconds (hard time limit)
- This is **partial evidence only** — does not certify n = 8.

## Key methods
- Reused the poset model from `scripts/obstruction_probe.py` (succ bitmasks, `linear_extensions` DP, `minimax` recursion, `add_relation` transitive closure).
- Wrote an independent C reimplementation (`/tmp/opencode/t4_n7.c`, `t4_n8.c`) for speed and memory efficiency, with open-addressing hash sets and memoized m-value computation capped at 5.
- Applied the sound pruning rule: when e(P) ≤ 12 and m(P) ≤ 4, prune the entire subtree (monotonicity of m under relation addition).

## Deliverable
- `exec-report.md` written with hypothesis, method/sources, results (distinguishing exhaustive from partial), strongest argument/obstacle, consequence for T(4)=12 all-n (remains conjecture), and next decisive question.

The worktree contains only `exec-report.md` as a new file; all scripts and logs are in `/tmp/opencode`. No commits, PRs, or Lean files were created.
