#!/usr/bin/env python3
"""Discover eligible issues from descriptions and Founder comments, not target registry.

Board CLI fetches are transiently fallible (incident 1795107689 and the
recurrence executive_unhealthy:1795150900). A bounded retry with bounded linear
backoff absorbs a short fetch flap; on exhaustion the COMPLETE raw stderr of
the failing invocation is appended to a durable JSONL so the underlying cause
can be established from checkable bytes rather than a truncated, rotated log.
"""
import base64
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

STATE_ROOT = os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state")
ERROR_LOG = os.environ.get(
    "VICHE_ELIGIBILITY_ERROR_LOG",
    os.path.join(STATE_ROOT, "oversight", "eligibility-board-errors.jsonl"),
)
BOARD_TIMEOUT = 35


def _int_env(name, default, low, high):
    """Read a bounded integer knob; bad values fall back to the safe default."""
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return default
    return max(low, min(value, high))


RETRIES = _int_env("VICHE_BOARD_RETRIES", 3, 1, 10)
BACKOFF = _int_env("VICHE_BOARD_RETRY_DELAY", 1, 0, 5)


def _as_bytes(value):
    if value is None:
        return b""
    if isinstance(value, bytes):
        return value
    return str(value).encode("utf-8", "replace")


def record_failure(command, last, attempts):
    """Append complete raw stderr/stdout of an exhausted board call to durable storage."""
    stderr = _as_bytes(last.get("stderr"))
    stdout = _as_bytes(last.get("stdout"))
    record = {
        "ts": int(time.time()),
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "command": list(command),
        "attempts": attempts,
        "exit": last.get("exit"),
        "error": last.get("error"),
        "stderr_bytes": len(stderr),
        "stderr_b64": base64.b64encode(stderr).decode("ascii"),
        "stderr_text": stderr.decode("utf-8", "replace"),
        "stdout_bytes": len(stdout),
        "stdout_b64": base64.b64encode(stdout).decode("ascii"),
    }
    try:
        path = Path(ERROR_LOG)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
        return str(path)
    except OSError as exc:
        return "telemetry-unavailable:" + str(exc)


def invoke(*args):
    """Run `antonina board ...` with bounded retry; persist full stderr on exhaustion."""
    command = ("antonina", "board", *args)
    last = {"exit": None, "stderr": b"", "stdout": b"", "error": None}
    used = 0
    for attempt in range(1, RETRIES + 1):
        used = attempt
        try:
            done = subprocess.run(command, capture_output=True, timeout=BOARD_TIMEOUT)
        except subprocess.TimeoutExpired as exc:
            last = {"exit": "timeout", "stderr": _as_bytes(exc.stderr),
                    "stdout": _as_bytes(exc.stdout),
                    "error": "timeout after %ds" % BOARD_TIMEOUT}
        else:
            if done.returncode == 0:
                try:
                    return json.loads(done.stdout)
                except ValueError as exc:
                    last = {"exit": 0, "stderr": _as_bytes(done.stderr),
                            "stdout": _as_bytes(done.stdout),
                            "error": "unparseable board JSON: %s" % exc}
                    break
            last = {"exit": done.returncode, "stderr": _as_bytes(done.stderr),
                    "stdout": _as_bytes(done.stdout), "error": None}
        if attempt < RETRIES:
            time.sleep(BACKOFF * attempt)
    reference = record_failure(command, last, used)
    stderr_text = _as_bytes(last["stderr"]).decode("utf-8", "replace")
    if str(last.get("error") or "").startswith("unparseable"):
        raise ValueError("unreadable board output; full stderr at " + reference)
    raise RuntimeError("board command unavailable: " + stderr_text[-180:] +
                       "; full stderr at " + reference)


def explicit(text):
    normalized = re.sub(r"\s+", " ", text.lower()) if isinstance(text, str) else ""
    pats = (
        r"(?:execution|dispatch|assignment|target)\s+(?:host|target|machine|server)\s*[:=]\s*billy-dev",
        r"(?:assign(?:ed|ment)?|route(?:d)?|dispatch(?:ed)?)\s+(?:\S+\s+){0,9}(?:to|on)\s+billy-dev",
        r"(?:agent|worker)(?:\s+\S+){0,13}\s+(?:must|shall|only|exclusively)(?:\s+\S+){0,12}\s+(?:on|at)\s+billy-dev",
        r"(?:agent|worker)\s+execution(?:\s+\S+){0,14}\s+(?:on|at)\s+billy-dev",
        r"billy-dev\s+only",
        r"only\s+(?:on|at)\s+billy-dev",
    )
    return any(re.search(p, normalized.replace(chr(96), "")) for p in pats)


def get_items():
    collected = []
    seen = set()
    for page in range(1, 101):
        batch = invoke("list", "--state", "open", "--page", str(page), "--json")
        if not isinstance(batch, list):
            raise RuntimeError("unreadable board list")
        for entry in batch:
            num = entry.get("number")
            if not isinstance(num, str) or not num or num in seen:
                raise RuntimeError("invalid/duplicate board issue")
            seen.add(num)
            collected.append(entry)
        if len(batch) < 50:
            return collected
    raise RuntimeError("board pagination incomplete")


def main():
    items = []
    for row in get_items():
        issue = invoke("show", "--id", str(row["number"]), "--page", "1", "--json")
        body = issue.get("body", "")
        assigned = explicit(body) or any(
            c.get("author") == "Vitalik"
            and ("this issue" in c.get("body", "").lower()
                 or c.get("body", "").lower().startswith("execution host:"))
            and explicit(c.get("body", ""))
            for c in (issue.get("messages") or []))
        if assigned and "legislature-only" not in body.lower() and not (
            "permanent public conversation" in body.lower()
            and "town hall" in row.get("title", "").lower()):
            items.append({"number": row["number"], "title": row.get("title", "")})
    result = {"host": "billy-dev", "eligible": items, "count": len(items),
              "complete": True, "source": "board_description_and_founder_comments"}
    target = Path(STATE_ROOT) / "branches/eligible-issues.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    tmp = target.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    tmp.replace(target)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, KeyError, subprocess.TimeoutExpired) as e:
        print("ELIGIBILITY_DISCOVERY_UNAVAILABLE: " + str(e), file=sys.stderr)
        sys.exit(1)
