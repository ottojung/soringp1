#!/bin/sh
# Skip a model dispatch when nothing the office reads has changed (Founder
# directive 2026-11-16, item 4). Measured cost of not having this: the
# Executive ran 222 times in 18 hours at about 105K tokens a pass, and 175 of
# 223 reports opened with the same recovery note.
#
#   dispatch-gate.sh check KEY [MAX_AGE_SECONDS] < normalized-inputs
#       exit 0   dispatch (stdout says why: first_pass, inputs_changed,
#                heartbeat or gate_off)
#       exit 10  skip: inputs are byte-identical to the last dispatched pass
#                and that pass is younger than MAX_AGE_SECONDS (default 21600)
#   dispatch-gate.sh commit KEY
#       record the fingerprint from the last `check` as dispatched. Call it
#       only after the dispatch was accepted; if it is not called the next
#       cycle dispatches again, so a failed launch never silences an office.
#   dispatch-gate.sh board-signature ISSUE...
#       print "<issue> <updatedAt> <latest-message-id>" per issue; a cheap
#       stable summary of Founder/agent activity. Exits 1 if any lookup fails
#       so callers can fail open (a broken probe must never suppress work).
#   dispatch-gate.sh stats [SINCE_EPOCH]
#       print "<key> <dispatches> <skips>" counted from the event log.
#
# VICHE_DISPATCH_GATE=off disables skipping entirely. A heartbeat guarantees
# every gated office still runs at least once per MAX_AGE_SECONDS.
set -eu
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
dir=$state/dispatch-gate
cmd=${1:-}
[ -n "$cmd" ] || { echo 'usage: dispatch-gate.sh check|commit|board-signature|stats ...' >&2; exit 2; }
shift

case "$cmd" in
  board-signature)
    [ "$#" -ge 1 ] || exit 2
    for issue in "$@"; do
      case "$issue" in ''|*[!a-zA-Z0-9_-]*) echo "bad issue id $issue" >&2; exit 2 ;; esac
      line=$(antonina board show --id "$issue" --page 1 --json 2>/dev/null |
             jq -r --arg n "$issue" '[$n, (.updatedAt // "-"), (.messages[0].id // "-")] | join(" ")') || exit 1
      [ -n "$line" ] || exit 1
      printf '%s\n' "$line"
    done
    ;;
  check|commit)
    [ "$#" -ge 1 ] || exit 2
    key=$1
    case "$key" in ''|*[!a-zA-Z0-9_-]*) echo 'invalid gate key' >&2; exit 2 ;; esac
    umask 077
    mkdir -p "$dir"
    now=$(date +%s)
    json=$dir/$key.json
    pending=$dir/$key.pending
    events=$dir/events.tsv
    if [ "$cmd" = commit ]; then
      [ -s "$pending" ] || exit 0
      fp=$(cut -f 1 "$pending")
      prev_total=0
      [ ! -s "$json" ] || prev_total=$(jq -r '.total_dispatches // 0' "$json" 2>/dev/null || echo 0)
      prev_skips=0
      [ ! -s "$json" ] || prev_skips=$(jq -r '.total_skips // 0' "$json" 2>/dev/null || echo 0)
      tmp=$(mktemp "$dir/.tmp.XXXXXX")
      jq -n --arg fp "$fp" --argjson now "$now" --argjson t "$((prev_total+1))" --argjson s "$prev_skips" \
        '{fingerprint:$fp,last_dispatch_at:$now,skips_since_dispatch:0,total_dispatches:$t,total_skips:$s}' > "$tmp"
      mv -f "$tmp" "$json"
      printf '%s\t%s\tdispatch\t%s\n' "$now" "$key" "$(cut -f 2 "$pending")" >> "$events"
      rm -f "$pending"
      exit 0
    fi
    max_age=${2:-21600}
    case "$max_age" in ''|*[!0-9]*) max_age=21600 ;; esac
    # Act 31: a change in the office's own deliveries (landed, rejected, red,
    # conflict) is an input of every office, so the proposer wakes to act on it.
    fp=$({ cat; cat "$state/delivery/office/$key.json" 2>/dev/null || :; } | sha256sum | cut -d ' ' -f 1)
    reason=
    if [ "${VICHE_DISPATCH_GATE:-on}" = off ]; then
      reason=gate_off
    elif [ ! -s "$json" ]; then
      reason=first_pass
    else
      last_fp=$(jq -r '.fingerprint // ""' "$json" 2>/dev/null || echo '')
      last_at=$(jq -r '.last_dispatch_at // 0' "$json" 2>/dev/null || echo 0)
      case "$last_at" in ''|*[!0-9]*) last_at=0 ;; esac
      if [ "$fp" != "$last_fp" ]; then
        reason=inputs_changed
      elif [ $((now-last_at)) -ge "$max_age" ]; then
        reason=heartbeat
      fi
    fi
    if [ -n "$reason" ]; then
      printf '%s\t%s\n' "$fp" "$reason" > "$pending"
      printf '%s\n' "$reason"
      exit 0
    fi
    skips=0
    total=0
    last_dispatch=$now
    if [ -s "$json" ]; then
      skips=$(jq -r '.skips_since_dispatch // 0' "$json" 2>/dev/null || echo 0)
      total=$(jq -r '.total_skips // 0' "$json" 2>/dev/null || echo 0)
      last_dispatch=$(jq -r '.last_dispatch_at // 0' "$json" 2>/dev/null || echo "$now")
    fi
    tmp=$(mktemp "$dir/.tmp.XXXXXX")
    jq --argjson s "$((skips+1))" --argjson t "$((total+1))" --argjson now "$now" \
       '.skips_since_dispatch=$s | .total_skips=$t | .last_skip_at=$now' "$json" > "$tmp"
    mv -f "$tmp" "$json"
    printf '%s\t%s\tskip\tunchanged\n' "$now" "$key" >> "$events"
    echo "unchanged since $last_dispatch"
    exit 10
    ;;
  stats)
    since=${1:-0}
    case "$since" in ''|*[!0-9]*) since=0 ;; esac
    [ -s "$dir/events.tsv" ] || exit 0
    awk -F '\t' -v since="$since" '$1 >= since {if ($3=="dispatch") d[$2]++; else if ($3=="skip") s[$2]++; seen[$2]=1}
      END {for (k in seen) printf "%s\t%d\t%d\n", k, d[k], s[k]}' "$dir/events.tsv" | sort
    ;;
  *)
    echo "unknown command: $cmd" >&2
    exit 2
    ;;
esac
