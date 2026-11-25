# antonina-cMxBCdos4CUFgN2XCP2r6n-defensive

Session: ses_e49bf3b77ffe6DOXrtz7F6oaPN
Workspace: /home/lubko/soring-fronts/exec-t11-oracle-accounting-20261107
Created: 1794059060436; updated: 1794059108058

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1b640c69c001Z4i9gztoPXKDay)

I’ll inspect the paper’s full theorem/proof and the cited local docs/script in parallel, then trace exactly what the reconstruction assumes and whether those operations are legal comparison queries.

## Output 63 (msg_1b641288c001YAdc4bHMHTA6KX)

## Result

Theorem 11’s reconstruction is a valid **linear-extension construction**, but its stated \(O(\log e(G))\) sorting-phase time is not an \(O(\log e(G))\) comparison bound. It uses a precomputed longest path and the sorted order of \(Y\) to insert the omitted path vertices **without querying comparisons**. Those are allowed preprocessing and computation resources in the paper’s algorithmic model, but they cannot be counted as comparisons or silently used as a comparison-only strategy.

That distinction matters: constructing *some* linear extension compatible with \(G\) is not the same task as identifying the unknown input order, nor does Theorem 11’s running-time claim establish that its reconstruction uses a particular number of comparisons.

## What the proof uses

In the proof of Theorem 11, the operations have these information sources:

| Operation | Information used | Cost in the proof |
|---|---|---|
| Find longest path \(P\) | The input DAG \(G\); computed during preprocessing, independently of comparisons | \(O(n+m)\) preprocessing, together with construction of \(H\) |
| For each \(u\notin P\), define its predecessor/successor on \(P\) | The edges of \(G\) and the chosen path \(P\) | Preprocessed; the proof gives no comparison cost |
| Build \(Y\) and \(H\) | \(G\), \(P\), and those path-neighbor designations | Preprocessing |
| Sort \(Y\) | The sorted order of \(Y\), produced by the separate algorithm for \((Y,H)\) | An input to reconstruction |
| Reconstruct \(L\) | \(L'\) on \(Y\), plus \(P\) and its predecessor pointers | Insert each omitted \(P\)-vertex immediately after its path predecessor; no comparison is specified |

The proof does **not** say reconstruction receives an oracle for \(\operatorname{Ext}(G)\), or a record of comparisons made. Its important advice is structural preprocessing: the selected path \(P\), the membership of vertices in \(P\) and \(Y\), and predecessor/successor information for off-path vertices. The paper accounts for preprocessing time, not the size of a framed comparison certificate encoding this information.

The claimed reconstruction step—“placing each item in \(P-Y\) right after its predecessor in \(P\)”—is a deterministic insertion into a represented order. Since \(P\) has its order fixed by the DAG, this can construct an extension without comparisons. But that is a **free computation only in the sense that it is not a comparison**; it depends on information computed from \(G\) in advance.

## Comparison-game legality

In the SoringP1 game, a query must be an incomparable pair in the **current** poset, and each query costs one comparison. The theorem’s reconstruction does not describe a sequence of such queries: it inserts vertices using the precomputed path order and predecessor relation. Therefore it is not, by itself, a legal comparison-game strategy for discovering an unknown order. Its validity is instead conditional: given a compatible \(L'\), it constructs a compatible extension \(L\).

## Why the requested transcript counts do not follow

I can’t report exact per-family comparison counts from the supplied evidence. The local exact evaluator, `scripts/evaluate.py`, computes minimax values for sorting the **antichain** on \(n\) elements. It does not implement Theorem 11’s \(G\mapsto(Y,H)\) preprocessing, its reconstruction, or minimax comparison costs on those induced posets. The cited `docs/research-plan.md` and `docs/research-certificates-barriers.md` also do not record the requested \(F> \lceil\log_2 e\rceil\) families or issue #48’s example. The grep result showing `B = (0, 0, 2, 1, 1, 9, 59)` identifies a test comment, not verified values for \(e(B)\) and \(F(B)\).

So no exact counts for \(B\), ordered sums, or a worst transcript can be responsibly supplied here. In particular, the prompt’s conflicting \(e(B),F(B)\) values should not be repeated as established facts. Deriving the requested counts requires first locating the documentation or script that defines those families and their exact \(e,F\), then implementing or hand-enumerating the actual \(G\mapsto(Y,H)\) pipeline under the stated comparison model.

## Certificate implication

The precise issue is not that Theorem 11 uses an \(\operatorname{Ext}(G)\) oracle. It is that its reconstruction’s time bound is an **algorithmic running-time** claim that relies on preprocessed DAG/path structure and a supplied sorted \(L'\). It does not provide a comparison transcript for reconstruction, or a polynomial-size framed certificate for optimal play. Any certificate claim must account for how the preprocessing advice is represented and verified, and separately prove that the comparisons used form legal queries in the current-poset game.

**Sources:** Rutschmann, *Sorting under Partial Information with Optimal Preprocessing Time via Unified Bound Heaps*, arXiv:2604.12653v2, §4, Theorem 11 and its proof; SoringP1 `scripts/evaluate.py`; `docs/research-plan.md`; `docs/research-certificates-barriers.md`.
