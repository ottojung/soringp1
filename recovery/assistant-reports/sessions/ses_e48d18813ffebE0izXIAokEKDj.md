# antonina-mfwzhaUN2zTarRHwnotVI8-michaud

Session: ses_e48d18813ffebE0izXIAokEKDj
Workspace: /home/lubko/soring-fronts/curator
Created: 1794074638325; updated: 1794075133485

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 97 (msg_1b72efd4000125Qw0Inb5gwmsp)

{"fronts": []}

## Output 199 (msg_1b735ca3c001mnWJQne46kGxN1)

## Recovery check (what actually happened)

- Git worktree: only one untracked file, `frontier-candidates.json`; no commits, tracked changes, PRs, or Lean edits.
- Durable ledger checked: no new curator entry or board post from the interrupted turn.
- The interrupted turn had only read `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/research-frontier.json`, and run read-only board digests. It had provisionally written `{"fronts": []}`.
- I continued only the unfinished parts: the mathematical claim attack and the front decision. No external actions were repeated.

## Claim attacked and outcome

**Claim (all n):** `S(n) = min { d : T(d) >= n! }`, where `T(d)` is the board’s universal tightness threshold (largest `E` such that every finite poset with `e(P) <= E` is sortable in `d` comparisons). This is the natural “extension-threshold exactly certifies the antichain root” claim.

**Refutation, n = 4.** Board #301’s T(5)=20 witness is a 7-element poset with `e = 21` and exact minimax depth `6`. I reproduced both values locally with the repository evaluator plus an independent ideal-DP/minimax script (`/tmp/opencode/verify_t5.py`; no repo changes). Also `S(4)=5`. Since `21 <= 4! = 24` and `6 > 5`, every `E >= 21` has a poset needing more than 5 comparisons, so `T(5) <= 20 < 24`. Hence `min{d : T(d) >= 24} >= 6 > S(4)`. The identity fails already at `n=4`.

**Infinite-family extension (paper argument).** Take the same gadget `G` (`|G|=7`, `e(G)=21`, `m(G)=6`) and let `G_t` be the ordinal sum of `t` copies: `e(G_t)=21^t`, `m(G_t)=6t`, ground size `7t`. Let `n_t = min{n : n! >= 21^t}`. Then `n_t = Theta(t/log t)` and `e(G_t) <= n_t!`. Merge sort gives `S(n_t) <= n_t ceil(log2 n_t) = 4.3923t + o(t)`, so for all large `t`, `m(G_t)=6t > S(n_t)`. Therefore `T(S(n_t)) < n_t!` for infinitely many `n`. This uses only elementary ordinal-sum additivity/multiplicativity and the standard merge-sort bound; the base gadget is the part checked computationally.

## Honest limits

- This refutes **completeness** of extension-threshold root certification; it does **not** impugn soundness of `e(P) <= T(d) => m(P) <= d`, which holds by definition.
- It is a statement about general finite posets with the board’s `T(d)`. It does not transfer automatically to a lower bound or algorithm for `S(n)`, and makes no P/NP/PSPACE claim.
- The infinite-family argument is a paper deduction, not kernel-checked, and the all-n form (`T(S(n)) < n!` for every `n >= 4`) remains open; only `n=4` and an infinite subsequence are supported.
- No board post was made, since the result is not yet independently refereed and the recovery instruction forbids duplicating external effects.

## Front written

`/home/lubko/soring-fronts/curator/frontier-candidates.json` now contains one new front, `root-threshold-incompleteness-alln`, asking whether the n=4/infinite-subsequence failures extend to every `n >= 4`, with an explicit single-`n` falsifier and the certificate-completeness consequence. Schema lengths validated.
