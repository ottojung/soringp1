#!/bin/sh
# Map durable logical seat/office keys to disposable Antonina agent IDs.
set -eu
{ [ "$#" -eq 2 ] || { [ "$#" -eq 6 ] && [ "$1" = replace ]; }; } ||
  { echo 'Usage: appointments.sh ensure|resolve KEY | replace KEY EXPECTED_ID CALLER TRIGGER REASON' >&2; exit 2; }
action=$1 key=$2
expected=${3:-}
caller=${4:-}
trigger=${5:-}
reason=${6:-}
case "$expected" in ''|*[!a-zA-Z0-9_-]*) [ -z "$expected" ] || exit 2;; esac
case "$action" in ensure|resolve|replace) :;; *) exit 2;; esac
case "$key" in ''|*[!a-zA-Z0-9_-]*) exit 2;; esac
if [ "$action" = replace ]; then
  case "$expected" in '') echo 'replacement requires expected prior ID' >&2; exit 2;; esac
  case "$caller" in ''|*[!a-zA-Z0-9_.-]*) echo 'replacement requires explicit caller identity' >&2; exit 2;; esac
  case "$trigger" in ''|*[!a-zA-Z0-9_.-]*) echo 'replacement requires explicit trigger' >&2; exit 2;; esac
  case "$reason" in '') echo 'replacement requires explicit reason' >&2; exit 2;; esac
  case "$reason" in *'	'*|*'\n'*) echo 'invalid replacement reason' >&2; exit 2;; esac
fi
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
seats=${VICHE_SEATS_ROOT:-/var/lib/lubko/wd/viche-seats}
root=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/appointments
# Defense in depth: no direct caller can bypass the enacted-charter +
# time-limited activation gate to manufacture a knowledge appointment.
case "$key" in
  statistics|foresight|strategy|spying)
    if [ "$action" != resolve ]; then
      grep -Eq '^## Act [0-9]+ — Institutional Knowledge and Communications Act \(enacted ' "$town/government/LAWS.md" || {
        echo "Knowledge appointment forbidden before lawful enactment" >&2; exit 1;
      }
      /bin/sh "$town/government/knowledge-activation-verify.sh" "$key" || {
        echo "Knowledge appointment forbidden without valid, office-specific, unexpired authorization" >&2; exit 1;
      }
    fi ;;
esac
mkdir -p "$root"
umask 077
tab=$(printf '\t')
title=
cwd=
while IFS="$tab" read -r seat_id seat_title focus; do
  if [ "$key" = "$seat_id" ]; then title=$seat_title; cwd=$seats/$key; break; fi
done < "$town/government/seats.tsv"
if [ -z "$cwd" ]; then
  case "$key" in
    executive) title=Executive;;
    judiciary) title=Judiciary;;
    innovation-centre)
      title='Legislative Innovation Centre'
      if grep -Eq '^## Act [0-9]+ — Executive Innovation Office Act \((re-)?enacted ' "$town/government/LAWS.md"; then
        title='Executive Innovation Office'
      fi ;;
    recovery-steward) title='Institutional Recovery Steward';;
    economy) title='Ministry of Economy';;
    statistics) title='Statistics Bureau';;
    foresight) title='Foresight Institute';;
    strategy) title='Ministry of Strategic Development';;
    spying) title='Ministry of Spying';;
    *) echo "unknown seat or office $key" >&2; exit 2;;
  esac
  cwd=$seats/branches/$key
  # Act 25: the stable appointment key remains innovation-centre, but the
  # active worktree is the clean Executive office once it exists. The
  # historical legislative worktree is evidence only, never an appointment,
  # policy-sync or recovery target.
  if [ "$key" = innovation-centre ] &&
     { [ -f "$seats/branches/innovation-office/.git" ] ||
       [ -d "$seats/branches/innovation-office/.git" ]; }; then
    cwd=$seats/branches/innovation-office
  fi
fi
[ -d "$cwd" ] || { echo "missing worktree $cwd" >&2; exit 1; }
registry=$root/appointments.tsv
if [ "$action" != resolve ]; then
  tries=0
  until mkdir "$root/lock" 2>/dev/null; do
    tries=$((tries+1))
    [ "$tries" -lt 20 ] || { echo 'appointment lock busy' >&2; exit 1; }
    sleep 1
  done
  trap 'rmdir "$root/lock"' EXIT HUP INT TERM
fi
old=
if [ -f "$registry" ]; then
  old=$(awk -F '\t' -v k="$key" '$1==k {n++; print $2} END {if(n>1) exit 9}' "$registry") ||
    { echo 'duplicate appointment record' >&2; exit 1; }
fi
live=false
if [ -n "$old" ]; then
  case "$old" in *[!a-zA-Z0-9_-]*|'') echo 'invalid stored ID' >&2; exit 1;; esac
  if ! meta=$(antonina agent status --id "$old" --json 2>/dev/null); then
    # A transient status-query failure is NOT evidence of a dead agent.
    # Replacing it could create a second live agent on the same worktree.
    echo "Viche: status of appointed agent $old is unreadable; refuse replacement until a terminal status is proven" >&2
    exit 1
  fi
  status=$(printf '%s\n' "$meta" | jq -er '.state') || exit 1
  # One "unknown" sample is a transient runtime observation, not a terminal
  # state: re-probe a bounded number of times before deciding. A persistent
  # unknown still fails closed for mutations below.
  probe=0
  while [ "$status" = unknown ] && [ "$probe" -lt 3 ]; do
    probe=$((probe + 1))
    sleep 1
    if meta=$(antonina agent status --id "$old" --json 2>/dev/null); then
      status=$(printf '%s\n' "$meta" | jq -er '.state' 2>/dev/null) || status=unknown
    else
      status=unknown
    fi
  done
  case "$status" in
    running|idle|clearexit) live=true;;
    failed|stopped|killed) :;;
    *)
      # A transient or unrecognized status (e.g. Antonina reporting "unknown"
      # while a session transitions or recovers) is not evidence of a dead
      # agent. Identity resolution must not fail for it, or a single transient
      # sample breaks every caller (sitting, liveness, oversight). Mutations
      # still require a positively identified terminal state.
      if [ "$action" = resolve ]; then live=unknown
      else echo "Viche: appointed agent $old still reports '$status' after $probe re-probe(s); refuse $action until a terminal state is proven" >&2; exit 1
      fi;;
  esac
fi
if [ "$action" = replace ] && [ -n "$expected" ] && [ "$old" != "$expected" ]; then
  echo "Viche: stale recovery appointment $expected for $key; actual is $old" >&2
  exit 1
fi
# Never register two live workers for the same worktree. A threshold reset of
# an oscillating, currently running agent must quiesce it first.
if [ "$action" = replace ] && [ "${status:-}" = running ]; then
  echo "Viche: running appointee $old must be stopped before replacement" >&2
  exit 1
fi
if [ "$action" = resolve ]; then
  [ -n "$old" ] || { echo "no appointment for $key" >&2; exit 1; }
  printf '%s\n' "$old"
  exit 0
fi
# Constitution VIII requires continuity after the box restarts. A runner
# physically lost during a positively identified PID1 restart is NOT an
# Antonina-model transient-error reset under Act19 §3.1. Replace its dead
# *appointment*, never resume the interrupted prompt or old session.
# Do not bypass any unsafe prompt hold; those require an independent review.
restart_orphan=no
if [ "$action" = ensure ] && [ -n "$old" ] && [ "${status:-}" = failed ] &&
   [ ! -s "${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/liveness/unsafe-holds/$key" ] &&
   [ -s "$town/government/restart-orphan.sh" ] &&
   printf '%s\n' "$meta" | /bin/sh "$town/government/restart-orphan.sh"; then
  restart_orphan=yes
  expected=$old
  caller=appointments.ensure
  trigger=restart_orphan
  reason='confirmed PID1 restart orphan; no prompt replay'
  action=replace
fi
# Founder directive 2026-11-16: an idle office whose conversation has grown
# too large is given a fresh session with a short handover note, instead of
# re-reading one ever-growing conversation every cycle. Only a positively
# idle/clearexit appointee rotates; a running, failed or held one never does.
rotation=no
if [ "$action" = ensure ] && [ -n "$old" ] && [ "$live" = true ] &&
   { [ "${status:-}" = idle ] || [ "${status:-}" = clearexit ]; } &&
   [ ! -s "${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/liveness/unsafe-holds/$key" ] &&
   [ "${VICHE_SESSION_ROTATION:-on}" != off ] &&
   [ -f "$town/government/handover.sh" ] &&
   /bin/sh "$town/government/handover.sh" due "$old"; then
  rotation=yes
  expected=$old
  caller=appointments.ensure
  trigger=session_rotation
  reason='conversation too large; fresh session with handover note'
  action=replace
fi
if [ "$action" = ensure ] && [ -n "$old" ]; then
  # Backend failures remain assigned until lawful Act19 recovery or explicit
  # review. An uncertain process disappearance outside the restart signature
  # is NOT evidence of a safe automatic retry.
  printf '%s\n' "$old"
  exit 0
fi
if [ "$action" = replace ] && [ "$old" != "$expected" ]; then
  echo "Viche: stale recovery appointment $expected for $key; actual is $old" >&2
  exit 1
fi
# The Act 19 supervisors need evidence of real failed invocations. Historically
# 'ensure' replaced a failed appointee BEFORE they could observe it. Capture
# exact terminal status, last log and worktree identity BEFORE replacement.
# Record at most once per disposable agent ID, even across repeated cycles.
# This does not authorize replay of an unsafe failed prompt or claim that a
# first-failure replacement met Act 19's reset threshold.
if [ -n "$old" ] && [ "$live" != true ]; then
  observed=${meta:-'{"state":"unreadable"}'}
  printf '%s\n' "$observed" |
    /bin/sh "$(CDPATH= cd "$(dirname "$0")" && pwd -P)/terminal-appointment-evidence.sh" "$key" "$old" "$cwd" ||
      { echo "Cannot preserve evidence of departing agent $old" >&2; exit 1; }
fi
# An old Git branch may carry a retired model or scope restriction.
# Refresh only idle appointees, not worktrees of currently running agents.
if [ -s "$town/AGENTS.md" ] && { [ -f "$cwd/.git" ] || [ -d "$cwd/.git" ]; } &&
   { [ "$live" != true ] || [ "$status" != running ]; }; then
  /bin/sh "$town/government/policy-sync.sh" "$cwd" ||
    { echo "Cannot dispatch $key: stale instructions could not be repaired" >&2; exit 1; }
fi
if [ "$live" = true ] && [ "$action" = ensure ]; then
  printf '%s\n' "$old"
  exit 0
fi
new=
transaction=
if [ "$action" = replace ] && [ -d "$root/replacement-intents" ]; then
  for candidate_intent in "$root"/replacement-intents/*.json; do
    [ -f "$candidate_intent" ] || continue
    if jq -e --arg office "$key" --arg prior "$old" --arg caller "$caller" \
      --arg trigger "$trigger" --arg reason "$reason" \
      '.state=="prepared" and .office==$office and .expected_prior_id==$prior and
       .caller==$caller and .trigger==$trigger and .reason==$reason' \
      "$candidate_intent" >/dev/null 2>&1; then
      candidate=$(jq -r '.proposed_successor' "$candidate_intent")
      if candidate_meta=$(antonina agent status --id "$candidate" --json 2>/dev/null) &&
         [ "$(printf '%s\n' "$candidate_meta" | jq -r '.state')" = idle ]; then
        new=$candidate
        transaction=$(jq -r '.transaction' "$candidate_intent")
        intent=$candidate_intent
        break
      fi
    fi
  done
fi
if [ -z "$new" ]; then
  new=$(antonina agent new --cwd "$cwd" --title "Viche: $title") || exit 1
fi
case "$new" in ''|*[!a-zA-Z0-9_-]*) echo 'malformed new agent ID' >&2; exit 1;; esac
[ "$new" != "$old" ] || { echo 'new agent reused old ID' >&2; exit 1; }
meta=$(antonina agent status --id "$new" --json) || exit 1
[ "$(printf '%s\n' "$meta" | jq -r '.state')" = idle ] || exit 1
if [ "$rotation" = yes ]; then
  # Written before the registry swap; a missing note never blocks the office.
  /bin/sh "$town/government/handover.sh" write "$key" "$old" "$new" ||
    echo "Viche: handover note for $key could not be written" >&2
fi
if [ -z "$transaction" ]; then transaction=$(date -u +%Y%m%dT%H%M%SZ)-$$-$key-$new; fi
tmp=$(mktemp "$root/roster.XXXXXXXX")
if [ -f "$registry" ]; then awk -F '\t' -v k="$key" '$1!=k {print}' "$registry" > "$tmp"; fi
printf '%s\t%s\n' "$key" "$new" >> "$tmp"
if [ "$action" = replace ]; then
  if [ -z "${intent:-}" ]; then
    prepared=$(mktemp "$root/replacement-intent.XXXXXXXX")
    jq -cn --arg transaction "$transaction" --arg at "$(date -u +%FT%TZ)" --arg office "$key" \
      --arg previous "$old" --arg successor "$new" --arg caller "$caller" \
      --arg trigger "$trigger" --arg reason "$reason" \
      '{transaction:$transaction,at:$at,state:"prepared",office:$office,
        expected_prior_id:$previous,proposed_successor:$successor,caller:$caller,
        trigger:$trigger,reason:$reason}' > "$prepared"
    mkdir -p "$root/replacement-intents"
    intent=$root/replacement-intents/$transaction.json
    mv -f "$prepared" "$intent"
  fi
fi
if [ "${VICHE_TEST_FAIL_REGISTRY_SWAP:-}" = yes ]; then
  rm -f "$tmp"
  echo 'injected registry swap failure' >&2
  exit 1
fi
if ! mv -f "$tmp" "$registry"; then
  rm -f "$tmp"
  echo 'appointment registry swap failed; prior registry remains authoritative' >&2
  exit 1
fi
# Registry plus the durable prepared intent is the commit/reconciliation
# evidence. Failure to install the committed provenance row leaves the intent
# prepared and cannot turn an already-committed replacement into a failed call.
if [ "$action" = replace ]; then
  provenance=$root/replacement-provenance.jsonl
  provenance_tmp=$(mktemp "$root/replacement-provenance.XXXXXXXX")
  copied=true
  if [ -f "$provenance" ]; then
    cp "$provenance" "$provenance_tmp" 2>/dev/null || copied=false
  fi
  if [ "$copied" = true ] && jq -c --arg at "$(date -u +%FT%TZ)" \
      '. + {state:"committed",completed_at:$at,successor:.proposed_successor}' "$intent" \
      >> "$provenance_tmp" 2>/dev/null; then
    if [ "${VICHE_TEST_FAIL_PROVENANCE_RENAME:-}" != yes ] &&
       mv -f "$provenance_tmp" "$provenance" 2>/dev/null; then
      rm -f "$intent" 2>/dev/null || :
    else
      rm -f "$provenance_tmp" 2>/dev/null || :
    fi
  else
    rm -f "$provenance_tmp" 2>/dev/null || :
  fi
fi
printf '%s\t%s\t%s\t%s\n' "$(date -u +%FT%TZ)" "$key" "${old:--}" "$new" >> "$root/appointments.log" 2>/dev/null || :
if [ "$restart_orphan" = yes ]; then
  # A discrete audited incarnation handoff, not an Act19 transient reset.
  # The terminal evidence directory was persisted before the new appointment.
  jq -cn --arg at "$(date -u +%FT%TZ)" --arg office "$key" \
    --arg previous "$old" --arg successor "$new" \
    --arg evidence "terminal-evidence/$old" \
    '{at:$at,kind:"container_restart_orphan_new_appointment_no_prompt_replay",
      office:$office,previous:$previous,successor:$successor,
       evidence:$evidence}' >> "$root/restart-renewals.jsonl" 2>/dev/null || :
fi
printf '%s\n' "$new"
