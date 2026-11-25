# incremental-sort-number-gap-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

sIryHXrQvFK8qc5gyEMtQT-albert

## exit_state

clearexit

## question

Is there a universal constant C such that S(n+1) <= S(n) + C holds for all n >= 1 for the exact comparison sorting number S(n)?

## basis

Definition of S(n) and known exact values/literature in docs/problem.md and docs/literature.md show nonuniform small increments but no all-n additive bound.

## falsifier

Exhibit any n >= 1 with S(n+1) - S(n) >= C+1 for every fixed candidate C tested, or prove an explicit infinite family with unbounded increment S(n_i+1)-S(n_i).

## implication

A uniform additive increment bound would constrain the growth and recurrence structure of exact S(n), informing dynamic or incremental evaluation strategies for SORT-BOUND-U.

## finding_unverified

es; $n\ge 23$ is open.
- **Trivial one-step upper bound (deduction, insertion):** $S(n+1)\le S(n)+\lceil \log_2(n+1)\rceil$ for all $n\ge 1$. Proof sketch: run an optimal strategy on any $n$ elements to obtain their total order in $\le S(n)$ comparisons, then binary-insert the $(n+1)$-th element into the $n+1$ possible positions in $\le \lceil \log_2(n+1)\rceil$ comparisons. Thus any increment obstruction cannot exceed $O(\log n)$ per step and is compatible with $S(n)=\Theta(n\log n)$.
- **Asymptotic gap (literature, Sergeev):** $S(n)-\log_2(n!)=O(n/(\log n)^{1/5})=o(n)$, so $S(n+1)-S(n)=\log_2(n+1) + o(n)$ in coarse form; this does not by itself yield an explicit infinite family of large single-step jumps nor a bounded-increment theorem.

## Failed/discriminating approaches and honest limits
- **Searching known values for a counterexample:** only disproves boundedness by very small fixed $C$ ($C<5$); insufficient for the all-$n$ universal question. No $n\le 22$ serves as a uniform falsifier for large $C$.
- **Using Sergeev/upper-bound asymptotics to force unbounded single-step increments:** inconclusive as a stepwise lower bound because $o(n)$ slack can dominate $\log n$ in the difference estimate; the clean refutation comes instead from the global information lower bound vs linear accumulation.
- **General-poset / certificate considerations:** not needed and not used; the result here is specific to the antichain-root sorting number $S(n)$ and its comparison-tree information bound (no claim about arbitrary posets, networks, or certificate completeness).
- **Exact obstruction/further precision:** I did **not** produce an explicit infinite family $(n_i)$ with a proved closed-form lower bound on $S(n_i+1)-S(n_i)$ beyond “for each $C$ some $n$ exists” (which already refutes universality). Determining finer increment behavior (e.g. infinitely often $\ge c\log n$, or sharp oscillations) remains open and would require stronger control of exact $S(n)$ than is currently available for large $n$.
- **No repository changes, no Lean, no new theorem claimed beyond this deduction from established facts.** If this is considered already implicit in standard bounds, that should be recorded as such on #301 rather than as a novel advance.
**Recovery audit result.** The interrupted turn left no repository side effects: `git status` clean, no new commits, and no board post for this front on #301 pages 1–55 (`--contains "universal constant"` returned zero). The only unfinished external action was the board report itself.

**Action completed (once).** Posted a single concise comment to Antonina #301 (id `sha256:wkKxSdNV6rnXmsqFtYo8JmoOG7JI--M5MrfKzGHKT_8`, 2026-11-17T12:23:31Z, author "OpenCode research billy-dev") with the mathematical finding and limits. No duplicate posts, commits, or repository changes were made.

**Finding reported:** There is no universal constant $C$ with $S(n+1)\le S(n)+C$ for all $n\ge 1$. Proof: such a $C$ would force $S(n)=O(n)$ by induction ($S(1)=0$), contradicting $S(n)\ge \lceil\log_2(n!)\rceil=\Theta(n\log n)$. Hence $\sup_{n\ge1}(S(n+1)-S(n))=+\infty$; for every fixed $C$ some $n$ has increment $\ge C+1$. Trivial upper bound remains $S(n+1)\le S(n)+\lceil\log_2(n+1)\rceil$ (binary insertion). Known small increments for $n\le 21$ max at $5$; $n\ge 23$ open, so no finite $n\le 22$ falsifies $C\ge 5$. No explicit infinite family with closed-form large single-step jumps was produced beyond existence. No Lean, repo, or PR changes.

## Other metadata

```json
{
  "finished_at": 1794918252.6241329,
  "started_at": 1794918089.1904728
}
```
