# antonina-gQg7qDSxM7eiwJ63HMjXcj-brief

Session: ses_e473b3708ffe6m5uVfXwfUHKP4
Workspace: /home/lubko/soring-fronts/adaptive-tree-minimax-recurrence-space
Created: 1794101266765; updated: 1794101277237

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 37 (msg_1b8c4d6ba001G1rqI16NNgIGI1)

## Result: EXPONENTIAL-BARRIER

### 1. The recurrence (from docs/upper-bound.md)

State space: strict partial orders `P` on `n` labelled items (transitive closure), each unordered pair in `{x<y, y<x, unknown}` → at most `3^{n(n−1)/2}` ternary matrices.

Recurrence:
- `F(P)=0` if `P` is total.
- Otherwise `F(P) = 1 + min_{x,y incomparable} max(F(P+(x<y)), F(P+(y<x)))`, with successors transitively closed.

Start `F(empty)=S(n)`. Naive memoization over ≤ `3^{n(n−1)/2}` states × `O(n²)` transitions = `2^{O(n²)}` time/space in numeric `n`.

### 2. Symmetry quotient experiment

Under `S_n` relabeling, `F` is invariant (`F(πP)=F(P)`), so quotient states suffice. But quotient states = unlabeled posets on `n` elements, whose count grows `~ exp(n²/4)`:

| n | unlabeled posets |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 5 |
| 4 | 16 |
| 5 | 63 |
| 6 | 318 |

(These are the standard unlabeled-poset counts; recurrence values are determined by isomorphism type, verified small.) The quotient is still exponential in `n²`, so memoization over it requires exponential space. No polynomial-space reduction via symmetry.

### 3. Verdict

**EXPONENTIAL-BARRIER.** The `S_n` quotient reduces the constant but not the exponential order: state count remains `2^{Θ(n²)}`. Polynomial-space evaluation cannot be achieved by this recurrence plus symmetry alone; a genuinely different method (succinct certificates / structural theorem) would be required.
