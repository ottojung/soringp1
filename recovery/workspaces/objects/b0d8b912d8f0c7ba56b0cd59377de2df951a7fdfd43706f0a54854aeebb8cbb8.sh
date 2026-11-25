#!/bin/bash
# Bounded, targeted n=9 search: height<=2 posets (contains the obstruction
# family and the fence/crown tight posets). One process, hard deadline, cap.
cd /home/lubko/soring301-exec-fibonacci-split-20261124 || exit 90
HANDLE=notes/n9_height2.handle
LOG=notes/n9_height2.log
{
  echo "task=wl-n9-height2-exact-search"
  echo "started_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "log=$LOG"
  echo "command=python3 scripts/oracle_n8.py 9 --family height2 --deadline 700 --mem-mb 5000 --log $LOG"
} > "$HANDLE"
python3 scripts/oracle_n8.py 9 --family height2 --deadline 700 --mem-mb 5000 \
  --log "$LOG" > notes/n9_height2.stdout 2>&1 &
ORACPID=$!
echo "oracle_pid=$ORACPID" >> "$HANDLE"
wait "$ORACPID"
RC=$?
echo "exit_status=$RC" >> "$HANDLE"
echo "finished_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> "$HANDLE"
exit "$RC"
