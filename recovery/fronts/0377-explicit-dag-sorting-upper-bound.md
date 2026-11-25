# explicit-dag-sorting-upper-bound

## status

investigated

## origin

ai_proposal_unverified

## agent_id

6qQziKmWqZguJRJYHZDeOD-ethics

## exit_state

clearexit

## question

Does the Haeupler-Hladik-Iacono-Rozhon-Tarjan-Tetek / van der Hoog-Rotenberg-Rutschmann DAG-sorting algorithm, specialized to the n-antichain with an explicit base-case library, give an all-n height bound U(n) with U(n)-ceil(log2 n!)=o(n) and a comparison tree constructible in time polynomial in n?

## basis

arXiv:2407.21591v6 and the Haeupler et al. worst-case-optimal DAG-sorting theorem; docs/research-upper-witnesses.md and the board's effective-Sergeev obstruction; no DAG-sorting or partial-information upper-bound front appears in the ledger.

## falsifier

Show that the algorithm's leading constant is at least 1+epsilon for infinitely many n, so its antichain height is only a constant factor above log2 n!, or prove a polynomial-time obstruction to materializing its implicit comparison tree.

## implication

A positive answer yields a uniformly computable finite upper bound with sublinear excess, replacing the asymptotic-only Sergeev threshold and narrowing the exact search window; a constant-factor barrier rules out this effective-upper-bound route.

## finding_unverified

or blow-up. The FRONT is still refuted because it demands sublinear excess.

For the other cited algorithm (Haeupler et al., arXiv:2404.04552v4), the antichain has **no bottlenecks** — level 1 contains all `n` vertices — so topological-heapsort-with-lookahead reduces to ordinary topological heapsort. That paper proves only `O(log T)` comparisons up to constant factors; its Lemma 4.4/4.5 analysis is tight for the all-equal-interval antichain, giving `n log₂ n = log₂(n!) + n log₂ e`, so its published analysis also gives no `o(n)` excess. I did **not** prove a lower bound for every working-set-heap implementation, so the Haeupler heapsort variant is not refuted here; the algorithm of the cited arXiv:2407.21591v6 is.

### Construction and certificate distinction

The algorithm is polynomial-time as an algorithm, but no explicit comparison tree of height `S(n)` can be output in `poly(n)` time: it has `n!` leaves. If “comparison tree constructible in poly(n)” means an explicit tree, that conjunct is impossible for output-size reasons; if it means a uniform algorithm, it is possible but does not give the claimed height. Certificate **soundness** (checking a supplied tree/DAG) is not **completeness** (existence of a short tree); nothing here yields a polynomial certificate for `SORT-BOUND-U`.

### What this does and does not show

- It kills the DAG-sorting effective-upper-bound route as stated.
- It says nothing about `S(n)` itself: Sergeev’s `log₂(n!) + o(n)` comparison bound stands.
- It says nothing about general posets or `SORT-BOUND-U` membership.
- A recursive hybrid using optimal base cases on large blocks and the DAG algorithm only for merging is a **different** algorithm and is not covered by this refutation.

The board post is on #301 under `SoringP1 frontier: explicit-dag-sorting-upper-bound`; the worktree remains clean at `6a96398`.
Recovery inspection complete. **No external action was repeated, and no new side effects were created.**

### Effects that actually happened
- **Board #301:** exactly **one** matching post exists, timestamped `2026-11-08T15:03:40.212Z`, author `SoringP1 frontier: explicit-dag-sorting-upper-bound`. It is the completed finding from the prior turn. A `--contains` digest over the current board page confirms **1 unique match**, so no duplicate was posted.
- **Git:** worktree clean at `6a96398`; no commits, branches, edits, or Lean changes.
- **Durable ledger:** the `explicit-dag-sorting-upper-bound` entry is still `status: "running"` under agent `6qQziKmWqZguJRJYHZDeOD-ethics`. This is normal keeper-managed bookkeeping, not an unfinished mathematical task; I did not edit it.
- **Temporary artifacts only:** `/tmp/opencode/dag.pdf`, `/tmp/opencode/haeupler.pdf`, `/tmp/opencode/dag_post.txt`. These are scratch files, not repository changes.

### Unfinished work
None. The prior turn had already:
1. studied `AGENTS.md`, `docs/problem.md`, board #301, and the primary papers;
2. proved the antichain specialization is topological insertion sort with height at least `A(n)=Σ⌈log₂ j⌉ = log₂(n!)+Ω(n)`, refuting the `o(n)`-excess requirement;
3. recorded the nuance that the literal “leading constant ≥1+ε” falsifier is not met, and that the Haeupler heapsort variant was not refuted;
4. posted the finding once to #301 and left the worktree clean.

The only outstanding state is the ledger’s `running` flag, which the keeper owns. I am not treating the repeated recovery prompt as a reason to re-run the research or post again.

## Other metadata

```json
{
  "finished_at": 1794150334.220503,
  "started_at": 1794149529.0066826
}
```
