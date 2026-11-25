# antonina-oOqM4hAL7nKTC8t1a73jEQ-toss

Session: ses_e061b16b8ffeHYRvtq7Nk3q9wM
Workspace: /home/lubko/soring-fronts/verify-info-tight-propagation
Created: 1795193891292; updated: 1795193942582

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f9e4ebaf001YkNqQZRPs1oFRy)

I’ll locate the cited board entry and its definitions, then check the lemma algebraically and recompute the listed indices independently without modifying the repository.

## Output 81 (msg_1f9e56992001EhtDI7qjS9WXRO)

## Audit result

**The propagation lemma is correct.** For \(n\ge2\), let
\[
L(n)=\lceil\log_2(n!)\rceil,\qquad c(n)=\lceil\log_2 n\rceil.
\]
Binary insertion gives \(S(n)\le S(n-1)+c(n)\). If the information bound has a full increment, \(L(n)-L(n-1)=c(n)\), and \(S(n-1)=L(n-1)\), then
\[
L(n)\le S(n)\le S(n-1)+c(n)=L(n-1)+c(n)=L(n).
\]
Thus \(S(n)=L(n)\). Equivalently, at a full-increment index, **nontightness propagates backward**: if \(S(n)>L(n)\), then \(S(n-1)>L(n-1)\).

### Exact full-increment criterion

Write \(a=\log_2((n-1)!)\), \(b=\log_2 n\), and let \(\{x\}\) denote fractional part. The exact criterion is
\[
L(n)-L(n-1)=\lceil\log_2 n\rceil
\]
iff **at least one** of these holds:
\[
\{a\}=0,\qquad \{b\}=0,\qquad \{a\}+\{b\}>1.
\]
In particular, powers of two always give full increments. The post’s criterion needs the two integer-log cases: without them, its “otherwise” condition misses \(n=3\), where \((n-1)!=2\) is a power of two and the increment is full despite the fractional-part sum not exceeding 1. When both logarithms are nonintegral, the post’s strict-sum criterion is correct.

### Independent check through \(n=22\)

I recomputed \(L(n)\) directly from the exact integer formula \(L(n)=\operatorname{bitlength}(n!-1)\), and compared successive differences with \(\lceil\log_2 n\rceil\). The full-increment indices are:
\[
\{2,3,4,6,7,8,11,13,14,15,16,20\}.
\]
The remaining indices through 22 are short increments:
\[
\{5,9,10,12,17,18,19,21,22\}.
\]
This independently confirms the listed index sets.

## What this says about infinitely many tight \(n\)

The lemma establishes a **conditional propagation rule**, not that its condition occurs infinitely often. Starting from known tight values through \(n=11\), propagation along full increments reaches only \(n=11\): it stops at the short increment \(n=12\). Later full increments cannot restart propagation without a tight predecessor; in particular, the full increment at \(20\) does not follow a tight \(19\). The known tight values at \(20,21\) therefore are not explained by this propagation from the initial tight run.

So the audit supports a constraint on possible tightness patterns and confirms the finite index computation. It establishes **neither** that \(S(n)=L(n)\) for infinitely many \(n\), **nor** that only finitely many \(n\) are tight. The infinitude question remains open.
