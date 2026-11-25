# antonina-E3ePXgQXlPAUyBgGFMVvCT-saddles

Session: ses_e0866cc96ffeE92i9hPiiW19ag
Workspace: /home/lubko/soring-fronts/greedy-evalue-closed-form-sparse-exception-alln
Created: 1795155375019; updated: 1795156987125

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1f79935b30010IQeJ7eu2YQLJX)

I'll start by understanding the environment, branch state, and the key documents.

## Output 21 (msg_1f799401b001CaUI0yxzTUxZ5x)

I'm on `billy-dev` with a clean worktree. Let me read the core documents and locate board #301.

## Output 40 (msg_1f7994bef001y9IEPy7GW2lcNb)

Now let me check board #301 digest and find the specific front and prior result.

## Output 55 (msg_1f799cd2a001lyQFWjkKjFytRD)

Let me read the full board posts relevant to this front.

## Output 70 (msg_1f79a3cc5001p8y2VsStmOLXKH)

The digest truncates. Let me find the full board data location.

## Output 85 (msg_1f79a4975001C0epH2YvrnFA7S)

Let me fetch the full text of the key board posts directly.

## Output 96 (msg_1f79a5c05001GxB1VstZZ1lnKn)

I now have a thorough understanding of the board state. Let me examine the prior scratch work and any repository research notes on the greedy value definition.

## Output 111 (msg_1f79a84140016tqpL0o6j4Lt8P)

Let me read the most recent scratch scripts (the "new computation" on unequal-value ties) and the greedy game model.

## Output 130 (msg_1f79a92ca001TX7d4c1TWqLHls)

Let me run the existing scratch probes to get concrete data before designing my own test.

## Output 149 (msg_1f79d0d960015F592HvKfXJl9i)

The brute-force script is too slow. Let me run the efficient probe and read supporting scripts.

## Output 160 (msg_1f79d7a68001iiWZNoOMVn9IZ6)

I have concrete data. Now let me test the key amplification idea: chain-union states (proved reachable) with colliding factorial-products but different greedy values.

## Output 178 (msg_1f79fb652001fJZnskWyJV4T1v)

The full partition enumeration is too slow due to G recursion. Let me compute a specific collision example and verify V additivity directly.

## Output 196 (msg_1f7a1d506001wxsJzcP8ruPQP0)

Let me test ordinal-sum additivity and reachability of layered posets, which determine whether amplification is possible.

## Output 214 (msg_1f7a2fc41001X11NhrCix16XmK)

V is additive under ordinal sum, and layered posets are reachable (n≤6). Key issue: budget. Let me check the concrete chain-union collision and gadget structure with a minimal fast script.

## Output 232 (msg_1f7a353ba001Zo4T6UJJSuemLV)

Key finding: e=56 is mixed at n=8 via chain-union collision 6! = 5!·3! (V=6 vs 7), both reachable. Let me test whether this collision persists when combined with arbitrary prime-chain-unions.

## Output 266 (msg_1f7a72d890011A47xMs82T7nFT)

n=10 is slow. Let me run with a longer timeout while also checking the canonicalization helper for speed.

## Output 286 (msg_1f7acbf27001xPzUlkiwCLInra)

Let me test the cross-pair greedy path to layered posets — this is cheap and determines reachability.

## Output 304 (msg_1f7ad6111001x3DzOvUFy1oEvq)

The cross-pair path is heavy in all tested cases. Let me verify the underlying lemma broadly and for the a=8 gadget size.

## Output 338 (msg_1f7aff2c7001qqSZMTuJ9FyTAI)

I now have a complete proof path. Let me verify the gadget values once more and check the board-post CLI syntax.

## Output 365 (msg_1f7b13736001Lvt32NHSPxb4kb)

I have a complete paper proof. Let me compose and post the finding to board #301.

## Output 383 (msg_1f7b18dc5001eIwCX6Io0xdY2e)

Let me verify the post landed correctly.

## Output 394 (msg_1f7b1ab32001AYrN59CQBeFFTy)

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
