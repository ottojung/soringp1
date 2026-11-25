# antonina-sZngOlCz5VSW1OAkCctFwk-schools

Session: ses_df83e6557ffeiPBDBaM3b6b2Rd
Workspace: /home/lubko/soring-fronts/profile-mincount-n7n8-defectfree-dp-20261123
Created: 1795426458381; updated: 1795428509113

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 641 (msg_207e0834f001lUiamrdH12WK0c)

## Result (posted to #301)

I posted exactly one #301 comment as `SoringP1 frontier: profile-mincount-n7n8-defectfree-dp-20261123` (comment `sha256:VBf7W281ymz1L0lOmL1faYHysCAu2BwTrFBTXUItNg8`, 2026-11-23T10:07:51.208Z). No repo/Lean/test/CI/ledger/main changes; worktree clean at `6a96398`; scratch only under `/tmp/opencode`.

## Exact values (requested literal structural DP, defect-free feasible family)

[experiment] Two independent implementations agree (C DP + independent Python DP over C primitives; both over canonicalized transitive-closure posets, exact `e(P)` by order-ideal subset DP, S_n canonicalization):

| n | n! | S(n)=C(n) | Π(A_n) literal DP | Π exact-set union DP | #canon e-states | #Pi states | time(C) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 2 | 1 | 1 | 1 | 2 | 2 | <0.01s |
| 3 | 6 | 3 | 2 | 2 | 5 | 5 | <0.01s |
| 4 | 24 | 5 | 2 | 2 | 12 | 12 | <0.01s |
| 5 | 120 | 7 | 4 | 4 | 19 | 19 | <0.01s |
| 6 | 720 | 10 | **6** (sanity) | 8 | 157 | 130 | 0.02s |
| 7 | 5040 | 13 | **17** | 18 | 858 | 600 | 1.5s |
| 8 | 40320 | 16 | **17** | 18 | 5761 | 3307 | 104s |

Primary answer (prompt's DP): **Π(A_6)=6, Π(A_7)=17, Π(A_8)=17**. Witness checks: all leaves = n!, max depth = L = S(n).

## Definition/DP used [definition]

- `σ_k = log2(2 e_k/e_{k-1})`, `e_k=|LE(P_k)|`, `Π(leaf)=1`.
- Balanced split `e1==e2==e/2` (σ=0): literal DP uses `Π(P)=min(Π(P+),Π(P-))` (collapse, mirror-isomorphism possible).
- Unbalanced `e1!=e2`: `Π(P)=Π(P+)+Π(P-)` (disjoint, different σ).
- Feasible family: defect-free, `L(P)=ceil(log2 e(P))`, every chosen comparison has both children `e_child <= 2^(L(P)-1)` and recursively feasible. At n<=8, `S(n)=C(n)=ceil(log2 n!)` [literature: Wells/Knuth/Peczarski/Stober–Weiß, as in docs].

## Precision/falsification [deduction][experiment]

- **Mirror-collapse realizability (key caveat):** for n=6, 21 balanced feasible split instances had non-isomorphic canonical children (`c1!=c2`) but equal Π values. Building a witness by taking each child's own optimal tree independently (no mirror relabelling) gives profile counts 10,23,23 for n=6,7,8, falsifying naive independent realization. An exact profile-set union DP (`balanced => |(0)+S1 ∪ (0)+S2|`, `unbalanced => disjoint`) gives 1,2,2,4,8,18,18. I report the prompt's requested literal-DP values as primary (sanity 6 matches) and exact-set as a precision bound; the gap is the mirror-collapse assumption.
- **Height-S(n) vs defect-free:** `S(n)=C(n)` forces root defect 0, but does not by itself force `D(P)=0` at nodes with local slack (`C(n)-d-L(P)>=1` could in principle allow `F(P)>L(P)` while fitting height). I did not find/construct such a node in the n<=8 feasible family; I computed Π over the requested defect-free feasible family and stated this caveat. No all-n height==defect-free claim.
- **Balanced-in-info != exactly-e/2:** defect-free allows `e_child <= 2^(L-1)`; unbalanced exact-count splits are common and handled by the disjoint case.

## Implications for leaf-deviation-profile-space-alln [deduction]

- Sanity n=6=6 reproduced. Min profile count grows 6,17,17 (literal DP) / 8,18,18 (exact-set) at n=6,7,8 — small-n data only, no evidence for poly(n) collapse or super-polynomial growth.
- The literal/exact-set gap means future all-n profile-mincount claims must fix the mirror-collapse convention.
- No all-n bound, no decision of the leaf-deviation-profile-space-alln front, no S(n)/SORT-BOUND-U complexity consequence, no theorem completion. Soundness != completeness.
