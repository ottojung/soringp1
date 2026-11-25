# antonina-rG3lAOXS9MofDzKPO2d1UW-triceps

Session: ses_e48d9e7aaffenOM15KDw2BaPFW
Workspace: /home/lubko/soring-fronts/exec-merge-tree-rounding-gap-20261107
Created: 1794074089560; updated: 1794074126556

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 60 (msg_1b726715b001Lno17N7UJhK03C)

## Result: the proposed rank-envelope abstraction loses essential correlation

I could not establish the requested polynomial-size framed DAG with height bounded by Sergeev’s comparison count. The natural abstraction—replace each pending key’s coupled container by an independent rank interval and intersect guarantees at joins—is **not sound as a representation of the required joint state**: its coordinate-wise envelopes admit combinations of ranks that need not be jointly feasible. No alternative invariant or join semantics that preserves Sergeev’s bound follows from that abstraction.

The obstruction is structural, not a lower bound against every possible certificate. A sound join must retain a relation containing every concrete permutation represented by each incoming path. Intersecting their guaranteed pairwise orders can discard correlations between pending keys; subsequent comparisons may rely on those correlations. Avoiding that loss may require retaining disjunctions of joint states, and the argument here gives no polynomial bound on their number. So this is a precise failure of the natural abstraction, **not** a proof that Sergeev’s algorithm cannot have a polynomial-size framed representation.

## Paper and bound

Primary source: Igor Sergeev, [*On the asymptotic complexity of sorting*](https://eccc.weizmann.ac.il/report/2020/096/), ECCC TR20-096 (2020), Theorem 3. The ECCC record describes the model as sorting elements of a linearly ordered set by pairwise comparisons and states the asymptotic result
\[
\log_2(n!)+o(n).
\]
The result is obtained by **group insertion**, not by the independent pending-key insertion scheme summarized in the repository’s rank-envelope note. The paper’s asymptotic statement alone is not an explicit finite comparison bound. I could inspect the primary report page but could not retrieve and inspect the PDF in this environment; therefore I cannot responsibly give Theorem 3’s exact finite bound or claim a line-by-line audit of its container construction. That limits this conclusion to the failure of the natural abstraction, rather than a definitive obstruction to the paper’s construction.

The task concerns adaptive comparisons on distinct labelled keys, matching the sorting-number model in `docs/problem.md`; the ECCC abstract’s linearly ordered elements are consistent with that model. **Theorem 3’s asymptotic bound must not be presented as an exact finite budget.**

## Certificate consequence and missing bridge

Even if a polynomial-size sound framed DAG reproducing Sergeev’s construction at its proved finite comparison bound were obtained, it would certify only a **near-optimal upper bound** on \(S(n)\), not a height-\(S(n)\) sorter. It does not settle the exact-optimal certificate question in issue #47.

To bridge to exact certificates, one would additionally need a theorem that, for every \(n\), supplies a polynomial-size sound framed DAG of height exactly \(S(n)\)—for example, a polynomial-size transformation from a certificate at Sergeev’s bound to an optimal sorter without increasing certificate size. No such transformation follows from the asymptotic gap: \(o(n)\) excess comparisons does not imply zero excess at any given \(n\).

**Sources consulted:** Sergeev, ECCC TR20-096 (primary report record); `docs/problem.md` (sorting model); `docs/research-framed-certificate-frontier.md` §§1, 3, 5 (framed join semantics and #47 distinction). No repository edits, Lean work, or board post.
