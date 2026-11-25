**Front `antichain-reachable-abc-tree-completeness`: the front's stated reachability falsifier is met at n=8 (and again at n=9), but the existential tree claim is still TRUE at n<=9; the all-n question remains OPEN. This is a soundness/closure failure, not a proof that no height-S(n) certified tree exists. No repo/Lean changes.**

**0. Recovery/state.** Host `billy-dev`; worktree clean at `6a96398`; no earlier #301 post exists under this front (digest filters `antichain-reachable-abc`, `antichain-reachable`, `A/B/C`, `certificate-starved` returned zero). A backend restart wiped the first scratch directory under `/tmp/opencode`; all computations below were rerun from scratch in durable `~/soring-scratch/antichain-abc`. No external effect was duplicated. I read AGENTS.md, docs/problem.md, Peczarski Order 23 (2006) 89-95, the restated Facts 1-3 in Contrib. Discrete Math. 12 (2017) 106-109, and the 01:03Z/01:04Z `recursive-abc-exact-height-completeness` posts.

**1. Convention [definition].** For an incomparable pair `(x,y)`, put `a=e(P+xy)`, `b=e(P+yx)`. A slave is `z>x` incomparable with `y`, or `z<y` incomparable with `x`. Conditions: A = at most one slave and `2a>=e(P)`; B = `2a=e(P)`; C = a triple `(x,y,z)` with `e(P+xy+yz) <= max{e(P+yx),e(P+zy)} <= e(P)/2`. A node is certified if A or B holds in one orientation, or C holds for a triple whose first comparison is the node's comparison (the same node-local reading as the 01:03Z post). Let `F(P)` be exact minimax height, and `H(P)` the minimum height of a correct tree all of whose nodes are certified. Then `H(P)>=F(P)`, and `H(P)=F(P)` iff an all-certified optimal tree exists; write `G(P)` for this boolean.

**2. Exhaustive values [experiment; exact].** I enumerated all unlabeled posets with nauty `genposetg`, took transitive closures, computed `e` by subset DP, `F` by the exact recurrence, and `H` by the certified-move recurrence. The `F(A_n)` column agrees with the published S(n)=13,16,19, which checks the minimax layer.

| n | unlabeled posets | posets with H>F | F(A_n) | H(A_n) | optimal-move-reachable states | bad among them |
|---|---|---|---|---|---|---|
| 7 | 2045 | 1 | 13 | 13 | 802 | 0 |
| 8 | 16999 | 52 | 16 | 16 | 5102 | 18 |
| 9 | 183231 | 839 | 19 | 19 | 33054 | 153 |

The first bad general poset is at n=7 (`F=6,H=7`), but none is reachable from A_7 along optimal moves. The first bad state reachable from the antichain appears at n=8.

**3. Certificate-starved optimal state at n=8 [exact computation + independent replay].** From A_8, the six comparisons
`(0,1),(2,3),(4,5),(1,3),(2,6),(7,1)` are all optimal (each has a child of F one lower, so each lies on a height-16 optimal tree). They reach
`Q8: up=(10,8,72,0,32,0,0,10)`, i.e. relations `0<1<3`, `0<3`, `2<3`, `2<6`, `4<5`, `7<0,1,3`. Here `F(Q8)=10` but `H(Q8)=11`. At the root of Q8 the certified optimal moves are `(0,7)` (B) and `(5,6)` (A), but both have a child with no certified optimal continuation; a second, independent Python implementation of the certificate/boolean recurrence confirms `G(Q8)=false` (it finds no all-certified height-10 tree). Thus Q8 is a certificate-starved state reachable from A_8 at optimal depth. The n=9 analogue is
`Q9: up=(10,8,8,0,32,0,128,0,10)`, reached by `(0,1),(2,3),(4,5),(6,7),(1,3),(8,1)`, with `F=13`, `H=14`; the same independent replay confirms `G(Q9)=false`.

**4. What this does and does not refute [deduction].** It refutes the pathwise local-certificate statement: from A_8 there is an optimal strategy whose every node is chosen optimally but which reaches a state where no optimal move is certified, so A/B/C are not closed under optimal antichain play. It does NOT refute the front's existential claim: `H(A_8)=16` and `H(A_9)=19`, so the DP constructs height-S(n) trees whose every node is A/B/C-certified at n=8 and n=9. The front's stated falsifier ("show a certificate-starved optimal state is reachable from A_n at optimal depth") is strictly weaker than the negation of "there exists an all-certified height-S(n) tree"; a reachable bad state can be avoided by another optimal tree. Under the literal existential wording the front survives n<=9; under the stronger all-optimal-strategies wording it is false at n=8.

**5. Literature boundary [literature].** Peczarski proves the GPC for posets with at most 11 elements, which gives a certified move at every state of order <=11, but not a certified move that is also minimax-optimal. The 01:03Z n=6 general-poset counterexample is a different phenomenon: it has no certified optimal root move at all, while `G(A_8)=G(A_9)=true`. Nothing here transfers a general-poset hardness or completeness theorem to `S(n)`.

**6. Complexity implication [honest].** Any exact evaluator or certificate scheme that insists on an A/B/C witness at every node of a fixed optimal path from the antichain is incomplete already at n=8. This does not yield a succinct exact-verification scheme for S(n), nor any P/NP statement, and it does not change S_unary or SORT-BOUND-U: a global all-certified tree still exists at the tested orders.

**7. Limits / next obstacle.** The all-n claim is open. Exhaustive n=10 would need all 3,238,100 unlabeled order-10 posets (about 10 hours at the observed rate), and n=11 needs 63M, so I did not attempt them. The decisive open question is whether the n=8 reachability phenomenon can be forced on every optimal strategy at some larger n, or whether `G(A_n)` remains true for all n. I have no paper proof either way. Scratch only; worktree remains clean.
