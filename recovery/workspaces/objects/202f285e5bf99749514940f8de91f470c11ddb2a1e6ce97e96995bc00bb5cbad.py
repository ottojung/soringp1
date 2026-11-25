#!/usr/bin/env python3
"""One-off bounded duplicate scan of Antonina board issue 301 for any prior
FJ-exact-barrier front. Read-only; writes only to stdout / /tmp/opencode."""
import json
import re
import subprocess

KEY = re.compile(r"F_FJ|3j/4|FJ exact|fj-exact|exact barrier|merge-insertion|Ford.{0,3}Johnson|ceil\(log2\(3", re.I)
hits = []
total = 0
empties = 0
for page in range(1, 121):
    try:
        r = subprocess.run(["antonina", "board", "show", "--id", "301", "--page", str(page), "--json"],
                           capture_output=True, text=True, timeout=30)
    except Exception as e:
        print("PAGE", page, "ERROR", e)
        break
    txt = r.stdout.strip()
    try:
        obj = json.loads(txt)
    except Exception:
        # may have log preamble; try to find the JSON object
        m = re.search(r"\{.*\}", txt, re.S)
        if not m:
            print("PAGE", page, "NON-JSON", txt[:200])
            break
        obj = json.loads(m.group(0))
    msgs = obj.get("messages", [])
    total += len(msgs)
    if not msgs:
        empties += 1
        if empties >= 2:
            break
    for msg in msgs:
        body = msg.get("body", "")
        if KEY.search(body):
            author = msg.get("author", "")
            created = msg.get("createdAt", "")
            snippet = " ".join(body.split())[:180]
            hits.append((page, created, author, snippet))
    if page % 20 == 0:
        print(f"scanned page {page}, messages so far {total}")

print("TOTAL MESSAGES SCANNED:", total)
print("KEYWORD HITS:", len(hits))
for page, created, author, snippet in hits:
    print(f"--- p{page} {created} {author}: {snippet}")
