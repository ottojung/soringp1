# antonina-poE2rc0aJ7K25ZoKVjMYWb-category

Session: ses_dff21a4cdffeK1uxhfgqjc9VtV
Workspace: /home/lubko/soring-fronts/tightness-density-zero-alln
Created: 1795310902188; updated: 1795311627057

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_200de605f001Ezqyi6PNsZfA8I)

I'll start by checking the environment, the research board location, and the core docs.

## Output 29 (msg_200de7f43001Vee23dahUSoFg7)

On billy-dev as required. Let me read the board #301 digest and the literature notes.

## Output 48 (msg_200de969a001EQ7wGmdF3YQb09)

Now let me look at the frontier ledger, the existing scripts/docs, and search for prior work on tightness/excess.

## Output 105 (msg_200e19b00001kdYQj1U0cXuMXD)

I'm on `billy-dev`. I have the layout now. Let me check the board-posting mechanism and start the literature lookups (Fredman 1976 on the information-bound gap; OEIS sequences for the exact sorting number).

## Output 132 (msg_200e42b87001e65amFxB0pVZLs)

Server restarted — continuing from where I left off. My work so far is read-only (studying docs, computing `L(n)=ceil(log2(n!))` tables); nothing was committed or posted. Let me resume: check the board-posting interface and rebuild the tight-set data table.

## Output 147 (msg_200e571c200196pJYiNyWxQ4zm)

Script bug — the tight-set list used the loop variable `t` instead of calling `tight(n)`. Fixing, and checking the board `comment` interface.

## Output 171 (msg_200e595e90011Ww4SeloiHnCbf)

Data table confirmed: known tight set through 22 is `{0..11, 20, 21}` — 13 of 22 integers in `[1,22]`, δ(22) ≈ 0.59; non-tight with excess ≥ 1 at 12,13,15,16,17,18,19,22 (n=14 unknown). Now let me skim the construction/lower-bound tools for attack ideas, then do the disproof and proof attempts.

## Output 195 (msg_200e7d8b5001wqE9faq13R5SZm)

Now the board update. First verify no prior post from this front's author/tag exists (recovery caution), then post one concise update per operations doc.

## Output 249 (msg_200e8e88e001VTR0sMvxlLWuSy)

Done — here is the report.

## Attack on the front `tightness-density-zero-alln`

**Claim attacked (horn B):** `limsup_{N→∞} δ(N) = 0` — tightness is asymptotically sparse. Falsifier's other horn: exhibit an infinite tight sequence with `|T ∩ [1,N_i]| ≥ c·N_i` (`c>0`, `N_i→∞`).

### Data (experiment; sources: docs/literature.md, research-certificates-barriers.md, research-n12-nontightness.md, kernel-results.md, research-state-compression.md, Wells/Kasai/Jing/Stober–Weiß values)

Known tight set through 22: `{0,1,…,11, 20, 21}` — `|T ∩ [1,22]| = 13`, so `δ(22) ≈ 0.591`. Non-tight with excess ≥ 1 at `{12,13,15,16,17,18,19,22}` (n=14 unknown). **S(n) exact only for n ≤ 22; n ≥ 23 is open** (research-certificates-barriers.md).

### Disproof attempt (horn A) — failed, obstruction documented

- **Computational:** nothing to exhibit — S(n) is open beyond 22, so no data past the horizon can be generated or falsified here.
- **Structural families** (attack.py): `n=2^k` tight at {1,2,4,8} but **16 non-tight**; `n=2^k−1` tight at {3,7} but **15 non-tight**; `2^k+1` tight at {3,5,9} but **17 non-tight**. Runs of tight/non-tight: tight `[1,11]`, non-tight `[12,19]`, tight `[20,21]`, non-tight `[22]`. No law of recurring tight windows; the second window is followed immediately by a non-tight value.
- To succeed one must prove `S(n)=L(n)` for infinitely many `n` with **positive lower density** — i.e. exhibit a positive-density sequence of optimal trees attaining the information bound. No construction or mechanism is known.

### Proof attempt (horn B) — failed, obstruction documented

Deduction (all n ≥ 2): **`T` is tight at n ⇔ there is a root comparison `(i,j)` plus two decision trees of height `L(n)−1`, each sorting exactly the `n!/2` inputs `{σ: i<j}` and `{σ: j<i}` respectively** (root split is forced to be `n!/2 + n!/2` by the bijection between `{i<j}` and `{j<i}`; classic info bound gives child height `≥ ⌈log₂(n!/2)⌉ = L(n)−1`; tightness forces `= L(n)−1`).

Obstructions: (1) Literature: "the sharper behavior (including whether the excess is unbounded) remains open" (research-certificates-barriers.md, citing Sergeev's `O(n/(log n)^{1/5})=o(n)` surplus) — the frequency of zero excess is not bounded anywhere; (2) non-tight clusters exist at 12–19 and 22, so any density-0 theorem must overcome real gaps; (3) the tight-tree condition is strong but admits no frequency law derivable from data.

### Honest limits

- `S(n)` open for n ≥ 23; density of `T` beyond the data horizon is unknown. **Both horns unattained: no constant-density tight sequence exhibited; no sparsity proof derived. The front remains open at the data horizon.** Process success is not confusion with resolution — this is an obstruction report, per the publication gate (no new theorem or counterexample).
- Scratch: `/tmp/opencode/tightness/{data.py,attack.py,attack.md,post.txt}`; no Lean/repo changes; worktree clean.

### General-poset results / certificate soundness vs completeness

The density of `T` concerns the **antichain minimax** `S(n)` — whether exact trees exist attaining `⌈log₂ n!⌉` at sizes n. General-poset results (S(12)=30 > 29, Wells; the local hypotheses H1–H6 of research-n12-nontightness.md) are poset-level statements that do not transfer to the global density of `T` without an encoding-preserving reduction. Certificate *soundness vs completeness* (board fronts `fo-tc-policy-interpreter`, `sortboundu-conp-membership-alln`) is a different question — about sound verifiers vs complete NP/coNP-style certificate families for SORT-BOUND-U; a tight tree is the completeness side (an actual optimal tree exists), not a certificate-soundness claim.

### Board update

Posted once to **Antonina issue #301** (author `SoringP1 researcher: tightness-density-zero-alln`, 2026-11-22T01:39:18Z; verified: exactly 1 hit on pages 1–3). Per AGENTS.md evidence labels: data `[experiment]`, tight-tree equivalence `[deduction]`, literature sources `[literature]`, unattained horns `[open]`.
