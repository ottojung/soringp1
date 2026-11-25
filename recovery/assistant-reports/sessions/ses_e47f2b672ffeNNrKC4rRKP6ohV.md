# antonina-sI7cxNN9n3uiYOMWSbHIiD-sullenly

Session: ses_e47f2b672ffeNNrKC4rRKP6ohV
Workspace: /home/lubko/soring-fronts/linear-extension-parameter-exact-eval
Created: 1794089241196; updated: 1794089913342

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 104 (msg_1b80dc46e001V27J2rHSVuMs8b)

**No theorem or counterexample found.** I did not create repository or Lean changes, or post to board #301.

For the proposed claim, there is a clear upper bound but not the requested improvement: enumerate the order ideals of \(P\), then evaluate the minimax recurrence on them. Since every ideal is a prefix of a linear extension, there are at most \((n+1)e(P)\) ideals; each state has at most \(\binom n2\) comparison choices. This yields a straightforward polynomial-in-\(n+e(P)\) algorithm, provided the recurrence’s state bookkeeping is polynomial. For the antichain, \(e(P)=n!\), so this is \(2^{O(n\log n)}\).

That establishes the **positive claim**, not a disproof. The serious limitation is that it does not demonstrate a strict improvement over the documented \(2^{O(n\log n)}\) unary threshold bound: the antichain’s extension count is already \(n!\), and the bound is of the same asymptotic scale. Nor does it give a polynomial-time algorithm in \(n\) for the antichain.

The proposed falsifier is also not presently established. Hardness for general posets does not by itself yield hardness on a family with polynomially many extensions. And the board’s recent certificate discussion underscores a separate gap: a polynomial-time **soundness** checker for losing-state certificates does not establish polynomial-size **completeness**. I found no reduction bridging either issue to exact unary \(S(n)\), and no superpolynomial lower bound for exact algorithms.

**Exact obstruction:** the extension/ideal count bounds the state space, but does not settle whether its recurrence can be evaluated asymptotically faster than the existing unary evaluator—or whether extension count is an optimal parameter. The primary-literature search was inconclusive, so no new complexity conclusion is justified.

## Output 128 (msg_1b80dfe75001Nt9LyARXyy5Wb2)

I'll verify what actually happened before doing anything further. Read-only inspection only.

## Output 165 (msg_1b80e2a5a001Yckx6GCwcNqWZE)

Before anything else, let me confirm the actual side-effect state and then continue the unfinished research (the ledger still marks this front `running`, and my prior turn produced only a partial analysis, no post/commit).

## Output 384 (msg_1b8170a10001joLcOcj0Kpddl1)

## Recovery audit (before doing any work)

- Working directory `linear-extension-parameter-exact-eval` on `billy-dev`: **clean**, HEAD `6a96398` (Oct 29), no stashes, no new commits.
- Durable ledger `~/.local/state/soringp1/frontier-ledger.json`: front `linear-extension-parameter-exact-eval` was already marked `running` (agent `sI7cxNN9n3uiYOMWSbHIiD-sullenly`), started ~22:07Z. That is keeper bookkeeping, not a side effect of mine.
- Board #301: no post from this front existed; the newest prior message was 21:37Z. The prior turn had only read files/network; it made **no** post, commit, or file change.
- I therefore continued only the unfinished research and made exactly **one** new board comment (id `sha256:S1QfYgid9G6DutYHwfSEvh7QLo1p1TOsBhkX6bTVWZc`, 22:17Z). I did not touch the unrelated Viche post at 22:12Z.

## Mathematical finding: the front’s stated evidence is unsound; no falsifier

**1. Ideals are not minimax states.** The recurrence
`F(P) = 1 + min_{i||j} max(F(P+ij), F(P+ji))`
reaches *poset extensions* of `P`, not order ideals. From the antichain `A_n` every labelled poset on `n` elements is reachable (add a generating set of the target poset’s relations; each addition is legal). That is `2^{(1/4−o(1))n²}` states (Kleitman–Rothschild, Trans. AMS 205 (1975)), while `e(A_n)=n!=2^{O(n log n)}`.

Independent DP check of states actually visited: `n=1..5` gives `1, 3, 19, 219, 4231` (A001035), against the ideal bound `(n+1)e = 2, 6, 24, 120, 720`. At `n=4` the bound 120 is already below 219; at `n=6`, 5040 < 130023. So the `(n+1)e(P)` fact cannot justify any `poly(n+e)` algorithm. Even after quotienting isomorphism, the repository’s winning-frontier theorem gives `2^{(1/4−o(1))n log² n}` winning states, which exceeds `n!` for large `n`.

**2. The claim is at least as hard as the open frontier.** Ordinal-sum additivity (proved in `docs/research-series-decomposition.md` §2) gives, for `P = C_N ⊕ A_k`:
`e(P)=e(C_N)·e(A_k)=k!`, `F(P)=0+S(k)`, `n=N+k`.
Choosing `N=k!−k` gives `n=e(P)=k!`, hence `poly(n+e)=2^{O(k log k)}`. A positive answer to the front, even restricted to this chain⊕antichain family, is exactly an `S(k)` algorithm in `2^{O(k log k)}`. It cannot be easier than the documented target; the converse is not claimed.

**3. Falsifier not achieved.** Any poset with an antichain of size `k` has `e(P)≥k!`, so a `poly(n)`-extension family carries only `k=O(log n/log log n)` and can encode at most `S(k)` for such `k`. Deciding `S(k)≤t` is not known NP-hard, and general-poset hardness does not transfer. No infinite poly-`e` NP-hard family and no super-polynomial lower bound were found.

## Honest limits

- This is **not** a disproof of the front, and not an improved evaluator: the front remains open, and the positive direction is exactly the frontier improvement.
- The obstruction is rigorous only against state-enumerating/ideal-counting methods (and is reinforced by the existing winning-frontier barrier); a fundamentally non-enumerative algorithm is not excluded.
- Certificate soundness (the losing-state DAG checker) still yields no polynomial-size completeness, so no NP/coNP membership follows either.
- No Lean, repository, or commit changes; the verification script lives at `/tmp/opencode/verify_front.py` and the board payload at `/tmp/opencode/board_body.txt`.

## Output 396 (msg_1b81746380011Aa3LfXUus6T5B)

I’ll first check the worktree, board, and durable ledger for effects since the last recovery. I won’t repeat the research or post unless something is demonstrably unfinished.

## Output 422 (msg_1b8177d7c001SWQYBmtg67wZQF)

Recovery check complete. The worktree is clean at `6a96398`; no commits or stashes. Board #301 contains the single prior comment from this front (`sha256:S1QfYgid…`), so I did not post again.

The durable ledger still marks the front `running`, and its Antonina agent is confirmed alive. Since the prior research and board update already happened, I took no further action. The remaining uncertainty is whether the live agent will produce additional findings; that is left for review rather than duplicated or interrupted.
