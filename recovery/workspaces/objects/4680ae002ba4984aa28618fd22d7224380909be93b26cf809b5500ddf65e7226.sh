#!/bin/sh
# Hermetic test of Act 17 (Audit Verdict Correction Act): superseding verdicts,
# the Git-anchored append-only corrections trail, corrected_finding visibility,
# finality (one correction per cycle, no bare re-flip) and honest procedural
# (not independent) second-pass labelling.
set -eu
repo=$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
mkdir -p "$scratch/bin" "$scratch/state/oversight/random/cases" \
    "$scratch/state/oversight/random/outcomes" "$scratch/town/records" \
    "$scratch/seats/branches/judiciary"
printf 'authoritative fixture\n' > "$scratch/charter"
: > "$scratch/town/records/SUMMONED.txt"
git -C "$scratch/town" init -q -b main
git -C "$scratch/town" -c user.name=Fixture -c user.email=fixture@example.invalid \
  commit --allow-empty -qm 'initial Git state: no effective corrections yet'
CASE=0123456789abcdef01
TOKEN=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
printf '{"case_id":"%s","population":"ignored_work","id":"301","at":2000000000}\n' \
    "$CASE" > "$scratch/state/oversight/random/cases/$CASE.json"
cat > "$scratch/bin/antonina" <<'MOCK'
#!/bin/sh
set -eu
case "$1 $2" in
"agent list")
    printf '{"agents":[{"id":"c1e00008"}],"unreadable":0}\n' ;;
"agent status")
    printf '{"state":"idle","model":"test-provider/example","variant":"low"}\n' ;;
*) echo "unexpected mock call: $*" >&2; exit 90 ;;
esac
MOCK
chmod +x "$scratch/bin/antonina"
PATH=$scratch/bin:$PATH
VICHE_STATE_ROOT=$scratch/state
VICHE_TOWN_ROOT=$scratch/town
VICHE_SEATS_ROOT=$scratch/seats
VICHE_CONSTITUTION=$scratch/charter
VICHE_OVERSIGHT_NOW=2000000000
VICHE_AUDIT_CYCLE_ID=$TOKEN
printf '%s\n' "$TOKEN" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000000\t%s\n' "$TOKEN" > "$scratch/state/oversight/audit-cycle-identities.tsv"
export PATH VICHE_STATE_ROOT VICHE_TOWN_ROOT VICHE_SEATS_ROOT VICHE_CONSTITUTION VICHE_OVERSIGHT_NOW VICHE_AUDIT_CYCLE_ID

trail="$scratch/town/records/oversight/corrections/$CASE.jsonl"
CTRL="$repo/government/audit-accountability.py"

# 1. Ordinary filing of a non-finding verdict (the prior lockout target).
python3 "$CTRL" report --case "$CASE" --verdict not_assigned \
    --evidence "board #301 original sample" >/dev/null

# 2. A correction of that non-finding is now permitted (Act 17 §2.1/§2.5).
python3 "$CTRL" report --case "$CASE" --verdict finding \
    --evidence "commit:deadbeef stronger replay" --correction \
    --cycle-id "$TOKEN" \
    --supersedes not_assigned --auditor c1e00008 --reason_code corrected_on_replay \
    --why_stronger "replayed the full sample with an independent evaluator" >/dev/null

# 3. Git-anchored authoritative trail exists and records the pending correction.
[ -s "$trail" ]
grep -q '"correction": true' "$trail"
grep -q '"confirmed": false' "$trail"
grep -q '"supersedes": "not_assigned"' "$trail"
grep -q '"phase": "correction_filed"' "$trail"
grep -q "\"cycle_id\": \"$TOKEN\"" "$trail"

# 4. Until the second procedural pass, the current verdict is unchanged and the
#    case is reported correction_pending (Act 17 §2.4).
python3 "$CTRL" check > "$scratch/check"
jq -e '[.signals[].type]|index("correction_pending")' "$scratch/check" >/dev/null
jq -e --arg c "$CASE" '.signals[]|select(.type=="correction_pending" and .case_id==$c)' \
    "$scratch/check" >/dev/null
# current verdict in the cache is still the prior one
jq -e --arg c "$CASE" '.verdict' "$scratch/state/oversight/random/outcomes/$CASE.json" >/dev/null
[ "$(jq -r .verdict "$scratch/state/oversight/random/outcomes/$CASE.json")" = not_assigned ]

# 5. Second procedural pass (same office/model — NOT independent) confirms it.
python3 "$CTRL" report --case "$CASE" --confirm --evidence "second procedural replay" >/dev/null
python3 "$CTRL" check > "$scratch/check"
jq -e --arg c "$CASE" '.signals[]|select(.type=="correction_not_effective" and .case_id==$c)' "$scratch/check" >/dev/null
# Only a committed Git version, not a writable state-dir cache or untracked
# file, makes that first confirmed correction legally effective.
git -C "$scratch/town" add records/oversight/corrections/"$CASE".jsonl
git -C "$scratch/town" -c user.name=Fixture -c user.email=fixture@example.invalid \
  commit -qm 'anchor first confirmed correction'
grep -q '"phase": "second_procedural_pass_not_independent"' "$trail"
grep -q '"confirmed": true' "$trail"
[ "$(jq -r .verdict "$scratch/state/oversight/random/outcomes/$CASE.json")" = finding ]
python3 "$CTRL" check > "$scratch/check"
if jq -e '[.signals[].type]|index("correction_pending")' "$scratch/check" >/dev/null; then
    echo "correction_pending cleared after confirmation" >&2; exit 1
fi

# 6. A finding may be corrected to a non-finding in a distinct dispatch cycle;
#    confirmation of that correction does not consume another slot.
TOKEN2=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
VICHE_AUDIT_CYCLE_ID=$TOKEN2
printf '%s\n' "$TOKEN2" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000001\t%s\n' "$TOKEN2" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$CASE" --verdict not_assigned \
    --evidence "commit:cafebabe still stronger retraction" --correction \
    --cycle-id "$TOKEN2" \
    --supersedes finding --auditor c1e00008 --reason_code retracted_on_stronger_evidence \
    --why_stronger "new replay shows the original finding was a false positive" >/dev/null
python3 "$CTRL" report --case "$CASE" --confirm --evidence "procedural retraction replay" >/dev/null
# This uncommitted retraction is a false-positive corrected_finding signal
# unless check() derives its effective state from Git HEAD instead of cache.
python3 "$CTRL" check > "$scratch/check"
jq -e --arg c "$CASE" '.signals[]|select(.type=="correction_not_effective" and .case_id==$c)' "$scratch/check" >/dev/null
jq -e --arg c "$CASE" '.signals[]|select(.type=="unresolved_finding" and .case_id==$c)' "$scratch/check" >/dev/null
git -C "$scratch/town" add records/oversight/corrections/"$CASE".jsonl
git -C "$scratch/town" -c user.name=Fixture -c user.email=fixture@example.invalid \
  commit -qm 'anchor second confirmed correction'
python3 "$CTRL" check > "$scratch/check"
jq -e '[.signals[].type]|index("corrected_finding")' "$scratch/check" >/dev/null
if jq -e '[.signals[].type]|index("unresolved_finding")' "$scratch/check" >/dev/null; then
    echo "corrected finding must not raise unresolved_finding" >&2; exit 1
fi

# After a confirmed finding correction, ordinary verdict submission cannot
# bypass the correction evidence and cycle-token requirements.
if python3 "$CTRL" report --case "$CASE" --verdict finding \
    --evidence "ordinary overwrite" 2>/dev/null; then
    echo "ordinary report bypassed post-correction safeguards" >&2; exit 1
fi
if python3 "$CTRL" report --case "$CASE" --confirm --evidence "unbound confirmation" \
    --cycle-id "$TOKEN" 2>/dev/null; then
    echo "confirmation of non-pending correction accepted" >&2; exit 1
fi

# The other correction direction (not_assigned -> finding) clears the
# corrected_from_finding signal. Ordinary reports must still be blocked both
# during the pending correction and after its confirmation.
CASE_PENDING=121212121212121212
printf '{"case_id":"%s","population":"ignored_work","id":"311","at":2000000000}\n' \
    "$CASE_PENDING" > "$scratch/state/oversight/random/cases/$CASE_PENDING.json"
TOKEN_PENDING=12121212121212121212121212121212
VICHE_AUDIT_CYCLE_ID=$TOKEN_PENDING
printf '%s\n' "$TOKEN_PENDING" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000016\t%s\n' "$TOKEN_PENDING" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$CASE_PENDING" --verdict not_assigned --evidence "initial" >/dev/null
python3 "$CTRL" report --case "$CASE_PENDING" --verdict finding --evidence "stronger" \
    --correction --cycle-id "$TOKEN_PENDING" --supersedes not_assigned --auditor c1e00008 \
    --reason_code corrected_to_finding --why_stronger "materially stronger evidence" >/dev/null
if python3 "$CTRL" report --case "$CASE_PENDING" --verdict not_assigned --evidence "pending overwrite" 2>/dev/null; then
    echo "ordinary verdict changed a pending correction" >&2; exit 1
fi
python3 "$CTRL" report --case "$CASE_PENDING" --confirm --evidence "confirmation" >/dev/null
if python3 "$CTRL" report --case "$CASE_PENDING" --verdict not_assigned --evidence "confirmed overwrite" 2>/dev/null; then
    echo "ordinary verdict changed a confirmed finding correction" >&2; exit 1
fi

# A non-finding-to-non-finding correction also establishes durable correction
# history and cannot be overwritten by ordinary reporting after confirmation.
CASE_NONFINDING=131313131313131313
printf '{"case_id":"%s","population":"ignored_work","id":"312","at":2000000000}\n' \
    "$CASE_NONFINDING" > "$scratch/state/oversight/random/cases/$CASE_NONFINDING.json"
TOKEN_NONFINDING=13131313131313131313131313131313
VICHE_AUDIT_CYCLE_ID=$TOKEN_NONFINDING
printf '%s\n' "$TOKEN_NONFINDING" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000017\t%s\n' "$TOKEN_NONFINDING" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$CASE_NONFINDING" --verdict not_assigned --evidence "initial" >/dev/null
python3 "$CTRL" report --case "$CASE_NONFINDING" --verdict inconclusive --evidence "stronger" \
    --correction --cycle-id "$TOKEN_NONFINDING" --supersedes not_assigned --auditor c1e00008 \
    --reason_code correction_nonfinding --why_stronger "materially stronger evidence" >/dev/null
python3 "$CTRL" report --case "$CASE_NONFINDING" --confirm --evidence "confirmation" >/dev/null
if python3 "$CTRL" report --case "$CASE_NONFINDING" --verdict not_assigned --evidence "confirmed overwrite" 2>/dev/null; then
    echo "ordinary verdict changed a confirmed non-finding correction" >&2; exit 1
fi

orphan_case=969696969696969696
printf '{"case_id":"%s","population":"ignored_work","id":"310","at":2000000000}\n' \
    "$orphan_case" > "$scratch/state/oversight/random/cases/$orphan_case.json"
TOKEN18=cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd
VICHE_AUDIT_CYCLE_ID=$TOKEN18
printf '%s\n' "$TOKEN18" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000015\t%s\n' "$TOKEN18" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$orphan_case" --verdict not_assigned --evidence "orphan prior" >/dev/null
python3 - "$scratch/state/oversight/random/outcomes/$orphan_case.json" <<'PY'
import json,sys
p=sys.argv[1]
data=json.load(open(p)); data.update(correction_pending=True, history=[{
 "correction":True,"confirmed":False,"verdict":"finding","supersedes":"not_assigned"}])
json.dump(data,open(p,"w"))
PY
if python3 "$CTRL" report --case "$orphan_case" --confirm --evidence "no trail row" 2>/dev/null; then
    echo "confirmation without authoritative correction entry accepted" >&2; exit 1
fi

# 7. Pending correction blocks a second same-cycle correction.
TOKEN3=cccccccccccccccccccccccccccccccc
VICHE_AUDIT_CYCLE_ID=$TOKEN3
printf '%s\n' "$TOKEN3" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000002\t%s\n' "$TOKEN3" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$CASE" --verdict verified \
    --evidence "commit:feedface third look" --correction \
    --cycle-id "$TOKEN3" \
    --supersedes not_assigned --auditor c1e00008 --reason_code third \
    --why_stronger "yet another replay" >/dev/null
if python3 "$CTRL" report --case "$CASE" --verdict finding \
    --evidence "commit:feedface dup" --correction --supersedes not_assigned \
    --cycle-id "$TOKEN3" \
    --auditor c1e00008 --reason_code dup --why_stronger "again" 2>/dev/null; then
    echo "second concurrent pending correction must be refused" >&2; exit 1
fi
# 8. Guardrails: a correction missing why_stronger / reason_code / auditor /
#    supersedes, or citing the original evidence, is refused.
if python3 "$CTRL" report --case "$CASE" --verdict inconclusive \
    --evidence "commit:x1" --correction --supersedes verified \
    --cycle-id "$TOKEN3" \
    --auditor c1e00008 --reason_code no_why --why_stronger "" 2>/dev/null; then
    echo "empty why_stronger must be refused" >&2; exit 1
fi
if python3 "$CTRL" report --case "$CASE" --verdict inconclusive \
    --evidence "commit:x1" --correction --supersedes verified \
    --cycle-id "$TOKEN3" \
    --auditor c1e00008 --reason_code no_why --why_stronger "diff" 2>/dev/null; then
    echo "duplicate evidence must be refused" >&2; exit 1
fi
if python3 "$CTRL" report --case "$CASE" --verdict inconclusive \
    --evidence "board #301 original sample" --correction --supersedes verified \
    --cycle-id "$TOKEN3" \
    --auditor c1e00008 --reason_code orig --why_stronger "same ref" 2>/dev/null; then
    echo "original evidence reuse must be refused" >&2; exit 1
fi

# 9. verified_fixed still requires a previous finding (unchanged).
CASE2=fedcba9876543210fe
printf '{"case_id":"%s","population":"claimed_delivery","id":"218","at":2000000000}\n' \
    "$CASE2" > "$scratch/state/oversight/random/cases/$CASE2.json"
if python3 "$CTRL" report --case "$CASE2" --verdict verified_fixed \
    --evidence "commit:nope" 2>/dev/null; then
    echo "verified_fixed without a prior finding must be refused" >&2; exit 1
fi

# 11. The trail is append-only: the number of committed lines equals the number
#    of correction/confirmation filings (no overwrite).
n=$(wc -l < "$trail")
[ "$n" -ge 4 ]

# A separate case exercises current/stale/forged/missing tokens without being
# confounded by its verdict history.
CASE3=abcdefabcdefabcdef
printf '{"case_id":"%s","population":"ignored_work","id":"303","at":2000000000}\n' \
    "$CASE3" > "$scratch/state/oversight/random/cases/$CASE3.json"
TOKEN5=55555555555555555555555555555555
VICHE_AUDIT_CYCLE_ID=$TOKEN5
printf '%s\n' "$TOKEN5" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000003\t%s\n' "$TOKEN5" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
VICHE_AUDIT_CYCLE_ENFORCE=1
export VICHE_AUDIT_CYCLE_ID
export VICHE_AUDIT_CYCLE_ENFORCE
python3 "$CTRL" report --case "$CASE3" --verdict not_assigned --evidence "start #303" >/dev/null
for invalid in forged stale missing; do
    case $invalid in
        forged) token=dddddddddddddddddddddddddddddddd ;;
        stale) token=$TOKEN ;;
        missing) token= ;;
    esac
    if python3 "$CTRL" report --case "$CASE3" --verdict finding \
        --evidence "rejected $invalid" --correction --cycle-id "$token" \
        --supersedes not_assigned --auditor c1e00008 --reason_code invalid \
        --why_stronger "not accepted" 2>/dev/null; then
        echo "invalid or stale cycle token accepted: $invalid" >&2; exit 1
    fi
done
# A valid current dispatch token files and confirms a correction.
python3 "$CTRL" report --case "$CASE3" --verdict finding --evidence "new cycle" \
    --correction --cycle-id "$TOKEN5" --supersedes not_assigned --auditor c1e00008 \
    --reason_code new_cycle --why_stronger "new dispatch evidence" >/dev/null
python3 "$CTRL" report --case "$CASE3" --confirm --evidence "confirmation" >/dev/null
if python3 "$CTRL" report --case "$CASE3" --verdict finding --evidence "same cycle retry" \
    --correction --cycle-id "$TOKEN5" --supersedes finding --auditor c1e00008 \
    --reason_code retry --why_stronger "retry after confirmation" 2>/dev/null; then
    echo "same-cycle correction after confirmation must be refused" >&2; exit 1
fi
# After confirmation, the same identity remains spent; a fresh current token
# can be issued only for a separate dispatch.
TOKEN6=66666666666666666666666666666666
VICHE_AUDIT_CYCLE_ID=$TOKEN6
printf '%s\n' "$TOKEN6" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000004\t%s\n' "$TOKEN6" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
if python3 "$CTRL" report --case "$CASE3" --verdict finding --evidence "missing token" \
    --correction --supersedes inconclusive --auditor c1e00008 \
    --reason_code missing --why_stronger "missing" 2>/dev/null; then
    echo "missing cycle token must fail closed" >&2; exit 1
fi
CASE4=ababababababababab
printf '{"case_id":"%s","population":"ignored_work","id":"304","at":2000000000}\n' \
    "$CASE4" > "$scratch/state/oversight/random/cases/$CASE4.json"
TOKEN19=abababababababababababababababab
VICHE_AUDIT_CYCLE_ID=$TOKEN19
printf '%s\n' "$TOKEN19" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000011\t%s\n' "$TOKEN19" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$CASE4" --verdict not_assigned --evidence "forged case original" >/dev/null

# Legacy correction history without cycle_id remains untouched/unclassified.
TOKEN11=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbc
VICHE_AUDIT_CYCLE_ID=$TOKEN11
printf '%s\n' "$TOKEN11" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000008\t%s\n' "$TOKEN11" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$CASE2" --verdict not_assigned --evidence "old original" >/dev/null
legacy_trail="$scratch/town/records/oversight/corrections/$CASE2.jsonl"
printf '{"case_id":"%s","correction":true,"confirmed":true}\n' "$CASE2" > "$legacy_trail"
cp "$legacy_trail" "$scratch/legacy-before"
TOKEN12=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbd
VICHE_AUDIT_CYCLE_ID=$TOKEN12
printf '%s\n' "$TOKEN12" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000009\t%s\n' "$TOKEN12" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
if python3 "$CTRL" report --case "$CASE2" --verdict finding --evidence "fresh evidence" \
    --correction --cycle-id "$TOKEN12" --supersedes not_assigned --auditor c1e00008 \
    --reason_code legacy --why_stronger "fresh evidence" 2>/dev/null; then
    echo "legacy correction trail without cycle_id must fail closed" >&2; exit 1
fi
cmp "$scratch/legacy-before" "$legacy_trail"

# A legacy correction row is preserved, but its absent identity cannot be
# assigned a guessed cycle or used as a safe basis for a new correction.
legacy_case=989898989898989898
printf '{"case_id":"%s","population":"ignored_work","id":"308","at":2000000000}\n' \
    "$legacy_case" > "$scratch/state/oversight/random/cases/$legacy_case.json"
TOKEN15=eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
VICHE_AUDIT_CYCLE_ID=$TOKEN15
printf '%s\n' "$TOKEN15" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000012\t%s\n' "$TOKEN15" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$legacy_case" --verdict not_assigned --evidence "before old trail" >/dev/null
legacy_trail="$scratch/town/records/oversight/corrections/$legacy_case.jsonl"
printf '{"case_id":"%s","correction":true,"confirmed":true}\n' "$legacy_case" > "$legacy_trail"
cp "$legacy_trail" "$scratch/legacy-before"
TOKEN16=ffffffffffffffffffffffffffffffff
VICHE_AUDIT_CYCLE_ID=$TOKEN16
printf '%s\n' "$TOKEN16" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000013\t%s\n' "$TOKEN16" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
if python3 "$CTRL" report --case "$legacy_case" --verdict finding --evidence "new" \
    --correction --cycle-id "$TOKEN16" --supersedes not_assigned --auditor c1e00008 \
    --reason_code old_trail --why_stronger "new" 2>/dev/null; then
    echo "legacy authoritative correction without cycle_id must fail closed" >&2; exit 1
fi
cmp "$scratch/legacy-before" "$legacy_trail"

malformed_case=999999999999999999
printf '{"case_id":"%s","population":"ignored_work","id":"307","at":2000000000}\n' \
    "$malformed_case" > "$scratch/state/oversight/random/cases/$malformed_case.json"
TOKEN13=cccccccccccccccccccccccccccccccc
VICHE_AUDIT_CYCLE_ID=$TOKEN13
printf '%s\n' "$TOKEN13" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000010\t%s\n' "$TOKEN13" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$malformed_case" --verdict not_assigned --evidence "prior" >/dev/null
malformed_trail="$scratch/town/records/oversight/corrections/$malformed_case.jsonl"
printf '{"case_id":"%s","correction":true,"confirmed":true}\nnot-json\n' \
    "$malformed_case" > "$malformed_trail"
TOKEN9=99999999999999999999999999999999
VICHE_AUDIT_CYCLE_ID=$TOKEN9
printf '%s\n' "$TOKEN9" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000000\t%s\n' "$TOKEN9" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
if python3 "$CTRL" report --case "$malformed_case" --verdict finding --evidence "new" \
    --correction --cycle-id "$TOKEN9" --supersedes not_assigned --auditor c1e00008 \
    --reason_code malformed --why_stronger "stronger" 2>/dev/null; then
    echo "malformed authoritative correction trail did not fail closed" >&2; exit 1
fi
[ "$(wc -l < "$malformed_trail")" -eq 2 ]

# A current-token file without the matching durable dispatch-ledger entry is
# forged and rejected; no environment variable alone creates a dispatch.
no_token_case=979797979797979797
printf '{"case_id":"%s","population":"ignored_work","id":"309","at":2000000000}\n' \
    "$no_token_case" > "$scratch/state/oversight/random/cases/$no_token_case.json"
TOKEN17=abababababababababababababababab
VICHE_AUDIT_CYCLE_ID=$TOKEN17
printf '%s\n' "$TOKEN17" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000014\t%s\n' "$TOKEN17" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
export VICHE_AUDIT_CYCLE_ID
python3 "$CTRL" report --case "$no_token_case" --verdict not_assigned --evidence "no-token prior" >/dev/null
rm "$scratch/state/oversight/current-audit-cycle"
if python3 "$CTRL" report --case "$no_token_case" --verdict finding --evidence "no current dispatch" \
    --correction --cycle-id "$TOKEN17" --supersedes not_assigned --auditor c1e00008 \
    --reason_code no_current --why_stronger "should fail closed" 2>/dev/null; then
    echo "missing current dispatch token accepted" >&2; exit 1
fi
TOKEN10=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab
VICHE_AUDIT_CYCLE_ID=$TOKEN10
printf '%s\n' "$TOKEN10" > "$scratch/state/oversight/current-audit-cycle"
if python3 "$CTRL" report --case "$CASE4" --verdict finding --evidence "forged dispatch" \
    --correction --cycle-id "$TOKEN10" --supersedes not_assigned --auditor c1e00008 \
    --reason_code forged --why_stronger "unsupported" 2>/dev/null; then
    echo "unledgered dispatch token accepted" >&2; exit 1
fi
# Two CLI submissions racing for the SAME case and cycle must not both
# pass the read/check/append gate. This is a real concurrent-process test.
RACE_CASE=454545454545454545
RACE_TOKEN=45454545454545454545454545454545
printf '{"case_id":"%s","population":"ignored_work","id":"301","at":2000000000}\n' \
  "$RACE_CASE" > "$scratch/state/oversight/random/cases/$RACE_CASE.json"
printf '%s\n' "$RACE_TOKEN" > "$scratch/state/oversight/current-audit-cycle"
printf '2000000020\t%s\n' "$RACE_TOKEN" >> "$scratch/state/oversight/audit-cycle-identities.tsv"
python3 "$CTRL" report --case "$RACE_CASE" --verdict not_assigned --evidence "baseline" >/dev/null
for contender in first second; do
 (
  set +e
  python3 "$CTRL" report --case "$RACE_CASE" --verdict finding \
    --evidence "strong-$contender" --correction --cycle-id "$RACE_TOKEN" \
    --supersedes not_assigned --auditor c1e00008 --reason_code parallel \
    --why_stronger "verified-new-$contender" > "$scratch/race-$contender.out" 2> "$scratch/race-$contender.err"
  echo "$?" > "$scratch/race-$contender.rc"
 ) &
done
wait
a=$(cat "$scratch/race-first.rc")
b=$(cat "$scratch/race-second.rc")
if ! { [ "$a" -eq 0 ] && [ "$b" -ne 0 ]; } &&
   ! { [ "$b" -eq 0 ] && [ "$a" -ne 0 ]; }; then
  echo "Concurrent same-cycle correction cap was bypassed: $a $b" >&2
  exit 1
fi
[ "$(wc -l < "$scratch/town/records/oversight/corrections/$RACE_CASE.jsonl")" -eq 1 ]
# Historical failure: a state cache advertises corrected_finding but its
# two correction rows were never Git anchored. Act17 §2.2 keeps the original
# finding operative. Do not create an imaginary independent confirmation.
UNANCHORED=787878787878787878
printf '{"case_id":"%s","population":"ignored_work","id":"999","at":2000000000}\n' \
  "$UNANCHORED" > "$scratch/state/oversight/random/cases/$UNANCHORED.json"
printf '{"case_id":"%s","verdict":"not_assigned","at":2000000000,"evidence_ref":"cached unanchored retraction","corrected_from_finding":true,"correction_pending":false,"history":[{"correction":true,"confirmed":true,"supersedes":"finding","verdict":"not_assigned"}]}\n' \
  "$UNANCHORED" > "$scratch/state/oversight/random/outcomes/$UNANCHORED.json"
python3 "$CTRL" check > "$scratch/check"
jq -e --arg c "$UNANCHORED" '.signals[]|select(.type=="correction_not_effective" and .case_id==$c)' "$scratch/check" >/dev/null
jq -e --arg c "$UNANCHORED" '.signals[]|select(.type=="unresolved_finding" and .case_id==$c)' "$scratch/check" >/dev/null
if jq -e --arg c "$UNANCHORED" '.signals[]|select(.type=="corrected_finding" and .case_id==$c)' "$scratch/check" >/dev/null; then
  echo 'Uncommitted cache falsely corrected an unresolved finding' >&2; exit 1
fi
# Exact historical failure pattern: original inconclusive -> (unanchored)
# finding -> (unanchored) not_assigned. Both invalid corrections cannot
# generate corrected_finding or turn the original inconclusive into finding.
TWO_STEP=898989898989898989
printf '{"case_id":"%s","population":"ignored_work","id":"998","at":2000000000}\n' \
 "$TWO_STEP" > "$scratch/state/oversight/random/cases/$TWO_STEP.json"
printf '{"case_id":"%s","verdict":"not_assigned","at":2000000000,"evidence_ref":"cached second retraction","corrected_from_finding":true,"history":[{"correction":true,"confirmed":true,"supersedes":"inconclusive","verdict":"finding"},{"correction":true,"confirmed":true,"supersedes":"finding","verdict":"not_assigned"}]}\n' \
 "$TWO_STEP" > "$scratch/state/oversight/random/outcomes/$TWO_STEP.json"
python3 "$CTRL" check > "$scratch/check"
jq -e --arg c "$TWO_STEP" '.signals[]|select(.type=="correction_not_effective" and .case_id==$c)' "$scratch/check" >/dev/null
if jq -e --arg c "$TWO_STEP" '.signals[]|select((.type=="corrected_finding" or .type=="unresolved_finding") and .case_id==$c)' "$scratch/check" >/dev/null; then
 echo 'Unanchored two-step history changed original inconclusive verdict' >&2;exit 1
fi
echo 'Act 17 audit correction smoke passed'
