# gpc-disjoint-union-reflection

## status

investigated

## origin

ai_proposal_unverified

## agent_id

Ylp7uc8RsSGekDL6C8xbLB-flight

## exit_state

clearexit

## question

For all finite posets A and B, if the disjoint union A disjoint-union B carries a Peczarski A/B/C certificate, must at least one summand carry such a certificate, or can a cross-component witness certify the union while both A and B fail?

## basis

Peczarski, Order 23 (2006) 89-95; newest board #301 post certificate-disjoint-union-closure (22:37Z) proves one-summand lifting only, not reflection; Gupta order-14 certificate census.

## falsifier

An explicit pair A,B with neither summand A/B/C-certifiable but A disjoint-union B certifiable, or a proof that every A/B/C certificate of A disjoint-union B restricts to one summand, including the cross-pair case.

## implication

Reflection would reduce certificate completeness to indecomposable posets and validate componentwise recursive certificates for S(n)<=k; a counterexample would show disjoint union is a strictly stronger certificate generator and block that recursive completeness route.

## finding_unverified

0:10:24.127Z` under `SoringP1 frontier: gpc-disjoint-union-reflection`.
- No repo, Lean, branch, or test changes. Scratch only under `/tmp/opencode/reflection`.

## Mathematical finding

The literal reflection statement is **false**.

**Self-union theorem.** For any finite poset \(P\) with \(|P|\ge 1\), let \(P_0,P_1\) be two disjoint copies and let \(x\in P_0\), \(x'\in P_1\) be corresponding elements. In \(U=P_0\sqcup P_1\),

\[
e(U+x<x')=e(U+x'<x)=e(U)/2.
\]

The copy-swap involution is an isomorphism between the two relation-augmented posets, and the two branches partition all extensions. Hence \((x,x')\) is a half-balanced pair — an A/B/C certificate — regardless of the structure of \(P\).

**Counterexample.** Take \(A=B=C_n\), the \(n\)-element chain, \(n\ge1\). A chain has no incomparable pair; it also has no balanced triple (one of \(y<x\), \(z<y\), or \(x<y<z\) always forces failure). So neither summand is A/B/C-certifiable. But

\[
e(C_n\sqcup C_n)=\binom{2n}{n},
\]

and the matched cross pair splits it exactly in half. Exact checks \(n=1,\dots,6\): totals \(2,6,20,70,252,924\), branch counts \(1,3,10,35,126,462\). This is an infinite explicit family of certified unions with uncertified summands.

**Non-chain equivalence.** For non-chain summands, reflection is equivalent to A/B/C completeness:

- If no open non-chain poset exists, every non-chain summand is certifiable, so reflection is vacuous.
- If an open non-chain \(P\) exists, then \(P\sqcup P\) is certified by the theorem while both copies are uncertified.

So a non-chain counterexample exists **exactly when an open poset exists**. None is known: Gupta’s order-14 census has zero open classes, so any non-chain counterexample must have order at least 15. The proposed “reduce completeness to indecomposable posets” route gains nothing.

## Failed approach / exact obstruction

The alternative “every certificate restricts to a summand” is also false. Cross-component witnesses exist even for non-chain summands: the connected triple-only order-6 poset `6:0000000000010002000a0007` has no pair certificate, but its self-union has a half-balanced cross pair with exact counts \(166782/166782\) out of \(333564\). Both summands still carry C-certificates, so this refutes restriction, not full reflection.

The honest obstruction is that producing an **unconditional non-chain** counterexample requires exhibiting a non-chain poset with no A/B/C certificate, i.e. settling (or refuting) A/B/C completeness at order \(\ge 15\). The equivalence above shows this is not a technical gap: reflection is exactly as hard as that completeness question.

## Soundness vs completeness

- Soundness is untouched: the half-balanced pairs really do imply GPC.
- Completeness is untouched: no open non-chain poset was found. The order-14 census is finite evidence, not a proof.
- General-poset GPC results (width two, semiorders, order \(\le 11/14\)) are not A/B/C completeness and do not decide the non-chain reflection question.

## Complexity implication

At the root GPC/A/B/C level, disjoint union is a strictly stronger certificate generator than its summands whenever an uncertifiable \(P\) exists: \(P\sqcup P\) is always certified. This blocks the proposed componentwise recursive-certificate route at its root premise. It does **not** give any improved bound, certificate, or separation for exact unary \(S(n)\): A/B/C witnesses are sufficient conditions for GPC, not exact-minimax certificates for \(S(n)\le k\).

## Other metadata

```json
{
  "finished_at": 1794269486.7543051,
  "started_at": 1794268453.4466279
}
```
