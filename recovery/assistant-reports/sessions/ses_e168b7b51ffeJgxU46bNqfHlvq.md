# antonina-Wwj0ucIAgWY7NTVIKboCJG-howl

Session: ses_e168b7b51ffeJgxU46bNqfHlvq
Workspace: /home/lubko/soring-fronts/information-tight-infinite-family
Created: 1794918089954; updated: 1794918215118

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 116 (msg_1e97580b5001P15AFht1f0wwtm)

**Scope / sources studied (billy-dev, hostname `billy-dev`, worktree clean at HEAD).**
- `AGENTS.md`, `docs/problem.md`, `docs/operations.md`, `docs/literature.md`, `docs/research-n12-nontightness.md`.
- Board #301 via `python3 scripts/board_digest.py --recent 7`, `--contains "ceil(log2(n!))"`, `--contains "information bound"` (recent front reports present: e.g. `info-bound-gap-invariant-alln`, `computable-entropy-balance-surrogates`, `n12-obstruction-invariant`; none records a proved all-`n` theorem for this front).
- Primary/indexed literature consulted (as cited in repo): Wells 1965/1971, Ford–Johnson 1959, Peczarski 2002/2004/2007/2012, Stober–Weiß ALENEX 2023 / arXiv:2206.05597v2, Knuth TAOCP §5.3.1, OEIS A036604/A003070 (indexes only, cross-checked against primary-value claims in docs/lit).

**Precise claim attacked (all-`n`, falsifiable; falsifier as stated).**
> **F (eventual uniform information-bound gap):** ∃N≥1 ∀n≥N, `S(n) >= C(n)+1`, where `C(n)=ceil(log2(n!))` and `S(n)` is the exact adaptive worst-case comparison sorting number (antichain root, `docs/problem.md`).

**FRONT (opposite existential family):** there exist infinitely many `n>=1` with `S(n)=C(n)`.

**Complexity/structural implication (model-faithful).** [deduction] `C(n) <= S(n) <= O(n log n)` is the standard information/algorithmic sandwich; `SORT-BOUND-U ∈ PSPACE` is already known here (`problem.md`). Infinitely many tight `n` would rule out any eventual uniform `+1` obstruction and would constrain any all-`n` lower-bound invariant claiming a permanent gap above the leaf-count bound. Conversely a proved eventual gap would be a strong uniform structural theorem about every sufficiently large root minimax tree (still far short of, and not by itself, a separation for unary threshold complexity classes). Neither direction is implied by the known `Ω(n log n)` comparison lower bound for *sorting inputs*; that is not a lower bound for *computing* `S(n)`.

**Known evidence (literature/index).** Exact values known for `n<=22` (Wells; Peczarski; Stober–Weiß; summarized by OEIS A036604/A003070): with `g(n)=S(n)-C(n)`,

| n | S(n) | C(n) | g(n) | 2^{C(n)}/n! |
|---|---:|---:|---:|---:|
| 1–4 | 0,1,3,5 | 0,1,3,5 | 0 | 1.0000,1.0000,1.3333,1.3333 |
| 5 | 7 | 7 | 0 | 1.0667 |
| 6–11 | 10,13,16,19,22,26 | 10,13,16,19,22,26 | 0 | 1.4222,1.6254,1.6254,1.4448,1.1558,1.6812 |
| 12–19 | 30,34,38,42,46,50,54,58 | 29,33,37,41,45,49,53,57 | 1 | 1.1208,1.3795,1.5765,1.6816,1.6816,1.5827,1.4069,1.1847 |
| 20 | 62 | 62 | 0 | 1.8955 |
| 21 | 66 | 66 | 0 | 1.4442 |
| 22 | 71 | 70 | 1 | 1.0503 |

(Values `n<=22` per A036604/A003070; tight/gap points `n=12,16,17,18` per Peczarski/Stober–Weiß as in `docs/literature.md`; `n=23` open.)

**Serious attempt to DISPROVE F (eventual uniform gap).** I sought a refutation in the strong sense needed: either infinitely many `n` with `g(n)=0`, or a concrete obstruction showing no all-large-`n` argument can force `g(n)>=1`.
- [literature/experiment, repo] **No scalar/slack invariant forces or rules out an eventual gap.** `docs/research-n12-nontightness.md` (audited) records: the “efficiency” pruning is equivalent to the node-level leaf-count bound (not stronger), `m(P)` is not monotone in `e(P)` and not even a function of `e(P)` (same-`e`, different-`m` witnesses), forced balanced prefixes occur at tight `n=5,10` as well as non-tight `n=12`, and symmetry is neither necessary nor sufficient. Thus no known invariant of `n!` alone or of local `e(P)`/slack predicts tightness; this blocks the obvious routes to proving F but does **not** refute F.
- [deduction from known values] **No monotone recovery/gap pattern.** `g(n)=0` recurs at `n=20,21` after a run of gaps at `12..19`, and `g(22)=1`. Therefore: for every `N<=21`, the universal clause `∀n>=N, g(n)>=1` is false (witness `n=20` or `21`); but for `N>=23` the clause is open because `S(n)` is unknown for `n>=23`. The data refute “gap for all `n>=12`”, not eventual gap.
- [obstruction] **No disproof obtained.** A refutation of F would require exhibiting an infinite family of tight `n` (FRONT) or proving a mechanism guaranteeing infinitely many perfect root routings. I found no such family, no transferable recurrence, and no literature theorem establishing infinitely many tight cases; exhaustive/certified search evidence is finite (`n<=22`, and `S(28)>=99` only gives a lower bound, not tightness). Hence F remains open, and I cannot honestly assert either F or FRONT.

**Distinctions (as requested).** This is about the *value/structure* of the minimax function `S(n)` at the antichain root (general-poset/partial-order states appear only as reachable search states, not as an arbitrary-poset optimization claim transferred without reduction). No certificate claim is made: local/heuristic bounds on `g(n)` may be *sound* upper windows in special cases but are not, from evidence here, complete or uniform all-`n` invariants tracking exact `S(n)` (cf. `info-bound-gap-invariant-alln` / `computable-entropy-balance-surrogates` notes on board: non-certification/insufficiency barriers, not theorems).

**Mathematical finding.** [deduction from primary/indexed values] The eventual-uniform-gap claim F is **false for every threshold `N<=21`** (counterexamples `n=20,21` with `S(n)=C(n)`), while **open for `N>=23`**; combined with the non-scalar/non-monotone obstruction evidence (`research-n12-nontightness.md`, Peczarski’s `n=13` phenomenon), this leaves the infinite-tight-family question (FRONT) and eventual-gap question genuinely unresolved in both directions by current evidence.

**Failed approach / exact obstruction.** Failed/refuted routes to a decisive answer: predicting tightness by initial slack `2^{C(n)}/n!`, by any monotone function of `e(P)` or by local efficiency/symmetry, or by forced-prefix alone (all non-predictive or not globally sufficient). Exact obstruction: known `n=12` non-tightness and local failures are certified strategically/exhaustively with no published compact reusable invariant; `n>=23` values are unknown, so no finite case analysis and no known uniform invariant currently settles “infinitely many `n` with `g(n)=0`” versus “eventual `g(n)>=1`”.

**Honest limits.** No proof or disproof of FRONT/F for large `n`; no new all-`n` theorem or counterexample found; no Lean/repository changes made (nothing met the publication gate). Any claim beyond the table above for `n>=23` would be conjecture.

## Output 158 (msg_1e9764545001cEZ7x4wCNDFdm1)

**Recovery check (billy-dev).**
- Repo: working tree clean; no uncommitted changes; HEAD `6a96398`.
- No new files were added to the repository by the interrupted turn.
- Board #301: searched for my content (`"infinitely many integers n"`) — no matching post found on page 1. A failed board attempt in `/tmp/opencode/ibgi_board_result.json` ("Message author is required") appears to be from a different process/agent (`iceman-contributor-free` at 04:14Z), not this session.
- Therefore: **no external side effect from this session is confirmed** (no post, no commit, no repo change). The prior output was a text report only.

**Unfinished work.** The research task itself was completed as a text finding in the prior turn; the only possible unfinished external action is a board #301 update, but I cannot confirm it was intended or attempted by this session, so I am not duplicating it. Summary of the finding (from the prior turn) is unchanged:

- **Claim attacked:** eventual uniform gap `∃N ∀n≥N: S(n) ≥ ceil(log₂(n!))+1` (F).
- **Result:** F is **false for every N≤21** (counterexamples `n=20,21` with `S(n)=C(n)`), and **open for N≥23** (`S(n)` unknown). No proof/disproof of infinitely many tight `n` (FRONT) either.
- **Obstruction:** no scalar/invariant of `n!`, `e(P)`, efficiency, symmetry, or forced prefix predicts tightness; `n=12` non-tightness is certified only by exhaustive search with no compact reusable invariant.

If you want a board #301 post for this result, I can prepare and post it (with proper author) — otherwise this remains a clean worktree with no external action taken.
