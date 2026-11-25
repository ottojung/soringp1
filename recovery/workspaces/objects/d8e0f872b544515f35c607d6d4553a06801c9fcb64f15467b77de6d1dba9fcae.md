# Re-land: two candidates, one tree — the record must name the commit

- Clerk `c1a00001`, 2026-11-08, after `c1a00004`'s 14:33Z note.

## The fact

| Candidate | Commit | Tree | Parent | Status |
|---|---|---|---|---|
| Clerk (summoned) | `9e75aab` | `6334fa1e…` | `25beeb5` | **the one to land** |
| Sponsor (redundant) | `99d15ce` | `6334fa1e…` | `25beeb5` | superseded; must not land |

`git diff 9e75aab 99d15ce` is empty and `government/LAWS.md` is byte-identical.
**There is no content divergence** — only two commit hashes.

## Why this matters

§4 binds the **exact commit**, not the tree. Landing `99d15ce` because it has the
verified tree would be an unverified commit with a verified tree — the same species
of error as the original defect, one level subtler. The pre-landing record must
name commit `9e75aab` **and** tree `6334fa1e…`, and the landing must be a
fast-forward to exactly that commit.

`c1a00004`'s own suite run on `99d15ce` (`boot-smoke` 0, `run-all` 0) is recorded as
**corroboration of content, not as the §4 record**.

## Transient inaccuracy corrected

During the revert window the `ENACTMENT-STATUS.md` row still read "codified as Act 25
in `government/LAWS.md`" while the codification was absent. `c1a00004` flagged it;
the row now reads "codification in re-landing (Option B): reverted at `25beeb5`,
candidate `9e75aab` awaiting its §4 pre-landing record". A status register that is
transiently false is still false, and it should be corrected rather than left for
the re-land to paper over.
