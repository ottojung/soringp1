"""Conservative Markdown rendering for archived research prose.

All source text is escaped. Raw HTML, scripts and remote images are not
rendered. Original Markdown remains available via an exact GitHub link.
"""
import html
import re
from urllib.parse import urlsplit


def esc(value):
    return html.escape(str(value), quote=True)


def slug(text):
    return re.sub(r'[^a-z0-9_-]+', '-', text.lower()).strip('-') or 'section'


def inline(text, resolve):
    # Code, inline links and basic emphasis; ordinary text is always escaped.
    pattern = re.compile(r'(`[^`\n]+`|!?\[[^\]\n]+\]\([^\s)]+\)|\*\*[^*\n]+\*\*|\*[^*\n]+\*)')
    result = []
    at = 0
    for m in pattern.finditer(text):
        result.append(esc(text[at:m.start()]))
        token = m.group()
        if token.startswith('`'):
            result.append('<code>'+esc(token[1:-1])+'</code>')
        elif token.startswith('[') or token.startswith('!['):
            link = re.fullmatch(r'!?\[([^\]]+)\]\(([^)]+)\)', token)
            label, url = link.groups()
            href = resolve(url)
            if href:
                result.append('<a href="'+esc(href)+'">'+esc(label)+'</a>')
            else:
                result.append(esc(label))
        elif token.startswith('**'):
            result.append('<strong>'+esc(token[2:-2])+'</strong>')
        else:
            result.append('<em>'+esc(token[1:-1])+'</em>')
        at = m.end()
    result.append(esc(text[at:]))
    return ''.join(result)


def cells(line):
    return [x.strip().replace('\\|','|') for x in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def markdown(source, resolve, omit_h1=False):
    lines = source.splitlines()
    out = []
    toc = []
    seen = {}
    i = 0
    skipped = False
    block_start = re.compile(r'^\s*(?:#{1,6}\s|[`~]{3,}|[-*+]\s|\d+[.)]\s|>\s|---+\s*$|\|)')
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        fence = re.match(r'^\s*([`~]{3,})(.*)$', line)
        if fence:
            close = fence.group(1)[0]
            j = i + 1
            while j < len(lines) and not re.match(r'^\s*'+re.escape(close)+r'{3,}\s*$',lines[j]):
                j += 1
            out.append('<pre><code>'+esc('\n'.join(lines[i+1:j]))+'</code></pre>')
            i = min(j+1,len(lines))
            continue
        head = re.match(r'^(#{1,6})\s+(.*)$', line)
        if head:
            level = len(head.group(1))
            label = head.group(2).strip()
            if omit_h1 and level == 1 and not skipped:
                skipped = True
                i += 1
                continue
            level = max(2, min(4, level))
            key = slug(label)
            seen[key] = seen.get(key, 0) + 1
            anchor = key if seen[key] == 1 else key+'-'+str(seen[key])
            if level <= 3:
                toc.append((label,anchor))
            out.append(f'<h{level} id="{anchor}">'+inline(label,resolve)+f'</h{level}>')
            i += 1
            continue
        if re.fullmatch(r'\s*(?:---+|\*\*\*+)\s*',line):
            out.append('<hr>')
            i += 1
            continue
        if line.lstrip().startswith('|') and i+1 < len(lines) and re.fullmatch(r'[\s|:-]+',lines[i+1]):
            rows = [cells(line)]
            j = i+2
            while j<len(lines) and lines[j].lstrip().startswith('|'):
                rows.append(cells(lines[j]))
                j+=1
            out.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+inline(c,resolve)+'</th>' for c in rows[0])+'</tr></thead><tbody>')
            for row in rows[1:]:
                out.append('<tr>'+''.join('<td>'+inline(c,resolve)+'</td>' for c in row)+'</tr>')
            out.append('</tbody></table></div>')
            i=j
            continue
        if line.lstrip().startswith('>'):
            j=i
            group=[]
            while j<len(lines) and lines[j].lstrip().startswith('>'):
                group.append(lines[j].lstrip()[1:].lstrip());j+=1
            out.append('<blockquote><p>'+inline(' '.join(group),resolve)+'</p></blockquote>')
            i=j
            continue
        item=re.match(r'^\s*([-*+]|\d+[.)])\s+(.*)$',line)
        if item:
            tag='ol' if item.group(1)[0].isdigit() else 'ul'
            out.append('<'+tag+'>')
            j=i
            while j<len(lines):
                m=re.match(r'^\s*([-*+]|\d+[.)])\s+(.*)$',lines[j])
                if not m or ('ol' if m.group(1)[0].isdigit() else 'ul')!=tag:break
                content=[m.group(2)]
                j+=1
                while j<len(lines) and lines[j].strip() and lines[j].startswith('  ') and not block_start.match(lines[j]):
                    content.append(lines[j].strip());j+=1
                out.append('<li>'+inline(' '.join(content),resolve)+'</li>')
            out.append('</'+tag+'>')
            i=j
            continue
        j=i+1
        while j<len(lines) and lines[j].strip() and not block_start.match(lines[j]):
            j+=1
        out.append('<p>'+inline(' '.join(lines[i:j]),resolve)+'</p>')
        i=j
    return '\n'.join(out),toc
