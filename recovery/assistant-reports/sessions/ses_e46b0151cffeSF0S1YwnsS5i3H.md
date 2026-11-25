# antonina-QuN2GRVxwhBW40RkFwCeUk-sweep

Session: ses_e46b0151cffeSF0S1YwnsS5i3H
Workspace: /home/lubko/soring-fronts/root-adversarial-forcing-width
Created: 1794110384939; updated: 1794110395323

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 37 (msg_1b94ffee6001ZANgdjbO3Nj1qA)

Based on the board and AGENTS.md, the honest mathematical finding is:

**No closed-form width-forcing recurrence at the root antichain is currently established for all n.** The existing width-two Fibonacci threshold (`e(P) ≥ F_{m(P)+2}`) is proved via Peczarski's Gold Partition Conjecture for width two, and its scope is explicitly width two. Lifting to the root antichain (width n) requires a width-n analogue of Gold Partition, which is exactly the open global threshold `T(r)=F_{r+3}-1` question; no all-n proof exists.

**Failed route / obstruction:** The shallow-state reachability lemma (`reachable iff |cov(P)| ≤ k`) was shown false (cover count necessary but not sufficient), so extension-threshold pruning does not rescue a recurrence. The "single optimal branch" variant (child depths `(m-1, ≥m-2)`) survived finite checks up to n≤7 but has no all-n proof and remains a conjecture.

**Complexity implication (if proved):** A width-forcing recurrence at the antichain root would give a uniform lower-bound gadget yielding a sharper exact bound on S(n); without it, the exponent remains as in `2^{O(n²)}` numeric time.

**Honest limit:** I did not create repo/Lean changes; the decisive obstacle is the absence of a width-n Gold Partition theorem. No new all-n theorem or counterexample was produced in this pass.
