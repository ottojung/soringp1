# antonina-1E2RISRtHxPLxoHM8qKD4e-democrat

Session: ses_e4702fb2cffeMW8Py5fsNqUwcv
Workspace: /home/lubko/soring-fronts/strategy-certificate-not-tree
Created: 1794104952044; updated: 1794104962138

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 19 (msg_1b8fd08c5001p2wWhKETk6uAQ4)

## Verdict: TREE-REQUIRED

**Evidence**

1. **Reconstructed result (Claim C, `docs/research-certificates-barriers.md` §4):** Every correct reduced sorting tree has exactly `n!` leaves and `2n!−1` nodes. The reduced-tree pruning argument (both outcomes feasible at every internal node) forces each leaf to be reached by exactly one permutation, so no subtree can repeat; merging identical subtrees yields no compression. This is a *deduction* backed by experiment.

2. **Experiment (`docs/research-certificates-barriers.md` §5):** For `n ≤ 6`, `nodes = 2·n! − 1` exactly (1, 3, 11, 47, 239, 1439) and `leaves = n!`. Thus the optimal tree is already irreducible under DAG compression of identical subtrees — no nontrivial compression occurs even for small `n`. The minimal DAG size equals the tree size.

3. **Candidate forms assessed (doc table):**
   - **DAG/branching-program compression:** worst-case state space is the number of labelled posets `2^{Θ(n²)}` (A001035: 1, 3, 19, 219, 4231, 130023 for `n=1..6`); no polynomial bound known, and the small-`n` irreducibility of the optimal tree is evidence against it.
   - **Program computing the strategy:** not known polynomially checkable over all `n!` inputs.
   - **Inductive potential certificates:** only the information bound `⌈log₂ n!⌉` is known, and it is not tight (first failure at `n=12`).
   - **Non-uniform advice `S(n)`:** exponential in input length.

4. **Consequence:** No polynomial-in-`n` (nor polynomial-in-input-length) succinct certificate for `S(n) ≤ k` is known or evidenced; the only sound+complete witness is the full reduced decision tree of size `2n!−1`. NP/`NP`-membership of `SORT-BOUND-U` remains open, and the absence of a succinct certificate is the stated central obstruction. The minimax correspondence is complete and untouched.

**Bottom line:** TREE-REQUIRED — the optimal sorting tree is irreducible under subtree merging for `n ≤ 6`, and no alternative succinct form has demonstrated polynomial verifiability.
