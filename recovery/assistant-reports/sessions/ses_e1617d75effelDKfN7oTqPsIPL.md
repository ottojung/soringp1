# antonina-k3t66eBGFeX5cXtf0hFQ5S-reacted

Session: ses_e1617d75effelDKfN7oTqPsIPL
Workspace: /home/lubko/soring301-exec-optimal-play-leaf-merge-bound-20261117
Created: 1794925668591; updated: 1794925780736

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 44 (msg_1e9e9bcd20013JWDVt5ISTNYWy)

Created `exec-report.md` with a local analysis of permutation-framed DAG certificates for height-`S(n)` exact optimal sorting strategies.

**Main findings (all `n`, labeled in report):**
- **Terminal outcomes/leaves:** [deduction] any sound, correct certificate must terminate with a total-order guarantee equal to the actual input order for every permutation, so distinct terminal total-order outcomes are exactly **`n!`** and cannot be compressed below `n!` (refutes terminal compressibility).
- **Merge/forgetting events:** [deduction] no universal `>0` lower bound is forced by the semantics alone (a non-sharing decision tree has `n!` leaves and zero forgetting); merges/forgetting are representation-dependent compression devices, constrained but not required in count.
- **Entropy/forgetting framework:** [literature/deduction, `docs/research-framed-certificate-frontier.md` §4] on auxiliary/majority-path accounting, cumulative imbalance+forgetting is bounded by `S(n)-log₂(n!)` (0 for `1 ≤ n ≤ 11`, <1 bit aggregate for `n=12`, `o(n)` asymptotically by Sergeev as cited), giving a tight necessary condition for exact-optimal certificates but not a polynomial-size refutation.
- **Concrete obstruction:** unconditional terminal identity obstruction **O1** (`n!` outcomes must be distinguished; polynomial compression cannot materialize/enumerate terminals) plus exact-optimal slack constraint **O2**; together these are barriers/constraints, while all-`n` polynomial-size exact-optimal framed-certificate completeness remains **open** (consistent with docs). Includes small-`n` table (`n!`, `S(n)`, slack) and implications for the NP-certificate frontier.

No repo/Lean/PR changes were made beyond `exec-report.md`.
