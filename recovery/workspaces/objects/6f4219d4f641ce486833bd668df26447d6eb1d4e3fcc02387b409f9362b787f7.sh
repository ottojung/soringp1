#!/bin/sh
# Independent read-only health checks. Do not source or execute town code.
set -eu
state=${VICHE_SENTINEL_STATE:-/var/lib/lubko/wd/viche-sentinel-state}
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
watch=${VICHE_OVERSIGHT_STATE:-/var/lib/lubko/wd/viche-state/oversight}/observations.tsv
govstamp=${VICHE_GOV_HEALTH_STATE:-/var/lib/lubko/wd/viche-state/health}/government-setup.last
svc=${VICHE_GOV_SERVICE:-/run/service/viche}
now=${VICHE_SENTINEL_NOW:-$(date +%s)}
case "$now" in ''|*[!0-9]*) exit 2;; esac
mkdir -p "$state"
umask 077
exec 9>"$state/check.lock"
flock -n 9 || exit 0
signals=
add() { case ",$signals," in *",$1,"*) :;; *) signals=${signals:+$signals,}$1;; esac; }
# Read-only Git probe with bounded retry/backoff. A transient timeout (exit 124
# from `timeout`) is retried after a short backoff; a genuine Git error is not
# retried (it will not heal on its own). On success sets GIT_PROBE_OUT to stdout
# and GIT_PROBE_STATUS=ok, and returns 0. On persistent failure (all attempts
# exhausted) returns 1 with GIT_PROBE_STATUS=timeout|error and GIT_PROBE_OUT
# empty. GIT_PROBE_SAW_TIMEOUT is 1 if any attempt timed out, so a slow-but-
# healthy repo is distinguishable from a genuine failure.
#
# This removes a measurement-sensitivity artifact: under high load a read-only
# Git call can exceed the per-attempt timeout, which the old code reported as
# `government_git_unreadable` (a false alarm). Detection is NOT weakened: a
# persistent failure still emits government_git_unreadable /
# government_git_refs_unavailable, plus a distinct `government_git_probe_timeout`
# signal so a timeout is distinguishable from a genuine Git error.
git_probe() {
    attempts_max=${VICHE_SENTINEL_GIT_PROBE_ATTEMPTS:-3}
    timeout_s=${VICHE_SENTINEL_GIT_PROBE_TIMEOUT:-12}
    backoff_s=${VICHE_SENTINEL_GIT_PROBE_BACKOFF:-1}
    case "$attempts_max" in ''|*[!0-9]*) attempts_max=3;; esac
    [ "$attempts_max" -ge 1 ] || attempts_max=1
    case "$timeout_s" in ''|*[!0-9]*) timeout_s=12;; esac
    [ "$timeout_s" -ge 1 ] || timeout_s=1
    case "$backoff_s" in ''|*[!0-9]*) backoff_s=1;; esac
    [ "$backoff_s" -ge 0 ] || backoff_s=0
    GIT_PROBE_ATTEMPTS=0
    GIT_PROBE_SAW_TIMEOUT=0
    GIT_PROBE_STATUS=error
    GIT_PROBE_OUT=
    while [ "$GIT_PROBE_ATTEMPTS" -lt "$attempts_max" ]; do
        GIT_PROBE_ATTEMPTS=$((GIT_PROBE_ATTEMPTS+1))
        rc=0
        GIT_PROBE_OUT=$(timeout "$timeout_s" "$@" 2>/dev/null) || rc=$?
        if [ "$rc" -eq 0 ]; then
            GIT_PROBE_STATUS=ok
            return 0
        fi
        if [ "$rc" -eq 124 ]; then
            GIT_PROBE_STATUS=timeout
            GIT_PROBE_SAW_TIMEOUT=1
            if [ "$GIT_PROBE_ATTEMPTS" -lt "$attempts_max" ]; then
                sleep "$backoff_s"
            fi
        else
            GIT_PROBE_STATUS=error
            break
        fi
    done
    return 1
}
service=unknown
if live=$(timeout 12 s6-svstat "$svc" 2>/dev/null); then
    case "$live" in 'up (pid '*) service=up;; *) service=down; add government_service_down;; esac
else add government_service_unknown; fi
git_status=ok
ahead=-1; behind=-1
if [ ! -d "$town/.git" ]; then
    git_status=missing; add government_checkout_missing
else
    if git_probe git -C "$town" ls-files -u; then
        if [ -n "$GIT_PROBE_OUT" ]; then git_status=conflicted; add government_git_conflict; fi
        if [ "$GIT_PROBE_SAW_TIMEOUT" -eq 1 ]; then
            echo "Sentinel: git status probe recovered after $GIT_PROBE_ATTEMPTS attempt(s); transient slowness, not unreadable" >&2
        fi
    else
        git_status=unreadable; add government_git_unreadable
        if [ "$GIT_PROBE_STATUS" = timeout ]; then add government_git_probe_timeout; fi
    fi
    if [ -f "$town/.git/MERGE_HEAD" ]; then add government_merge_incomplete; fi
    if git_probe git -C "$town" rev-list --left-right --count HEAD...refs/remotes/origin/main; then
        counts=$GIT_PROBE_OUT
        ahead=$(printf '%s\n' "$counts" | awk '{print $1}')
        behind=$(printf '%s\n' "$counts" | awk '{print $2}')
        case "$ahead:$behind" in *[!0-9:]*|'':*) add government_git_refs_invalid;; *)
            if [ "$ahead" -gt 0 ] && [ "$behind" -gt 0 ]; then add government_git_diverged
            elif [ "$ahead" -gt 0 ]; then add government_unpublished_main
            elif [ "$behind" -gt 0 ]; then add government_update_pending; fi
        ;; esac
        if [ "$GIT_PROBE_SAW_TIMEOUT" -eq 1 ]; then
            echo "Sentinel: git refs probe recovered after $GIT_PROBE_ATTEMPTS attempt(s); transient slowness, not unavailable" >&2
        fi
    else
        add government_git_refs_unavailable
        if [ "$GIT_PROBE_STATUS" = timeout ]; then add government_git_probe_timeout; fi
    fi
fi
setup_age=-1
if [ -s "$govstamp" ]; then
    stamp=$(cat "$govstamp")
    case "$stamp" in ''|*[!0-9]*) add government_setup_stamp_invalid;; *)
        if [ "$stamp" -le "$now" ]; then
            setup_age=$((now-stamp))
            [ "$setup_age" -le 7200 ] || add government_setup_stale
        else add government_setup_stamp_future; fi
    ;; esac
else add government_setup_stamp_missing; fi
watch_age=-1
if [ -s "$watch" ]; then
    stamp=$(tail -n 1 "$watch" | cut -f1)
    case "$stamp" in ''|*[!0-9]*) add oversight_stamp_invalid;; *)
        if [ "$stamp" -le "$now" ]; then
            watch_age=$((now-stamp))
            [ "$watch_age" -le 7200 ] || add oversight_stale
        else add oversight_stamp_future; fi
    ;; esac
else add oversight_missing; fi
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$now" "$service" "$git_status" "$ahead" "$behind" "$setup_age" "$watch_age" "${signals:-clear}" >> "$state/checks.tsv"
if [ -z "$signals" ]; then
    if [ -s "$state/incident.json" ]; then
        jq -c --argjson now "$now" '. + {closed_at:$now,closure:"health_signals_clear_not_delivery_verified"}' "$state/incident.json" >> "$state/history.jsonl"
        rm -f "$state/incident.json"
    fi
else
    first=$now
    if [ -s "$state/incident.json" ]; then
        earlier=$(jq -r '.first_seen // 0' "$state/incident.json" 2>/dev/null) || earlier=0
        case "$earlier" in ''|*[!0-9]*) :;; *) [ "$earlier" -gt 0 ] && [ "$earlier" -le "$now" ] && first=$earlier;; esac
    fi
    tmp=$(mktemp "$state/incident.XXXXXXXX")
    jq -n --argjson first "$first" --argjson now "$now" --arg signals "$signals" --arg service "$service" --arg git "$git_status" --arg ahead "$ahead" --arg behind "$behind" --argjson setup "$setup_age" --argjson watch "$watch_age" '{first_seen:$first,observed_at:$now,signals:($signals|split(",")),service:$service,git:$git,local_ahead:$ahead,local_behind:$behind,government_setup_age_seconds:$setup,oversight_age_seconds:$watch,meaning:"health_inquiry_required_not_delivery_verdict"}' > "$tmp"
    mv "$tmp" "$state/incident.json"
    if [ ! -e "$state/sent-$first" ] && [ ! -s "$state/pending-message" ]; then
        printf 'Viche Sentinel incident %s: %s. Service=%s, Git=%s, local ahead=%s behind=%s, government setup age=%ss, oversight age=%ss. Hourly deterministic health finding, not proof of Kawun delivery failure.\n' "$first" "$signals" "$service" "$git_status" "$ahead" "$behind" "$setup_age" "$watch_age" > "$state/pending-message"
        printf '%s\n' "$first" > "$state/pending-id"
    fi
fi
# Alert publication is optional; failed delivery stays in a durable outbox.
if [ -s "$state/pending-message" ] && [ -n "${VICHE_TOWNHALL_ID:-}" ]; then
    id=$(cat "$state/pending-id")
    if timeout 20 antonina board comment --id "$VICHE_TOWNHALL_ID" --author "Viche Sentinel" --body "$(cat "$state/pending-message")" >/dev/null 2>&1; then
        printf '%s\n' "$now" > "$state/sent-$id"
        rm -f "$state/pending-message" "$state/pending-id"
    else echo 'Sentinel: notification queued until Town Hall is reachable' >&2; fi
fi
printf '%s\n' "$now" > "$state/last-completed"
printf 'Sentinel: %s\n' "${signals:-clear}"

