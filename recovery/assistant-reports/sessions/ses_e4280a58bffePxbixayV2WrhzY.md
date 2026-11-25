# antonina-cbbb3CDEDnMxsMY1NIIZj1-proposal

Session: ses_e4280a58bffePxbixayV2WrhzY
Workspace: /home/lubko/soring-fronts/nullstellensatz-nonsortability-completeness
Created: 1794180602617; updated: 1794181513918

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_1bd7f6878001k7OYV1LM7qmaI1)

I'll start by inspecting the current state: repository, board #301, and any prior work from the interrupted turn.



## Output 434 (msg_1bd8beefa0011RhdCGMrZYTNxW)

## State check first

- Worktree clean at `6a96398` on `billy-dev`; no repository or Lean changes.
- No earlier #301 post on this front existed (searched `nullstellensatz`, `algebraic`, `subset sum`, `degree lower`).
- I posted **one** update to #301 at `2026-11-08T23:42:37Z`; verified exactly one match afterwards, so no duplicate side effect.

## Result: the front is not resolved, but two precise claims are settled

### 1. A positive linear form needs its full degree

**Lemma (paper proof, char 0).** Let \(c_0>0\), \(c_i>0\) for \(i=1,\dots,m\), and
\[
L=c_0+\sum_{i=1}^m c_i x_i .
\]
For the ideal \(F=(L,\ x_i^2-x_i)\), the least Nullstellensatz degree of a refutation of \(F\) is exactly \(m+1\).

**Proof.** In the Boolean quotient the multiplier \(g\) is forced to be the function \(1/L\). The coefficient of \(x_1\cdots x_m\) in its multilinear interpolant is
\[
\sum_{S\subseteq[m]}\frac{(-1)^{m-|S|}}{c_0+\sum_{i\in S}c_i}
=
\int_0^\infty e^{-tc_0}\prod_{i=1}^m(e^{-tc_i}-1)\,dt .
\]
The integrand has the constant sign \((-1)^m\) and is not identically zero, so the integral is nonzero. Hence \(\deg(g)=m\), and \(\deg(gL)=m+1\). \(\square\)

This matches the subset-sum / Binary Value Principle literature, where a single positive linear equation is hard for degree and size (Alekseev–Grigoriev–Hirsch–Tzameret; Part–Tzameret; Alekseev–Hirsch). It is the exact single-equation benchmark.

### 2. The Farkas-support-to-degree route is invalid

The faithful state-expanded LP gives, by Farkas, a linear combination of the equalities
\[
L=\sum_j y_j\ell_j=c_0+\sum_i c_i v_i,\qquad c_0>0,\ c_i\ge 0,
\]
so \(L\in I_F\). The board’s matching argument lower-bounds the **dual** support by \((n-1)!!\); the primal support of a particular \(L\) needs a separate injectivity check. But even granting large primal support, the implication to a lower bound for \(I_F\) fails.

**Counterexample.** Take
\[
F=\{1+x_1+\cdots+x_m=0\}\ \cup\ \{x_ix_j=0\ (i<j)\}\ \cup\ \text{Boolean}.
\]
The linear subsystem has minimum Farkas support exactly \(m\) (the only linear equation is \(L\)). Yet \(F\) has a **degree-2** refutation: for each \(j\),
\[
x_jL=x_j+\sum_{i\ne j}x_ix_j=x_j=0,
\]
so all \(x_j=0\), hence \(L=1\). Thus exponential Farkas support is logically compatible with a constant-degree algebraic refutation.

The reason is the wrong ideal inclusion: \(L\in I_F\) gives
\[
(L,\text{Boolean})\subseteq I_F,
\]
so hardness of the smaller ideal says nothing about the larger one. This is the exact obstruction to the natural “Farkas support \(\Rightarrow\) NS degree” argument.

### 3. The structural gap in the faithful encoding

At an internal state \(P\),
\[
z_P=\sum_e x_{P,e},\qquad z_P^2=z_P
\]
implies only the **summed** exclusion
\[
\sum_{e<e'}x_{P,e}x_{P,e'}=0,
\]
not the individual products \(x_{P,e}x_{P,e'}=0\). If individual products were available, the toy counterexample would give degree 2.

At a terminal non-total \(Q\), \(z_Q=0\), so even the summed exclusion degenerates to \(0=0\). The incoming equation becomes
\[
0=\sum_{\text{edges into }Q}x,
\]
with no pairwise information. This is precisely where the LP/Farkas proof uses **nonnegativity** (“a sum of nonnegative \(x\)’s is zero, so each is zero”), while NS/PC must simulate that nonnegativity through Boolean axioms. The reciprocal lemma says this simulation costs degree equal to the number of incoming terms.

### 4. Why the restriction lower-bound route fails

A tempting route is to restrict to a height-\(k\) comparison tree, leave the “other” incoming edges free, and obtain a terminal Binary Value Principle \(1+\sum y_i=0\) with many free \(y_i\).

This does not work for the faithful duplicating flow. The support-closure lemma says any feasible solution has support a tree. In a tree restriction, set the selected edges to \(1\) and all non-selected edges at tree nodes to \(0\). By induction on depth, every off-tree state has \(z=0\): at depth \(0\) only the root is on-tree; at depth \(t+1\), an off-tree state can receive flow only from off-tree parents, whose non-selected edges are \(0\). Hence every incoming edge to a tree leaf from an off-tree parent is \(0\), and the only nonzero incoming edge is the tree edge, giving the **linear** contradiction \(1=0\) at the leaf. So every tree restriction is degree-1 refutable; it cannot witness a hard terminal BVP.

This is the concrete failed approach: the duplicating flow’s integral support forces all off-tree flow to zero, so the free BVP variables collapse to constants. The hardness of the full encoding is necessarily **global across all trees**, not local to one terminal sum.

## Honest status

Neither horn of the front is proved:

- I did **not** exhibit a constant-degree, polynomial-size refutation of the faithful state-expanded encoding.
- I did **not** prove an infinite-family \(\omega(1)\) degree lower bound for that encoding.

What is established is:

1. an exact degree lemma for a single positive linear form;
2. a counterexample showing the exponential-support Farkas family does **not** imply a degree lower bound;
3. a structural explanation of the gap: terminal \(z=0\) loses mutual-exclusion information, and tree restrictions are always linearly easy.

The decisive next obstacle is a **global** degree lower bound combining all \(2^k\) tree contradictions — e.g. a low-degree reduction from functional pigeonhole / bounded-degree expander PHP (Mikša–Nordström; Lauria–Nordström) to the state-expanded flow, or an explicit low-degree refutation using new algebraic identities that survive the loss of individual exclusions at terminal states. The framed-certificate checker remains an **upper-side soundness** tool; it does not certify non-sortability, and its soundness is not completeness of algebraic refutations.

## Output 503 (msg_1bd8d2a0f001xaovWvhM9TAHua)

## Recovery inspection

I inspected the existing conversation, worktree, Git state, board, and ledger before doing anything.

**Effects that actually happened (verified):**

- **Board #301:** exactly one post from this front, at `2026-11-08T23:42:37Z`, author `SoringP1 frontier: nullstellensatz-nonsortability-completeness`. It is the lemma/obstruction report from the previous turn. Searches on pages 1 and 2 found no duplicate.
- **Repository:** clean worktree at `6a96398` on `billy-dev`; no commits, no stashes, no new files, no Lean changes.
- **Scratch:** only `/tmp/opencode/` artifacts; no repository side effects.

**Uncertain / unfinished bookkeeping:**

- The durable frontier ledger still shows `nullstellensatz-nonsortability-completeness` as `status: running` with `finished_at: null`, `exit_state: null`, and no `finding_unverified`. I did **not** edit this, following the earlier operational precedent that the keeper/executive reconciles ledger state. It should be reviewed there rather than guessed at.

**Mathematical status:** unchanged from the prior turn — the front is not resolved. The reported result is the reciprocal-degree lemma, the counterexample showing the Farkas-support-to-degree route is invalid, and the structural obstruction at terminal states / tree restrictions. No new claim or duplicate post was created.

No further external action is needed from me; only the ledger reconciliation remains for the keeper/executive.
