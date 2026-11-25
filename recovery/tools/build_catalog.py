#!/usr/bin/env python3
"""Build a deterministic, GitHub-browsable catalogue from the archival evidence."""
from pathlib import Path
from collections import defaultdict, Counter
import json, re, os, string, argparse, sys

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'catalog'
TOPIC_RE = re.compile(r'^## (.+) \(\d+\)$')
FRONT_RE = re.compile(r'^- \[([^\]]+)\]\(fronts/([^\)]+)\)')
MSG_RE = re.compile(r'^## (\d{4}-\d\d-\d\dT[^ ]+) — (.+)$', re.M)
MID_RE = re.compile(r'^Message ID: (.+)$', re.M)

def read(p):
    return p.read_text(encoding='utf-8', errors='replace')

def data(p):
    return json.loads(read(p))

def flat(s, n=180):
    s = ' '.join(str(s).split())
    return s if len(s) <= n else s[:n-1] + '…'

def esc(s):
    return str(s).replace('|', '\\|').replace('<', '&lt;').replace('>', '&gt;').replace('[', '\\[').replace(']', '\\]')

def link(label, path, page, line=None):
    relative = os.path.relpath(path, page.parent)
    if line is not None:
        relative += f'?plain=1#L{line}'
    return f'[{esc(label)}]({relative})'

def section(s, key):
    match = re.search(r'^## '+re.escape(key)+r'\n\n(.*?)(?=\n## |\Z)',s,re.M|re.S)
    return match.group(1).strip() if match else ''

def slug(s):
    return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')

def chunks(rows, size):
    return [rows[i:i+size] for i in range(0,len(rows),size)]

def main(check=False):
    outputs = {}
    def emit(path, lines):
        outputs[OUT/path] = ('\n'.join(lines).rstrip()+'\n')
    topics = defaultdict(list)
    front_ids = {}
    for line in read(ROOT/'THEMES.md').splitlines():
        m = TOPIC_RE.match(line)
        if m: topic=m.group(1); continue
        m = FRONT_RE.match(line)
        if not m: continue
        ident, filename = m.groups()
        p = ROOT/'fronts'/filename
        txt = read(p)
        rec = {'id':ident,'path':str(p.relative_to(ROOT)),'topic':topic,
               'status':section(txt,'status'),'question':section(txt,'question'),
               'agent':section(txt,'agent_id'),'board':[], 'sessions':[], 'workspaces':[]}
        topics[topic].append(rec); front_ids[ident] = rec
    assert len(front_ids) == 750
    # Use exact ID tokens in message headings/authors, plus exact agent ID.
    # A matching reference is a navigation lead, not proof or attribution.
    ids_sorted = sorted(front_ids, key=len, reverse=True)
    front_rx = re.compile(r'(?<![A-Za-z0-9_-])(?:'+'|'.join(map(re.escape,ids_sorted))+r')(?![A-Za-z0-9_-])')
    agent_to_front=defaultdict(list)
    for rec in front_ids.values():
        if rec['agent']: agent_to_front[rec['agent']].append(rec['id'])
    board=[]
    for page in sorted((ROOT/'board').glob('*/page-*.md')):
        text=read(page); heads=list(MSG_RE.finditer(text))
        for i,m in enumerate(heads):
            part=text[m.end():heads[i+1].start() if i+1<len(heads) else len(text)]
            mid=MID_RE.search(part)
            if not mid: continue
            body=part[mid.end():].strip()
            if body.endswith('---'): body=body[:-3].rstrip()
            title=next((l.strip() for l in body.splitlines() if l.strip()),'')
            verdict=next((l.strip() for l in body.splitlines() if re.match(r'^\s*(?:\*\*)?(VERDICT|DISPOSITION)\b',l,re.I)), '')
            focus=set(front_rx.findall(m.group(2)+' '+title+' '+verdict))
            # Some Executive reviews refer to a front only in their opening paragraph.
            if not focus: focus.update(front_rx.findall(body[:500]))
            for aid, fs in agent_to_front.items():
                if aid and aid in m.group(2): focus.update(fs)
            row={'id':mid.group(1).strip(),'date':m.group(1),'author':m.group(2),'path':str(page.relative_to(ROOT)), 'line':text.count('\n',0,m.start())+1,'title':flat(title,240),'verdict':flat(verdict,300),'fronts':sorted(focus)}
            board.append(row)
            for f in row['fronts']: front_ids[f]['board'].append(row['id'])
    assert len({b['id'] for b in board}) == len(board)
    board.sort(key=lambda b:(b['date'],b['id']))
    board_by_id={b['id']:b for b in board}
    # Relate workspace IDs by exact name, or exact ID followed by a dated suffix.
    def match_workspace(w):
        name=Path(w).name
        if name in front_ids: return [name]
        name=re.sub(r'-20\d{6}[a-z]*$','',name)
        if name in front_ids: return [name]
        return []
    workspaces=[]; sources=defaultdict(list)
    for p in sorted((ROOT/'workspaces/manifests').glob('*.json')):
        x=data(p); w=x['source']; rel=str(p.relative_to(ROOT))
        row={'workspace':w,'manifest':rel,'files':len(x['files']),'fronts':match_workspace(w),'head':x.get('head','')}
        workspaces.append(row)
        for f in row['fronts']: front_ids[f]['workspaces'].append(rel)
        for original,obj in x['files'].items():
            target=ROOT/'workspaces/objects'/obj
            if not target.is_file(): raise ValueError(f'missing object {target}')
            sources[(Path(original).name,str(target.relative_to(ROOT)))].append(w+'/'+original)
    for original,obj in data(ROOT/'supplement/manifest.json').items():
        target=ROOT/'supplement/objects'/obj
        if not target.is_file():raise ValueError(f'missing object {target}')
        sources[(Path(original).name,str(target.relative_to(ROOT)))].append(original)
    sessions=[]
    for name in ['session-index.json','agent-index.json']:
        for x in data(ROOT/'assistant-reports'/name):
            rel='assistant-reports/'+x['path']
            assert (ROOT/rel).is_file(),rel
            fs=set(match_workspace(x['workspace']))
            title=x.get('title','')
            for aid, f in agent_to_front.items():
                if aid and aid in title:fs.update(f)
            fs.update(agent_to_front.get(x.get('agent',''),[]))
            row={'id':x.get('session',x.get('agent','')),'workspace':x['workspace'],'path':rel,'outputs':x['outputs'],'fronts':sorted(fs)}
            sessions.append(row)
            for f in fs: front_ids[f]['sessions'].append(rel)
    commits=[]
    for folder in ['workspaces/commits','followup/patches']:
        for p in sorted((ROOT/folder).glob('*.patch')):
            # Git show --format=fuller, first indented subject in header.
            head=read(p)[:5000].split('\ndiff --git',1)[0]
            subject=next((l.strip() for l in head.splitlines() if l.startswith('    ') and l.strip()),p.stem)
            commits.append({'id':p.stem,'path':str(p.relative_to(ROOT)),'subject':subject})
    # Markdown catalogue, split into comfortably sized pages.
    overview=['# Research catalogue','','This index is generated from the archived evidence. Links connect questions, dated board messages, original source objects, assistant reports and historical patches. Matching IDs are navigation aids, not new verification.','','Start with the [mathematical synthesis](../SYNTHESIS.md), [result register](../RESULTS.md), and [open questions](../OPEN-QUESTIONS.md).','','## Research topics','']
    for topic, rows in topics.items():
        p=OUT/'topics'/f'{slug(topic)}.md'
        overview.append(f'- {link(topic,p,OUT/"README.md")} — {len(rows)} fronts')
        lines=[f'# {topic}','','[Catalogue home](../README.md) · [Evidence status guide](../../RESULTS.md)','','Status is the original workflow label, not mathematical proof. Linked messages may contain corrections or rejected claims.','']
        for f in rows:
            lines.extend([f'## {f["id"]}','',f'{esc(f["question"])}','',f'**{f["status"]}** · {link("Full research report",ROOT/f["path"],p)}'])
            ev=[]
            for mid in f['board'][-5:]:
                b=board_by_id[mid]
                ev.append(link(b['date'][:10]+' '+('review' if b['verdict'] else 'message'),ROOT/b['path'],p,b['line']))
            if ev:lines.append('Board: '+' · '.join(ev)+(f' ({len(f["board"])} total; use search for all)' if len(f['board'])>5 else ''))
            if f['sessions']:lines.append('Assistant reports: '+' · '.join(link(Path(x).stem,ROOT/x,p) for x in f['sessions'][:3])+(f' ({len(f["sessions"])} total)' if len(f['sessions'])>3 else ''))
            if f['workspaces']:lines.append('Source manifests: '+' · '.join(link(Path(x).stem,ROOT/x,p) for x in f['workspaces'][:3]))
            lines.append('')
        emit(p.relative_to(OUT),lines)
    overview.extend(['','## Evidence collections',''])
    def collection(name, heading, rows, title, render, size=100):
        ip=OUT/name/'README.md'
        overview.append(f'- {link(heading,ip,OUT/"README.md")} — {len(rows):,} {title}')
        il=[f'# {heading}','','[Catalogue home](../README.md)','','Entries are original evidence, not claims independently checked during archival.','']
        for n,batch in enumerate(chunks(rows,size),1):
            page=OUT/name/f'{n:03d}.md'
            label=f'{n:03d} · {title} {1+(n-1)*size}–{(n-1)*size+len(batch)}'
            il.append(f'- {link(label,page,ip)} — {esc(flat(batch[0].get("label",""),70))}')
            lines=[f'# {heading}: {label}','','[Collection index](README.md) · [Catalogue home](../README.md)','']
            for row in batch:lines.extend(render(row,page))
            emit(page.relative_to(OUT),lines)
        emit(ip.relative_to(OUT),il)
    for b in board:b['label']=b['date']
    collection('board','Board messages',board,'messages',lambda b,p:[f'- {link(b["date"]+" — "+b["author"],ROOT/b["path"],p,b["line"])} · {esc(b["id"])}',f'  - {esc(b["verdict"] or b["title"])}'+(' · Front: '+', '.join(b['fronts']) if b['fronts'] else '')],100)
    workspaces.sort(key=lambda w:w['workspace'])
    for w in workspaces:w['label']=w['workspace']
    def workspace_lines(w,p):
        x=data(ROOT/w['manifest'])
        return [f'### {esc(w["workspace"])}','',f'{link("Manifest",ROOT/w["manifest"],p)} · {w["files"]} source entries · HEAD {w["head"][:12]}','']+[f'- {link(path,ROOT/"workspaces/objects"/obj,p)}' for path,obj in sorted(x['files'].items())]+['']
    collection('workspaces','Workspace source maps',workspaces,'workspaces',workspace_lines,75)
    sr=[{'label':name,'name':name,'path':path,'origins':sorted(set(paths))} for (name,path),paths in sources.items()]
    sr.sort(key=lambda s:(s['name'].lower(),s['path']))
    def source_lines(s,p):
        return [f'- {link(s["name"],ROOT/s["path"],p)} · {len(s["origins"])} source locations',f'  - '+esc(flat(s['origins'][0],220))+(f' (+{len(s["origins"])-1} locations; see manifest/search)' if len(s['origins'])>1 else '')]
    collection('sources','Source files by original name',sr,'file versions',source_lines,100)
    sessions.sort(key=lambda s:(s['workspace'],s['id']))
    for s in sessions:s['label']=s['workspace']
    collection('sessions','Assistant report sessions',sessions,'sessions',lambda s,p:[f'- {link(s["id"],ROOT/s["path"],p)} · {s["outputs"]} outputs · {esc(s["workspace"])}'],100)
    commits.sort(key=lambda c:(c['subject'].lower(),c['id']))
    for c in commits:c['label']=c['subject']
    collection('commits','Historical commit patches',commits,'patches',lambda c,p:[f'- {link(c["id"][:12],ROOT/c["path"],p)} · {esc(flat(c["subject"],170))}'],150)
    overview.extend(['','## Search on a local clone','','The dependency-free search tool covers front reports, full board messages, recovered code, patches, assistant outputs, and original path mappings. See [search and integrity checks](../tools/README.md).','','The raw archive is linked in [the recovery guide](../README.md).'])
    emit(Path('README.md'),overview)
    # Small structured lookup index for the CLI and reproducibility.
    index={'fronts':sorted(front_ids.values(),key=lambda f:f['id']),'board':board,'workspaces':workspaces,'sources':sr,'sessions':sessions,'commits':commits}
    outputs[OUT/'index.json']=json.dumps(index,ensure_ascii=False,separators=(',',':'))+'\n'
    bad=[]
    for path,txt in outputs.items():
        if check:
            if not path.is_file() or read(path)!=txt:bad.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(txt,encoding='utf-8')
    print('fronts',len(front_ids),'board',len(board),'workspaces',len(workspaces),'source versions',len(sr),'sessions',len(sessions),'patches',len(commits),'catalogue files',len(outputs))
    if bad:
        print('stale/missing generated files:',*bad[:20],sep='\n',file=sys.stderr)
        return 1
    return 0

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true')
    sys.exit(main(p.parse_args().check))
