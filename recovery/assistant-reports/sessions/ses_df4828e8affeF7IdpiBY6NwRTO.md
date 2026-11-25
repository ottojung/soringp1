# antonina-9O249kj17xFzJZga2ORKXJ-immense

Session: ses_df4828e8affeF7IdpiBY6NwRTO
Workspace: /home/lubko/soring-fronts/surplus-eventual-flatness-alln
Created: 1795489100239; updated: 1795489624666

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20b7d7a11001vpzJpoX8XHjE3d)

I'll start by studying the repo state: worktrees/branches, the board, and the docs that AGENTS.md points to.

## Output 21 (msg_20b7eb5ee001s5RQ2Zz6B11aWV)

We're already on `billy-dev`. Now let me read the key docs: problem definition, operations/board, and literature.

## Output 36 (msg_20b7ec0b1001TiSzXPr2qOqFb3)

Board #301 is Antonina issue #301, accessed via `scripts/board_digest.py`. Let me read the board digest and the literature + plan docs in parallel.

## Output 55 (msg_20b7ece67001v72WpTQyGnvo3C)

`research-plan.md` is under `docs/`. Let me read it, run the board digest, and look at the Sergeev asymptotic doc.

## Output 74 (msg_20b7efb01001EeIh1RenfONZBx)

We're on `billy-dev`, clean. I have the baseline: `research-plan.md` table gives S(n) for n≤11 and states exact values known through n=22. Now let me get the full board #301 digest and compute the information-bound sequence L(n) = ⌈log₂(n!)⌉.

## Output 102 (msg_20b7f9d09001c9oro8frIB34JU)

L(n) table computed. Known S values through 22 (from research-plan + board): S(n)=L(n) for n≤11; surplus +1 at 12,13,16,17,18,22; surplus 0 at 20,21; and S(28)≥99 → L(28)=98 so surplus ≥1 there. Now let me get the full board text, the OEIS sequences, and the structural-lower-bound docs.

## Output 121 (msg_20b802c01001iZNUb5dOboAEbb)

Now I have the authoritative data. Let me read the full board digest and fetch the OEIS b-files for exact values, then compute the surplus sequence.

## Output 140 (msg_20b80b07c001CBdpWLseZDKXyb)

Now I have authoritative data: `A036604` = S(n) for n=1..22 and `A003070` = L(n). Let me compute the surplus table, pull the full board posts about "surplus"/"excess" fronts, the ledger, and the Stober–Weiss paper (for S(28)≥99).

## Output 163 (msg_20b8149aa001kNKeghuj8nhzGG)

Data is now clear. Let me recompute the surplus table with the correct formula, check the literature for further exact values (Peczarski papers), and search the web for the surplus question.

## Output 182 (msg_20b822baf0016RQ7Eud8HEiHLW)

Let me retry the web search and fetch the other Peczarski papers which may contain a surplus table.

## Output 210 (msg_20b825291001TRXJQ0Qc20v3lk)

Let me grep the Stober–Weiss HTML for the "Further Experimental Results" appendix and any data on n≥19, plus retry the web search.

## Output 225 (msg_20b829d99001J1MPg8cv6ziuVd)

Let me read the Stober–Weiss appendix tables (around lines 555–635 and 855–895) for more surplus data.

## Output 240 (msg_20b82ceea001VfONQHDuN3eODU)

This appendix table is a goldmine — it has S(n) known ranges for n=23..47. Let me read the table header and surrounding text to interpret columns and the ★ marker.

## Output 383 (msg_20b853760001CVvuGkRr5lPoGe)

## Final report: `surplus-eventual-flatness-alln`

**Mathematical finding (obstruction, not a proof).** The claim "∃N: S(n)=⌈log₂ n!⌉ for all n≥N" (eventual zero surplus) is **unrefuted by certified data and unprovable by current techniques**. Two disproof attempts failed:

**Attempt 1 — data route (failed).** Known exact values (OEIS A036604/A003070): surplus Δ(n)=S(n)−⌈log₂ n!⌉ is 0 for n≤11, +1 at 12–19 and 22, 0 at 20–21. Stober–Weiß (ALENEX 2023): S(28)∈{99,100,101}, L(28)=98, so Δ(28)∈{1,2,3} — exact value open. No certified n≥19 with Δ≥2. The `excess-gap-two-alln` front (blocked) attempted the same and failed.

**Attempt 2 — structural route (failed, concrete obstruction).** The `info-bound-tightness-infinite` front suggested a Fredman lower bound S(n)≥L(n)+n−log₂ n−O(1), which would refute Claim A. This is a **misremembering**: Fredman 1976 (*How good is the information theory bound in sorting?*, Theoret. Comput. Sci. 1(4), 355–361) gives an *upper* bound S(n)≤L(n)+O(n) (constant-factor-optimal strategy), not a lower bound. Moreover, Sergeev TR20-096 Theorem 3 gives Δ=O(n/log^{1/5}n)=o(n), ruling out any Ω(n) lower bound on surplus. No structural disproof exists.

**Density question.** The surplus-1 set {n≥23: Δ=1} has unknown density; no positive-density family is known, data consistent with sparse +1s.

**Soundness vs completeness / general-poset note.** Cospectral gap results and certificate *soundness* (local L₀/L₁ rules, valid witness rules) do **not** transfer to the antichain root S(n); soundness ≠ completeness. The `excess-at-most-one-alln` front independently reached the same obstruction class.

**Honest limits.** Claim A and the density question remain open. Obstruction: absence of any lower-bound technique on Δ beyond exhaustive data; S(28) exact value open. No Lean/repository changes; worktree clean. Concise update posted to board #301 (comment sha256:oizzhAzWA32l6XXibXBszoRw_7xPlNLVuLLbUSDNAx4).

## Output 404 (msg_20b8568d00011He3qvEdcn48s5)

Recovery check complete — no duplicate action needed.

- **Git state:** clean on `billy-dev` at `6a96398`; no uncommitted changes, no commits made.
- **Board #301:** the `surplus-eventual-flatness-alln` finding post (id `sha256:oizzhAzWA32l6XXibXBszoRw_7xPlNLVuLLbUSDNAx4`, 2026-11-24T03:06:41Z) is present and unique — already landed; not reposted.
- **Task status:** complete. The mathematical finding (obstruction) and its honest limits were reported in the prior turn; no further computation, Lean, or repository work remains.

No additional action taken.
