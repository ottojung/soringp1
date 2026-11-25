#!/bin/sh
set -eu
cd "$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)"
root=$(pwd -P)
scratch=$(mktemp -d)
trap 'rm -rf "$scratch"' EXIT HUP INT TERM
python3 - "$root" "$scratch" <<'PY'
import fcntl
import os
from pathlib import Path
import subprocess
import sys

root, temp = map(Path, sys.argv[1:])
state=temp/"state"
lock=state/"delivery/integrator/internal.lock"
lock.parent.mkdir(parents=True, exist_ok=True)
with lock.open("a+") as handle:
    fcntl.flock(handle.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
    env=dict(os.environ,VICHE_STATE_ROOT=str(state),
             VICHE_TOWN_ROOT=str(temp/"missing-repo"))
    p=subprocess.run([sys.executable,str(root/"government/integrator.py"),"run"],
                      env=env,text=True,capture_output=True,timeout=6)
    assert p.returncode==0,(p.returncode,p.stderr)
    assert "internal lock busy" in p.stderr,p.stderr
    assert not (state/"delivery/integrator/state.json").exists()
print("integrator internal flock prevents competing workspace mutation")
PY
