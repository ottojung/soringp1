# antonina-CkTIH0WqIj5TpepX2iVPqF-railways

Session: ses_df4252505ffe71ZIpf8Az4PEAE
Workspace: /home/lubko/soring301-exec-fibonacci-split-20261124
Created: 1795495222047; updated: 1795503368373

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1476 (msg_20c57085c001GmjoDrN4aiqX4q)

Done. Work stayed entirely in the scratch directory; canonical repo, Lean files, CI, and board #301 were untouched.

**Result:** No counterexample found. An exact minimax oracle checked every isomorphism class of finite posets on `n = 1..7` elements — **2450 classes total** (`1, 2, 5, 16, 63, 318, 2045`) — and in every poset with `m(P) ≥ 2` there is an optimal comparison with child depths `{m−2, m−1}` or `{m−1, m−1}`.

**Validation:** class counts match known unlabelled-poset counts; antichain depths match `S(n)` for `n≤7`; two independent oracle implementations agree on all 4473 labelled posets for `n≤5`. A memoization bug found mid-run was fixed and the full `n≤7` computation re-run from scratch.

**Artefacts:**
- `notes/summary.md` — scope, counts, validation, honest limits.
- `notes/proof-attempt.md` — partial constructive argument (pushing a grandchild comparison to the root) and the precise obstruction: it only guarantees the better child at depth `≥ m−3`, one step short of the required `m−2`.
- `notes/run.log` — final exhaustive run output.
- `scripts/oracle3.py` (`scripts/gen.py`, `scripts/oracle.py`) — oracle and enumerators.

**Honest limit:** This is finite evidence only. It does not prove the all-`n` statement; a counterexample at `n ≥ 8` remains possible. No theorem for all `n` is claimed.
