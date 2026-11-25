# Audit: frame normalization / stronger joins at `(n,k)=(12,30)` (SoringP1 #301)

**Audit target:** `/home/lubko/soring-fronts/framed-n12-framenorm-join-20261105/docs/framed-n12-framenorm-join.md` (local note, 2026-11-05).

**Inputs read (this workspace):** `AGENTS.md`, `docs/problem.md`, `docs/research-framed-certificate-frontier.md`, `scripts/check_framed_strategy.py`; prior audit `/home/lubko/soring-fronts/audit-framed-n12-exact30-20261105/docs/framed-n12-exact30-falsify-audit.md`.

**Verdict (summary):** The note's main claims are **locally supported** by PGF/checker semantics and by reproduced fragments: C_id-loss-style joins can be rejected at `(12,30)` (O1), frame normalization (F-norm) can repair an isomorphic residual when all required downstream facts are compatible with chosen edge frames, and a non-isomorphic residual gives a reproducible constraint where no pair of edge permutations preserves all required facts in the single-poset meet. The note does **not** claim global `(12,30)` PGF nonexistence, a size lower bound, or NP/coNP/separation; that scope is appropriate. No complete exact-height-30 total-sorting PGF for `n=12` is constructed or ruled out.

Labels: `[definition]`, `[deduction]`, `[literature]` (as cited), `[experiment]` (checker reproductions below).

## 1. Baseline (checker/model)

- `[definition/experiment]` `scripts/check_framed_strategy.py` implements the PGF format from `docs/research-framed-certificate-frontier.md`: forward DAG, root `R(0)=∅`; feasible comparison adds `smaller<larger`, closes transitively, applies edge permutation; joins take bitwise intersection of feasible incoming renamed relations; leaves must totally order all pairs; depth `<= budget`. Impossible outcomes are skipped when the current relation already contradicts the outcome (`relations[v][larger] & (1<<smaller)`).
- `[literature]` `docs/problem.md`/frontier note: `S(12)=30` is literature (Wells); `C(12)=29`. PGF soundness/checkability is polynomial in explicit graph size and `n`; **no all-`n` exact-height-`S(n)` polynomial-size completeness theorem is known**. Unary `SORT-BOUND-U` is the active target; NP membership is not established by exhibiting a large strategy/certificate object.
- `[definition]` The current checker has **no disjunctive/multi-state join annotation** beyond single-poset intersection with per-edge permutations (`compare/lt/gt/leaf` only). Any "stronger join annotation beyond C_id-loss" is therefore not checker-acceptable in the existing format without changing format/checker/soundness proof.

## 2. Frame normalization and join-repair claims

**Claim:** F-norm chooses edge permutations so joined histories have compatible guaranteed posets; it can repair O1 when the required residual below the join is join-stable/isomorphic in that frame.

**Assessment:** **Supported as a local mechanism.** `[deduction]` A join is `J = ⋂ rename(R_in, perm_in)` over feasible incoming edges. Applying permutations before intersection can align equivalent facts (e.g. normalizing `1<0` to `slot0<slot1`) so the meet preserves them. This is exactly the frontier note's warning/allowance: arbitrary comparator-network joins may discard correlations if outcomes are joined immediately, but explicit frames can be used when sound. F-norm is a repair only where the *required* downstream facts become common to all feasible incoming renamed states.

## 3. Bounded F1-F3 class and checker results

The note defines a bounded C_id-loss/F-norm class with explicit fragments. Reproductions used the existing checker on JSON certificates constructed from the note's specifications.

| Fragment | `(n,k)` | Description | Expected | Reproduced (`check_framed_strategy.py`) |
|---|---:|---|---|---|
| F1/A | (12,30) | root `(0,1)`, branches `0<1`/`1<0`, join on `2<3` with identity frames, leaf | reject, loses `0,1` | `REJECT: leaf 3 does not sort 0,1` |
| F2/n3 | (3,3) | root `(0,1)` normalized by swap on `gt`; completed to total order | accept | `ACCEPT: n=3, depth=3, nodes=8` |
| F3/swap | (12,30) | non-isomorphic residuals `R1={0<1,0<5}`, `R2={1<0,0<5}`; swap repair on `gt` preserves `0v1` direction | reject (loses required relation to `5`) | `REJECT: leaf 3 does not sort 0,2` |
| F3/id | (12,30) | same residuals, identity frames | reject (loses `0v1`) | `REJECT: leaf 3 does not sort 0,1` |

**Notes:**
- `[experiment]` F1 confirms O1 is active at hard-case parameters as a concrete local constraint: the meet discards the disjunctive `0v1` fact and a total-order leaf cannot be certified.
- `[experiment]` F2 confirms checker-acceptable F-norm repair for an isomorphic/normalized residual in a small complete example.
- `[deduction/experiment]` F3 matches the note's finite constraint: preserving `0<1` and `0<5` in the meet after `p1=id` would require `p2(0)=1` and `p2(0)=0`, impossible. Thus `meet` retains only `{0<1}` under swap or only `{0<5}` under identity in that fragment; neither is sufficient for a total completion, and the checker rejects at the first missing pair it finds.
- `[not reproduced here]` The note also claims F2 at `n=4,budget=5` (`S(4)=5`, literature) is accepted with `depth=5 nodes=25`. This audit reproduced the `n=3` normalized-join completion and the F3/non-isomorphic failures; the `n=4` JSON was not reconstructed. The claim is plausible given checker semantics and F2/n3, but should be treated as **reported, not independently reconstructed in this audit**.

## 4. Can a small bounded extension at `(12,30)` be repaired?

- **Conditionally yes (bounded, checker-acceptable):** only where all required residual obligations below the proposed join are made compatible by explicit edge frames (F2-style join-stable residual). The existing checker can accept such normalized joins.
- **No for the named C_id-loss / non-isomorphic residual class:** if the meet loses a required pair (F1) or no edge-frame pair preserves all downstream-required facts in a single meet (F3/constraint), the existing checker rejects the fragment. The explicit `(12,30)` instances in the note reproduce this.
- **Stronger annotations beyond meet:** not checker-acceptable in the current format; extending it is out of scope and would require new soundness/checking arguments. No NP or global conclusion follows.

## 5. Scope assessment

The audited note's scope statements are appropriate:

- **No global `(12,30)` nonexistence claim:** correct. Fragments/F1-F3 show class-sensitive constraints, not exhaustive absence of all PGFs at exact height 30.
- **No size/lower-bound claim for `n=12` PGFs:** correct. No global search or counting argument is made.
- **No NP/coNP/separation claim:** correct. Even an accepted certificate would not imply unary NP membership without an all-`n` polynomial-size exact-height completeness theorem (frontier note, `AGENTS.md` model fidelity).
- **No `SORT-BOUND-U ∈ NP` / `∉ NP` claim:** correct.
- **Literature boundary:** `S(12)=30>C(12)=29` is cited as `[literature, Wells]`; experiments only test join/normalization mechanisms at those parameters.

## 6. Residual risks / caveats

1. **Bounded-class only:** F3 is a constructed non-isomorphic obligation pattern; it demonstrates impossibility of preserving those specific required facts in one meet, not that every exact `(12,30)` strategy induces this pattern.
2. **Checker is the oracle, not a completeness proof:** acceptance means the explicit PGF passes local checks; it does not prove optimality or global existence/absence.
3. **Reported but not reconstructed:** the complete `n=4,S(4)=5` F-norm certificate and the exact node-counted messages in the note were not fully reconstructed in this audit; F2/n3 and the constraint logic were reproduced.
4. **External obstruction dependency:** O1 motivation references an external obstruction note not re-audited here; this audit evaluates the note's internal claims against the local PGF checker/frontier docs.

**Overall:** careful local falsify/repair analysis. The frame-normalization/join-repair claims are valid within the stated bounded class and checker model; scope limits prevent complexity overclaims.
