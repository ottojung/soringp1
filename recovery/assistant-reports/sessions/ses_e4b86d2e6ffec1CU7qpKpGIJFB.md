# antonina-13fHdic1rN5H63fqcpXxiH-dieu

Session: ses_e4b86d2e6ffec1CU7qpKpGIJFB
Workspace: /home/lubko/soring-fronts/exec-successor-pair-quotient-20261107
Created: 1794029202716; updated: 1794029465385

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 62 (msg_1b47b7703001B3Hy00Kzqiw75u)

The refinement-based canonicalizer is not an exact canonical form: even on brute-force enumerated classes through n=5, its output disagrees with the all-permutations minimum. I’m checking whether those disagreements actually merge distinct classes or merely choose different representatives, then finishing the n≤6 partition comparison using a brute-force class oracle.

## Output 113 (msg_1b47d00f4001SR5HRffiUaDK4E)

**Audit result:** the script’s requested n≤6 partition claim is independently supported, but its refinement canonicalizer is not a canonical *minimum* under all relabelings. Its output is nevertheless an isomorphism invariant on the tested reachable classes; those are distinct properties.

- **Partitions, n≤6:** I independently enumerated reachable labelled states, grouped them into 1, 2, 5, 16, 63, and 318 isomorphism classes for n=1,…,6 using the refinement output, and compared the partitions of incomparable pairs. The Aut(P)-orbits were computed from all permutations; child-pair signatures were compared using a separate backtracking isomorphism test, with unordered child classes. The partitions were **equal in every class**. Thus both inclusions hold in these bounded cases.
- **Canonicalizer:** Refinement-cell permutations do not produce the lexicographically least encoding over all permutations: the outputs differ on some classes already at n=3. On the tested reachable classes through n=5, however, distinct exact brute-force isomorphism classes had distinct refinement outputs (5, 16, and 63 outputs). At n=6, 318 refinement outputs were found, but I did not complete an independent exact-isomorphism check that they exhaust and separate all classes. So exactness through n=6 is **not established** by this audit; the cell-minimum description should not be mistaken for the ordinary all-permutations minimum.
- **Recurrence:** For all 318 n=6 refinement representatives, grouping moves by the script’s child-signature key preserved the local minimax minimum when checked against exact labelled-DP values. The labelled recurrence gives S(6)=10. This is a bounded check, not a general recurrence theorem.
- **Instrumentation and timing:** `direct_permutations` counts the product of factorials of refinement-cell sizes, but is not an instrumentation of actual canonicalizer permutation leaves; it also excludes refinement work. `direct_seconds` includes canonicalization and additional refinement/counting, while `orbit_seconds` times the orbit baseline. Neither is a clean apples-to-apples timing comparison. The labelled-DP value lookups/checks occur outside `direct_sec` and `orbit_sec`, but they do add to overall runtime and the cap.
- **Misleading assertions:** `assert len(signatures) <= len(reps) or True` is vacuous. The signature-value loop compares identical canonicalized keys and checks equality of labelled values, but does not independently establish that the canonicalizer correctly identifies isomorphism classes. The final min check establishes only that the selected representatives preserve the minimum for those computed labelled values.

No asymptotic or general claim follows from these bounded results. I made no repository changes.
