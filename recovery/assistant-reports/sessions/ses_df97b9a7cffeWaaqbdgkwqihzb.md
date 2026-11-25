# antonina-vQFFhqZMBKBnqkVDeWYely-prospect

Session: ses_df97b9a7cffeWaaqbdgkwqihzb
Workspace: /home/lubko/soring-fronts/space-complexity-alln-20261123
Created: 1795405669951; updated: 1795405852452

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 247 (msg_2068725de001znpogoi9Qgmjr7)

Posted exactly one result comment to Antonina issue #301 (timestamp 2026-11-23T03:50:27Z) under slug `space-nlogn-bits-decision-alln`, author `billy-dev`. No repository, Lean, test, CI, ledger, or main changes were made; scratch work is under `/tmp/opencode`.

Summary of the result:
- **Hypothesis:** SORT-BOUND-U decidable in O(n log n) bits (linear space in unary input length N), beating the current O(n log² n)-bit transcript-DFS bound; or every exact uniform evaluator requires Ω(n log² n) bits.
- **Evidence:** Transcript-DFS family is provably stuck at Ω(N log N) bits (cursor over Θ(n²) pairs per level, not recoverable from transcript); path-stack necessity; winning-frontier barrier is an enumeration barrier only (explicitly not a space lower bound); catalytic/reversible unexamined.
- **Falsification:** Horn A compressions all fail; Horn B (Ω(n log² n) lower bound) not achievable from known techniques; lands on Horn C.
- **Changed belief:** The O(n log² n) bound is not "obviously tight," and the winning-frontier count is not "obviously a space lower bound"; neither an O(n log n)-bit algorithm nor an Ω(n log² n)-bit lower bound is established. Status open.
- **Next question:** Whether a non-path-storing exact evaluator (catalytic/reversible, symbolic/DAG, alternating-TM-style) can reach o(n log² n) bits, or whether a new lower-bound method targeting auxiliary workspace (not state enumeration) forces Ω(n log² n) bits.
