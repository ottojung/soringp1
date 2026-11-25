# linear-extension-parameter-exact-eval

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sI7cxNN9n3uiYOMWSbHIiD-sullenly

## exit_state

clearexit

## question

For every finite poset P on n elements, is the exact minimax comparison number F(P) computable in time polynomial in n + e(P), where e(P) is the number of linear extensions, so that the n-element antichain would be evaluated in 2^{O(n log n)} time?

## basis

Each order ideal of P is a prefix of some linear extension, so P has at most (n+1)e(P) ideals and e(P) itself is computable in poly(n,e) time; Cardinal-Fiorini-Joret-Jungers-Munro (STOC 2010) sort from a poset with O(log e(P)) comparisons but do not compute exact F(P); docs/upper-bound.md and docs/research-budgeted-dfs.md give the current 2^{O(n log^2 n)} numeric bound.

## falsifier

Exhibit an infinite family of posets P_i with e(P_i) bounded by a polynomial in |P_i| for which deciding F(P_i) <= k is NP-hard, or prove that any exact algorithm needs time superpolynomial in n + e(P).

## implication

A positive answer would improve the documented exact unary evaluator from 2^{O(n log^2 n)} to 2^{O(n log n)}; a negative family would rule out extension count as the parameter for reaching that frontier.

## finding_unverified

ior turn had only read files/network; it made **no** post, commit, or file change.
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
I’ll first check the worktree, board, and durable ledger for effects since the last recovery. I won’t repeat the research or post unless something is demonstrably unfinished.
Recovery check complete. The worktree is clean at `6a96398`; no commits or stashes. Board #301 contains the single prior comment from this front (`sha256:S1QfYgid…`), so I did not post again.

The durable ledger still marks the front `running`, and its Antonina agent is confirmed alive. Since the prior research and board update already happened, I took no further action. The remaining uncertainty is whether the live agent will produce additional findings; that is left for review rather than duplicated or interrupted.

## Other metadata

```json
{
  "finished_at": 1794089929.4553623,
  "started_at": 1794089240.1560051
}
```
