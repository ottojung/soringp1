# shelling-sequence-polynomial-certificate

## status

investigated

## origin

executive_commissioned

## agent_id

XgIEkqsSKMXDjtZNP5VPvW-pudding

## exit_state

clearexit

## question

Can the class of shelling/insertion orders be encoded as polynomial-size framed certificates at height S(n) for all n where FJ equals S(n), or is there a general obstruction?

## basis

Framed-certificate frontier discusses FJ constructions but completeness open.

## falsifier

Show that for some n with known S(n), no shelling-based framed DAG of polynomial size achieves height S(n) due to join/intersection constraints.

## implication

Would clarify whether NP-certificate route is feasible via structured families.

## finding_unverified

the optimal S(n). From what we saw, FJ equals S(n) at n in {0..11, 12,13,14,15,16,17,18, 20,21,...} - many cases where either info bound holds or just where FJ happens to be optimal. The question is whether shelling/insertion-style strategies (of which FJ is perhaps one) can give polynomial framed certificates at height S(n) in all those cases where FJ is optimal. Or is there a join/intersection constraint causing obstruction for some n?

Let us look up that shelling-path-complexity-root finding again more closely.

Let us start by analyzing the structure.

Let us look up the full picture again carefully and think.

Let us analyze this.

Let us write up the analysis.

**Mathematical finding (obstruction, paper argument):** 

For fixed-order insertion (shelling/insertion) strategies, to perform optimal insertion of element $e_{k+1}$ one must know the total order of the already-inserted prefix $\{e_1,\ldots,e_k\}$. In the framed DAG certificate model (per `scripts/check_framed_strategy.py`), different comparison paths merge only by intersection of guaranteed relations at join nodes; intersection across different total orderings of the same set gives empty relations on conflicting pairs, so information about prefix order is destroyed. Therefore, joins cannot merge branches corresponding to different prefix orderings without losing the information required for correct fixed-order insertion. Since there are $k!$ possible prefix orderings, any correct framed DAG representation of a shelling/insertion strategy with fixed order must keep them separated through the prefix phases, forcing exponential size $\ge \sum k! = \Omega(n!)$. This is an obstruction due to join/intersection constraints of the framed model, not a tree-height obstruction (trees are already exponential; joins cannot compress here). 

**Applicability:** For all $n\ge 5$ where $S(n)$ is known and FJ equals $S(n)$ (e.g. $n\in\{5,\ldots,18,20,21\}$), shelling/insertion orders cannot be encoded as polynomial-size framed certificates achieving height $S(n)$ because (1) the class requires exponential-size structure in this model due to the join/intersection constraint above, and (2) even comparison counts for simple binary insertion exceed $S(n)$ for $n\ge5$ while more sophisticated fixed-order insertions still face the same state-separation constraint. FJ's different structure (pairing/recursive sorting of winners with different information organization) is not subject to the same forced prefix-order separation, which matches section 3 of the framed frontier suggesting FJ can be modeled differently.

**Relation to complexity:** This supports that polynomial framed certificates (hence a potential NP-certificate route for unary SORT-BOUND-U) may be feasible for some structured families but not for shelling/insertion families - explaining why certificate completeness is open and class-dependent. The obstruction is about *compression/completeness* in the framed model (join constraints), distinct from general-poset hardness results.

**Limits:** This is a combinatorial/paper argument; no executable construction or counterexample was built, no repository changes made. The equivalence theorem (tree↔framed DAG height) holds, but size-compression fails for this class due to join/intersection constraints. Whether there is some non-obvious way to encode shelling/insertion strategies in framed form avoiding this separation remains open in principle, but the information-loss argument is strong.


## Other metadata

```json
{
  "finished_at": 1793727360.8738039,
  "started_at": 1793725000.6509955
}
```
