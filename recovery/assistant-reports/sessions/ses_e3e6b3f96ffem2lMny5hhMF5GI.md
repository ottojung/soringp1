# antonina-XQBysN8CjHnOAEui4ZbnrQ-poklonny

Session: ses_e3e6b3f96ffem2lMny5hhMF5GI
Workspace: /home/lubko/soring-fronts/fibonacci-lexicographic-preservation
Created: 1794249113907; updated: 1794253564424

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 1017 (msg_1c1d88680001JT7oR1RhLhnkXd)

**Finding (posted once to board #301): the front collapses to the base inequality.**

For `Fib(P) := [e(P) >= F_{m(P)+2}]`, the preservation statement for all finite `P,Q,i` is **exactly equivalent** to `Fib(P)` for every finite poset `P`:

- Take `Q` to be a singleton. Then `e(Q)=1`, `m(Q)=0`, `F_2=1`, so `Fib(Q)` holds, while `P circ_i Q ≅ P`. Hence preservation implies the universal statement.
- Conversely, if every poset satisfies `Fib`, then `P circ_i Q` does too, with no hypothesis on `Q`.

So the hypothesis `Fib(Q)` is never used. The lexicographic-composition framing adds no independent leverage over the base all-`n` inequality.

**Mathematical obstruction.** Any falsifier is exactly a finite poset `R` with `e(R) < F_{m(R)+2}` (take `P=R`, `Q` a singleton). If the board’s GPC-to-Fibonacci step is valid, `R` must be non-GPC, hence `|R| >= 15` by Gupta’s order-14 census. The cited Dolores-Cuenca–Guzmán-Sáenz–Kim theorem preserves **GPC**, not `Fib`; the published GPC consequence is only `e >= phi^m`, which is strictly weaker than `e >= F_{m+2}` for `m >= 4`.

**Exact work done.**
- Exhaustive all unlabeled posets through `n=7` (2045 classes): zero `Fib` violations and zero violations of the stronger split property. This improves the earlier “total size 7” check, which only covered `|Q| <= 6`.
- All fence superposets (adjacent-pin orientations, no consecutive backward pins) through `n=14` (508,992 admissible patterns at `n=14`): zero `Fib` violations; equality only on fences and end-pinned subfences.
- Attempted exhaustive `n=8`; the naive labeled-state cache blew up (12.8M states after 10k of 16,999 classes) and was killed. No `n=8` claim is made. A canonical-labelling attempt failed a correctness check and was discarded.

**Honest limit.** This is not a proof of the universal Fibonacci inequality, and it is not a counterexample. The decisive open step is either a paper proof of `e(P) >= F_{m(P)+2}` (or a verified GPC-to-Fibonacci implication plus a non-GPC witness at `n>=15`), or a correct isomorphism-quotiented exhaustive check of `n=8..14`.

No repository changes, no Lean, worktree clean at `6a96398`.
