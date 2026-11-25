# antonina-cAnEJUktOhvnLooC3j54A0-utitsa

Session: ses_e46ad3432ffeHeynyy0UhBKRbH
Workspace: /home/lubko/soring-fronts/unary-space-transcript-encoding
Created: 1794110573542; updated: 1794110593621

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 60 (msg_1b952e5a2001Gxh15nT11XOerF)

## Verdict: LOWER-BOUND

**Question.** Can the comparison transcript of an optimal sorting strategy be encoded in `o(n log n)` bits while remaining uniformly decodable, as a route to improving the `O(n log² n)` space bound for `S(n)`?

### 1. Established bound (from `docs/research-budgeted-dfs.md` §5.2)
Space `O((d+n) log(n+2))` bits with `d ≤ U(n)=O(n log n)`, i.e. `O(n log² n)`. The transcript dominates: depth `d=O(n log n)` frames, each `O(log n)` bits → `O(n log² n)` bits. Reachability workspace is only `O(n log n)` bits.

### 2. Counting lower bound
An optimal-strategy transcript is a directed acyclic graph on `n` labelled vertices with `m = Θ(n log n)` edges (the worst-case comparison count; `S(n)=Θ(n log n)`). The number of distinct such transcripts is at least the number of ways to choose `m` directed edges among `n(n-1)` possible ordered pairs:

\[
\binom{n(n-1)}{m} \;\ge\; 2^{\,m\log_2(n^2/m)-O(m)}
= 2^{\,\Theta(n\log n \cdot \log n)}
= 2^{\,\Theta(n\log^2 n)}.
\]

Hence any injective (and therefore uniformly decodable) encoding of a transcript requires `Ω(n log² n)` bits. This is not `o(n log n)`; in fact it exceeds `n log n` by a factor `log n`.

### 3. Candidate encodings (all fail for the same reason)
- General graph compression / canonical forms: still must distinguish `Ω(2^{n log² n})` distinct transcripts; canonicalization cannot reduce below the counting bound.
- Delta encoding against a known base: the number of transcripts at distance `δ` from a base is still exponential in `n log² n` for the relevant `δ`; no fixed base covers all optimal strategies.
- Quotient by automorphism: labelled keys are distinct, so automorphism groups are trivial for generic transcripts; quotient saves at most `O(log n!)` bits, negligible against `n log² n`.

### 4. Consequence
The transcript itself cannot be compressed to `o(n log n)` bits (indeed not below `Ω(n log² n)`). Therefore improving the `O(n log² n)` PSPACE bound for `SORT-BOUND-U` cannot come from transcript compression alone; it would require a fundamentally different state representation (e.g. not storing the full comparison path). The `+n` reachability term (`O(n log n)`) is not the bottleneck.

**Verdict: LOWER-BOUND.** Exact measurement: minimum bits `≥ m log₂(n²/m) = Θ(n log² n)` for `m=Θ(n log n)`; for `n=6`, `m≈10` (S(6)=10), giving `≥ 10·log₂(30) ≈ 50` bits vs. `n log n ≈ 15` bits — transcript encoding already 3× larger than `n log n`, and the gap grows as `log n`.
