# antonina-k2voN2eBTLvteXUBcAQscC-inflamed

Session: ses_e497bd2cdffewrZFZZ0Cjn9XXX
Workspace: /home/lubko/soring-fronts/exec-t5-threshold-20261107
Created: 1794063478071; updated: 1794063647502

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 33 (msg_1b6845be00016CxblPJtraEYuS)

The insertion-generation rule appears structurally sound: each new maximal element is specified by a predecessor ideal, then inserted after those predecessors in each existing linear extension. I’m checking the actual exhaustive run and the two non-enumerative reductions separately; the connected-core claim depends on those being correctly applied.

## Output 80 (msg_1b686975c001sUxz1eIsQf3fcX)

The reproduction script’s SHA-256 matches the supplied hash. It completes and reports the claimed witness (`e=21`, minimax `6`) and no failing connected cores: 324 at `e=18`, 304 at `e=19`, and 305 at `e=20`.

The core enumeration is **complete, conditional on its stated spanning-tree bound**. Every finite poset can be given a natural labeling by repeatedly removing a maximal element. In this generation, the new element’s predecessors must form an ideal; for each existing extension, insertion after the last predecessor gives exactly the legal positions. The extension count cannot decrease when a maximal element is added, so pruning above 20 is safe. The `n≤e` cutoff is safe for connected incomparability graphs by the spanning-tree inequality: each edge contributes a strict order in one direction, and a spanning tree forces at least `n` distinct extensions. Duplicate generation, if any, does not affect coverage.

For each tested core, the split check examines every pair of incomparable elements, hence every nontrivial legal comparison. The minimax DP uses the full extension set and its recurrence is exact: terminal states have one extension; otherwise minimize over legal comparison splits the maximum child depth plus one. The witness result therefore gives `T(5)≤20`.

The lower-bound argument also checks out, with one important qualification: the **T(4)=12 input is assumed**, not reproved by this script. Given that input and the stated Kahn–Saks balancing theorem, the `e≤17` case is covered; the enumerated `e=18,19,20` cores have a legal split into two states of at most 12 extensions, so each child has depth at most 4. Ordinal-sum factors multiply extension counts and add minimax depths. The factor arithmetic is consistent: among factors with positive depth, any total depth at least 6 requires an extension-count product of at least 24 using the supplied thresholds (the minimum is `T(2)·T(4)=3·8=24`, or `T(3)·T(3)=25`); hence it cannot occur with total count ≤20. Thus, **conditional on the cited T(4) result and the Kahn–Saks bound, the script supports `T(5)=20`**.

The 120-second foreground attempt timed out during enumeration, but the background run completed with the output above. No files were edited and nothing was posted.
