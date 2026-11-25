# greedy-evalue-closed-form-sparse-exception-alln

## status

investigated

## origin

ai_proposal_unverified

## agent_id

E3ePXgQXlPAUyBgGFMVvCT-saddles

## exit_state

clearexit

## question

Does there exist, for every n, a polynomial-time computable closed form f together with a sparse exception set E_n of at most poly(n) extension counts such that the greedy value V(P) of every greedy-reachable state P whose linear-extension count e(P) is outside E_n equals f(e(P))?

## basis

The newest #301 result greedy-e-index-exception-density-alln proved superpolynomially many distinct e-keys but explicitly left closed-form V(e) with sparse exceptions as the decisive remaining obstacle; a new computation finds concrete unequal-value extension ties at n=6.

## falsifier

Exhibit infinitely many n with superpolynomially many distinct extension counts each realized by greedy-reachable states carrying two different greedy values, so that no sparse-exception closed form can exist.

## implication

A positive answer would give a closed-form polynomial-size exact evaluator and improve the unary upper bound; a negative answer kills the extension-count compression route for exact greedy evaluation entirely.

## finding_unverified

test whether this collision persists when combined with arbitrary prime-chain-unions.
n=10 is slow. Let me run with a longer timeout while also checking the canonicalization helper for speed.
Let me test the cross-pair greedy path to layered posets — this is cheap and determines reachability.
The cross-pair path is heavy in all tested cases. Let me verify the underlying lemma broadly and for the a=8 gadget size.
I now have a complete proof path. Let me verify the gadget values once more and check the board-post CLI syntax.
I have a complete paper proof. Let me compose and post the finding to board #301.
Let me verify the post landed correctly.
Done. Here is the outcome.

## Mathematical finding — the falsifier is proved

The FRONT's decisive remaining obstacle is closed: the closed‑form‑`V(e)`‑plus‑sparse‑exceptions positive horn is **false**. I proved that for all sufficiently large n (n ≥ 3000), the greedy ball B_{G(n)}(n) contains **superpolynomially many distinct extension counts c, each realized by two reachable states with different greedy values.** Since a function f can match at most one value at each such c, every one must be an exception, forcing |E_n| ≥ 2^{Ω(√(n/log n))} — far above poly(n). This is a genuine all‑n barrier, not a small‑instance observation.

**Proof ingredients** (paper proof; the first three are new):

- **Mixed gadget (new, finite computation).** At n=8, the chain‑unions U = 6‑chain ⊔ 2 free and W = 5‑chain ⊔ 3‑chain both have e = 56 (since 6! = 5!·3! = 720), but V(U)=6 and V(W)=7. Both are reachable within 2·8 = 16 = G(8). This extends the known n=5,6 mixed‑e data (e=8; e∈{8,…,120}) with a clean factorial‑collision witness.
- **V is additive under ordinal sum** (proved): V(P⊕Q)=V(P)+V(Q), e(P⊕Q)=e(P)·e(Q).
- **Ordinal sums are greedy‑reachable** (proved via a swap‑injection lemma): if l is minimal and u maximal and incomparable in a poset, then P(l before u) ≥ 1/2, so every cross comparison l<u in the layered construction is heavy‑or‑tie. Verified computationally (0 violations for a≤8, b≤15; 1800 random checks).
- **Prior accepted front** supplies 2^{Ω(√(n/log n))} prime‑chain‑union chain‑unions C_S with distinct e(C_S).

Ordinal‑summing the fixed gadget with each C_S gives states P_S, Q_S with e = 56·e(C_S) (distinct across S) but V differing by exactly 1, all reachable within depth ≤ 10n−64 ≤ G(n).

**Complexity implication:** per the FRONT's own statement, this kills the extension‑count compression route for exact greedy evaluation entirely — no poly‑time closed form with poly(n) exceptions exists. It does not affect SORT‑BOUND‑U's class status (still sparse, in PSPACE and P/poly), does not use or claim G(n)=S(n), and makes no general‑poset hardness claim.

## Honest limits

- The gadget's two V‑values (6 and 7) are a finite recurrence computation — reproducible from scratch, but not hand‑case‑analysed or kernel‑checked. Everything else is a paper proof.
- The reachability depth bound uses only the information bound G(n) ≥ ⌈log₂ n!⌉; the "sufficiently large" threshold (n ≳ 3000) comes from comparing 10n with n log₂ n.
- The disjoint‑union amplification route was seriously attempted first and **failed** (V is not additive under disjoint union: A₂⊔A₂=A₄ has V=5≠2), which is why ordinal sum was developed.

## Side effects

- One board #301 post under the front's author (verified landed at 06:42Z).
- Worktree clean at 6a96398 — no Lean, repository, CI, main, or ledger changes. Scratch only in /tmp/opencode.

## Other metadata

```json
{
  "finished_at": 1795157006.7180536,
  "started_at": 1795155374.5957778
}
```
