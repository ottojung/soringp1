# antonina-RVlDky2cJr4121wIdzeRsV-moods

Session: ses_df6adc281ffekqNQyn4M1ugLLO
Workspace: /home/lubko/soring-fronts/excess-sequence-regularity-unary-p-alln
Created: 1795452714436; updated: 1795453975050

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 13 (msg_20959ac8c001cMB6baYTv12zbV)

I'll start by carefully inspecting the current state — git status, the key documents, and any durable task records — before doing anything else. This is important because of the warning about a possible interrupted turn with external side effects.

## Output 28 (msg_20959e9c1001J04M2T4Cevg50Z)

Good — we're on `billy-dev` with a clean worktree. Let me read the key documents and find the board record.

## Output 47 (msg_2095a02110015b5i4mZzbjWG2U)

Let me check the research board digest and the durable ledger for this front, plus the repository structure.

## Output 66 (msg_2095a35230013FhaCIs0gZB4lj)

Let me search the ledger and the board for this specific front to see if anything was already done (recovery audit).

## Output 85 (msg_2095a830c001fHJ3qKH77VYR28)

The ledger shows my front `excess-sequence-regularity-unary-p-alln` as `running` with no finding recorded, and the board has no post under that slug. Let me complete the recovery audit: check scratch space, git reflog/stash, and search all board pages for any post from this front under other keywords.

## Output 104 (msg_2095b0a2b0016HrAZ55N7KrTEm)

The digest only searches page 1. Let me check its options and search all pages, plus locate the referenced barrier notes ("k-regular-sorting-number", "nonholonomy") which may live in other front directories.

## Output 119 (msg_2095ba45b001FLkwB5VzGdsByS)

Found the barrier notes. Let me read them and scan all board pages for any post from this front (to complete the recovery audit).

## Output 138 (msg_2095da6c0001lZbsyKe3mRFJGd)

Let me check the board data source directly (faster than 75 Python invocations) and look for scratch files from this front.

## Output 166 (msg_2095e6a890018l6uDoX2xlEUpw)

Recovery audit is clean: no prior board post, no git/repo changes, no scratch files from this front; the ledger entry is still `running` with no finding. Nothing to repeat. Now I'll study the remaining primary/literature basis and attack the mathematics.

## Output 194 (msg_2096189ad001g0wiP4sfGxLmZX)

Let me compute the exact known excess values and run a small sanity experiment, and check whether the P-recursive collapse lemma is already in the literature.

## Output 231 (msg_2096296140012OIZ2u8FEx0Nms)

The mathematics is now clear. Let me verify the posting mechanism (from a prior front's scratch) before making exactly one board post at the end.

## Output 255 (msg_20963a80a0010hztSGoYHBBd2l)

I have everything needed. Let me write up the finding carefully and make exactly one board post. First the scratch draft, then the single post with verification.

## Output 275 (msg_20964bb2c001GdgXgePg6VHGHR)

Post succeeded. Let me verify exactly one comment landed with my author tag.

## Output 295 (msg_20964f930001NoViByk3dHL828)

## Recovery audit (done first)

| Effect | Status |
|---|---|
| Git / repo / Lean / CI / ledger | Untouched — clean at `6a96398` on `billy-dev` |
| Prior board post from this front | None existed (all 75 pages scanned for the slug/keywords) |
| Prior scratch files | None from this front |
| My external writes this turn | **Exactly one** #301 comment (verified live, `2026-11-23T17:11:51Z`) |

The front was claimed at 16:51Z and no side effect had actually happened, so there was nothing to repeat.

## Mathematical finding

**1. New all-n theorem (paper deduction): the P-recursive horn collapses to eventual periodicity.**

For any integer sequence with `a_n = o(n)`, P-recursive ⟺ eventually periodic. Proof: if `G(z)=Σa_n z^n` is D-finite and not a polynomial, integer coefficients plus `o(n)` give radius exactly 1; Polya–Carlson then forces rationality (natural boundary is impossible for a D-finite function). Rational GF ⟹ eventually an LRS; `o(n)` kills all roots with `|λ|>1` and all unit-circle roots with polynomial degree ≥1, so the sequence is bounded; a bounded integer LRS has finite state space and is eventually periodic. Converse is trivial.

Applied to `D(n)=S(n)−⌈log₂ n!⌉` (integer, `o(n)` by Sergeev + information bound): **D is P-recursive iff D is eventually periodic (hence bounded).** So proving `D` unbounded or non-periodic would refute that horn outright. This uses no exact `S(n)` value and is *not* a corollary of the repository's non-holonomy theorem, whose `c·n log n` leading term cancels in `D`. It also shows the horns are genuinely inequivalent: `s₂(n)` is 2-regular, `o(n)`, unbounded, non-periodic, so k-regularity does not collapse; p-automaticity forces boundedness only under the finite-alphabet reading, not the weaker `D mod p` reading.

**2. Why the existing barriers provably cannot settle D.** The k-regular proof of `S` needs the transcendental constant `−1/ln 2` in `S(k^m)/k^m`; for `D` that limit is 0 (algebraic). The non-holonomy proof needs `S(n)~(1/ln2)n log n`; `D=o(n)` permits a rational GF with bounded coefficients. Both methods are silent on `D`.

**3. The proposed falsifier is invalid.** Sergeev is an ineffective one-sided upper bound — an `o(n)` bound cannot force unbounded k-kernel dimension. Finite data cannot either: `D(1..22)=0000000000011111111001` is trivially fit by an eventually periodic (hence P-recursive, k-regular, automatic) sequence. "Fits every known value" is a soundness check, not an all-n correctness proof, so that converse criterion is vacuous.

## Concrete obstructions / honest limits

I tried and failed to refute k-regularity via kernel-subsequence LRS growth (Sergeev permits `k^{γm}`, `γ<1`), Polya–Carlson directly (removed by `o(n)`), deriving unboundedness from Sergeev (one-sided — the Nov-22 fallacy), and Cobham-style two-base attacks (no second hypothesis). The exact obstruction: the only published lower bound is the information bound itself; no ω(1) additive lower bound on the excess is known, the infinitude of positive excess is open, and `S(23)` is unknown. **Neither horn was settled** — no representation was found and no barrier was proved; `SORT-BOUND-U` remains open, with no new placement or separation. No Lean or repository changes were made; scratch only in `/tmp/opencode`.

## Output 307 (msg_209655c1d001h1JSRdTTIcBpgS)

No unfinished work; no actions taken. State is unchanged from the audit I just reported:

- **Git/repo**: `billy-dev` at `6a96398`, clean working tree, no commits/stashes/Lean/test/CI/ledger changes.
- **Board #301**: exactly one post from `SoringP1 frontier: excess-sequence-regularity-unary-p-alln`, at `2026-11-23T17:11:51.769Z` (page 1). No duplicate.
- **Scratch**: draft/result in `/tmp/opencode/excess_regularity_post*`; no other side effects.

The front is not resolved mathematically (neither horn proved/disproved), but all reporting/side effects for this turn are already complete and nothing should be repeated.
