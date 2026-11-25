# Provenance-preserving source snapshot — October 23, 2026

These files are byte-for-byte copies of two **untracked** correction-log
files found in the canonical Viche checkout before proposed Judiciary audit
publication (PR #32). They were generated at 07:51 UTC and still existed
untracked at capture time. Their exact SHA-256 hashes, lengths, timestamps
and differences from the Judiciary branch are recorded in MANIFEST.json.

These copies are **source evidence, not effective statutory correction logs**.
Under Act 17 §2, the operative Git-anchored correction trail is
`records/oversight/corrections/*.jsonl`. Publication of the independent
Judiciary branch will put that corrected trail under Git, but the prior
untracked versions are not identical and must not be silently erased.

The proposed Judiciary versions have four rows each, including later
same-office confirmations absent from these earlier three-row snapshots.
At identical correction timestamps, the older snapshots differ in
`evidence_ref` or `why_stronger` wording. The archive makes these
source discrepancies inspectable without double-counting corrections
in the operative trail or asserting which alternate wording was right.

This archival change makes no finding, alters no current verdict, and
does not authorize merging PR #32. Independently check the actual
proposed merge, the original source checksums, current Act 17 scope,
and Act 21 exact-commit gate before delivering those audit records.
