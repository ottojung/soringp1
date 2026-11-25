# antonina-6FfwzJmqKqA1pqweVE0rRB-restless

Session: ses_e159f3faaffe5eP43M7Jc3jiji
Workspace: /home/lubko/soring301-exec-gap-pattern-structural-20261117e
Created: 1794933571689; updated: 1794933710334

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 70 (msg_1ea62a343001nShMP0WFQ6QUwe)

Created `exec-report.md` in `/home/lubko/soring301-exec-gap-pattern-structural-20261117e/`.

**Falsifiable question & hypothesis (structural/computable).** Characterized information-bound tightness as existence of a winning strategy in the $C(n)$-budget *information-feasible* poset/comparison game: $S(n)=C(n) \iff W_{C(n)}(P_0,0)$, where states $(P,c)$ must satisfy $e(P)\le 2^{C(n)-c}$ and moves are $h$-admissible comparisons (definitional/structural in reachable posets and strategy, equivalent to efficiency-frontier feasibility).

**Derivation.** Proved necessity from any height-$C(n)$ tree (leaf-count/nodewise feasibility) and sufficiency by constructing a height-$\le C(n)$ tree from a witness strategy; noted it is decidable in principle by finite AND/OR search over the admissible poset game (a game/strategy reformulation, not a scalar fit).

**Check against known $n\le 22$.** Verified consistency with all established values/tightness: tight at $n=1$–$11,20,21$ ($W_{C(n)}$ true) and non-tight at $n=12$–$19,22$ ($W_{C(n)}$ false, e.g. Wells/Stober–Weiß for $n=12$), with a full $n,C(n),S(n),$ gap table.

**Generalization attempt & falsification/obstruction.** The equivalence generalizes to all $n$, but a *predictive/tractable* structural $n$-predicate is obstructed: prior literature/experiments (as synthesized in `docs/research-n12-nontightness.md`) refute scalar/local proxies—$m(P)$ not monotone/function of $e(P)$, local bound failures misaligned with global tightness, forced-prefix/symmetry/chain-merge not predictive, irregular tightness pattern—so any sufficient characterization must track the global strategic poset game. Known $n=12$ non-tightness lacks a compact structural certificate (search-only).

**Consequence.** Defensible: tightness $\Leftrightarrow$ win in the information-feasible strategy game (global/structural), ruling out $e(P)$-only, fixed-local, and simple scalar predictors. Decisive obstacle: a compact unavoidable-subgame certificate for $\neg W_{C(n)}$ (e.g. $n=12$) or a provable invariant deciding $W_{C(n)}$ without full enumeration. No new $S(n)$ values or complexity claims made.
