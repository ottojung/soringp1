#!/usr/bin/env python3
"""Verify generated and curated relative Markdown navigation without external I/O."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / 'recovery'


def main():
    pages = {ROOT/'README.md', ROOT/'AGENTS.md', ROOT/'docs/README.md',
             ARCHIVE/'followup/README.md', ARCHIVE/'tools/README.md',
             ARCHIVE/'followup/github-discussions/README.md',
             ARCHIVE/'followup/github-discussions/PULL-REQUESTS.md'}
    pages.update(ARCHIVE.glob('*.md'))
    pages.update((ARCHIVE/'catalog').rglob('*.md'))
    errors = []
    count = 0
    line_counts = {}
    for p in sorted(pages):
        if not p.is_file():
            errors.append(f'Missing navigation page: {p.relative_to(ROOT)}')
            continue
        for m in re.finditer(r'(?<!\\)\]\(([^\s)]+)\)', p.read_text(encoding='utf-8')):
            u = m.group(1)
            if u.startswith(('#', 'http:', 'https:', 'mailto:', '/')):
                continue
            path = unquote(urlsplit(u).path)
            if not path:
                continue
            count += 1
            t = (p.parent/path).resolve()
            label = f'{p.relative_to(ROOT)} -> {u}'
            if not t.is_relative_to(ROOT):
                errors.append(label + ' (outside repository)')
                continue
            if not t.exists():
                errors.append(label + ' (missing)')
                continue
            anchor = re.search(r'#L(\d+)', u)
            if anchor and t.is_file():
                if t not in line_counts:
                    line_counts[t] = len(t.read_bytes().splitlines())
                if int(anchor.group(1)) > line_counts[t]:
                    errors.append(label + ' (line anchor out of range)')
    print(f'Navigation: {len(pages)} pages, {count} relative links, {len(errors)} errors')
    for error in errors[:50]:
        print(error, file=sys.stderr)
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
