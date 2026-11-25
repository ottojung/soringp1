# sort-bound-pspace-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

CSZSX3nDoaBacQeuy1SZ4T-gross

## exit_state

clearexit

## question

Is the unary threshold language SORT-BOUND-U = {1^n # 1^k : S(n) <= k} PSPACE-complete under polynomial-time many-one reductions, or does the comparison/antichain structure force it strictly below PSPACE?

## basis

SORT-BOUND-U is in PSPACE (budgeted DFS) and sparse; sparsity alone does not block PSPACE-completeness under poly-time reductions, but arbitrary-poset optimization hardness does not transfer without a reduction exploiting the comparison model.

## falsifier

Construct an explicit poly-time m-reduction from a known PSPACE-complete language to SORT-BOUND-U that preserves the antichain-root structure, or prove an invariant obstruction (beyond sparsity/barriers already known) that rules out all such reductions for all PSPACE-complete sources.

## implication

PSPACE-completeness would show computing S(n) is PSPACE-hard (in the unary/decision sense), placing it among the hardest problems in PSPACE; a strict containment proof would reveal new structure limiting adversarial power in the minimax sorting game.

## finding_unverified

**Finding (mathematical):** SORT-BOUND-U cannot be PSPACE-complete under polynomial-time many-one reductions.

**Obstruction (unconditional, sparsity):** SORT-BOUND-U is sparse — only $O(N^2)$ strings of length $N$ have the form $1^n \# 1^k$. Let $L$ be PSPACE-complete (e.g. QBF) and $f$ a poly-time m-reduction $L \le_m^p \text{SORT-BOUND-U}$. For $x\in L$, $|x|\le n$, $f(x)\in \text{SORT-BOUND-U}\cap \{0,1\}^{\le p(n)}$ so $|L\cap\{0,1\}^n| \le |\text{SORT-BOUND-U}\cap\{0,1\}^{\le p(n)}| = O(p(n)^2)=\mathrm{poly}(n)$. Thus $L$ would be sparse, contradicting non-sparseness of standard PSPACE-complete sets. Same argument rules out many-one EXPTIME-hardness. (This is the unconditional sparsity barrier, stronger than Mahaney’s NP case.)

**On the antichain/comparison structure:** The sparsity is enforced by the unary encoding of $(n,k)$ (the antichain-root threshold form). Arbitrary-poset optimization hardness does not transfer because reductions cannot create dense preimages into this tally/sparse image without breaking polynomial time; no “comparison-structure invariant” beyond this sparsity is needed — the counting obstruction is decisive. I found no way to construct an explicit reduction and no plausible path around the counting argument.

**Conclusion:** The falsifier fails. SORT-BOUND-U is PSPACE-easy in containment (budgeted DFS) but strictly below PSPACE under poly-time m-reductions by unconditional sparsity; it is not PSPACE-complete.


## Other metadata

```json
{
  "finished_at": 1793390486.0577574,
  "started_at": 1793390333.815735
}
```
