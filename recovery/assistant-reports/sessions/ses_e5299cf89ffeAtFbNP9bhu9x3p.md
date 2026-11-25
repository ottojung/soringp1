# antonina-ivNhBrrNvCSK7K0T6RLs8w-street

Session: ses_e5299cf89ffeAtFbNP9bhu9x3p
Workspace: /home/lubko/soring-fronts/recovery-steward-sibling-budget-20261105
Created: 1793910517881; updated: 1793910610593

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1ad663093001X3gVwCD5oe29KF)

I’ll inspect the cited frontier and reviewed evidence, then work the candidate relation on root-reachable histories only. I’ll keep the work read-only and won’t alter the dirty worktree.

## Output 67 (msg_1ad66b440001Q27LYpamZWszfc)

The reviewed evidence separates two objects that can easily be conflated: the huge set of locally winning reachable posets, and the narrower set lying on some globally height-\(S(n)\) strategy (where both siblings must fit). I’m testing a history equivalence built from the *entire residual two-branch behavior*, rather than a scalar invariant such as \((e,\mathrm{covers})\); that can give a formal congruence, but it may simply encode the original minimax problem.

## Output 139 (msg_1ad674eaf001ak29Wj3rcUZVvC)

## Result: a safe quotient is clear; a useful polynomial one is not

**No verified counterexample or polynomial-size quotient follows from the reviewed evidence.** There is a precise, exact two-outcome congruence for histories, but it retains the full continuation game and therefore does not establish a polynomial class-count bound. The structural candidate \((e(P),\mathrm{covers}(P))\) is still unproved beyond the finite census; I found no small counterexample in the existing corrected \(n\le6\) evidence, nor in a read-only \(n=5\) check.

### Exact history congruence

Represent a history by its transcript poset \(P\), remaining height budget \(b\), and root-reachability status under a height-\(S(n)\) strategy. For a legal comparison \(q=\{x,y\}\), write its two children \(P_0,P_1\), and define the **continuation signature**
\[
\Sigma_b(P)=\bigl(\text{terminal status},\ \{(\Sigma_{b-1}(P_0),\Sigma_{b-1}(P_1))\}_{q}\bigr),
\]
with outcome order retained (or identified only under a label bijection). Then histories with equal signatures are equivalent.

**Lemma (two-outcome closure).** Equal signatures have the same legal comparisons and matching two children for each comparison; corresponding children have equal signatures at budget \(b-1\). Thus the equivalence is a congruence for the minimax recurrence
\[
F(P)\le b \iff \exists q\;\; F(P_0)\le b-1\ \land\ F(P_1)\le b-1.
\]
This explicitly preserves the sibling constraint: a path’s chosen child alone is insufficient for root-optimal reachability.

This is a direct recursive definition/proof, not a compression result: the signature can encode the whole depth-\(b\) game tree, and no polynomial bound on its number of classes is established. Restricting the definition to histories reachable in some height-\(S(n)\) strategy does not change that limitation.

### Why the tempting structural key remains open

The proposed smaller candidate from `notes/research-realizability-window.md` is \(P\sim Q\) iff \((e(P),\mathrm{covers}(P))=(e(Q),\mathrm{covers}(Q))\), restricted to root-reachable optimal-play states. Equality of the key does **not by itself** provide two-outcome closure: the key gives no identified children, and the note explicitly says transition structure is not a function of the key.

The corrected reachability DP requires **both** children to fit the residual budget. Its window theorem is necessary but not sufficient (the \(n=5\) false positives); the reported \((e,\mathrm{covers})\)-rigidity is only a finite experiment through \(n=6\), and the note says all-\(n\) soundness is open. My read-only \(n=5\) check of reachable classes found no key split, consistent with—not extending into a proof of—the census. This is distinct from any \(n=7\) extension-pair \(K\) question.

### Class counts and frontier avoidance

No reviewed result proves a polynomial bound on the number of classes for either the structural key or another nontrivial root-reachable congruence. A finite census cannot supply such an all-\(n\) bound.

The winning-frontier theorem gives at least \(2^{(1/4-o(1))n\log^2 n}\) **nonisomorphic** reachable states at a common depth, including states winning at the exact optimal budget. Therefore full-frontier enumeration—even modulo relabelled-poset isomorphism—cannot be the proposed escape.

A quotient that avoids enumerating that frontier would need to aggregate states **symbolically**, with a proven child-transition rule and a polynomial number of aggregate classes (or another compact representation). The continuation-signature lemma supplies congruence but not compactness; \((e,\mathrm{covers})\) suggests compactness but has no established congruence. That gap is the specific unresolved obstruction. The winning-frontier result is an enumeration barrier, not a time lower bound for every selective or symbolic evaluator.

I made no repository changes, commits, posts, or Lean work. The pre-existing dirty files remain untouched.
