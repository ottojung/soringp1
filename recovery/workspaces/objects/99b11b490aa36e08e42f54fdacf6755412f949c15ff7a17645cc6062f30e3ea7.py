#!/usr/bin/env python3
"""Generate small replayable oracle-aided trace examples for check_oracle_trace.py.

Examples:
- g4k4_refuter_oracle.json: full G(4,4) adversary-win claim is NOT emitted as raw
  search; instead root is an oracle node whose exhaustive_cannot_sort constraint is
  mechanically checked by budgeted_dfs.can_sort within node_cap.
- g4k4_refuter_fragment.json: explicit small refuter fragment showing trace format
  (covers one concrete path/state with explicit tc edges/checkable constraints).
- g4k5_sorter_oracle.json: sorter-win claim for G(4,5) as checked oracle (S(4)=5).
"""
from __future__ import annotations
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from budgeted_dfs import antichain, extend, incomparable_pairs

OUT = HERE.parent / "docs" / "oracle-traces"
OUT.mkdir(parents=True, exist_ok=True)


def succ_list(s): return [int(x) for x in s]


def refuter_root_oracle(n, k, node_cap=10_000_000):
    return {
        "kind":"refuter","n":n,"k":k,"root":"r","nodes":{
            "r":{
                "state": succ_list(antichain(n)),
                "budget": k,
                "type":"oracle",
                "oracle":{
                    "name":"exhaustive_budgeted_dfs_refuter",
                    "params":{"node_cap":node_cap},
                    "constraints":[
                        {"type":"root_antichain"},
                        {"type":"budget_eq","value":k},
                        {"type":"state_tc"},
                        {"type":"non_total"},
                        {"type":"exhaustive_cannot_sort","value":False,"node_cap":node_cap},
                    ],
                },
            }
        }
    }


def sorter_root_oracle(n, k, node_cap=10_000_000):
    return {
        "kind":"sorter","n":n,"k":k,"root":"r","nodes":{
            "r":{
                "state": succ_list(antichain(n)),
                "budget": k,
                "type":"oracle",
                "oracle":{
                    "name":"exhaustive_budgeted_dfs_sorter",
                    "params":{"node_cap":node_cap},
                    "constraints":[
                        {"type":"root_antichain"},
                        {"type":"budget_eq","value":k},
                        {"type":"state_tc"},
                        {"type":"exhaustive_can_sort","value":True,"node_cap":node_cap},
                    ],
                },
            }
        }
    }


def refuter_fragment_g4k4():
    # Explicit, small fragment: root oracle claim plus one explicit adversary reply to move (0,1)
    # and that child's losing status as an oracle checked by exhaustive search. This is a trace
    # fragment illustrating explicit tc_edge/covers constraint style; full total-coverage refuter
    # for all 6 root moves is intentionally NOT materialized here.
    n,k=4,4
    s0=antichain(n)
    s1=extend(s0,0,1)  # answer 0<1
    doc = {
        "kind":"refuter","n":n,"k":k,"root":"r","nodes":{
            "r":{
                "state": succ_list(s0), "budget": k, "type":"oracle",
                "oracle":{
                    "name":"root_refuter_oracle_plus_explicit_child",
                    "constraints":[
                        {"type":"root_antichain"},{"type":"budget_eq","value":k},
                        {"type":"state_tc"},{"type":"tc_edge","move":[0,1],"answer":"lt","child":"c01"},
                        {"type":"exhaustive_cannot_sort","value":False,"node_cap":10_000_000},
                    ],
                },
            },
            "c01":{
                "state": succ_list(s1), "budget": k-1, "type":"oracle",
                "oracle":{
                    "name":"child_refuter_oracle_after_0lt1",
                    "constraints":[
                        {"type":"budget_eq","value":k-1},{"type":"state_tc"},{"type":"non_total"},
                        {"type":"exhaustive_cannot_sort","value":False,"node_cap":10_000_000},
                    ],
                },
            }
        }
    }
    return doc


def g12k29_blocking_oracle(node_cap=1_000_000):
    # NOT a proof/certificate of S(12)>29: root oracle would require exhaustive_cannot_sort but
    # budgeted_dfs hits node_cap; emitted as a negative/blocked trace object for documentation only
    # by marking impossible-to-check with huge cap? we instead omit exhaustive claim and include
    # structural constraints plus an explicit infeasibility marker in oracle params.
    n,k=12,29
    return {
        "kind":"refuter","n":n,"k":k,"root":"r","nodes":{
            "r":{
                "state": succ_list(antichain(n)), "budget":k, "type":"oracle",
                "oracle":{
                    "name":"G12K29_blocked",
                    "params":{
                        "blocked":True,
                        "reason":"exhaustive budgeted_dfs cannot_sort check infeasible at n=12,k=29 within tested cap",
                        "tested_node_cap":node_cap,
                        "root_incomparable_pairs":66,
                        "required_refuter_semantics":"for every sorter move at every reachable state supply adversary answer with losing child (total coverage)",
                    },
                    "constraints":[
                        {"type":"root_antichain"},{"type":"budget_eq","value":k},{"type":"state_tc"},{"type":"non_total"},
                    ],
                },
            }
        }
    }


def main():
    cases = [
        ("g4k4_refuter_oracle.json", refuter_root_oracle(4,4)),
        ("g4k5_sorter_oracle.json", sorter_root_oracle(4,5)),
        ("g4k4_refuter_fragment.json", refuter_fragment_g4k4()),
        ("g12k29_blocked.json", g12k29_blocking_oracle()),
    ]
    for name, doc in cases:
        p = OUT / name
        p.write_text(json.dumps(doc, indent=2, sort_keys=True) + "\n")
        print("wrote", p)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
