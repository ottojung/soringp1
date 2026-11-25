#!/bin/sh
# Fresh office sessions with a short handover note (Founder directive,
# 2026-11-16). POSIX /bin/sh. No model call: the note is assembled from the
# outgoing session's own last reports and pointers to durable records.
#
#   handover.sh due ID
#       Exit 0 when the appointee ID is idle and its conversation is large
#       enough to replace: its last model request carried at least
#       VICHE_ROTATE_CONTEXT_TOKENS of context (default 120000), or it has
#       accepted at least VICHE_ROTATE_PROMPTS prompts (default 150).
#       Exit 1 otherwise, including whenever the evidence is unreadable.
#   handover.sh write KEY OLD_ID NEW_ID
#       Write the handover note for office KEY from OLD_ID to NEW_ID.
#   handover.sh show KEY ID
#       Print the note when ID is its successor and has not yet received a
#       prompt. Prints nothing otherwise. Never fails the caller.
#
# Why: one Clerk conversation reached 2,966 prompts and a median of 152K
# (max 892K) context tokens per model step; every sitting re-read all of it.
# Durable records, not a conversation, are the Town's memory (Constitution
# VIII), so a successor loses nothing that is actually authoritative.
set -eu
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
town=${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}
dir=$state/handover
cmd=${1:-}

valid_id() { case "$1" in ''|*[!a-zA-Z0-9_-]*) return 1;; esac; return 0; }

case "$cmd" in
  due)
    [ "$#" -eq 2 ] && valid_id "$2" || exit 2
    meta=$(antonina agent status --id "$2" --json 2>/dev/null) || exit 1
    st=$(printf '%s\n' "$meta" | jq -r '.state // empty' 2>/dev/null) || exit 1
    case "$st" in idle|clearexit) :;; *) exit 1;; esac
    prompts=$(printf '%s\n' "$meta" | jq -r '.prompts // 0' 2>/dev/null) || exit 1
    case "$prompts" in ''|*[!0-9]*) exit 1;; esac
    [ "$prompts" -gt 0 ] || exit 1
    if [ "$prompts" -ge "${VICHE_ROTATE_PROMPTS:-150}" ]; then exit 0; fi
    context=$(antonina agent log --id "$2" --lines 400 2>/dev/null | python3 -c '
import json, sys
last = 0
for line in sys.stdin:
    if not line.startswith("{\"type\":\"step_finish\""):
        continue
    try:
        tokens = json.loads(line)["part"].get("tokens") or {}
    except Exception:
        continue
    last = int(tokens.get("input", 0)) + int((tokens.get("cache") or {}).get("read", 0))
print(last)
' 2>/dev/null) || exit 1
    case "$context" in ''|*[!0-9]*) exit 1;; esac
    [ "$context" -ge "${VICHE_ROTATE_CONTEXT_TOKENS:-120000}" ]
    ;;
  write)
    [ "$#" -eq 4 ] && valid_id "$2" && valid_id "$3" && valid_id "$4" || exit 2
    key=$2 old=$3 new=$4
    mkdir -p "$dir"
    umask 077
    tmp=$(mktemp "$dir/.note.XXXXXX")
    {
      printf 'successor: %s\n' "$new"
      printf 'predecessor: %s\n' "$old"
      printf 'office: %s\n' "$key"
      printf 'rotated_at: %s\n' "$(date -u +%FT%TZ)"
      printf '%s\n' '---'
      printf 'You are a FRESH session for office %s. Your predecessor %s was\n' "$key" "$old"
      printf 'retired because its conversation had grown too large to re-read every cycle.\n'
      printf 'Its conversation is NOT available to you and is NOT authority. The\n'
      printf 'authoritative state is durable: Git records under %s/records,\n' "$town"
      printf 'records/handoffs/, the Town Hall cursor, the Antonina board, and %s.\n' "$state"
      printf 'Do not redo work your predecessor finished; verify it from those records.\n'
      printf 'Do not repeat external actions (posts, merges, dispatches) without checking.\n'
      printf '\nPredecessor'"'"'s last reports (newest last, truncated):\n'
      antonina agent log --id "$old" --lines 3000 2>/dev/null | python3 -c '
import json, sys
texts = []
for line in sys.stdin:
    if not line.startswith("{\"type\":\"text\""):
        continue
    try:
        text = (json.loads(line)["part"].get("text") or "").strip()
    except Exception:
        continue
    if text:
        texts.append(" ".join(text.split()))
for text in texts[-3:]:
    print("- " + (text[:900] + " [...]" if len(text) > 900 else text))
if not texts:
    print("- (no readable report; reconstruct from durable records)")
' 2>/dev/null || printf '%s\n' '- (predecessor log unreadable; reconstruct from durable records)'
    } > "$tmp"
    mv -f "$tmp" "$dir/$key.md"
    printf '%s\t%s\t%s\t%s\n' "$(date -u +%FT%TZ)" "$key" "$old" "$new" >> "$dir/rotations.log"
    ;;
  show)
    [ "$#" -eq 3 ] && valid_id "$2" && valid_id "$3" || exit 0
    note=$dir/$2.md
    [ -s "$note" ] || exit 0
    [ "$(sed -n 's/^successor: //p' "$note" | head -n 1)" = "$3" ] || exit 0
    prompts=$(antonina agent status --id "$3" --json 2>/dev/null | jq -r '.prompts // empty' 2>/dev/null) || exit 0
    [ "$prompts" = 0 ] || exit 0
    printf '\n=== HANDOVER NOTE (fresh session) ===\n'
    sed '1,/^---$/d' "$note"
    printf '=== END HANDOVER NOTE ===\n'
    ;;
  *)
    echo 'usage: handover.sh due ID | write KEY OLD NEW | show KEY ID' >&2
    exit 2
    ;;
esac
