# Referee seed-completion lemma

Session: ses_e434c67aaffeggt91NeSl9OLYn
Workspace: /home/lubko/soring-fronts/fixed-pattern-defect-bound
Created: 1794167249047; updated: 1794167402827

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 5 (msg_1bcb398f00017ev70E07VoaUcT)

**Verdict: the lemma is correct, and the proof has no flaw. But it is an elementary/folklore observation, not a structural theorem.**

## Where the proof could have failed, and why it does not

The only delicate step is the relabelling. Let \(X\) be the \(q+m\) keys and \(X_q\) the chosen \(q\) keys. After phase 1 we know their actual order \(y_1<\cdots<y_q\). Fix a linear extension \(z_1<\cdots<z_q\) of \(Q\) and define \(\varphi(y_i)=z_i\), with the remaining \(m\) keys mapped bijectively onto \(A_m\).

The actual total order \(\prec\) on \(X\) induces a total order \(\prec'\) on \(Q\sqcup A_m\). For any relation \(a<_Q b\), since \(z\) is a linear extension of \(Q\), we have \(a=z_i,\ b=z_j\) with \(i<j\). Hence \(\varphi^{-1}(a)=y_i\), \(\varphi^{-1}(b)=y_j\), and \(y_i\prec y_j\), so \(a\prec' b\). Thus \(\prec'\) is indeed a linear extension of \(Q\sqcup A_m\). This is the point that would break if the labelling were arbitrary; choosing \(z\) to match the sorted order fixes it.

Phase 2 is legitimate: the sorter for \(Q\sqcup A_m\) identifies \(\prec'\), and since \(\varphi\) is known after phase 1, we pull back to \(\prec\). The composed object is a valid adaptive decision tree of depth at most \(S(q)+F(Q\sqcup A_m)\). In particular:

- Quantifier/adaptivity: \(\varphi\) depends on the phase-1 outcome, but the composition is still a decision tree, and the worst case is additive.
- Comparisons inside \(Q\) in phase 2 are consistent with phase 1; they can be answered for free or simply charged inside the \(F(Q\sqcup A_m)\) budget.
- \(F\) is worst-case over all linear extensions, so the induced extension being a valid input is all that is needed.

So \(\;S(q+m)\le S(q)+F(Q\sqcup A_m)\;\) holds, and consequently
\[
D_Q(q+m)=S(q+m)-F(Q\sqcup A_m)\le S(q).
\]
That corollary is also correct.

## Why it is trivial rather than structural

For any linear extension \(z\) of \(Q\), the total order \(C_z\) on the \(q\) elements is a **superposet** of \(Q\) (it has all of \(Q\)'s relations and more). Hence
\[
F(C_z\sqcup A_m)\le F(Q\sqcup A_m),
\]
and the chain special case
\[
S(q+m)\le S(q)+F(\text{chain}_q\sqcup A_m)
\]
is just the obvious "sort \(q\) elements, then insert the remaining \(m\) into the resulting chain". Therefore the general-\(Q\) lemma is *weaker* than an already trivial chain statement. It is a two-phase decision-tree composition / insertion bound, folklore-level.

No exact theorem name comes to mind; it sits in the "sorting number of a poset" literature (Faigle–Turán and the information-theoretic poset-sorting tradition), but this particular inequality is not a named result.

## Comments on the claims surrounding the lemma

- **"\(D_Q\) is bounded for each fixed \(Q\)"** — true, with bound \(S(q)\), but generally very weak. For \(Q=A_q\), \(D_Q\equiv0\); the chain-like case is where the bound is close to tight (heuristically \(D_Q(n)\approx \log_2(q!/e(Q))\), which is \(S(q)\) up to lower-order terms for a chain).
- **"Attained at \(m=0\) when \(Q\) is a chain"** — technically correct: \(F(\text{chain})=0\), so \(D_{\text{chain}}(q)=S(q)\). But this is the degenerate case where the lemma reads \(S(q)\le S(q)+0\), so it demonstrates nothing beyond the definition of \(S(q)\).

**Bottom line:** no correction is needed; the lemma is valid. It should be labelled *trivial/folklore* (a decision-tree composition or "sort-and-insert" bound), not a genuine structural theorem about \(S(n)\).
