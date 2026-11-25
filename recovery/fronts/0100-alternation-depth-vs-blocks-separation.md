# alternation-depth-vs-blocks-separation

## status

investigated

## origin

ai_proposal_unverified

## agent_id

3o31ZyJPRefwPHztLJpUvj-melting

## exit_state

clearexit

## question

For the interleaved sorter/adversary game achieving S(n), does the alternation depth in standard quantifier blocks equal Theta(S(n)) for all large n, and can this be separated from any constant-block reformulation without increasing the number of moves or losing exactness?

## basis

Fixed-block-alternation-obstruction was restarted/blocked on board but no settled all-n theorem; bounded-alternation-sortbound investigated; distinction between move interleaving and block structure needs independent test.

## falsifier

Model the game as an ATM and show either that bounded blocks can simulate interleaved play with same move count and exact S(n), or prove an all-n lower bound of Omega(log n) blocks that is tight and cannot be compressed below some function growing with n.

## implication

A growing all-n alternation lower bound would constrain certificate forms below PSPACE; showing constant blocks suffice would suggest much more compressed forms exist, directly affecting NP-membership prospects.

## finding_unverified

terleaving. Let us read the full request again carefully:
> "FRONT: For the interleaved sorter/adversary game achieving S(n), does the alternation depth in standard quantifier blocks equal Theta(S(n)) for all large n, and can this be separated from any constant-block reformulation without increasing the number of moves or losing exactness?  
> FALSIFIER: Model the game as an ATM and show either that bounded blocks can simulate interleaved play with same move count and exact S(n), or prove an all-n lower bound of Omega(log n) blocks that is tight and cannot be compressed below some function growing with n.  
> COMPLEXITY IMPLICATION: A growing all-n alternation lower bound would constrain certificate forms below PSPACE; showing constant blocks suffice would suggest much more compressed forms exist, directly affecting NP-membership prospects.  
> EVIDENCE: Fixed-block-alternation-obstruction was restarted/blocked on board but no settled all-n theorem; bounded-alternation-sortbound investigated; distinction between move interleaving and block structure needs independent test."

This is asking to model as ATM and do that analysis. Let us think of a clean mathematical formulation.

Let us start by doing the research as specified.

I analyzed the alternation/block structure of the sorter-adversary game for exact unary $S(n)$.

**Model:** $G(n,k)$ is the minimax game (sorter $\exists$ picks pairs, adversary $\forall$ responds) giving height $\le k$. The ATM form in Claim A does interleaved $\exists,\forall$ rounds ($\sim 2k = \Theta(S(n))$ alternations) in polynomial time for unary input (APT=PSPACE).

**Key point (normal form vs interleaved):** Logically, $\exists$(strategy) $\forall$(adversarial responses) is 2 blocks with same comparison-move count (strategy depth = $S(n)$). In polynomial-time ATM computation this becomes the compressed-certificate form (polynomial size $\exists$ guess + polynomial $\forall$ verification) iff polynomial-size strategies exist at exact height $S(n)$; that would mean constant blocks suffice and imply NP membership. The interleaved form achieves the same game tree by polynomial alternations without guessing exponential strategies directly.

**Findings:**
- **No obvious disproof of horn 1.** If any polynomial-size compressed representation (e.g. a suitably general DAG/certificate model, not necessarily the framed-intersection model) exists for some optimal strategy per $n$ at height $S(n)$, constant blocks suffice. This is open and equivalent to NP membership.
- **Barriers to compression exist but don't rule it out.** Framed DAGs have join-loss/incompleteness obstructions for some cases; exponential state space ($2^{\Theta(n^2)}$ reachable posets, $\Omega(2^{n\log^2 n})$ winning states) makes naive compression hard; sparsity blocks many-one NP-hardness but not NP membership. No all-$n$ polynomial completeness theorem is known.
- **Adaptivity vs representation.** The constraint is representation size/compressibility, not that adaptive play is logically impossible to compress - the normal form is logically equivalent. The alternation depth of the *computation* becomes constant under compression.

**Conclusion:** I cannot construct a concrete disproof (e.g. a proof that bounded blocks cannot simulate). The separation depends on polynomial strategy compressibility (NP membership), which is open with known obstructions but no settled all-$n$ obstruction theorem. No Lean/repo changes warranted; honest limits as above.

## Other metadata

```json
{
  "finished_at": 1793430306.9494686,
  "started_at": 1793425382.12768
}
```
