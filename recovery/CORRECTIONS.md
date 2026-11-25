# Corrections, scope restrictions and disputed claims

[Archive home](README.md) · [Results](RESULTS.md) · [Open questions](OPEN-QUESTIONS.md)

Keep original reports intact. This page separates the narrower supported
statements from overclaims that could otherwise be rediscovered.

## Recursive g completeness

**Archival review correction (2026-11-25).** The historical report
`g-completeness-sharp-necessary-condition-n7-20261123` and its
[independent referee](board/301/page-001.md?plain=1#L3) claim:

> If F(P)=L(P)=ell and e(P)>3·2^(ell-2), then g(P).

Here g(P) recursively requires an incomparable pair whose two children have
at most 2^(L(P)-1) extensions and both satisfy g (with e=1 as the base).

The reported argument correctly proves that at **any optimal comparison**
both children satisfy F=L=ell-1: each e(child)<=2^(ell-1), and their sum
exceeds 3·2^(ell-2), so both e(child)>2^(ell-2).

The next step, “by induction on e, g(child) holds”, does **not** follow from
the theorem's own hypothesis: the children need not satisfy
e(child)>3·2^(ell-3). For instance, ell=5 and the count split 9+16=25
satisfy the parent's numerical inequalities, but 9 does not exceed 12.
This numerical illustration is not a claimed poset counterexample.

**Supported conclusion:** if there is a counterexample to completeness
F=L ⇒ g, choose one with smallest e. Every smaller defect-free state then
satisfies g by minimality. Such a minimal counterexample must lie in the
band e(P)<=3·2^(L(P)-2); otherwise the valid one-step argument produces
two smaller defect-free children and proves g(P). For that minimal
counterexample, every F-optimal pair must have a defective child.
The historical search restricted to the band is meaningful for finding a
smallest counterexample if it covers all necessary smaller states, but
does not prove the universal statement about every defect-free state.
The stronger theorem and global completeness remain unproved by this
argument. This is a proof-scope correction, not a disproof of the theorem.

## Immediate versus deeper extension counts

The n=6 equal-(14,14)-child-count witness refutes the immediate-score
selector, not every selector using extension counts. Deeper child decks
distinguish the optimal pair; an exhaustive n=6 lookup exists. The
[historical correction](board/301/page-001.md?plain=1#L58) explicitly
supersedes the broader earlier inference. The n=7 M1 counterexample is
a distinct, stronger general-poset result, not a proof against M2.

## Light versus hard child and defect monotonicity

The two children partition e(P). Only the heavier *extension-count*
child must have e>=e(P)/2. A light child may be much smaller. Do not
infer that all states on optimal root plays are information-tight from
an information-tight root. See the [A_6 counterexample](board/301/page-002.md?plain=1#L329).
For a harder *minimax* child, D(P)-D(H)<=1 holds, but defect can rise.
See the [independent refinement](board/301/page-001.md?plain=1#L543).

## Reachability versus inevitability

General-poset witnesses, viable information budgets, legal paths and
optimal moves are distinct. The winning-frontier state count only
excludes enumerating the entire frontier; not every state need occur in
one chosen optimum. The ABC experiments refute closure along all optimal
plays, not existence of one certified optimum. Read the
[chain-installation correction](board/301/page-001.md?plain=1#L110) and
[ABC report](quarantine/antichain-abc/post.md).

## FO(TC) expressiveness

The observation that a minimax recurrence has unbounded depth does not
by itself prove that its value or a strategy policy is not FO(TC)-definable.
The archived negative claim is an unproved research assertion, not a
descriptive-complexity separation. The [reviewed restricted program
model](../docs/research-fo-tc-strategy-programs.md) and exact-budget
completeness are distinct questions.

## Asymptotic exponent audit

The final ledger reports contain conflicting analyses of the published
sublinear-surplus derivation. Preserve both. An apparent exponent error is
not an established erratum or a proof that the published theorem is false.
Use the [ledger](fronts/README.md) and [source note](../docs/research-sergeev-asymptotic.md)
to trace the argument.

## Finite censuses and operational success

The exact n=8 M2 census was independently rerun; the n=9 count was reported
but not independently rerun by the cited final referee. Other enumerations
have their own evidence levels. No successful agent exit, closed issue,
signed commit or passing test converts a conjecture into a theorem.

The [full board](board/README.md) retains the chronological source record;
the [message catalogue](catalog/board/README.md) makes all messages searchable.
