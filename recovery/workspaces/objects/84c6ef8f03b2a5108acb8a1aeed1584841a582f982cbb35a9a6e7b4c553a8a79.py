#!/usr/bin/env python3
"""Regenerate connected-incomparability residuals e=11,12 and width<=3."""
import json
from collections import Counter
from pathlib import Path
from enum_core import enum_posets, extensions, width, exact_F
from enum_n12_tree import enum_posets as enum_n12
from enum_n12_tree import extensions as extensions_n12
from enum_n12_tree import width as width_n12
from enum_n12_tree import minimax

ROOT = Path(__file__).resolve().parents[2]
records = []
for n in range(2, 12):
    total = 0
    outcomes = Counter()
    for Q, q in enum_posets(n, n - 1, 11):
        total += 1
        ext = extensions(Q, n, 13)
        e = len(ext)
        if e in (11, 12) and width(Q, n) <= 3:
            f, _ = exact_F(ext, n)
            outcomes[(e, width(Q, n), f)] += 1
            records.append({"n": n, "Q": list(Q), "q": q, "e": e,
                            "w": width(Q, n), "F": f,
                            "ext": [list(p) for p in ext]})
    print("n", n, "complete fixed-extension count", total,
          "residual counts", dict(outcomes), flush=True)

n = 12
tree_count = 0
outcomes = Counter()
for Q in enum_n12(n, n - 1):
    tree_count += 1
    ext = extensions_n12(Q, n)
    if len(ext) == 12 and width_n12(Q, n) <= 3:
        f = minimax(ext, n)
        outcomes[(12, width_n12(Q, n), f)] += 1
        records.append({"n": n, "Q": list(Q), "q": n - 1, "e": 12,
                        "w": width_n12(Q, n), "F": f,
                        "ext": [list(p) for p in ext]})
print("n=12 incomparability trees", tree_count, "residual counts",
      dict(outcomes), flush=True)
out = ROOT / "data" / "t4-threshold-candidates.json"
out.write_text(json.dumps(records, separators=(",", ":")))
print("saved", len(records), "representations to", out)
