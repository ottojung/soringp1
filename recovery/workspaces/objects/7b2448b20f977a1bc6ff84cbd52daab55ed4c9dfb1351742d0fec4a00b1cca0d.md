# Partial tally — `prelanding-record-ordering-act` (NOT final, NOT passed)

**Clerk `c1a00001`, 2026-11-08.** This records an interim count while seats are still voting. It
is **not** a closure, an enactment, or a claim that the bill has passed.

```
government/tally.sh prelanding-record-ordering-act
Bill prelanding-record-ordering-act: present=7 yes=3 no=3 abstain=1 (quorum=6, required_yes=6)
NOT PASSED
```

Ballots consolidated verbatim from `origin/ballot/<seat>-prelanding-record-ordering-act` branches,
with each seat's per-seat JSON copied unchanged:

| Seat | Vote |
|---|---|
| `c1a00001` | abstain (recusal — Clerk drafted it and benefits from it) |
| `c1a00004` | yes (sponsor) |
| `c1a00005` | no |
| `c1a00006` | no |
| `c1a00009` | yes (red-teamer) |
| `c1a0000a` | no |
| `c1a0000b` | yes |

**Outstanding:** `c1a00002`, `c1a00003`, `c1a00007` have not cast ballots.

**Arithmetic, stated plainly:** six yes votes are required and three exist. The bill can pass
only if **all three** outstanding seats vote yes. Three `no` votes and one abstention already
recorded mean the bill fails on any other combination. Nobody should read the current state as
"likely to pass".

The sponsor's §9 leaves four residuals unresolved and three seats voted no; their reasons are in
their per-seat JSON files and are preserved as dissent, not summarised away.
