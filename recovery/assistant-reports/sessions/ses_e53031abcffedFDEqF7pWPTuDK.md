# antonina-lXRYwmPGH0jq8BJMXzW5uo-endured

Session: ses_e53031abcffedFDEqF7pWPTuDK
Workspace: /home/lubko/soring301
Created: 1793903617354; updated: 1793903662688

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1acfce56a001o3XdKwL0uPauGE)

I’ll inspect the assigned research notes and source references first, then focus on a formal invariant and its failure modes. I’ll keep this read-only and won’t modify or publish anything.

## Output 52 (msg_1acfd3002001x1FRffotTz9XC7)

## Finding: the local gadgets do not yet yield a global excess bound

**Conclusion:** The one-ply witness gives a rigorous *local* one-comparison deficit, but I do not see a valid lemma that turns \(q(n)\) copies into an \(\Omega(q(n))\) excess over \(\lceil\log_2(n!)\rceil\) for the root antichain. The main obstacle is not just comparisons crossing gadget boundaries: a lower bound on a restricted family of permutations does not add to the root information bound.

Let \(W\) be the \(n=5\) witness from `docs/research-one-ply-obstruction.md` (or an isomorphic minimal witness). It has \(e(W)=8\), \(F(W)=4\), and information bound \(3\). For \(q\) blocks, consider the restricted input family in which the blocks occupy fixed consecutive rank intervals and each block’s order is one of the eight extensions of \(W\). Comparisons across blocks have predetermined outcomes. The induced decision tree must distinguish \(8^q\) inputs, and its height is at least \(4q\): its restriction to the product family is a comparison tree for \(q\) independent copies of \(W\), whose worst-case cost is at least \(qF(W)\).

That is a valid restricted-family lower bound, but **not** the desired result. The family has only \(8^q\) inputs, while the root has \(n!\) possible orders. The inequality \(S(n)\ge 4q\) cannot be added to the independent root bound \(S(n)\ge\lceil\log_2(n!)\rceil\). The two arguments may concern different paths, and the depth spent distinguishing this family may already be required to distinguish other inputs. The fixed-interval promise also does not supply a decomposition of every root-to-leaf path into \(q\) copies of \(W\).

A plausible invariant would need to charge **additional** comparisons beyond the entropy consumed on the same adversarial path—e.g. establish that each surviving gadget contributes a local deficit while arbitrary cross-gadget comparisons cannot eliminate or amortize those deficits. Neither the notes’ one-ply inequality \(L_1(P)\le F(P)\) nor the witness’s \(L_1-L_0=1\) supplies that persistence claim. A cross-boundary comparison can impose a relation among keys from different gadgets and change the residual extension set; the one-ply analysis only certifies the current state’s next move, not a count of surviving independent obstructions after arbitrary such moves.

## Sergeev compatibility

The primary-source record is Sergeev, *On the asymptotic complexity of sorting*, ECCC TR20-096, Theorem 3, p. 29; the ECCC abstract states the group-insertion algorithm achieves \(\log_2(n!)+o(n)\). The repository’s source note `docs/research-sergeev-asymptotic.md` records the sharper bound
\[
S(n)=\log_2(n!)+O\!\left(n/(\log n)^{1/5}\right).
\]
Thus a proposed lower bound of \(\Omega(q(n))\) excess is not contradicted when \(q(n)=\lfloor n/(\log n)^a\rfloor\) with \(a\ge 1/5\): it is of the same or smaller scale than that upper bound. For \(a<1/5\), an \(\Omega(q(n))\) excess would conflict with Sergeev’s asymptotic upper bound. This is compatibility only, not evidence that the proposed lower bound holds.

**Precise obstacle:** To prove the requested claim, one needs an all-\(n\) root-adversary argument that simultaneously (i) maintains \(\Omega(q(n))\) local deficits on a single branch and (ii) accounts for the branch’s total extension count so the deficits survive subtraction of the global information bound. The product-family argument establishes neither property. I have no rigorous invariant surviving arbitrary cross-gadget comparisons, nor an explicit all-\(n\) counterstrategy disproving one; the proposed amplification remains unproved. This concerns lower bounds on \(S(n)\), not the complexity of computing \(S(n)\), and implies no class separation.

**References:** `docs/research-one-ply-obstruction.md` §§1, 3; `docs/research-obstruction-next.md` §§2–3; Sergeev, ECCC TR20-096 (2020), Theorem 3, p. 29, https://eccc.weizmann.ac.il/report/2020/096/.
