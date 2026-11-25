#!/bin/sh
# Durable per-ID terminal evidence before any appointment replacement.
# Never modify the old agent or worktree. Caller serializes normal mutations.
set -eu
[ "$#" -eq 3 ] || { echo 'Usage: terminal-appointment-evidence.sh KEY ID CWD' >&2; exit 2; }
key=$1 id=$2 cwd=$3
case "$key:$id" in *[!a-zA-Z0-9_:-]*|'') echo 'Invalid terminal appointment key' >&2; exit 2;; esac
umask 077
root=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}/appointments
mkdir -p "$root/terminal-evidence"
dest=$root/terminal-evidence/$id
index=$root/terminal-events.jsonl

if [ ! -d "$dest" ]; then
    tmp=$(mktemp -d "$root/.terminal-XXXXXXXX") || exit 1
    trap 'rm -rf "$tmp"' EXIT HUP INT TERM
    cat > "$tmp/status.json"
    jq -e 'type=="object" and (.state | type=="string")' "$tmp/status.json" >/dev/null ||
      { echo 'Malformed terminal appointment evidence' >&2; exit 1; }
    state=$(jq -r '.state' "$tmp/status.json")
    case "$state" in
      failed|killed|stopped|unreadable) : ;;
      *) echo "Refusing to log nonterminal state: $state" >&2; exit 1 ;;
    esac

    # Diagnostic capture is best-effort, but failure is explicitly recorded.
    log_ok=false
    log_truncated=false
    if timeout 10 antonina agent log --id "$id" --lines 80 > "$tmp/log-tail.txt" 2> "$tmp/log-error.txt"; then
        log_ok=true
    fi
    log_bytes=$(wc -c < "$tmp/log-tail.txt")
    if [ "$log_bytes" -gt 131072 ]; then
        head -c 131072 "$tmp/log-tail.txt" > "$tmp/log-limited.txt"
        mv "$tmp/log-limited.txt" "$tmp/log-tail.txt"
        log_truncated=true
    fi
    head_ok=false
    if timeout 10 git -C "$cwd" rev-parse HEAD > "$tmp/worktree-head.txt" 2> "$tmp/head-error.txt"; then
        head_ok=true
    else
        printf 'unavailable\n' > "$tmp/worktree-head.txt"
    fi
    worktree_ok=false
    if timeout 10 git -C "$cwd" status --short > "$tmp/worktree-status.txt" 2> "$tmp/worktree-error.txt"; then
        worktree_ok=true
    else
        printf 'UNAVAILABLE: unable to establish worktree status\n' > "$tmp/worktree-status.txt"
    fi

    jq -cn --arg key "$key" --arg id "$id" --arg cwd "$cwd" \
      --arg at "$(date -u +%FT%TZ)" --argjson log_ok "$log_ok" \
      --argjson log_truncated "$log_truncated" --argjson head_ok "$head_ok" \
      --argjson worktree_ok "$worktree_ok" --slurpfile m "$tmp/status.json" \
      '{at:$at, office:$key, agent_id:$id, cwd:$cwd, state:$m[0].state,
        finished_at:($m[0].finished_at//null), prompts:($m[0].prompts//null),
        failure_class:($m[0].backend_error.classification//null),
        transient:$m[0].backend_error.transient,
        automatic_retry_safe:$m[0].backend_error.automatic_retry_safe,
        log_captured:$log_ok, log_truncated:$log_truncated,
        worktree_head_captured:$head_ok, worktree_status_captured:$worktree_ok,
        evidence:("terminal-evidence/" + $id)}' > "$tmp/event.json"
    mv "$tmp" "$dest"
    trap - EXIT HUP INT TERM
fi

# An earlier process may crash after moving the evidence dir but before indexing.
# The appointment lock serializes these calls; repair the missing index row.
[ -s "$dest/event.json" ] ||
  { echo "Incomplete terminal snapshot for $id" >&2; exit 1; }
if ! { [ -f "$index" ] && grep -Fq "\"agent_id\":\"$id\"" "$index"; }; then
    cat "$dest/event.json" >> "$index" ||
      { echo "Could not index terminal evidence for $id" >&2; exit 1; }
fi
echo "Viche: retained terminal appointment $id before replacement" >&2
