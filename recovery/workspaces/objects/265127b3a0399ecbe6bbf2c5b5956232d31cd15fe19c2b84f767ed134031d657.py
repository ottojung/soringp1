#!/usr/bin/env python3
"""Small, de-duplicated views of the Antonina research board.

Do not paste the huge raw Antonina board show JSON into agent context.
This reads one board page locally and prints only relevant excerpts.
"""
import argparse
import json
import subprocess
import sys

ANTONINA = "/home/lubko/.local/bin/antonina"
ISSUE_ID = "301"


def fetch_messages(page: int):
    result = subprocess.run(
        [ANTONINA, "board", "show", "--id", ISSUE_ID,
         "--page", str(page), "--json"],
        capture_output=True, text=True, timeout=30, check=True,
    )
    data = json.loads(result.stdout)
    messages = data.get("messages")
    if not isinstance(messages, list):
        raise ValueError("Antonina returned no messages array")
    return messages


def select_messages(messages, recent: int, contains: str):
    needle = contains.casefold()
    ordered = sorted(messages, key=lambda item: item.get("createdAt", ""), reverse=True)
    selected = []
    seen = set()
    for message in ordered:
        body = " ".join(str(message.get("body", "")).split())
        author = str(message.get("author", ""))
        if needle and needle not in (author + " " + body).casefold():
            continue
        if not body or body in seen:
            continue
        seen.add(body)
        selected.append((message.get("createdAt", ""), author, body))
        if len(selected) == recent:
            break
    return selected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--recent", type=int, default=7,
                        help="maximum unique messages (default: 7)")
    parser.add_argument("--contains", default="",
                        help="case-insensitive keyword/phrase filter")
    parser.add_argument("--page", type=int, default=1,
                        help="Antonina board page; only this page is searched")
    parser.add_argument("--max-chars", type=int, default=850,
                        help="maximum characters per message (default: 850)")
    args = parser.parse_args()
    if not (1 <= args.recent <= 20 and 1 <= args.page <= 1000
            and 100 <= args.max_chars <= 2000):
        parser.error("recent 1..20, page 1..1000, max-chars 100..2000")
    try:
        messages = fetch_messages(args.page)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired,
            ValueError, json.JSONDecodeError, OSError) as exc:
        print(f"Antonina board lookup failed: {exc}", file=sys.stderr)
        return 1
    selected = select_messages(messages, args.recent, args.contains)
    print(f"Antonina issue #{ISSUE_ID}, page {args.page} only, "
          f"{len(messages)} messages on page, {len(selected)} unique matches.")
    if args.contains:
        print(f"Filter: {args.contains}")
    for created, author, body in selected:
        print(f"\n[{created}] {author}")
        if len(body) > args.max_chars:
            print(body[:args.max_chars].rstrip() + " ... [excerpt truncated]")
        else:
            print(body)
    if not selected:
        print("No matches on this page; try another --page or --contains.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
