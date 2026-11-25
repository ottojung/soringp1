# antonina-yN3TDqAv1ePoZYWLzuswuG-persian

Session: ses_e4702fcb5ffedBEWYCXWe7x3j2
Workspace: /home/lubko/soring-fronts/canonical-form-reachable-posets
Created: 1794104951660; updated: 1794104962365

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 51 (msg_1b8fd15b00010CqKuAxXeZHyZE)

## Verdict: EXPONENTIAL-STATE-COUNT

### Reachable state class (precise)

States are strict partial orders on the `n` labelled keys induced by comparisons made so far. **Every** labelled poset is reachable (add its comparable pairs one at a time; each not-yet-implied pair is incomparable at insertion). So the reachable class is exactly labelled posets (OEIS A001035), not `2^{n!}`.

### Enumerated counts (n≤9)

| n | labelled A001035 | unlabelled quotient A000112 | S(n) |
|---|---|---|---|
| 3 | 19 | 5 | 3 |
| 4 | 219 | 16 | 5 |
| 5 | 4231 | 63 | 7 |
| 6 | 130023 | 318 | 10 |
| 7 | 6129859 | 2045 | 13 |
| 8 | — | 16999 | 16 |
| 9 | — | 183231 | 19 |

Both sequences are `2^{Θ(n²)}` (measured `log₂ A001035`: 12, 17, 22.5, 28.7, 35.4 for n=4..8). The full `S_n` automorphism quotient (the maximum possible relabelling collapse) shrinks by a factor `2^{Θ(n log n)}` but **does not change the exponent**: A000112 is still `2^{Θ(n²)}`.

### Canonical form / DP

The only sound canonical form at the maximum compression is the unlabelled poset isomorphism class. The minimax recurrence is equivariant under `S_n`, so `G([P])` is well-defined and `G([∅])=S(n)` (sound, exact). But:

- No polynomial-in-`n` canonical form exists that preserves `F`: the quotient class count is `2^{Θ(n²)}`, so any DP over it is `2^{Ω(n²)}` time/space, far above `2^{O(n log n)}`.
- Coarser invariants (linear-extension count, width) fail: the linear-extension-count restricted class returns 20 for n=9 while S(9)=19. The full poset structure is required.

### Citations

- `docs/research-state-compression.md` (Findings 1–3, falsification at n=9).
- `scripts/state_compression.py` (labelled DP, quotient recurrence, colour-refinement + brute-force canonicalizer).
- OEIS A001035, A000112; Peczarski 2012 for S(n) values.

### Bottom line

The `S_n` quotient is exact and useful (extends computation to n=9 in pure Python), but it is a constant/superpolynomial factor, not an asymptotic improvement. The state space remains `2^{Θ(n²)}` even after the maximal automorphism collapse. No polynomial canonical form preserving `F` exists; therefore a DP in `2^{O(n log n)}` over reachable states is impossible without a decomposition theorem not currently known.
