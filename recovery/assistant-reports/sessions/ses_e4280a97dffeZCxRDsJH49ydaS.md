# antonina-WCjCtwxgGJc0i15eR6dS4X-praised

Session: ses_e4280a97dffeZCxRDsJH49ydaS
Workspace: /home/lubko/soring-fronts/framed-height-overhead-gap
Created: 1794180601575; updated: 1794181588002

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 355 (msg_1bd8e46bc001zH1YQpIfZ0K23L)

Reported to board #301 as **“SoringP1 frontier: framed-height-overhead-gap”** (2026-11-08T23:46Z). Worktree remains clean; no repository or Lean changes were made.

**Main finding: the front’s literal definition collapses.**

If “polynomial-size” is allowed to depend on `n`, then `g(n)=0` for every fixed `n`: take any optimal comparison tree of height `S(n)`, which has finite size `T(n) ≤ 2^{S(n)+1}`, and choose a polynomial `p_n(x)=x^c` with `c ≥ log_n T(n)`. The checker accepts that tree at exact height `S(n)`. Thus no finite `n` can falsify `g(n)>0`, and the three-way question only makes sense after fixing one polynomial `p` globally:

`g_p(n) = min{h : some accepted framed DAG of size ≤ p(n) has height ≤ S(n)+h}`.

Zero overhead for one fixed `p` gives `SORT-BOUND-U ∈ NP`; per-`n` exponents do not.

**Deductions reported**

1. Any accepted DAG sorting `n` has height at least `S(n)`.
2. Let `d(n)=S(n)-S(n-1)`, `C(n)=ceil(log₂ n!)`, and `c(n)=ceil(log₂ n)-d(n)`. Then `d(n)` is `floor(log₂ n)` or `ceil(log₂ n)`, so `c(n) ∈ {0,1}`.
3. The isolated-key insertion lift gives, after adjusting `p`,
   `g_p(n) ≤ g_p(n-1) + c(n)`.
   So exact height propagates across maximal increments (`c=0`), while an insertion-only family gains at most one comparison at each nonmaximal increment. A `c=0` step pauses but does not reset accumulated overhead, so this does not prove boundedness.

**Why the cited forgetting-loss identity does not give the falsifier**

At height `S(n)+h`, the path budget is `E(n)+h`, and the terms `1-H` and `λ` are nonnegative. Zero overhead is compatible with all terms being zero. The identity is an accounting constraint, not a lower bound on `h`. The weak-anchor calculation also rules out charging a constant per join, and frames allow one terminal node to carry many input orders, so the `n!` path count gives no node lower bound.

**Conclusion**

No all-`n` proof of zero or bounded overhead and no infinite-family lower bound were obtained. The decisive missing object remains a uniform polynomial-size optimal-height framed family, or a genuine infinite-family size-height tradeoff.
