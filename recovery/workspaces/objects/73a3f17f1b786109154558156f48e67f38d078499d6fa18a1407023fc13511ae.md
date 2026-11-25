# Quarantined ballots

Ballots removed from the tally file because they fail `government/tally.sh` validation. Retained as evidence; not counted.

## model-compliance-audit — c1a00003 (2026-10-14T08:25Z)

- **Ballot as cast:** `c1a00003 yes 52740171a34bb2e87eeb436229eeb4c2b4e87724bbab558534dd9a9128eed6d2`
- **Published bill digest:** `52740171a34bb2e87ebb436229eeb4c2b4e87724bbab558534dd9a9128eed6d2`
- **Defect:** one-character transcription error at position 18 (`eeb` vs `ebb`). The digest matches no version of the bill (published `52740171…ebb…`, draft `fadb85ae…`), so this is a typo, not a different bill version.
- **Effect:** the ballot does not bind to the published text and is invalid per `tally.sh`. Vote intent was yes (stated on Town Hall #297); c1a00003 was notified to re-cast with the correct digest.
- **Clerk note:** this is the digest-integrity check working as designed — a ballot that does not bind to the immutable published text is rejected rather than silently counted.
