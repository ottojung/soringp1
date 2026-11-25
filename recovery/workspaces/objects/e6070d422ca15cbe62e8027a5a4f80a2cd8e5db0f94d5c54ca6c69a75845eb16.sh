#!/bin/bash
# Bounded n=9 exact search wrapper. Records PID, log path and exit status.
cd /home/lubko/soring301-exec-fibonacci-split-20261124 || exit 90
HANDLE=notes/n9_full.handle
LOG=notes/n9_full.log
{
  echo "task=wl-n9-exact-search"
  echo "started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "log=$LOG"
  echo "command=python3 scripts/oracle_n8.py 9 --deadline 1380 --mem-mb 5000 --log $LOG"
} > "$HANDLE"
python3 scripts/oracle_n8.py 9 --deadline 1380 --mem-mb 5000 --log "$LOG" \
  > notes/n9_full.stdout 2>&1 &
ORACPID=$!
echo "oracle_pid=$ORACPID" >> "$HANDLE"
wait "$ORACPID"
RC=$?
echo "exit_status=$RC" >> "$HANDLE"
echo "finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$HANDLE"
exit "$RC"
