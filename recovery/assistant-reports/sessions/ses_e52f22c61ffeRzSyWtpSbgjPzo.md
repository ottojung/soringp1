# antonina-cLxgE3acEfVYhYXg9QLhLq-theatre

Session: ses_e52f22c61ffeRzSyWtpSbgjPzo
Workspace: /home/lubko/soring-fronts/audit-fj-framed-certificate-20261105
Created: 1793904727193; updated: 1793904763112

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 34 (msg_1ad0e06d4001qdhISxC0A0YtBr)

I’ll treat “feasible histories” as all linear orders consistent with the framed DAG’s propagated guarantees. The key distinction is whether each scheduled insertion’s *actual* rank window remains small after merging histories, not merely whether each separate path gives a useful bound.

## Output 43 (msg_1ad0e1684001wCVCD6gr6qaR1y)

**Result: the requested all-history induction is not established, and I can’t decisively refute it.** The precise remaining issue is how the proposed *shared framed-DAG joins* are constructed and proved to preserve the insertion windows—not the classical Ford–Johnson comparison bound.

At a join, the checker in `scripts/check_framed_strategy.py` intersects guaranteed relations after applying each edge’s slot permutation. Thus a join preserves a common ordered chain if every incoming frame maps its sorted winners to the same ordered slots. Likewise, loser pairing is preserved only if the frame also maps each associated loser consistently. The frontier note (§3) asserts these properties, but does not give the recursive frame construction or prove the join intersections preserve them.

The remaining lemma can be stated precisely:

> For every recursive winner-sort DAG and every shared join, construct edge slot permutations such that the common guarantee contains the ordered winner chain, each paired loser remains paired with its winner and below it, and every pending loser’s common guarantee implies the relaxed rank window required when that loser is next inserted. The odd unpaired element must retain a valid full-range window. The insertion stage must then have height at most its scheduled Ford–Johnson allowance, so total path cost is at most  
> \[
> F_{\rm FJ}(n)=\sum_{j=1}^{n}\left\lceil\log_2(3j/4)\right\rceil .
> \]

The generic rank-envelope argument in §3 does **not** discharge this lemma: it assumes certified windows and bounded shifts, but does not derive those windows through recursive winner sorting and joins. Conversely, intersecting relations is not itself a counterexample: outcome-dependent permutations can make different sorted winner orders agree in slot order at a join. A refutation would need to show that no permitted framing can preserve the required pairing and windows, not merely that histories differ.

The sum above is the standard Ford–Johnson upper-bound cost; it is not a proof of the framed-DAG invariant. Even if the lemma were proved, it would establish **certificate soundness at Ford–Johnson cost**, not polynomial certificates at the exact optimum \(S(n)\), and hence not NP membership for `SORT-BOUND-U`.
