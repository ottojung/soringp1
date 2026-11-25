# antonina-xKBGMa5TSnO6uQZpaSykQ5-lingered

Session: ses_e1567b91affeXPMHCkk5GHWhH5
Workspace: /home/lubko/soring301-exec-root-reachable-certified-quotient-20261117e
Created: 1794937210660; updated: 1794937368244

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 126 (msg_1ea9a834d001IXvSclRMXhp7xV)

Wrote `exec-report.md` in the worktree.

**Summary**
- **Question/front:** tested candidate exact root-reachable equivalences of optimal comparison histories stronger (interpreted as coarser) than relabelled-poset isomorphism, requiring an explicitly checkable two-outcome congruence and polynomially many classes for all `n`.
- **Candidates examined:** C0 relabelled-poset isomorphism on root-reachable optimal states (baseline, exact/checkable but not coarser; `quotient(1/ all)` reproduced for `n<=5` via `scripts/strategy_dag_probe.py`), C1 comparability-graph isomorphism (coarser on root-optimal states for `n<=6` in an ad hoc probe, `F` constant on that sample), C2 `(depth,F)` / `(depth,F,e(P))` partitions, C3 framed guarantee/join notion from `docs/research-framed-certificate-frontier.md`/`scripts/check_framed_strategy.py`.
- **Falsification/negative evidence:** C1 fails as a universal exact certified congruence (in-repo `docs/research-compression-next.md`: `F` non-invariant for isomorphic comparability graphs at `n=7`, transition ill-defined at `n=5`; root-reachable status of that witness not established here). C2 is not an explicitly checkable two-outcome strategy congruence. No infinite family was exhibited forcing superpolynomial classes for every admissible equivalence.
- **Findings:** **negative/inconclusive**. No candidate satisfying all requested properties (exact root-reachable, explicit two-outcome congruence, polynomial all-`n` bound) was identified or proved; simpler concrete candidates fail required properties. Polynomial root-optimal quotient + locally checkable height certificate would imply an NP certificate for `SORT-BOUND-U` (deduction), but existence remains open.
- **Key obstacles / next decisive question:** prove an all-`n` local two-outcome congruence with polynomial reachable class bound for a specific invariant/certificate scheme (e.g. rank-envelope/guarantee), or construct an explicit infinite root-reachable family refuting such congruence+bounds for a proposed candidate.

All claims in the report are labeled (definition/literature/deduction/experiment/conjecture/open/inconclusive); no completeness or complexity-class separation is claimed.
