# antonina-XJfw36i5a7WndXgZFDyrfV-moles

Session: ses_e042e6784ffem96J8eDEO9whbt
Workspace: /home/lubko/soring-fronts/exec-fo-tc-policy-verifier-20261121
Created: 1795226179815; updated: 1795226724740

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_1fbd19b6b001M985FJaGfPkNAj)

I'll start by reading the contract docs and understanding how research reports are posted to the board.

## Output 203 (msg_1fbd392050015t0pOj2ZmAWgLe)

Now let me read the full refereed FO(TC) strategy-program note — it defines the strategy-program language, Lemma A, and the Sigma_2^P fragment.

## Output 230 (msg_1fbd40424001iyqiRiiH74KzYM)

I have the full FO(TC) note. Now let me gather supporting context: the minimax/antichain definition, the ESP executable witness script, the certificates-barriers doc, and the frontier ledger entry for this front.

## Output 289 (msg_1fbd8c75b001C3XoGICeVpRw2f)

I now have all the material I need. Let me write the finding and post it to #301.

## Output 327 (msg_1fbd9aecd0018twdBb97114i65)

Posted to Antonina #301 (newest post, `2026-11-21T02:04:58Z`). Summary of the finding:

**Candidate scheme (the note's natural form):** certificate = FO(TC)_v program `p` (poly size); verifier `V(p,n,k) := ∀X∈S_n: Verify(p,X,n,k)` — `QWIN_{v,d,c}`, note §6.

**Proved:**
- *Soundness* [deduction]: if `V` accepts, `p` is a correct strategy with worst-case depth ≤k, so `S(n) ≤ k`.
- `QWIN_{v,d,c} ∈ Σ₂^P` [deduction, note §2.2].

**Obstructed:**
- Not poly-time checkable: verifying "`p` correct, `k(p)≤k` on the antichain" is the Π₂ check `∀X Verify(p,X)` — simulation over `n!` orders isn't polynomial, so the scheme is Σ₂-style, not NP-style (note §6: "NP would require … the universal quantifier over X would be eliminated").
- Hard-verification-task obstruction: the natural certificate (the program itself) leaves verification as game-solving on `A_n`. Concrete repo-established size obstruction: the antichain's winning frontier at the exact optimal budget is `2^{(1/4−o(1)) n (log₂ n)²}` nonisomorphic states (winning-frontier barrier, via Sergeev `S(n)−C(n)=o(n)`); explicit tree witnesses have `≥ 2n!−1` nodes (research-certificates-barriers). Any certificate enumerating the frontier is exponential; compact programs are the only possible NP route.

**Open remainder (precise):**
1. `SORT-BOUND-U ∈ NP`? — unknown; not claimed (problem.md).
2. FO(TC)-route to NP: for every `(n,k) ∈ SORT-BOUND-U` a poly-size program `p` plus a poly-time-checkable compact correctness proof — open (Conjecture C, note §4/§9; note §5.3: "poly possible, no polytime universal verifier is known"; QWIN completeness open).
3. Continuity: ledger front `fo-tc-policy-interpreter` was investigated with no result; this pass makes soundness rigorous and isolates the NP-route obstruction.

No repo changes; nothing claimed beyond deduction and the repo's established barriers.
