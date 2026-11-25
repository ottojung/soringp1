# antonina-e8qXfYUIeC3VkGoFRoiUsE-conquests

Session: ses_df7a957e7ffea0xzdvX1KSTn4C
Workspace: /home/lubko/soring-fronts/fj-defectfree-n11-20261123
Created: 1795436226650; updated: 1795437896845

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 568 (msg_2086fae10001JSZ5eFeCsj1wBx)

## Result (posted to #301 once)

- **Front**: `fj-defectfree-n11-20261123` (scratch only under `/tmp/fj_n11`; no repo/Lean/test/CI/ledger/main/case/bill changes).
- **Question**: Is the Ford–Johnson/merge-insertion sorting tree for `n=11` (height `S(11)=26=ceil(log2 11!)`) defect-free, i.e. `D(P)=F(P)-ceil(log2 e(P))==0` at every reachable state?
- **Method [definition/experiment/deduction]**: From-scratch C FJ decision-tree generator (`/tmp/fj_n11/fj_tree.c`, GCC 15.2.0). Full DFS over the FJ tree with transitive-closure poset bitmasks; `e(P)` = leaf count of FJ subtree, `h(P)` = FJ subtree height. Sound defect-free certificate: `h(P) <= ceil(log2 e(P))`. For defective FJ nodes, inherent-defect certificate: every incomparable pair splits `e` into children with `max(e1,e2) > 2^(d-1) => F(P) >= d`.

## Validation [experiment]
- FJ counts match `M(n)=sum_{k=1..n} ceil(log2(3k/4))`; exhaustive small-n FJ correctness checks (n<=10 sanity), leaf total-order check, root `e=11!=39916800`, `total_nodes=79833599`, `max_h=26`.
- FJ defect scan: `n=5..10` all `defective_nodes=0` (heights 7,10,13,16,19,22).
- `e(P)` subset-DP cross-checked against brute-force linear extensions on 200 random n=8 posets (0 mismatches).
- Representative defective-state split independently verified by Python subset-DP.

## n=11 result [experiment/deduction]

| n | n! | FJ height | ceil(log2 n!) | defective FJ nodes | first (h,e,cl) |
|---:|---:|---:|---:|---:|---|
| 11 | 39916800 | 26 | 26 | 256 | (16,31185,15) |

All 256 defective nodes are in class `(h_FJ,e,ceil(log2 e))=(16,31185,15)`.

Representative certified state (first found, succ hex per element 0..10): `[28a,288,288,280,2a0,280,280,200,200,0,0]`
- `e(P)=31185`, `ceil(log2 e(P))=15`.
- 34 incomparable pairs; min over pairs of `max(e1,e2)` is `16401 > 16384 = 2^14` (example: pair 1-8 gives 16401+14784). Thus no comparison yields two children sortable in 14 comparisons: `F(P) >= 16`.
- FJ gives `h_FJ(P)=16`, so `F(P) <= 16`. Hence `F(P)=16`, `D(P)=1 > 0`.

## Verdict
**NO-for-this-tree.** FJ/merge-insertion at `n=11` is not defect-free; it reaches a certified inherently defective state (`F(P)=16 > ceil(log2 e(P))=15`).

## Implication for smallest-failure-n in {11,12}
- Smallest `n` where the **FJ tree** is not defect-free is `11` (n<=10 defect-free by scan).
- Existence of **any** defect-free optimal tree at `n=11` remains open; smallest-failure-n for existence stays in `{11,12}`, with FJ eliminated at `n=11`.

## Next decisive question
Is there any optimal height-26 comparison tree for `n=11` with `F(P)==ceil(log2 e(P))` at every reachable state? A defect-free optimal tree moves smallest-failure-n to 12; a forcing proof that every optimal height-26 tree hits `F(P)>ceil(log2 e(P))` moves it to 11.

**External write**: exactly one `antonina board comment --id 301` posted (author `SoringP1 researcher: fj-defectfree-n11-20261123`, id `sha256:Z0J8dSCNFBL-F1jttKVtgScmN6MTIGLUD0qw2D-c7VI`, 2026-11-23T12:44:19.752Z).
