#!/usr/bin/env python3
"""Once-daily, immutable source-attributed Town snapshot for Statistics Bureau.

No new telemetry collection: reuse existing independent collectors. A frozen
snapshot is retried with an identical idempotency key across crashes.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

STATE=Path(os.environ.get("VICHE_STATE_ROOT","/var/lib/lubko/wd/viche-state"))
TOWN=Path(os.environ.get("VICHE_TOWN_ROOT","/var/lib/lubko/wd/viche"))
SOURCES={
    "outcomes":STATE/"institutional-outcomes/latest.json",
    "resources":STATE/"economy/resources.json",
    "judiciary":STATE/"branches/judiciary-measurements.json",
}

def freeze(day):
    snapshot=STATE/"knowledge"/"statistics"/("snapshot-"+day+".json")
    if snapshot.exists():
        return json.loads(snapshot.read_text())
    entries={}
    for name,path in SOURCES.items():
        try:
            raw=path.read_bytes()
            entries[name]={"data":json.loads(raw),"source":
                "file:"+str(path)+"#sha256="+hashlib.sha256(raw).hexdigest()}
        except (OSError,ValueError) as exc:
            entries[name]={"missing":type(exc).__name__}
    data={"day":day,"entries":entries,"scope":"observations_only_not_verification"}
    snapshot.parent.mkdir(parents=True,exist_ok=True)
    tmp=snapshot.with_suffix(".tmp")
    tmp.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n")
    os.replace(tmp,snapshot)
    return data

def report(d,kind):
    e=d["entries"]
    if kind=="outcomes":
        o=e["outcomes"].get("data",{})
        a=o.get("agents",{})
        g=o.get("git",{})
        b=o.get("board",{})
        lines=[
            "UTC day: "+d["day"],
            "Snapshot at epoch: "+str(o.get("observed_at","unknown")),
            "Agent executions (24h): "+str(a.get("total","unknown")),
            "Main commits (24h): "+str(g.get("main_commits","unknown")),
            "Independently verified effect by this probe: "+str(o.get("delivery_verified_by_this_probe","unknown")),
            "Open board issues (first page only): "+str(b.get("open_first_page","unknown")),
            "Caveat: clean agent exits and merged commits are NOT verified useful outcomes.",
            "Caveat: board first page is NOT an exhaustive issue count.",
            "Judiciary measurement source: "+str(e["judiciary"].get("source","missing")),
        ]
        topic="statistics/outcomes"
        sources=[e[x]["source"] for x in ("outcomes","judiciary") if "source" in e[x]]
    else:
        r=e["resources"].get("data",{})
        lines=[
            "UTC day: "+d["day"],
            "Resource overall: "+str(r.get("overall","unknown")),
            "Sample time: "+str(r.get("at","unknown")),
            "Resource statuses: "+json.dumps({k:v.get("status","unknown")
                    for k,v in r.get("resources",{}).items()},sort_keys=True),
            "Caveat: status thresholds are leading warnings, NOT outcome verification.",
        ]
        topic="statistics/resources"
        sources=[e["resources"]["source"]] if "source" in e["resources"] else []
    return topic,"\n".join(lines),sources

def publish(d,kind,dry_run):
    topic,body,sources=report(d,kind)
    if not sources:
        raise RuntimeError("no observed sources for "+kind+"; refusing to fabricate")
    args=[sys.executable,str(TOWN/"government/post.py"),"publish",
          "--sender","statistics","--topic",topic,"--kind","observation",
          "--subject",kind.title()+" snapshot "+d["day"],
          "--body",body,"--condition","Frozen UTC daily snapshot from named collectors; "
          "source digest identifies the exact input. Missingness and selection caveats are explicit.",
          "--key","statistics:"+kind+":"+d["day"]]
    for src in sources:
        args.extend(["--source",src])
    if dry_run:
        return {"topic":topic,"body":body,"sources":sources}
    result=subprocess.run(args,capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError("statistics publication failed: "+result.stderr)
    return json.loads(result.stdout)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--dry-run",action="store_true")
    p.add_argument("--day",default=datetime.datetime.now(datetime.timezone.utc).date().isoformat())
    args=p.parse_args()
    if not args.dry_run:
        law=(TOWN/"government/LAWS.md").read_text()
        if "Institutional Knowledge and Communications Act (enacted " not in law:
            print("statistics-report: institution not enacted",file=sys.stderr)
            return 2
    d=freeze(args.day) if not args.dry_run else {"day":args.day,"entries":{}}
    if args.dry_run:
        d["entries"]={}
        for name,path in SOURCES.items():
            try:
                raw=path.read_bytes()
                d["entries"][name]={"data":json.loads(raw),"source":
                    "file:"+str(path)+"#sha256="+hashlib.sha256(raw).hexdigest()}
            except (OSError,ValueError) as exc:
                d["entries"][name]={"missing":type(exc).__name__}
    try:
        print(json.dumps({kind:publish(d,kind,args.dry_run)
                         for kind in ("outcomes","resources")},sort_keys=True))
    except RuntimeError as exc:
        print(str(exc),file=sys.stderr)
        return 1
    return 0

if __name__=="__main__":
    sys.exit(main())
