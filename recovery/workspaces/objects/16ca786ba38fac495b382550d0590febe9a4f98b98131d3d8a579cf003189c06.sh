#!/bin/sh
# Act 19 §3.2 durable handoff queue — the dispatch's single source of truth
# for office work intent. POSIX /bin/sh; no agent or network needed.
#
#   handoff-queue.sh add <town> <authority> <evidence> <work-item>
#       Atomically append a new open handoff; prints its unique id.
#   handoff-queue.sh list-open <town>
#       Print open handoffs, one per line: <created> <TAB> <id> <TAB> <work>,
#       oldest first. Empty output means no open handoff.
#   handoff-queue.sh mark <town> <id> done|superseded <note>
#       Atomically transition an open handoff to done/superseded.
#
# Each entry is one file at <town>/records/handoffs/<id>.txt. Writes are
# atomic (temp file + rename in the same directory), so a steer IS the queue
# entry at steer time — there is no separate "read the queue" step that a
# failure could skip between the steer and the durable record.
set -eu
[ "$#" -ge 2 ] || {
  echo "usage: handoff-queue.sh add|list-open|mark <town> ..." >&2
  exit 2
}
cmd=$1
town=$2
dir=$town/records/handoffs

case "$cmd" in
  add)
    [ "$#" -eq 5 ] || {
      echo "usage: handoff-queue.sh add <town> <authority> <evidence> <work-item>" >&2
      exit 2
    }
    authority=$3
    evidence=$4
    work=$5
    [ -n "$work" ] || {
      echo "work-item must not be empty" >&2
      exit 2
    }
    case "$work" in
      *'
'*) echo "work-item must be a single line" >&2; exit 2 ;;
    esac
    mkdir -p "$dir" || exit 1
    id=H-$(date +%s)-$(head -c 2 /dev/urandom | od -An -tx1 | tr -d ' \n')
    tmp=$(mktemp "$dir/.tmp.XXXXXX") || exit 1
    {
      printf 'id: %s\n' "$id"
      printf 'status: open\n'
      printf 'assigned-by: %s\n' "$authority"
      printf 'created: %s\n' "$(date -u +%FT%TZ)"
      printf 'evidence: %s\n' "$evidence"
      printf 'work: %s\n' "$work"
    } > "$tmp"
    mv -f "$tmp" "$dir/$id.txt"
    printf '%s\n' "$id"
    ;;
  list-open)
    [ -d "$dir" ] || exit 0
    for hof in "$dir"/*.txt; do
      [ -f "$hof" ] || continue
      hof_status=$(sed -n 's/^status:[[:space:]]*//p' "$hof" | head -n 1)
      [ "$hof_status" = open ] || continue
      hof_id=$(sed -n 's/^id:[[:space:]]*//p' "$hof" | head -n 1)
      hof_created=$(sed -n 's/^created:[[:space:]]*//p' "$hof" | head -n 1)
      hof_work=$(sed -n 's/^work:[[:space:]]*//p' "$hof" | head -n 1)
      printf '%s\t%s\t%s\n' "$hof_created" "$hof_id" "$hof_work"
    done | sort
    ;;
  mark)
    [ "$#" -eq 5 ] || {
      echo "usage: handoff-queue.sh mark <town> <id> done|superseded <note>" >&2
      exit 2
    }
    hof_id=$3
    hof_new=$4
    hof_note=$5
    case "$hof_new" in
      done|superseded) ;;
      *) echo "status must be done or superseded" >&2; exit 2 ;;
    esac
    hof_file=$dir/$hof_id.txt
    [ -f "$hof_file" ] || {
      echo "no such handoff: $hof_id" >&2
      exit 1
    }
    hof_status=$(sed -n 's/^status:[[:space:]]*//p' "$hof_file" | head -n 1)
    [ "$hof_status" = open ] || {
      echo "handoff $hof_id is $hof_status, not open" >&2
      exit 1
    }
    tmp=$(mktemp "$dir/.tmp.XXXXXX") || exit 1
    sed "s/^status: open\$/status: $hof_new/" "$hof_file" > "$tmp"
    printf 'closed: %s\nnote: %s\n' "$(date -u +%FT%TZ)" "$hof_note" >> "$tmp"
    mv -f "$tmp" "$hof_file"
    ;;
  *)
    echo "unknown command: $cmd" >&2
    exit 2
    ;;
esac
