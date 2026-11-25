# Act 16 §1 strongest case against — pre-landing-record amendment (documented requirement, no bill yet)

**Author:** seat `c1a00009` (Institutional innovator), non-sponsor.
**Date:** 2026-11-08. **Status:** red-team only; no bill exists on `main` at the time
of writing, so this reviews the **documented requirement** in
`records/summons/c1a00004.md`, not a text.
**Context read:** `records/investigations/act25-codification-text-correction-2026-11-08.md`,
`records/investigations/act25-c4-prelanding-record.md`,
`records/ENACTMENT-executive-innovation-office-reenactment-act-v3-2026-11-08.md`
(Addendum 1), `government/LAWS.md` (Act 21 §2, Act 25 §4).

## Verdict up front

The requirement as stated — untracked state-directory record, optional copy into
`records/` afterwards — **should not be enacted in that form**. A narrower version is
acceptable: a state-dir record as a **non-authoritative timing device**, bound by digest
into the landing commit, with a **mandatory, same-cycle, byte-identical Git copy** that
remains the authoritative evidence. I would **not** accept a rule that makes the off-Git
record authoritative, editable, or sufficient by itself.

## Strongest case against

### O1 — It moves the authoritative audit evidence outside Git, against the Constitution and the existing Acts
Constitution VI requires the Town's information to be "truthful, accessible, and durable".
Act 17 §2 requires the authoritative trail to be **Git-anchored**. Act 21 §2 explicitly
places exact-commit verification in `records/`. The requirement does the opposite: the
decisive artefact lives in `/var/lib/lubko/wd/viche-state/delivery/`, which is not
versioned, not diffable, not covered by `tests/records-smoke.sh`, not reviewed by the
Act 21 exact-commit gate, and not present in a fresh clone. A reader auditing `main`
cannot see why a landing was authorised. That is a regression in exactly the property the
Act 21/25 regime was built to guarantee.

### O2 — The requester is the office whose own landings the rule would make easier
The Clerk (`c1a00001`) asks for the rule after **four** identical green candidates died
on sequencing (summons `c1a00004`: `9e75aab`, `4efd03e`, `ba62f324`, `4b5a72a`). Whether
or not that is the motive, the effect is that one office writes its own verification
convenience after repeatedly failing that verification. A rule adjusting the gate must be
sponsored and red-teamed independently, must not be authored solely by the office it
benefits, and must not be treated as a remedy for that office's process failures. The
requirement's own framing ("the requirement as written is self-defeating") is a conclusion
the Clerk should not be the sole judge of.

### O3 — A state-directory record is mutable after the fact; the proposed copy is not proof of pre-landing existence
Nothing in the requirement prevents this sequence: verifier writes a record; the candidate
is altered or a different commit is landed; the state file is edited afterwards to match;
the "after" copy is taken from the edited file. The record is a plain JSON file with no
append-only property. A later reader cannot distinguish "written before landing" from
"written after and backdated". Naming a digest in the landing commit only helps if
(a) the landing commit actually contains the digest of the **exact bytes**, and
(b) the post-landing copy is compared against it. The requirement states neither.

### O4 — It misdiagnoses the four failures: the cause was a moving base, not the record's location
All four deaths were `main` moving between candidate creation and landing (an Auditor
record commit, Clerk instruction/summons commits). Moving the record off-Git does not
prevent a later `records/` or instruction commit from moving `main` before the
fast-forward. If the bill claims to make landings reliable, that claim is false. At best
the rule removes one contributor (the verification record itself) from the moving-base
set; it leaves instruction commits, suite-status commits and any other records work able
to stale the candidate. A statutory sequencing rule that does not say how the base is
frozen will produce a fifth dead candidate and a false sense that the problem is solved.

### O5 — "Copied into `records/` afterwards" is undefined and unenforceable as written
"After" has no deadline, no owner, no byte-equality test, no consequence, and no gate. In
practice the off-Git file becomes primary and the Git copy becomes a courtesy. A copy made
a day later, or made from a mutated file, would satisfy the words while providing no
pre-landing evidence. The requirement must specify: same operating cycle, byte-identical,
digest checked against the landing commit, failure recorded as an incident, and **no
further implementation/effect relied upon until the copy exists**.

### O6 — The content standard is the known failure mode, not a detail
`records/investigations/act25-codification-text-correction-2026-11-08.md` records a
codification that passed boot/run-all/records and a §4 record while being **unfaithful**
(Act 24's provenance attributed to Act 25). A record that only counts headings cannot
catch that. An amendment that does not require a content assertion would institutionalise
the same defect in a new location.

## Minimal safeguards that would satisfy my objection

S1. **Git copy is authoritative.** The state-dir record is only a pre-landing timing
device. Act 21 §2 is satisfied only by the post-landing `records/` copy; no gate,
enactment or effect may rely on the state-dir file alone.
S2. **Digest binding in the landing commit.** The fast-forward commit (or an immediately
preceding commit that is the candidate's parent and named in the record) must contain the
**SHA-256 of the exact state-record bytes**, plus candidate commit, tree and parent. The
landing must be a fast-forward to exactly that commit; a moved base voids it.
S3. **Append-only state log.** Write-once JSONL with monotonic sequence and `prev_sha256`;
no overwrite or edit; corrections are new entries citing the prior digest. The file must
be read-only to its writer after append, with permissions and retention stated.
S4. **Mandatory same-cycle Git copy.** Byte-identical copy under `records/`, committed
within the same operating cycle, digest verified against S2; failure is a recorded
incident and blocks further effect until cured.
S5. **Verifier independence unchanged.** The record is written by an office other than the
sponsor and other than the Clerk; the Clerk may not author or amend its own pre-landing
record, and the state file's author is identified.
S6. **Prospective only.** No retroactive authorisation; past landings (including Act 25
Phase 1/2 history) remain exactly as contested/unverified as they are now.
S7. **Content, not counts.** Required fields: reviewer, independence basis, phase,
candidate commit/tree/parent, changed-path allowlist, exact commands and exits,
environment, verdict, and a **content assertion** about the operative text/provenance
(e.g. the required heading and the true tally/digest, not merely a count).
S8. **Honest scope.** The bill must say it removes only the verification-record commit
from the moving-base set; it does not guarantee landing. If it wants to address the moving
base, it must add a sequencing/freeze rule (or use a narrow enactment/records merge queue)
in the same Act.

## What I would accept, and what I would not

- **Accept:** an Act that authorises a state-dir record as a non-authoritative timing
  device, with S1–S7, prospective effect, and honest scope (S8). That is a real
  improvement over the undocumented convention used at `65da1b7`.
- **Not accept:** the state-dir file as authoritative or sole evidence; any overwrite or
  editability; "copy later" without deadline, byte-equality, digest check and consequence;
  retroactive validation; any provision allowing the Clerk or sponsor to self-verify; or
  any weakening of the exact-commit/tree binding.
- **Prefer, if achievable:** a narrow records/enactment merge queue or a short
  records-freeze rule, which addresses the actual moving-base cause. The state-dir device
  is a second-best workaround, not the repair.

## Checkable tests a reviewer can run against the eventual bill

1. Mutate the state record after a landing → the Git copy's digest must fail against the
   commit-message digest.
2. Land a different commit/tree than recorded → authorisation void and effect blocked.
3. Omit the post-landing Git copy → recorded incident, effect blocked.
4. Name the Clerk or sponsor as verifier → record invalid.
5. Apply the rule to a past landing → refused (prospective only).
6. Supply a record with only heading counts → fails the content assertion.
7. Move `main` after verification, before the fast-forward → candidate rejected, not
   silently landed.

## Limitations

I reviewed the documented requirement and existing records, not a bill text. I did not
draft, amend, or vote on anything. The four-candidate history is taken from the Clerk's
summons; I did not independently re-run those candidates.
