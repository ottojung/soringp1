# height-two-full2wl-child-completeness

## status

investigated

## origin

ai_proposal_unverified

## agent_id

InGq521mTNMCJDyfb4EnzU-precede

## exit_state

clearexit

## question

For every n and every height-at-most-two n-element poset P, does the stable full/paired 2-WL colour of an incomparable pair determine the unordered pair of isomorphism types of its two comparison children, or can one colour class contain child pairs of two different isomorphism types at some n?

## basis

Board #301 2026-11-09T15:56Z height-two-full2wl-n10 post reports constant unordered child-isomorphism type for every height-at-most-two poset through n=10, with an n=11 supplementary scan; the 2026-11-09T17:12Z kwl post records the same phenomenon for all posets through n=10 but only for the weaker move-value quotient. The all-n height-two child-isomorphism statement is not in the ledger.

## falsifier

Exhibit a height-two poset with two incomparable pairs of identical stable full/paired 2-WL colour but non-isomorphic unordered child-type pairs, with the colour refinement and both child canonical forms computed explicitly.

## implication

A positive all-n theorem would explain the exhaustive height-two stability through n=11 and would give a sound move quotient for height-two minimax states, including the one-comparison state Q_n whose exact value is S(n)-1; a counterexample would bound 2-WL completeness even on the simplest nontrivial height class.

## finding_unverified

Z`). No repository, ledger, Lean, branch, or test changes were made; the worktree is clean at `6a96398`. Scratch work is under `/tmp/opencode/h2full12`.

### Counterexample

Let \(G=\mathbb Z_2\times\mathbb Z_8\) and

\[
D=\{(0,0),(0,1),(1,0),(1,2),(1,5),(1,6)\}.
\]

This is a \((16,6,2)\) difference set; the 30 ordered nonzero differences cover every nonidentity element of \(G\) exactly twice. Let \(P\) be the incidence poset of the resulting symmetric design: points \(0,\dots,15\), blocks \(16,\dots,31\), point \(x<16+\operatorname{idx}(g)\) iff \(x=\operatorname{idx}(g+d)\) for some \(d\in D\). Then \(P\) has 32 elements and height two. The design is one of the three non-isomorphic \((16,6,2)\) biplanes; the difference set is the one given by Assmus–Salwach, *The (16,6,2) designs*, Internat. J. Math. Math. Sci. 2 (1979), 261–280, for their \(D_7\).

### The collision

Full/paired 2-WL stabilizes after 2 rounds. All \(\binom{16}{2}=120\) point-pairs lie in the single colour class

\[
(4,4).
\]

In particular,

\[
c(0,1)=c(1,0)=c(0,4)=c(4,0)=4.
\]

So \(\{0,1\}\) and \(\{0,4\}\) are incomparable pairs with identical stable full/paired 2-WL colour.

### The children differ

The blocks containing points \(0,1,4\) are

\[
N(0)=\{16,23,24,26,27,30\},\quad
N(1)=\{16,17,25,27,28,31\},\quad
N(4)=\{19,20,26,28,30,31\}.
\]

Thus \(P+0<1\) adds

\[
\{0<1,\ 0<17,\ 0<25,\ 0<28,\ 0<31\},
\]

while \(P+0<4\) adds

\[
\{0<4,\ 0<19,\ 0<20,\ 0<28,\ 0<31\}.
\]

Exact VF2 checks give **all four** cross-isomorphisms false, so the unordered child-type pairs differ. An independent invariant agrees: refining the disjoint union of the two 32-element children by the same full/paired 2-WL yields **352** stable colour classes on the first child and **106** on the second, so the children are not even 2-WL-equivalent, hence not isomorphic. Random relabellings reproduce the original colour equality.

### Interpretation and limits

This is a **completeness failure** of stable full/paired 2-WL as a child-isomorphism quotient on height-two posets, not a proof that the weaker numerical \(T\)-quotient is unsound. I did **not** compute the exact \(F\) values of the two children, so no \(T\)-collision is claimed. The statement that finite stability through \(n=11\) extends to all \(n\) is now decisively false; the exhaustive small-\(n\) phenomenon is a small-size effect. The remaining narrower question is whether the numerical \(T\)-quotient can also be falsified on this 32-element state, and what the minimal height-two counterexample is.
Recovery check complete. No interrupted work was repeated.

- **Working directory / Git:** clean at `6a96398` on branch `billy-dev`; no commits, branches, or repository edits.
- **Durable board record:** exactly **one** matching post exists, timestamp `2026-11-09T20:39:06.390Z`, author `SoringP1 frontier: height-two-full2wl-child-completeness`, body length 4,905. No duplicate was posted.
- **Scratch evidence:** counterexample scripts and outputs remain under `/tmp/opencode/h2full12/`.
- **Mathematical result:** unchanged. The all-\(n\) height-two child-isomorphism claim is false, with an explicit 32-element counterexample: the Assmus–Salwach \(D_7\) biplane incidence poset, point-pairs `{0,1}` and `{0,4}` of identical stable full/paired 2-WL colour `(4,4)` but non-isomorphic unordered comparison-child pairs. This is a completeness failure, not a claimed numerical \(T\)-collision.

No further external action is needed, and none was taken.

## Other metadata

```json
{
  "finished_at": 1794256898.5332189,
  "started_at": 1794252611.0144649
}
```
