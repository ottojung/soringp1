# antonina-Ya7UwwLJvGvjX8hHateMEL-tver

Session: ses_e52dd8c9bffeD4Z7KG5ajul4YH
Workspace: /home/lubko/soring301
Created: 1793906078616; updated: 1793906143935

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 43 (msg_1ad229d24001GCYel2mgKRnRq3)

I’ll test a concrete candidate key against the exact residual minimax value, rather than infer that matching signatures imply equivalence. I’ll use the smallest counterexample I can establish and distinguish it from any runtime or general compression lower bound.

## Output 80 (msg_1ad234aea0016iQUu0BwB7ueV6)

**The proposed extension-count boundary key is falsified at \(n=5\).** It retains the multiset of unordered pairs of child linear-extension counts—one pair per incomparable comparison, with both answer orientations included—but forgets which child signatures belong together across the two successors.

Using the repository’s successor-bitmask representation, the smallest witness I found is:

- \(P\): `4<1, 4<2, 3<0`, with \(F(P)=3\).
- \(Q\): `3<1, 3<2, 4<2`, with \(F(Q)=4\).

Both have the same proposed key: a multiset containing **one** `(2, 2)` pair and **four** `(1, 1)` pairs. Yet their residual minimax values differ. The residual values are exact, from the recurrence \(F(P)=1+\min\max(F(\text{child}_1),F(\text{child}_2))\); the witness search enumerated all labelled posets for \(n\le5\), and found no collision with differing \(F\) at smaller \(n\). This falsifies congruence for the candidate key, not for compressed boundary invariants generally.

A bounded-width decomposition does not, by itself, repair this: a quotient would still need to preserve the paired existential choice of comparison and universal choice of orientation, and width bounds alone do not establish that congruence. I have not proved that all such decompositions fail, nor established a lower runtime bound. **No exact all-\(n\) runtime improvement follows**; the existing \(2^{O(n\log^2 n)}\) bound remains unchanged. No repository files were edited.
