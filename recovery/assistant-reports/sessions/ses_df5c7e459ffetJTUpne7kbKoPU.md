# antonina-NH31ssLTrXUKX0Tl6XjIHu-gadsden

Session: ses_df5c7e459ffetJTUpne7kbKoPU
Workspace: /home/lubko/soring-fronts/curator
Created: 1795467778992; updated: 1795467981032

Assistant-visible text only. Tool calls, hidden reasoning, user messages and credentials are excluded. Historical assertions are not independently certified.

## Output 6 (msg_20a381bdb001kFHoLBE7ZtOk3p)

I'll start by understanding the repository state, the key documents, and how to access board #301.

## Output 38 (msg_20a383dd7001inqdqARgtsfmuO)

I'm on `main` but must work on `billy-dev`. Let me switch and read the operational docs plus discover board access.

## Output 53 (msg_20a384c6a001Qj6WCX5h31g2GZ)

`billy-dev` is the execution host, not a git branch (per operations.md). Let me confirm and read the literature and frontier docs.

## Output 72 (msg_20a3862c20018I0cfIpMyUSqRY)

Confirmed: hostname is `billy-dev`. Now let me read board #301 via the digest tool and check existing candidate file/ledger.

## Output 87 (msg_20a3877e3001XR4R9oiJ84vIbd)

Let me examine the board digest interface and read the full text of the most relevant recent posts (especially the "frontier depletion" disposition).

## Output 107 (msg_20a389776001IVy6pE3UYOSFXb)

Let me read the research notes to map what's been explored and find genuinely new directions.

## Output 143 (msg_20a38f7410016lm9mzd3Yb9gyz)

Let me mine the ledger and board for existing slugs/topics to avoid duplicate investigations.

## Output 154 (msg_20a3967f5001656KY4H6lPPlx5)

The ledger is very dense (731 entries). Let me read the full "frontier depletion" disposition and dump all existing IDs to find genuine gaps.

## Output 181 (msg_20a39a4e8001D7PcrVZQMqZZLp)

The ledger has 731 entries covering an enormous space. Let me scan the board for the "frontier depletion" disposition and any recent curator outcome, to decide whether any genuinely new direction remains.

## Output 192 (msg_20a39db74001iKlbCjdihdi2I7)

Let me inspect the closest existing ledger questions to test whether my candidate directions are genuinely non-duplicative.

## Output 203 (msg_20a3a0178001LulgUPPM22pyL8)

Let me do a final targeted duplicate check for my candidate angles (sibling pairing, F-annotated decks, co-spectral pairs) before writing.

## Output 214 (msg_20a3a69e3001X9lnRuOBYvyrGS)

I've confirmed three genuinely new directions absent from all 731 ledger entries, grounded in the newest board #301 finding. Let me write the JSON deliverable.

## Output 225 (msg_20a3afe98001kMwLh8kfs8jlLz)

Let me validate the JSON, field lengths, slug format, and non-duplicate IDs.

## Output 234 (msg_20a3b1472001U6ROMJAB9gVnZL)

Done. I worked on host `billy-dev` (confirmed via `hostname`), studied `AGENTS.md`, `docs/problem.md`, `docs/literature.md`, `docs/operations.md`, the relevant research notes, board #301 (pages 1–4 digest + the 20:45Z "frontier depletion" disposition), and mined all 731 live ledger entries to enforce non-duplication.

**Deliverable:** `/home/lubko/soring-fronts/curator/frontier-candidates.json` — a single JSON object with 3 fronts, all schema-valid (slug 40–46 chars; question/falsifier/implication/basis lengths all within limits) and confirmed absent from the 731-entry ledger:

1. **`annotated-child-deck-f-completeness-alln`** — generalizes board #301's independently verified fact that the *(e,F)*-annotated child deck determines minimax F for all posets of size ≤ 7, asking whether it holds for every finite poset.
2. **`cospectral-difference-ordinal-propagation-alln`** — asks whether the verified n=7 (e,M1)-cospectral pair with F=5 vs 6 keeps its F-gap under ordinal sums/disjoint unions with antichains for all m.
3. **`annotated-deck-state-count-exponent-alln`** — asks whether the count of distinct annotated decks stays below \(2^{o(n\log^2 n)}\), a potential new lever on the exact-evaluation exponent.

**Honest limits:** Each front is framed as a question with an explicit falsifier — I claim no proof, verification, counterexample, new S(n) value, improved bound, or class placement. The two deck/structure fronts are explicitly flagged as general-poset results with no transfer to S(n) without a reduction, and soundness is kept distinct from completeness throughout.

**No external side effects:** no Lean, test, CI, ledger, commit, or board #301 post. The only working-tree change is the requested untracked `frontier-candidates.json`.
