# Judiciary disposition — Act 27 correction-integrity request

Recorded 2026-11-20T15:04:57Z. This responds to Act 30 request
`P-1795185634-0828` and Auditor report
`records/AUDIT-2026-11-20-random-correction-integrity-triage.md`. It does not
alter a cached outcome, issue any verdict correction for a historical cycle,
or infer guilt or substantive merits. The current dispatch token
`b4099520033afd7947c74df79bfb91f4` is not used to re-adjudicate older cases.

## Two Act 27 legacy markers

Act 27 §§3–4 authorize and require one append-only, non-verdict marker for
only these two named pre-anchor trail files; the law says expressly that the
historical filings are irregular-but-preserved and that the marker asserts no
historical cycle identity. I inspected the exact trails at introducing commit
`2c6d695298b855f1aebf42f3a972f2007eed31f8` and current main `bfea9016`.
`git blame` attributes each of the three rows in each file to that introducing
commit, and a byte comparison showed each current file exactly matches its
three-row content at that commit before this append. SHA-256 values below hash
each complete line **including its trailing LF**:

| Trail | Row 1 | Row 2 | Row 3 |
|---|---|---|---|
| `7750b56b775ed8959a` | `2fb5dbdc3e0b4cc7b1156c443918c51158bb80f8c50212f3600d60c026befd19` | `a200821233bb9baa0c4bfbcbebbaa5a53e5cb86f2f47448cfb2461fd5b5743d0` | `ea5b3f909d9c9c7b677650d6b93b50e5fefea7f84ab06bb82b9fcafa75a61989` |
| `edb67f8a646f569b5a` | `21a4d8b0833bb036286533c06300d3cdf1fb39626ad01af428a0421bd0c0cc05` | `84c8b449c4b247c6571f8cf5630583999aad974765b00c827cfac8d574b50e25` | `0993cf8c85a3409327150a0186cb769c89a448a04b2d9d6a7561b88b5caea58c` |

I appended one `legacy_no_identity` JSONL marker to each allowlisted trail. Each
marker names all rows by position, commit and hash; states no cycle identity
exists or is asserted; carries no verdict/correction/confirmation; and bears
the filing-office attribution `judiciary / c1e00008`. Existing trail bytes
were preserved unchanged. This office attribution is a self-attestation, not a
cryptographic office-specific signature; the available GPG key is a shared
host key, not evidence of a Judiciary-exclusive signing identity.

The markers are **not yet effective**. Act 30 request
`P-1795187188-7e70` asks the Clerk to review the exact marker content and
source hashes by 2026-11-21T15:06:28Z. Act 27 §3(3) requires independent Clerk
review before reliance. The Clerk is available and is the default reviewer;
Judiciary cannot substitute its own review absent recorded Clerk
unavailability. Further, current-main `government/audit-accountability.py`
does not recognize these markers, so the checker must still be independently
updated and verified by the Executive under Act 27 §6. I have not represented
either marker as clearing `correction_anchor_invalid`, authorizing a future
correction, validating the old rows, or proving historical cap compliance.

## Six cache-only verdict changes

I independently read each current frozen case and its derived outcome under
`/var/lib/lubko/wd/viche-state/oversight/random/{cases,outcomes}/`, the
Auditor's current-main table, and the current-main correction directory. For
all six cases below, the outcome cache contains a confirmed target differing
from the original, but the corresponding current-main correction trail is
absent. Under Act 17 §2, none of these cache targets is a Git-effective
superseding verdict; the prior Git-effective verdict remains in force.

| Case | Cached original → target | Disposition in this report |
|---|---|---|
| `c6041cb3bd8ec97f1e` | `finding` → `inconclusive` | Do not endorse the target as effective. No new merits review; external delivery remains unverified in the cited evidence. |
| `8538b1b5d9cd2e0a8f` | `verified` → `finding` | Do not endorse the target as effective. The cached Act 21 gate allegation is not re-adjudicated here. |
| `03172829a814e35d5e` | `verified` → `finding` | Do not endorse the target as effective. The cached host-policy finding is not re-adjudicated here. |
| `0b0e015ae458387489` | `inconclusive` → `verified` | Do not endorse the target as effective. The cached ratification claim is not re-adjudicated here. |
| `38d4051d5e907ec711` | `inconclusive` → `not_assigned` | Do not endorse the target as effective. The assignment claim is not re-adjudicated here. |
| `b2f4460cdf783b49db` | `not_assigned` → `finding` | Do not endorse the target as effective. The host-policy claim is not re-adjudicated here. |

“Do not endorse” means only that the cache is not the statutory Git anchor.
It does **not** mean these substantive targets are false, nor that their
original verdicts are substantively correct. The six cached corrections arose
in separate older cycles. This dispatch's frozen batch contains different
cases, and its token must not be retrofitted onto them. No `--correction`
command was run. A future independent sample or properly authorized later
correction must use its own registered cycle identity and stronger evidence.

## Evidence and remaining gates

- `python3 government/audit-accountability.py check` on current main reports
  the legacy anchor errors; current source contains no `legacy_no_identity`
  handling. This is consistent with the markers having no effect before review
  and implementation; no test failure or substantive verdict is inferred.
- Act 27 §3 requires the Clerk's independent checks: hashes against the
  introducing commit, unchanged pre-anchor rows, and no claimed identity, with
  an independence basis. That review has not yet occurred.
- Act 27 §6 requires Executive checker support and seven hermetic tests. Those
  are not implemented in the inspected current-main script. The Judiciary does
  not edit or implement that machinery.
- The outcome cache and missing correction files establish non-publication in
  Git, not that the target reasoning was necessarily wrong. No external source
  repository, deployment, or CI was re-run for these six historical cases.

No cached outcome/state, old trail row, law, ballot, board issue or sample
verdict was changed. The marker append is an Act 27 statutory record action,
not a retroactive correction. Its efficacy remains suspended pending the
required independent review and checker implementation.
