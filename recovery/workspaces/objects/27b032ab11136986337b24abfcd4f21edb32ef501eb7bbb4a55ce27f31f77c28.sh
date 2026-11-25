#!/bin/sh
# Recognize a known container-restart orphan, NOT a failed model call.
# Reads one Antonina agent-status JSON object from stdin.
# No old session, invocation or prompt is ever resumed here.
set -eu
[ "$#" -eq 0 ] || exit 2
birth=$(stat -c %Y /proc/1) || exit 1
case "$birth" in ''|*[!0-9]*) exit 1;; esac
# Hermetic regression fixture only. Production cannot override PID1 birth.
if [ "${VICHE_TEST_NO_SYNC:-0}" = 1 ] &&
   [ -n "${VICHE_TEST_PID1_BIRTH:-}" ]; then
  birth=$VICHE_TEST_PID1_BIRTH
fi
case "$birth" in ''|*[!0-9]*) exit 1;; esac
jq -e --argjson birth "$birth" '
  .state == "failed"
  and .alive == false
  and .backend_error == null
  and .exit_code == null and .exit_signal == null
  and .last_error == "runner/model process disappeared without a captured exit status"
  and ((.steers_pending // 0) == 0)
  and .next_steer == null
  and ((.steer_preempting // false) == false)
  and (.started_at | type == "number" and . < $birth)
  and (.finished_at | type == "number"
       and . >= ($birth - 2) and . <= ($birth + 120))
' >/dev/null
