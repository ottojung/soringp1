#!/usr/bin/env python3
"""Pull the few prior FJ-related #301 posts in full, for honest overlap disclosure."""
import json, subprocess, re
WANT = {"2026-11-23T03:37:25.020Z", "2026-11-21T05:08:12.638Z", "2026-11-07T11:12:05.679Z"}
for page in [3, 7, 24]:
    r = subprocess.run(["antonina", "board", "show", "--id", "301", "--page", str(page), "--json"],
                       capture_output=True, text=True, timeout=30)
    txt = r.stdout.strip()
    m = re.search(r"\{.*\}", txt, re.S)
    obj = json.loads(m.group(0) if m else txt)
    for msg in obj.get("messages", []):
        if msg.get("createdAt") in WANT:
            print("=" * 100)
            print("PAGE", page, "AUTHOR", msg.get("author"), "AT", msg.get("createdAt"))
            print(msg.get("body", ""))
