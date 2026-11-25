# antonina-gh2hMxBEZMpogh549m75zU-deduced

Session: ses_e2cd0cabaffenYaa1GNCV9oc5f
Workspace: /home/lubko/soring-fronts/info-lower-bound-additive-gap-boundedness
Created: 1794544448910; updated: 1794553607506

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 122 (msg_1d3b98fac001uv7kVMRv316IAu)

## Scope, recovery/state, and board #301

- **Recovery check (no side effects repeated):** inspected this session/worktree only (`git status --porcelain -uall` clean; no local edits, no commits/PR actions). I did **not** post to any board, create branches/files, or run Lean.
- **Sources studied (repo):** `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, `docs/research-frontier.json`, and targeted notes including `docs/research-n12-nontightness.md`, `docs/research-structural-lower-bounds.md`, `docs/research-obstruction-next.md` (grep). Tried the local board digest (`python3 /home/lubko/soring301/scripts/board_digest.py --recent 10`); it returned recent #301 messages but **no entry matching the additive-gap front**. I cannot independently verify “current board #301” state beyond this local read-only access. `websearch` calls failed in this environment, so primary-literature claims below are limited to what is recorded/cited in-repo plus standard, explicitly labeled deductions.
- **No substantive new theorem/counterexample found; no repository changes made** (per contract).

## Front (as stated)

**Question.** Is there an absolute constant `C` such that for all `n >= 1`,
`S(n) <= ceil(log2(n!)) + C`?
- **Falsifier (i):** for every proposed `C` exhibit an explicit `n` with a *proved* value `S(n) >= ceil(log2(n!)) + C + 1` (unbounded additive gap).
- **Falsifier (ii):** prove some fixed `C` works for all `n` (uniformly bounded additive gap).

Model/notation (definition, from `docs/problem.md`): `S(n)` is the exact worst-case adaptive comparison complexity (minimax decision-tree height) for sorting `n` distinct labelled keys; `L(n)=ceil(log2(n!))` is the information-theoretic lower bound.

## Mathematical finding (honest status)

**Finding: OPEN / no resolution either way from available evidence.** `[literature]+[deduction]`

1. **Established sandwich (literature, recorded in repo):** `L(n) <= S(n) <= O(n log n)` for the exact sorting number; exact values known for `n <= 22` with recorded additive gaps `g(n)=S(n)-L(n)` equal to `1` at `n=12` and at `n=16,17,18` and `0` at the other recorded points in that range (Stober–Weiß ALENEX 2023, as summarized in `docs/literature.md`/`docs/problem.md`). This is **consistent with** bounded gap (even `C=1` on known data) but is only finite evidence and does **not** imply any all-`n` constant.

2. **No recorded all-`n` theorem:** neither a proof of a uniform constant `C` nor a proof that `g(n)` is unbounded is recorded in the studied docs/board digest. I found no argument in-repo that settles this front. `[literature/repo survey]`

3. **Complexity/context (deduction from `AGENTS.md`/`problem.md`, not a separation):** a uniform additive bound would be a strong structural tightening of the `Theta(n log n)` sandwich for `S(n)` itself (it would pin the exact optimum to within `O(1)` of `L(n)` for all `n`), relevant to how tightly the information bound characterizes the minimax value. It would **not** by itself yield NP/coNP membership, a succinct certificate, or a uniform algorithmic speedup for evaluating `SORT-BOUND-U` beyond what is already known, because `S(n)` is the function value, not a checkable witness; conversely, unbounded gap would rule out constant-additive optimality of the information bound as a universal target. No complexity-class separation follows in either direction.

## Falsification attempts (serious, paper-level)

### (i) Attempt to disprove boundedness (exhibit/prove unbounded `g(n)`)

- **Finite exact data:** `g(n) in {0,1}` for all exactly-known `n <= 22` gives no growing witness; cannot supply any explicit `n` with proved `g(n) >= C+1` for `C >= 1`. **Fails as falsifier.** `[literature]`
- **Asymptotic upper bounds as proxy:** standard uniform sorting algorithms give comparison counts `n log2 n + Theta(n)` in magnitude, hence additive excess over `L(n)=n log2 n - Theta(n)` of order `Theta(n)` for those algorithms — but this is a property of *specific algorithms*, not of the optimum `S(n)`. It cannot witness `S(n)-L(n) -> ∞`. **Not a disproof.** `[deduction, model fidelity]`
- **General-poset/local-gap intuition:** `docs/research-n12-nontightness.md` (and related obstruction notes) shows the obstruction is structural/non-scalar: local/node information bounds can fail and `m(P)` is not monotone in `e(P)` even for small posets (e.g. same `e`, different minimax cost; merge factors with `m(P)>ceil(log2 e(P))`). However, these are **general reachable/poset states**; transferring a local or infinite-family poset gap to the fixed root family `S(n)=m(antichain_n)` for all large `n` requires an all-`n` strategic argument that every optimal (or every) tree is forced through such states with accumulating deficit. No such root-forcing theorem is established. **Insufficient to refute boundedness.** `[deduction; distinction: general-poset/local ≠ root S(n)]`

**Outcome:** no proved unbounded-growth witness or theorem found.

### (ii) Attempt to prove boundedness (exhibit fixed `C`)

- **Proof from known exact values:** impossible (finite range). `[deduction]`
- **Proof from an explicit all-`n` algorithm with constant additive overhead:** would require, for every `n`, a uniform/explicit comparison strategy (or a certified decision tree argument) of height `<= L(n)+C`. No such strategy/certificate is known; the repo records only `O(n log n)`-type algorithmic upper bounds at the problem level and sharper but still non-constant-additive-in-form bounds are not established here. I did not find a reusable invariant implying a global constant surplus. **No proof obtained.** `[literature/repo survey]`
- **Certificate/soundness vs completeness:** exhibiting one tree of near-optimal height for some `n` is a *sound* upper-bound witness for that `n` only; it gives no completeness/forall-`n` guarantee. Conversely, pruning/efficiency arguments (e.g. in n=12 analyses) are sound lower-bound obstacles for a fixed budget but, as noted in `research-n12-nontightness.md`, are equivalent in force to leaf/information constraints at the node level and do not by themselves yield a uniform additive lower bound over all `n`. **No all-`n` boundedness follows.** `[deduction]`

**Outcome:** no fixed-`C` theorem found.

## Exact obstruction

The decisive gap is **strategic and global**: `g(n)>0` at the root means that for height `L(n)+C` the information/efficiency necessary conditions cannot be satisfied along *every* root-to-leaf line of any single adaptive tree simultaneously (a quantified, all-strategy obstruction), yet for general posets the minimax cost is non-scalar (not determined by `e(P)` alone) and locally non-tight states do not force a global root gap. Therefore:
- to **falsify boundedness** one needs an all-`n` (or infinitely many explicit `n`) **adversary/forcing invariant** sound against every sorting strategy at the antichain root that accumulates `>C` deficit — none known;
- to **prove boundedness** one needs an all-`n` **constructive strategy or inductive invariant** whose height tracks `L(n)+O(1)` — none known.

Finite computation (exact `S(n)`) is currently feasible only for small `n` and has not revealed growth; asymptotic algorithmic upper bounds are too loose (additively) and do not control the optimum. This is the concrete barrier, not resolved here.

## Limits of this report

- No new proved value of `S(n)`, no new all-`n` bound, and no counterexample family; result is a **negative/inconclusive** front analysis. `[deduction]`
- Could not fully audit live board #301 beyond the local digest, and could not fetch external web sources in-session; claims about “no theorem recorded” are relative to studied repo docs + digest results and the in-repo literature baseline (esp. Stober–Weiß for `n<=22`).
- I did **not** run new exhaustive searches or attempt reproduction at larger `n` (and prior notes indicate pure-Python forward search does not reach `n=12`); no experiment discriminated the all-`n` question here.
- Per `AGENTS.md`, this is **not** a basis for Lean/repo changes. A genuine advance would require either (ii) a checkable all-`n` constant-additive strategy/certificate or (i) a proved infinite family (or theorem) forcing unbounded root deficit, each with a full paper argument against the root quantifier and model.

## Output 151 (msg_1d3bacf0a001DYqPCWUyMsNkS7)

Recovery check complete. The worktree is clean, there are no `*301*` task files, and the latest commit is unchanged. The board digest search found no “additive gap” post on page 1; the prior turn explicitly reported that it did not post.

The mathematical report was already delivered in the conversation. No external action is confirmed or needed, so I made no changes and did not post.
