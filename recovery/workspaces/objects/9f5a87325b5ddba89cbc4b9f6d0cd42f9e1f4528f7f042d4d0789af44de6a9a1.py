#!/usr/bin/env python3
"""Idempotent, nondestructive pointer import from former communication channels.

Preserves the original files and their state. A "reviewed" folder is NOT proof
that the underlying defect was corrected, and import makes no such claim.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

STATE=Path(os.environ.get("VICHE_STATE_ROOT","/var/lib/lubko/wd/viche-state"))
POST=Path(__file__).with_name("post.py")
MAILBOX=STATE/"oversight/judiciary-mailbox"
INNOVATION="GT2QzYsFG4t92DvJkE4Wuk-lodge"

def invoke(*args):
    result=subprocess.run([sys.executable,str(POST),*args],capture_output=True,text=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip())
    return json.loads(result.stdout)

def migrate(dry_run):
    counts={}
    for state in ("inbox","reviewed","expired"):
        files=sorted((MAILBOX/state).glob("*"))
        counts[state]=0
        for item in files:
            if not item.is_file():continue
            data=item.read_bytes()
            digest=hashlib.sha256(data).hexdigest()
            key="legacy-judiciary:"+state+":"+item.name+":"+digest
            source="file:"+str(item)+"#sha256="+digest
            text=("Legacy Judiciary report pointer, state="+state+
                  ". Original record: "+str(item)+
                  ". Exact SHA256: "+digest+
                  ". State is historical filing/triage only; no verified remediation inferred.")
            if not dry_run:
                if state=="inbox":
                    invoke("send","--public","--sender","legacy-import","--to","judiciary",
                           "--subject","Unreviewed legacy record: "+item.name,
                           "--body",text,"--source",source,"--key",key)
                else:
                    invoke("publish","--sender","legacy-import","--topic",
                           "archive/judiciary","--subject","Legacy "+state+": "+item.name,
                           "--body",text,"--source",source,"--key",key)
            counts[state]+=1
    if not dry_run:
        invoke("publish","--sender","legacy-import","--topic","archive/innovation",
               "--subject","Historic Innovation–Legislature dialogue",
               "--body","Standing Antonina board hub "+INNOVATION+
               " and topic-specific issues are preserved there. Post is the new channel. "
               "No earlier discussion is erased or converted into a law.",
               "--source","antonina:"+INNOVATION,"--key","legacy-innovation-hub-v1")
    return {"archive_counts":counts,"dry_run":dry_run,
            "historical_files_preserved":True,"innovation_hub":INNOVATION}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    actions=parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--dry-run",action="store_true")
    actions.add_argument("--import",dest="do_import",action="store_true")
    args=parser.parse_args()
    try:
        print(json.dumps(migrate(args.dry_run),sort_keys=True))
    except (OSError,RuntimeError) as exc:
        print("post-migrate: "+str(exc),file=sys.stderr)
        sys.exit(1)
