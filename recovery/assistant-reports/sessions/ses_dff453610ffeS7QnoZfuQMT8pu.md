# antonina-fWSsuYDypdM5mVzVFXz3q5-ischial

Session: ses_dff453610ffeS7QnoZfuQMT8pu
Workspace: /home/lubko/soring-fronts/unary-threshold-linear-space-nondecomposition-alln
Created: 1795308571177; updated: 1795309137694

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 438 (msg_200c35bec001wOxnBfbZTkpHH5)

Posted the finding to Antonina #301 (no repository/Lean/test changes).

**Result:** Neither horn of the falsifier was achieved. O(N) space for `SORT-BOUND-U` remains open; no Ω(N log N) lower bound for arbitrary uniform deciders was proved.

Key points:
- Transcript/play-simulating methods are forced to Ω(N log N) bits; reversible computation gives no improvement; alternating O(N) space would imply a 2^{O(N)}-time algorithm.
- Catalytic storage has capacity Ω(N log N), and encrypted-storage fails due to Ω(N log N) ordinary key bits; no catalytic algorithm is known.
- The winning-frontier barrier is enumeration-only: it rules out listing winning posets, not selective/symbolic/catalytic methods, and does not prove arbitrary-solver hardness.
- Certificate soundness is easy for explicit trees, but succinct sound certificates (NP membership) and completeness remain open; the frontier count does not rule out succinct certificates.
- General-poset hardness results do not transfer to the antichain root without a reduction.

Honest limit: O(N) space is at least as hard as improving the time bound from 2^{O(N log N)} to 2^{O(N)} (or proving a matching time lower bound). Next decisive check is whether S(n) is computable in 2^{O(n)} time.
