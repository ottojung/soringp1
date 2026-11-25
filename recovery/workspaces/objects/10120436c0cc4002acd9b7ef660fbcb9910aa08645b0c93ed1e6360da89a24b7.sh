#!/bin/sh
# A stalled Executive/Judiciary must not delay the constitutional seat dispatcher.
set -eu
cd "$(CDPATH= cd "$(dirname "$0")/.." && pwd -P)"
python3 - "$(pwd -P)" <<'PY'
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

project=Path(sys.argv[1])
with tempfile.TemporaryDirectory() as td:
    root=Path(td)
    town=root/"town"
    government=town/"government"
    seats=root/"seats"
    state=root/"state"
    government.mkdir(parents=True)
    (seats/"c1a00001").mkdir(parents=True)
    (seats/"c1a00001"/".git").touch()
    (state/"inaugurated").touch() if state.exists() else state.mkdir()
    (town/"government/LAWS.md").write_text("Not an enactment: fixture\n")
    (town/"government/seats.tsv").write_text("c1a00001\tClerk\tFounding seat\n")
    (government/"boot.sh").write_bytes((project/"government/boot.sh").read_bytes())
    (government/"branch-liveness.sh").write_text(
        "#!/bin/sh\n"
        "if [ \"$1\" = legislature ]; then exit 0; fi\n"
        "sleep 8\nexit 7\n")
    (government/"oversight-watch.sh").write_text("#!/bin/sh\nsleep 8\nexit 9\n")
    subprocess.run(["git","init","-q",str(town)],check=True)
    env=dict(os.environ,VICHE_TOWN_ROOT=str(town),
             VICHE_SEATS_ROOT=str(seats),VICHE_STATE_ROOT=str(state))
    start=time.monotonic()
    run=subprocess.run(["/bin/sh",str(government/"boot.sh")],
        env=env,capture_output=True,text=True,timeout=4)
    elapsed=time.monotonic()-start
    assert run.returncode==0,(run.returncode,run.stderr)
    assert elapsed<3,(elapsed,run.stderr)
    assert (state/"health/government-setup.last").exists(),run.stderr
    # Child processes are no longer on boot's critical path. The expected
    # per-office lock names also prevent duplicate supervisor invocations.
    for name in ("executive","judiciary","oversight"):
        for _ in range(30):
            if (state/"boot-independent"/(name+".lock")).exists():
                break
            time.sleep(.01)
        assert (state/"boot-independent"/(name+".lock")).exists(),name
    print(f"non-parliamentary hangs do not block seats: boot returned in {elapsed:.3f}s")
PY
