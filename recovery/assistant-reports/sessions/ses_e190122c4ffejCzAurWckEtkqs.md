# antonina-2NhzpjwitsaGeZpkyhFAZr-keloid

Session: ses_e190122c4ffejCzAurWckEtkqs
Workspace: /home/lubko/soring-fronts/info-bound-gap-invariant-alln
Created: 1794876824945; updated: 1794878606414

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 366 (msg_1e71a0141001BZcOOakSJxO2zm)

I investigated the invariant question in the scratch worktree without modifying the repository.

Key results:
- The literal all-n question is already answered affirmatively by the existing one-ply bound `L1`: its suffix-extended family `W ⊕ C_t` (n=5 witness plus a total chain) is reachable, has `C=3`, `L1=4=F` for every `t≥0`, so a sound invariant stays strictly above the information bound on arbitrarily large states. Thus the “eventual equality for every invariant” falsifier is false.
- This does **not** generalize the `n=12` antichain root: `L1(A_n)=C(n)` for `n≤12`.
- New exact checks: `L2(A_n)=C(n)` for `n≤12`, and for `n=12`, `L1(child)=28=C(child)` and `L2(child)=28`. Fixed-depth ply bounds do not lift the antichain root.
- Scalar/merge invariants remain refuted as root generalizers; exact minimax `F` is trivially `>C` on known gaps but gives no cheaper strengthening.

No new theorem beyond verified computations; no post to #301. Concise local report written to `/tmp/scratchpad/local_report_n12.md`. Worktree remains clean.
