#!/bin/sh
# Regression: a legal seat survives deletion and terminal failure of its appointee.
set -eu
town=${1:-$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)}
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT HUP INT TERM
mkdir -p "$tmp/bin" "$tmp/town/government" "$tmp/seats/a1" "$tmp/seats/branches/executive" "$tmp/state" "$tmp/mock"
printf 'a1\tClerk\tFounder intake\n' > "$tmp/town/government/seats.tsv"
cp "$town/government/restart-orphan.sh" "$tmp/town/government/restart-orphan.sh"
cat > "$tmp/bin/antonina" <<'EOF'
#!/bin/sh
set -eu
if [ "$1" = agent ] && [ "$2" = new ]; then
  num=0; [ ! -f "$MOCK/counter" ] || num=$(cat "$MOCK/counter")
  num=$((num+1)); printf '%s\n' "$num" > "$MOCK/counter"
  id="fresh-$num"; printf idle > "$MOCK/$id"
  printf '%s\n' "$id"
elif [ "$1" = agent ] && [ "$2" = status ]; then
  id=$4
  [ -f "$MOCK/$id" ] || exit 1
  status=$(cat "$MOCK/$id")
  if [ "$status" = failed ]; then
    printf '{"state":"failed","finished_at":1792775220.5,"prompts":2,"backend_error":{"classification":"upstream_endpoint_unavailable","transient":true,"automatic_retry_safe":false}}\n'
  elif [ "$status" = failed-permanent ]; then
    printf '{"state":"failed","finished_at":1792775230.25,"prompts":3,"backend_error":{"classification":"invalid_api_key","transient":false,"automatic_retry_safe":false}}\n'
  elif [ "$status" = failed-restart ]; then
    printf '{"state":"failed","alive":false,"started_at":1999999990,"finished_at":2000000000.5,"last_error":"runner/model process disappeared without a captured exit status","backend_error":null,"exit_code":null,"exit_signal":null,"steers_pending":0,"next_steer":null}\n'
  elif [ "$status" = failed-restart-late ]; then
    printf '{"state":"failed","alive":false,"started_at":2000000001,"finished_at":2000000002,"last_error":"runner/model process disappeared without a captured exit status","backend_error":null,"exit_code":null,"exit_signal":null}\n'
  elif [ "$status" = failed-restart-with-error ]; then
    printf '{"state":"failed","alive":false,"started_at":1999999990,"finished_at":2000000000.5,"last_error":"runner/model process disappeared without a captured exit status","backend_error":{"classification":"invalid_api_key","transient":false},"exit_code":null,"exit_signal":null}\n'
  elif [ "$status" = failed-restart-with-steer ]; then
    printf '{"state":"failed","alive":false,"started_at":1999999990,"finished_at":2000000000.5,"last_error":"runner/model process disappeared without a captured exit status","backend_error":null,"exit_code":null,"exit_signal":null,"steers_pending":1}\n'
  else
    printf '{"state":"%s","model":null,"variant":"low"}\n' "$status"
  fi
else
  echo 'unexpected mocked command' >&2; exit 7
fi
EOF
chmod +x "$tmp/bin/antonina"
export MOCK=$tmp/mock
export VICHE_TOWN_ROOT=$tmp/town
export VICHE_SEATS_ROOT=$tmp/seats
export VICHE_STATE_ROOT=$tmp/state
PATH=$tmp/bin:$PATH; export PATH
# PID1 birth override is only honored inside test-only government fixtures.
VICHE_TEST_NO_SYNC=1 VICHE_TEST_PID1_BIRTH=2000000000
export VICHE_TEST_NO_SYNC VICHE_TEST_PID1_BIRTH
script=$town/government/appointments.sh
a=$(/bin/sh "$script" ensure a1)
[ "$a" = fresh-1 ] || exit 1
b=$(/bin/sh "$script" ensure a1)
[ "$a" = "$b" ] || exit 1
r=$(/bin/sh "$script" resolve a1)
[ "$r" = "$a" ] || exit 1
# A clean exit is reusable, not an unknown state or a failed appointment.
printf clearexit > "$MOCK/$a"
[ "$(/bin/sh "$script" ensure a1)" = "$a" ]
[ "$(/bin/sh "$script" resolve a1)" = "$a" ]
# A transient/unrecognized status ("unknown" while a session transitions) must
# not break identity resolution; otherwise one sample flaps oversight incidents
# and liveness/sitting callers. Mutations still require a terminal state.
printf unknown > "$MOCK/$a"
[ "$(/bin/sh "$script" resolve a1)" = "$a" ] || { echo 'resolve failed on transient unknown status' >&2; exit 1; }
printf clearexit > "$MOCK/$a"
test "$(cat "$MOCK/counter")" -eq 1
rm "$MOCK/$a"
if /bin/sh "$script" resolve a1 >/dev/null 2>&1; then echo 'resolve invented missing agent' >&2; exit 1; fi
if /bin/sh "$script" ensure a1 >/dev/null 2>&1; then echo 'unreadable agent was replaced' >&2; exit 1; fi
[ ! -d "$tmp/state/appointments/terminal-evidence/fresh-1" ]
[ "$(awk -F '\t' '$1=="a1"{print $2}' "$tmp/state/appointments/appointments.tsv")" = fresh-1 ]
# Even confirmed stopped stays assigned until explicit supervisor replacement.
printf stopped > "$MOCK/$a"
[ "$(/bin/sh "$script" ensure a1)" = fresh-1 ]
if VICHE_TEST_FAIL_REGISTRY_SWAP=yes /bin/sh "$script" replace a1 "$a" appointments-smoke fixture 'injected failed swap'; then
  echo 'injected registry swap unexpectedly succeeded' >&2; exit 1
fi
[ "$(/bin/sh "$script" resolve a1)" = "$a" ] || { echo 'failed swap changed incumbent' >&2; exit 1; }
intent=$(printf '%s\n' "$tmp"/state/appointments/replacement-intents/*.json)
[ -s "$intent" ] || { echo 'failed swap lost prepared intent' >&2; exit 1; }
jq -e --arg prior "$a" '.state=="prepared" and .caller=="appointments-smoke" and
  .trigger=="fixture" and .expected_prior_id==$prior and .proposed_successor=="fresh-2" and
  .reason=="injected failed swap" and .transaction!=""' "$intent" >/dev/null
test "$(cat "$MOCK/counter")" -eq 2
if /bin/sh "$script" replace a1 "$a" >/dev/null 2>&1; then echo 'replacement accepted missing context' >&2; exit 1; fi
c=$(/bin/sh "$script" replace a1 "$a" appointments-smoke fixture 'injected failed swap')
[ "$c" = fresh-2 ] || exit 1
[ "$(cat "$MOCK/counter")" -eq 2 ] || { echo 'retry created a duplicate replacement agent' >&2; exit 1; }
[ "$(/bin/sh "$script" resolve a1)" = "$c" ]
jq -e --arg prior "$a" --arg successor "$c" '.state=="committed" and
  .expected_prior_id==$prior and .successor==$successor and .transaction!=""' \
  "$tmp/state/appointments/replacement-provenance.jsonl" >/dev/null
jq -e '.state=="stopped" and .agent_id=="fresh-1"' \
  "$tmp/state/appointments/terminal-evidence/fresh-1/event.json" >/dev/null
printf failed > "$MOCK/$c"
[ "$(/bin/sh "$script" ensure a1)" = fresh-2 ]
x=$(/bin/sh "$script" replace a1 "$c" appointments-smoke fixture 'confirmed failed fixture agent')
[ "$x" = fresh-3 ] || exit 1
# Preserve the real failed status, no duplicate observation of this invocation.
jq -e '.state=="failed" and .agent_id=="fresh-2" and .office=="a1" and
       .finished_at==1792775220.5 and .prompts==2 and
       .failure_class=="upstream_endpoint_unavailable" and
       .transient==true and .automatic_retry_safe==false' \
  "$tmp/state/appointments/terminal-evidence/fresh-2/event.json" >/dev/null
[ -s "$tmp/state/appointments/terminal-evidence/fresh-2/status.json" ]
# The mock has no 'agent log'; this MUST be explicitly marked unavailable,
# not masquerade as a successfully captured log. Worktree is not Git either.
jq -e '.log_captured==false and .worktree_status_captured==false and
       .worktree_head_captured==false' \
  "$tmp/state/appointments/terminal-evidence/fresh-2/event.json" >/dev/null
[ "$(wc -l < "$tmp/state/appointments/terminal-events.jsonl")" -eq 2 ]
# Recovery after a crash between primary evidence publication and index append:
sed -i '/"agent_id":"fresh-2"/d' "$tmp/state/appointments/terminal-events.jsonl"
[ "$(wc -l < "$tmp/state/appointments/terminal-events.jsonl")" -eq 1 ]
/bin/sh "$town/government/terminal-appointment-evidence.sh" a1 fresh-2 "$tmp/seats/a1" </dev/null
[ "$(wc -l < "$tmp/state/appointments/terminal-events.jsonl")" -eq 2 ]
[ "$(/bin/sh "$script" ensure a1)" = fresh-3 ]
[ "$(wc -l < "$tmp/state/appointments/terminal-events.jsonl")" -eq 2 ]
y=$(/bin/sh "$script" replace a1 "$x" appointments-smoke fixture 'confirmed failed fixture agent')
[ "$y" = fresh-4 ] || exit 1
e=$(/bin/sh "$script" ensure executive)
[ "$e" = fresh-5 ] || exit 1
# A confirmed nontransient terminal failure must retain false, not be erased
# into null by jq's alternative operator (false // null is null).
printf failed-permanent > "$MOCK/$e"
[ "$(/bin/sh "$script" ensure executive)" = "$e" ]
f=$(/bin/sh "$script" replace executive "$e" appointments-smoke fixture 'permanent failure fixture')
[ "$f" = fresh-6 ] || exit 1
jq -e '.state=="failed" and .failure_class=="invalid_api_key" and
        .transient==false and .automatic_retry_safe==false and
        .prompts==3 and .finished_at==1792775230.25' \
  "$tmp/state/appointments/terminal-evidence/fresh-5/event.json" >/dev/null
[ "$(wc -l < "$tmp/state/appointments/appointments.tsv")" -eq 2 ] || exit 1
# A verified container-restart orphan is a new independent appointment, NOT
# a first-failure Act19 transient reset or continuation of the previous prompt.
printf failed-restart > "$MOCK/$f"
g=$(/bin/sh "$script" ensure executive)
[ "$g" = fresh-7 ] || { echo 'Restart orphan did not renew' >&2; exit 1; }
jq -e '.state=="failed" and .agent_id=="fresh-6" and .failure_class==null' \
  "$tmp/state/appointments/terminal-evidence/fresh-6/event.json" >/dev/null
jq -e '.kind=="container_restart_orphan_new_appointment_no_prompt_replay" and
       .previous=="fresh-6" and .successor=="fresh-7"' \
  "$tmp/state/appointments/restart-renewals.jsonl" >/dev/null
[ "$(/bin/sh "$script" ensure executive)" = "$g" ]
[ "$(wc -l < "$tmp/state/appointments/restart-renewals.jsonl")" -eq 1 ]
jq -e '.caller=="appointments.ensure" and .trigger=="restart_orphan" and
       .expected_prior_id=="fresh-6" and .reason=="confirmed PID1 restart orphan; no prompt replay"' \
  "$tmp/state/appointments/replacement-provenance.jsonl" >/dev/null
# An unrelated failure that happened after this incarnation began must NOT
# be mistaken for an orphan, even if the error text was identical.
printf failed-restart-late > "$MOCK/$g"
[ "$(/bin/sh "$script" ensure executive)" = "$g" ]
h=$(/bin/sh "$script" replace executive "$g" appointments-smoke fixture 'late restart signature fixture')
[ "$h" = fresh-8 ]
# A backend error is not a missing-container-process error.
printf failed-restart-with-error > "$MOCK/$h"
[ "$(/bin/sh "$script" ensure executive)" = "$h" ]
i=$(/bin/sh "$script" replace executive "$h" appointments-smoke fixture 'backend error fixture')
[ "$i" = fresh-9 ]
# Pending steers require explicit review; do not discard their intent.
printf failed-restart-with-steer > "$MOCK/$i"
[ "$(/bin/sh "$script" ensure executive)" = "$i" ]
j=$(/bin/sh "$script" replace executive "$i" appointments-smoke fixture 'pending steer fixture')
[ "$j" = fresh-10 ]
# Even true container orphans may not bypass an explicit unsafe hold.
mkdir -p "$tmp/state/liveness/unsafe-holds"
printf 'executive\told-id\tunsafe\n' > "$tmp/state/liveness/unsafe-holds/executive"
printf failed-restart > "$MOCK/$j"
[ "$(/bin/sh "$script" ensure executive)" = "$j" ]
[ "$(wc -l < "$tmp/state/appointments/restart-renewals.jsonl")" -eq 1 ]
# A post-registry provenance rename failure is a successful replacement with
# its prepared intent retained for reconciliation, never a failed retry signal.
printf stopped > "$MOCK/$y"
before=$(cat "$MOCK/counter")
recovered=$(VICHE_TEST_FAIL_PROVENANCE_RENAME=yes /bin/sh "$script" replace a1 "$y" appointments-smoke fixture 'provenance rename failure')
[ "$(/bin/sh "$script" resolve a1)" = "$recovered" ]
test "$(cat "$MOCK/counter")" -eq "$((before+1))"
prepared=$(printf '%s\n' "$tmp"/state/appointments/replacement-intents/*.json)
jq -e --arg prior "$y" --arg successor "$recovered" \
  '.state=="prepared" and .expected_prior_id==$prior and .proposed_successor==$successor and
   .caller=="appointments-smoke" and .reason=="provenance rename failure"' "$prepared" >/dev/null
[ "$(/bin/sh "$script" ensure a1)" = "$recovered" ]
test "$(cat "$MOCK/counter")" -eq "$((before+1))"
# No secret powers granted by supplying an unknown role key.
if /bin/sh "$script" ensure a2 >/dev/null 2>&1; then exit 1; fi
printf 'a1\tbad-1\na1\tbad-2\n' > "$tmp/state/appointments/appointments.tsv"
if /bin/sh "$script" ensure a1 >/dev/null 2>&1; then echo 'duplicate appointee accepted' >&2; exit 1; fi
echo 'appointment recovery tests passed'
