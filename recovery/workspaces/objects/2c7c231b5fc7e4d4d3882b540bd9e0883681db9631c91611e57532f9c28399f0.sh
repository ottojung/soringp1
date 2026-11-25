#!/bin/sh
# Proceed-by-default ledger (Founder directive 2026-11-16, "Act 30").
#
# The rule: an office that needs something from another office files a
# REQUEST with a deadline (default 24h, never more than 72h). If the
# addressee has not answered by then, the requester may go ahead; the
# addressee (or the Judiciary) audits afterwards. Waiting is no longer the
# default. Irreversible acts are the exception: they never proceed by
# default, and `proceed` refuses them.
#
#   proceed-by-default.sh request TOWN REQUESTER ADDRESSEE HOURS CLASS ACTION...
#       CLASS is reversible|irreversible. Prints the request id.
#   proceed-by-default.sh answer  TOWN ID approved|declined NOTE...
#       Addressee answers before the deadline. `declined` ends the request.
#   proceed-by-default.sh proceed TOWN ID NOTE...
#       Requester records that it went ahead after the deadline passed.
#   proceed-by-default.sh audit   TOWN ID upheld|reversed|concern NOTE...
#       Addressee or Judiciary reviews an action taken by default.
#   proceed-by-default.sh sweep   TOWN
#       Mark pending requests whose deadline passed as `due`.
#   proceed-by-default.sh list    TOWN [pending|due|proceeded|all]
#   proceed-by-default.sh brief   TOWN OFFICE
#       Prompt block for OFFICE: requests it may proceed on, requests waiting
#       on it (with deadlines), and actions it must audit. Empty if none.
#
# One file per request at TOWN/records/proceed/P-<epoch>-<hex>.txt, written
# atomically; Git records keep the history (Act 5).
set -eu
cmd=${1:-}
[ -n "$cmd" ] || { echo 'usage: proceed-by-default.sh request|answer|proceed|audit|sweep|list|brief TOWN ...' >&2; exit 2; }
shift
[ "$#" -ge 1 ] || { echo 'TOWN required' >&2; exit 2; }
town=$1
shift
dir=$town/records/proceed
now=$(date +%s)
iso() { date -u -d "@$1" +%FT%TZ; }
field() { sed -n "s/^$2:[[:space:]]*//p" "$1" | head -n 1; }
epoch_of() {
  [ -n "$1" ] || { echo 0; return; }
  date -u -d "$1" +%s 2>/dev/null || echo 0
}
one_line() { printf '%s' "$*" | tr '\n\t' '  '; }
write_atomic() { # file <- stdin
  tmp=$(mktemp "$dir/.tmp.XXXXXX") || exit 1
  cat > "$tmp"
  mv -f "$tmp" "$1"
}
need_file() {
  file=$dir/$1.txt
  [ -f "$file" ] || { echo "no such request: $1" >&2; exit 1; }
  printf '%s\n' "$file"
}
set_status() { # file new_status note_key note
  tmp=$(mktemp "$dir/.tmp.XXXXXX") || exit 1
  sed "s/^status: .*\$/status: $2/" "$1" > "$tmp"
  printf '%s: %s\n%s-at: %s\n' "$3" "$(one_line "$4")" "$3" "$(iso "$now")" >> "$tmp"
  mv -f "$tmp" "$1"
}

case "$cmd" in
  request)
    [ "$#" -ge 5 ] || { echo 'usage: request TOWN REQUESTER ADDRESSEE HOURS CLASS ACTION...' >&2; exit 2; }
    requester=$1 addressee=$2 hours=$3 class=$4
    shift 4
    action=$(one_line "$*")
    case "$requester$addressee" in *[!a-zA-Z0-9_-]*|'') echo 'office names are [a-zA-Z0-9_-]+' >&2; exit 2 ;; esac
    case "$hours" in ''|*[!0-9]*|0) echo 'HOURS must be a positive integer' >&2; exit 2 ;; esac
    [ "$hours" -le 72 ] || { echo 'deadline may not exceed 72 hours' >&2; exit 2; }
    case "$class" in reversible|irreversible) : ;; *) echo 'CLASS must be reversible or irreversible' >&2; exit 2 ;; esac
    [ -n "$action" ] || { echo 'action text required' >&2; exit 2; }
    mkdir -p "$dir"
    id=P-$now-$(head -c 2 /dev/urandom | od -An -tx1 | tr -d ' \n')
    deadline=$((now + hours * 3600))
    {
      printf 'id: %s\nstatus: pending\nrequester: %s\naddressee: %s\nclass: %s\n' "$id" "$requester" "$addressee" "$class"
      printf 'created: %s\ndeadline: %s\naction: %s\n' "$(iso "$now")" "$(iso "$deadline")" "$action"
    } | write_atomic "$dir/$id.txt"
    printf '%s\n' "$id"
    ;;
  answer)
    [ "$#" -ge 3 ] || { echo 'usage: answer TOWN ID approved|declined NOTE...' >&2; exit 2; }
    id=$1 verdict=$2
    shift 2
    case "$verdict" in approved|declined) : ;; *) echo 'verdict must be approved or declined' >&2; exit 2 ;; esac
    file=$(need_file "$id")
    case "$(field "$file" status)" in pending|due) : ;; *) echo "request $id is $(field "$file" status)" >&2; exit 1 ;; esac
    set_status "$file" "$verdict" answer "$*"
    ;;
  proceed)
    [ "$#" -ge 2 ] || { echo 'usage: proceed TOWN ID NOTE...' >&2; exit 2; }
    id=$1
    shift
    file=$(need_file "$id")
    [ "$(field "$file" class)" = reversible ] ||
      { echo "request $id is irreversible; it never proceeds by default" >&2; exit 3; }
    case "$(field "$file" status)" in
      pending|due) : ;;
      approved) echo "request $id was approved; proceeding is covered by the approval" >&2; exit 0 ;;
      *) echo "request $id is $(field "$file" status), cannot proceed" >&2; exit 1 ;;
    esac
    [ "$now" -ge "$(epoch_of "$(field "$file" deadline)")" ] ||
      { echo "request $id deadline $(field "$file" deadline) has not passed" >&2; exit 1; }
    set_status "$file" proceeded proceed-note "$*"
    ;;
  audit)
    [ "$#" -ge 3 ] || { echo 'usage: audit TOWN ID upheld|reversed|concern NOTE...' >&2; exit 2; }
    id=$1 verdict=$2
    shift 2
    case "$verdict" in upheld|reversed|concern) : ;; *) echo 'verdict must be upheld, reversed or concern' >&2; exit 2 ;; esac
    file=$(need_file "$id")
    [ "$(field "$file" status)" = proceeded ] || { echo "request $id did not proceed by default" >&2; exit 1; }
    set_status "$file" "audited-$verdict" audit-note "$*"
    ;;
  sweep)
    [ -d "$dir" ] || exit 0
    for file in "$dir"/P-*.txt; do
      [ -f "$file" ] || continue
      [ "$(field "$file" status)" = pending ] || continue
      [ "$now" -ge "$(epoch_of "$(field "$file" deadline)")" ] || continue
      set_status "$file" due due-note 'deadline passed without an answer'
    done
    ;;
  list)
    which=${1:-all}
    [ -d "$dir" ] || exit 0
    for file in "$dir"/P-*.txt; do
      [ -f "$file" ] || continue
      st=$(field "$file" status)
      [ "$which" = all ] || [ "$which" = "$st" ] || continue
      printf '%s\t%s\t%s>%s\t%s\t%s\t%s\n' "$(field "$file" id)" "$st" "$(field "$file" requester)" \
        "$(field "$file" addressee)" "$(field "$file" class)" "$(field "$file" deadline)" "$(field "$file" action)"
    done
    ;;
  brief)
    [ "$#" -ge 1 ] || { echo 'usage: brief TOWN OFFICE' >&2; exit 2; }
    office=$1
    [ -d "$dir" ] || exit 0
    may= waiting= audit=
    for file in "$dir"/P-*.txt; do
      [ -f "$file" ] || continue
      st=$(field "$file" status)
      line="$(field "$file" id) | $(field "$file" requester) -> $(field "$file" addressee) | deadline $(field "$file" deadline) | $(field "$file" action)"
      case "$st" in
        pending|due)
          dl=$(epoch_of "$(field "$file" deadline)")
          if [ "$(field "$file" requester)" = "$office" ] && [ "$(field "$file" class)" = reversible ] && [ "$now" -ge "$dl" ]; then
            may="$may$line
"
          elif [ "$(field "$file" addressee)" = "$office" ]; then
            waiting="$waiting$line [class $(field "$file" class)]
"
          fi ;;
        proceeded)
          if [ "$(field "$file" addressee)" = "$office" ] || [ "$office" = judiciary ]; then
            audit="$audit$line | proceeded: $(field "$file" proceed-note)
"
          fi ;;
      esac
    done
    [ -n "$may$waiting$audit" ] || exit 0
    echo '=== PROCEED-BY-DEFAULT LEDGER (records/proceed/; Act 30) ==='
    if [ -n "$may" ]; then
      echo 'DEADLINE PASSED, NO ANSWER: you may now proceed on these reversible requests. Do the work, then run'
      echo "government/proceed-by-default.sh proceed $town ID NOTE   (do not wait any longer):"
      printf '%s' "$may"
    fi
    if [ -n "$waiting" ]; then
      echo 'WAITING ON YOU: answer before the deadline, or the requester proceeds without you and you audit afterwards'
      echo "(government/proceed-by-default.sh answer $town ID approved|declined NOTE):"
      printf '%s' "$waiting"
    fi
    if [ -n "$audit" ]; then
      echo 'PROCEEDED BY DEFAULT, AWAITING YOUR AFTER-THE-FACT AUDIT'
      echo "(government/proceed-by-default.sh audit $town ID upheld|reversed|concern NOTE):"
      printf '%s' "$audit"
    fi
    echo '=== END PROCEED-BY-DEFAULT LEDGER ==='
    ;;
  *)
    echo "unknown command: $cmd" >&2
    exit 2
    ;;
esac
