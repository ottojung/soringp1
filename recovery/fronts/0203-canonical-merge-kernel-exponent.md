# canonical-merge-kernel-exponent

## status

investigated

## origin

ai_proposal_unverified

## agent_id

5QtzV245wBvhenAiVII7bM-conduct

## exit_state

clearexit

## question

Is there a polynomial-time computable canonical form for root-reachable posets in the union of all optimal comparison strategies that identifies states with equal F(P) and has at most 2^(O(n log n / h(n))) classes for some h(n)->infty, or does the winning frontier force exponential kernel size regardless of canonicalization?

## basis

Winning-frontier gives 2^((1/4-o(1)) n (log n)^2) nonisomorphic winning states; need to know if optimal-strategy orbits are compressible vs transcript classes.

## falsifier

Prove a kernel lower bound: any function mapping root-reachable winning states to canonical labels that is F-preserving requires >= 2^(Omega(n (log n)^2 / log log n)) labels for infinitely many n, or give a constructive O(n^c)-size kernel for all optimal paths.

## implication

A subexponential kernel would open a path to 2^(O(n log n)) exact evaluation; a strong lower bound would formalize why the winning-frontier barrier blocks state compression and impact certificate strategies.

## finding_unverified

g means if labels equal then $F$ equal ($f(P)=f(Q)\implies F(P)=F(Q)$). “Identifies states with equal $F(P)$” in the front might mean the opposite in casual language, or might mean it identifies (determines) states having equal $F(P)$ — i.e. preserves $F$-equality. Maybe a bit garbled, but the falsifier is clear: $F$-preserving = label-equality implies $F$-equality.

So we want to know if there is a polynomial-time canonical form (so $f$ polynomial-time, maybe canonical/unique per class) that is $F$-preserving and has subexponential classes. The winning frontier gives exponentially many non-isomorphic winning states; if many of these must remain in different classes under any $F$-preserving $f$ (because they force different $F$ or because you can’t merge them without breaking $F$-preservation), that gives a lower bound.

**Assessment**
- **Combinatorial obstruction is real but not obviously giving that exact exponent.** The $S_n$-quotient already shows isomorphism classes are large; $F$-preserving is weaker than isomorphism but the “degrees of freedom” in that rectangular family are $C(M,m)\ge 2^{((1/4-o(1))n(\log n)^2)}$. To have $f$ polynomial-time and $F$-preserving with few classes, either (a) most $P_A$ have same $F$ but the structure is still incompressible (unlikely for explicit structure), or (b) different $P_A$ have different $F$ and you can’t merge. But (b) would mean $F$ already distinguishes them — then $F$ itself would be a kind of canonical form in values but computing $F$ is the problem; not directly giving a small kernel.
- **Restriction to optimal strategies is critical.** General posets are hard, but root-reachable on optimal strategies is tiny relative to all posets. There might be a special structure (e.g. “shelling orders”, or states that are “interval orders” in some cases? No). Or perhaps they form a “laminar” family? Unclear. A constructive polynomial kernel would be a big structural result.
- **Distinguish from general poset theory.** GI-completeness is for isomorphism testing; it doesn’t automatically imply exponential kernel size for $F$-preserving quotients on this special class. Also the class is very restricted (only states on minimax optimal paths of sorting).
- **Soundness vs completeness for certificates.** Even if kernel is exponential, certificate soundness might be easy; completeness (existence of small witness) is what fails. The question is about the kernel/quotient structure affecting certificate strategies.

**Concrete conclusion**
I do not see a obvious way to construct a polynomial kernel; the combinatorial freedom in the winning frontier is large. However, I also do not have a clean proof of the stated lower bound. The restriction to “optimal strategies” is not well-characterized enough from the docs alone to do a rigorous disproof. The most honest answer is: the winning frontier shows $2^{\Omega(n(\log n)^2)}$ non-isomorphic states exist, and $F$-preserving canonicalization cannot be easier than isomorphism on general posets, but this class is restricted to optimal-strategy states (a very special subgraph). Without a characterization of that subgraph, I cannot rule out a special canonical form, nor can I prove the stronger lower bound — I can only point to the barrier as evidence that state compression is hard and that enumeration is blocked. No new theorem or counterexample was found; the obstruction is the lack of structural characterization of optimal-strategy states, not an explicit proof.

## Other metadata

```json
{
  "finished_at": 1793647729.571201,
  "started_at": 1793647383.2863936
}
```
