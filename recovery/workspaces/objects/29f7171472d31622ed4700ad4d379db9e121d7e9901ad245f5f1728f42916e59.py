#!/usr/bin/env python3
"""Act 18 (Board Reporting Act) §7 — generate records/board-trail/index.json.

The index is GENERATED, never hand-maintained. The issue->work mapping comes
from the curated cross-check file records/board-trail/originating.tsv (the
Act 18 §5 lens input), NOT from parsing bill/LAWS prose (which mis-maps: bills
cite other issues as examples). For each originating issue the generator emits
one entry — issue, title, work, owning_office, stage, terminal_status,
git_only_gap — using that mapping plus the Antonina board's terminal-update
check. Issue ids may be opaque strings (not only numeric); they are parsed as
strings and ordered deterministically (numeric ascending, then opaque
lexically), so an opaque-id originating issue is not silently dropped.

git_only_gap is true when the underlying work is enacted/completed in Git while
the originating issue lacks a terminal board update — the defect class Act 18 §2
names, decidable from Git and the board alone.

The board scan is best-effort but must not fabricate a gap: each `board show`
call is retried a bounded number of times, and a persistent failure is recorded
as `board_readable: false` with `git_only_gap: false` — a failed board call is
NOT evidence of a missing terminal update (the false-signal class the Sentinel
`timeout 12` artifact and the Act 13 over-deferral belong to). The title is left
blank and the index is still produced from the curated mapping. POSIX-friendly;
no third-party deps.
"""
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

TOWN = Path(os.environ.get("VICHE_TOWN_ROOT", "/var/lib/lubko/wd/viche"))
STATE = Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state"))
INDEX = TOWN / "records" / "board-trail" / "index.json"
ORIGINATING = TOWN / "records" / "board-trail" / "originating.tsv"

STAGE_MARKERS = ("proposal", "enactment", "deployment", "verification")
TERMINAL_STATES = (
    "verification:confirmed",
    "verification:blocked",
    "enactment:not_enacted",
    "deferred",
)
BOARD_PAGE_SIZE = 50
MAX_BOARD_PAGES = 20

# Act 18 §3.4 content standard: a terminal update carries exactly one stage
# marker AND a DECLARED terminal state. Both the §5 lens
# (government/board-trail-check.sh) and this §7 generator use the SAME rules so
# the two instruments cannot disagree. A terminal token counts only in a
# declaration position — start of line, after a sentence/clause terminator, or
# after a declaration label — never as a bare prose/quoted mention.
STAGE_MARKER_RE = re.compile(
    r"(?i)stage\s*marker[^\n]{0,12}\b(proposal|enactment|deployment|verification)\b")
TERMINAL_DECLARATION_RE = re.compile(
    r"(?m)(^|[.:;—-]\s*|(?i:state|status|terminal|result|outcome|transition)\s+)"
    r"(verification:confirmed|verification:blocked|enactment:not_enacted|deferred)"
    r"([.\s,;:]|$)")

# Act 18 §3.3.4: automated scheduler/agent status lines are not updates.
AUTOMATED_RE = re.compile(
    r"(?i)\[(scheduler-turn|terminal-handoff|progress-checkpoint)\]")
# A terminal token counts only when DECLARED, never inside an inline-code or
# quoted span: strip those before matching so a comment that merely QUOTES a
# declaration (or the classifier's own fixture) cannot false-positive.
INLINE_CODE_RE = re.compile(r"`[^`]*`")
QUOTED_RE = re.compile(r'"[^"\n]*"')


def unquote(text):
    """Remove inline-code and double-quoted spans (Act 18 §3.3/§3.4: a terminal
    token must be DECLARED, not a quoted/prose mention)."""
    return QUOTED_RE.sub(" ", INLINE_CODE_RE.sub(" ", text))


def read(path):
    try:
        return Path(path).read_text()
    except OSError:
        return ""


def env_int(name, default):
    try:
        value = int(os.environ.get(name, str(default)))
    except (TypeError, ValueError):
        return default
    return value if value >= 1 else default


def board_invoke(*args):
    """Run a read-only board command, retrying a bounded number of times.

    A transient board/network error (nonzero exit, timeout, or unparsable
    output) is retried with a short backoff; only after every attempt fails does
    it raise. This keeps a single transient failure from becoming a false
    `git_only_gap` (Act 18 §2/§7)."""
    attempts = env_int("VICHE_BOARD_TRAIL_RETRIES", 3)
    backoff = env_int("VICHE_BOARD_TRAIL_BACKOFF", 1)
    last = None
    for attempt in range(1, attempts + 1):
        try:
            done = subprocess.run(("antonina", "board", *args),
                                  capture_output=True, text=True, timeout=35)
            if done.returncode:
                raise RuntimeError(done.stderr[-160:])
            return json.loads(done.stdout)
        except Exception as err:
            last = err
            if attempt < attempts:
                time.sleep(backoff)
    raise last


def fetch_issue(num):
    """Return the issue with all bounded comment pages, or raise if incomplete.

    The board-trail lens scans every page. The generated Founder-facing index
    must use the same complete history: a terminal update can fall beyond page
    one on a high-traffic originating issue, and treating a partial read as
    complete creates a false Git-only gap. Histories beyond the shared 20-page
    ceiling are unreadable rather than silently truncated.
    """
    first = board_invoke("show", "--id", str(num), "--page", "1", "--json")
    issue = dict(first)
    messages = list(first.get("messages") or [])
    page = 1
    while len(first.get("messages") or []) >= BOARD_PAGE_SIZE:
        if page >= MAX_BOARD_PAGES:
            raise RuntimeError(
                f"issue {num} exceeds the {MAX_BOARD_PAGES}-page board history limit")
        page += 1
        next_page = board_invoke("show", "--id", str(num), "--page", str(page), "--json")
        page_messages = list(next_page.get("messages") or [])
        messages.extend(page_messages)
        first = next_page
        if len(page_messages) < BOARD_PAGE_SIZE:
            break
    issue["messages"] = messages
    return issue


def issue_title(issue):
    return (issue.get("title", "") or "") if issue is not None else ""


def issue_terminal_state(issue):
    """Return the DECLARED terminal state of an issue object, or None.

    Act 18 §3.3/§3.4: a terminal update carries a stage marker AND a declared
    terminal state — a terminal token in a declaration position, not a
    quoted/prose mention. Automated scheduler/agent status lines are not
    updates (Act 18 §3.3.4). Inline-code and quoted spans are stripped first so
    a comment that merely QUOTES a declaration (or the classifier's own test
    fixture) cannot false-positive. Mirrors the §5 lens exactly (same rules) so
    §5 and §7 agree. A None issue (board unreadable) is handled by the caller,
    which records board_readable=false rather than a gap."""
    if issue is None:
        return None
    for msg in issue.get("messages") or []:
        body = msg.get("body") or ""
        if AUTOMATED_RE.search(body):
            continue
        clean = unquote(body)
        if not STAGE_MARKER_RE.search(clean):
            continue
        declared = TERMINAL_DECLARATION_RE.search(clean)
        if declared:
            return declared.group(2)
    return None


def parse_issue(raw):
    """Return an originating issue id as an int when it is all digits (keeping
    the existing numeric JSON form), else the opaque string id unchanged.

    Antonina issue ids may be opaque strings (e.g.
    `ErkrX8EKQJXF6fCQv5fzYl-cannon`); a numeric-only parser silently dropped
    them from the Act 18 §5/§7 universe."""
    raw = raw.strip()
    if raw.isdigit():
        return int(raw)
    return raw


def issue_sort_key(issue):
    """Deterministic order: numeric issues ascending by value, then opaque
    string ids lexically, so the generated index is stable across runs."""
    if isinstance(issue, int):
        return (0, issue, "")
    if str(issue).isdigit():
        return (0, int(issue), "")
    return (1, 0, str(issue))


def parse_originating():
    """Return list of {issue, work_id, act, enacted_epoch, type} from the
    curated mapping file. Accepts opaque-string issue ids, not only numeric.
    Skips comments/blank/header rows and rows with an empty issue id."""
    rows = []
    for line in read(ORIGINATING).splitlines():
        line = line.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) < 5 or cols[0].strip() == "issue":
            continue
        issue = parse_issue(cols[0])
        if issue == "":
            continue
        rows.append({
            "issue": issue,
            "work_id": cols[1].strip(),
            "act": cols[2].strip(),
            "enacted_epoch": int(cols[3]) if cols[3].strip().isdigit() else 0,
            "type": cols[4].strip(),
        })
    return rows


def work_title(row):
    """Human-readable work description: the bill's title if available, else id."""
    bid = row["work_id"]
    if row["act"] not in ("-", ""):
        law = re.search(
            r"(?m)^## Act " + re.escape(row["act"]) + r" — (.+)$",
            read(TOWN / "government" / "LAWS.md"))
        if law:
            title = law.group(1).strip()
            title = re.sub(r"\s*\(enacted.*$", "", title)
            return f"Act {row['act']} — {title}"
    hm = re.search(r"(?m)^# (.+)$", read(TOWN / "records" / "bills" / f"{bid}.md"))
    if hm:
        return hm.group(1).strip()
    return bid


def owning_office(row):
    # Act 18 §3.2: Clerk owns legislative items (bills, drafts, mandates,
    # proceedings); Executive owns task items.
    return "Executive" if row["type"] == "task" else "Clerk"


def build_index():
    rows = parse_originating()
    by_issue = {}
    for row in rows:
        by_issue.setdefault(row["issue"], []).append(row)

    entries = []
    for num in sorted(by_issue, key=issue_sort_key):
        work_list = by_issue[num]
        enacted = any(w["type"] == "law" and w["enacted_epoch"] > 0 for w in work_list)
        try:
            issue = fetch_issue(num)
            board_readable = True
        except Exception:
            issue = None
            board_readable = False
        title = issue_title(issue)
        declared = issue_terminal_state(issue)
        has_terminal = declared is not None
        # git_only_gap: work enacted/completed in Git but no terminal board update.
        # Only decidable when the board was read: a failed board call MUST NOT
        # fabricate a gap (Act 18 §2/§7).
        git_only_gap = enacted and board_readable and not has_terminal
        stage = "enactment" if enacted else "proposal"
        if enacted and has_terminal:
            terminal = declared
        elif enacted:
            terminal = None  # enacted but not yet a terminal board update
        elif any(w["type"] == "draft" for w in work_list):
            terminal = "enactment:not_enacted"
        else:
            terminal = None
        entries.append({
            "issue": num,
            "title": title,
            "work": "; ".join(work_title(w) for w in work_list),
            "owning_office": owning_office(work_list[0]),
            "stage": stage,
            "terminal_status": terminal,
            "board_readable": board_readable,
            "git_only_gap": git_only_gap,
            "transition_history": [
                {"transition": "enacted" if (w["type"] == "law" and w["enacted_epoch"] > 0) else "proposed",
                 "stage": "enactment" if (w["type"] == "law" and w["enacted_epoch"] > 0) else "proposal",
                 "timestamp": w["enacted_epoch"],
                 "evidence_link": f"records/bills/{w['work_id']}.md"}
                for w in work_list
            ],
        })

    return {
        "generated_at": int(os.environ.get("VICHE_BOARD_TRAIL_NOW", time.time())),
        "generator": "government/board-trail-index.py",
        "mapping_source": "records/board-trail/originating.tsv",
        "issues": entries,
    }


def main():
    index = build_index()
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    tmp = INDEX.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(index, sort_keys=True, indent=2) + "\n")
    os.replace(tmp, INDEX)
    print(f"board-trail-index: {len(index['issues'])} originating issue(s) -> {INDEX}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as err:
        print(f"board-trail-index failed: {err}", file=sys.stderr)
        sys.exit(1)
