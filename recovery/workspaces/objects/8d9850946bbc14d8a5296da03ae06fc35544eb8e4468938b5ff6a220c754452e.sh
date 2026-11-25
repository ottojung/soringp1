#!/bin/sh
# Other smoke fixtures control the runtime themselves; this stub supplies only
# a predictable logical-key lookup. Generated-ID behavior is tested separately
# by appointments-smoke.sh with a stateful mock Antonina backend.
set -eu
[ "$#" -eq 2 ] || exit 2
case "$2" in
  executive) id=c1e00002;;
  judiciary) id=c1e00008;;
  innovation-centre) id=c1e00011;;
  c1a*|c1e*) id=$2;;
  *) exit 2;;
esac
case "$1" in
  ensure|resolve) printf '%s\n' "$id";;
  replace)
    if [ -n "${MOCK_ROOT:-}" ]; then
      # Two audit events preserve the preexisting tests' expected count,
      # without calling Antonina delete or asking it to reuse an ID.
      printf 'replacement-requested\nreplacement-recorded\n' >> "$MOCK_ROOT/recovery"
      printf 'replacement-requested\nreplacement-recorded\n' >> "$MOCK_ROOT/actions"
      if [ -f "$MOCK_ROOT/status.json" ]; then
        printf '{"state":"idle","model":"test-provider/example","variant":"low"}\n' > "$MOCK_ROOT/status.json"
      fi
      if [ -f "$MOCK_ROOT/status" ]; then
        printf '{"state":"idle"}\n' > "$MOCK_ROOT/status"
      fi
    fi
    printf '%s\n' "$id"
    ;;
  *) exit 2;;
esac
