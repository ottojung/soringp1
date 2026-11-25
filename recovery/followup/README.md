# Follow-up recovery and coverage audit

On 2026-11-25, after the initial 77 recovery commits, a second audit checked
for omitted, untracked, staged and unreachable research material. The
original archive and these additional discoveries are on the default branch.

## Coverage and provenance

| Audit | Results |
|---|---|
| [Git references and reflogs](git-audit.json) | 43 additional relevant historical patches; unrelated Viche history excluded |
| [All SoringP1 Git object inventories](orphan-audit.json) | 784 Git stores, 777 distinct inventories; zero additional unaccounted commit objects; six orphan draft blobs recovered from the central store |
| [Dangling objects](dangling-drafts/audit.json) | Five additional abandoned staged or dangling drafts, all preserved |
| [Physical text files](file-audit.json) | 131,989 candidate text files; 142 additional provenance mappings, five unique new content files |
| [Research ledger](ledger.json) · [Earlier variants](historical-ledger-versions.json) | All 750 recorded fronts, with two superseded ledger versions retained |
| [Antonina issue coverage](board-audit.json) | 88 open and 379 closed issue titles checked; two SoringP1 research issues identified, already archived |
| [Scratch references](scratch-reference-audit.json) | 570 missing exact paths, 14 candidate filename matches, no confirmed recovery at the original paths |
| [Mixed-session scan](mixed-reports/README.md) | 27,033 candidate assistant messages checked; 1,540 distinct relevant texts archived |
| [Historical task texts](task-commissions/README.md) | 1,386 distinct commissions, 1,710 retained occurrences |
| [GitHub discussions](github-discussions/README.md) | Four issue bodies and all 16 returned comments copied into the archive |

The machine-readable audit records retain source paths, identifiers, checks
and exclusion reasons. Objects are deduplicated by sanitized content. The
[search tools](../tools/README.md) verify their integrity and provide access
to the complete [catalogue](../catalog/README.md). The data are historical;
the archive is not a fresh independent proof review.

## Known limits

- Original files that were deleted before recovery cannot be recreated
  from an absent path. Related reports may still record their findings.
- Some references are examples or placeholders. A matching filename alone
  is not evidence that two source files have identical contents.
- The workspace snapshot stores changed and additional text, not all
  baseline files or runnable copies of every historical checkout.
- Historical Git patches preserve textual changes and commit provenance.
  They are not a claim that all original commits are ancestors of main.
- Large regenerable inputs, binaries, build outputs, credentials, hidden
  reasoning, unrelated projects and generic operational messages are out of
  scope. Mixed-session selection is heuristic, so completeness is limited
  to the identifiable material under the recorded criteria.

See [results and evidence status](../RESULTS.md) and [corrections](../CORRECTIONS.md)
for mathematical interpretation. No suspended research work was resumed.
