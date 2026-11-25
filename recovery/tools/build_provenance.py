#!/usr/bin/env python3
"""Cross-reference missing scratch paths and report labels in the published archive.

This operates only on already-archived public project text. It does not
recover missing file bytes, infer mathematical validity or read agent state.
"""
from collections import defaultdict
from pathlib import Path
import argparse
import hashlib
import json
import os
import re

ROOT=Path(__file__).resolve().parents[1]
FOLLOW=ROOT/'followup'
PATH=re.compile(r'/tmp/[A-Za-z0-9_./+@-]+')
LABEL=re.compile(r'(?:SoringP1\s+(?:frontier|front|researcher|executive):\s*|\[front:\s*|\bFront\s+`)([A-Za-z0-9][A-Za-z0-9_-]{6,})',re.I)

def data(path):
    return json.loads(path.read_text(encoding='utf-8'))

def short(text,n=160):
    text=' '.join(str(text or '').split())
    return text if len(text)<=n else text[:n-1]+'…'

def esc(text):
    return str(text).replace('|','\\|').replace('<','&lt;').replace('>','&gt;').replace('[','\\[').replace(']','\\]')

def link(label,target,source,line=None):
    rel=os.path.relpath(ROOT/target,(FOLLOW/source).parent)
    if line is not None:rel+=f'?plain=1#L{line}'
    return f'[{esc(label)}]({rel})'

def emit(path,lines,check,errors):
    path=FOLLOW/path
    text='\n'.join(lines).rstrip()+'\n'
    if check:
        if not path.is_file() or path.read_text()!=text:errors.append(str(path))
    else:
        path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text,encoding='utf-8')

def emit_json(path,value,check,errors):
    emit(path,[json.dumps(value,ensure_ascii=False,indent=2)],check,errors)

def build(check=False):
    x=data(ROOT/'catalog/index.json')
    ids={f['id']:f for f in x['fronts']}
    lower={f.lower():f for f in ids}
    old=data(FOLLOW/'scratch-reference-audit.json')
    targets={row['original_reference']:row for row in old}
    references=defaultdict(dict)
    labels=defaultdict(dict)
    board_files=defaultdict(list)
    errors=[]
    def scan(path,text,kind,title,related=(),line=1,date=''):
        related=sorted(set(f for f in related if f in ids))
        topics=sorted({ids[f]['topic'] for f in related})
        for m in PATH.finditer(text):
            p=m.group().rstrip('.,')
            if p not in targets:continue
            ln=line+text.count('\n',0,m.start())
            k=(kind,path,line)
            if k not in references[p]:
                references[p][k]={'kind':kind,'path':path,'line':ln,'title':short(title,180),'date':date,'fronts':related,'topics':topics}
    for f in x['fronts']:
        scan(f['path'],(ROOT/f['path']).read_text(errors='replace'),'front',f['id'],[f['id']])
    for b in x['board']:board_files[b['path']].append(b)
    for path,rows in sorted(board_files.items()):
        lines=(ROOT/path).read_text(errors='replace').splitlines()
        rows.sort(key=lambda r:r['line'])
        for i,b in enumerate(rows):
            start=b['line']-1;end=rows[i+1]['line']-1 if i+1<len(rows) else len(lines)
            text='\n'.join(lines[start:end])
            related=list(dict.fromkeys(b['fronts']+b.get('mentions',[])))
            scan(path,text,'board',b['title'] or b['author'],related,b['line'],b['date'])
            for m in LABEL.finditer(b['author']+'\n'+b['title']):
                name=m.group(1)
                if '-' not in name or name.lower() in lower:continue
                labels[name.lower()][b['id']]={'path':path,'line':b['line'],'id':b['id'],'date':b['date'],'title':short(b['title'] or b['author'],200),'author':b['author'],'verdict':short(b.get('verdict',''),300),'fronts':related}
    for kind,collection in [('session','sessions'),('commission','commissions'),('mixed report','mixed_reports')]:
        for row in x[collection]:
            path=row['path'];title=row.get('title',row.get('workspace',row.get('id',path)))
            scan(path,(ROOT/path).read_text(errors='replace'),kind,title,row.get('fronts',[]))
    for row in x['sources']:
        for original in row['origins']:
            scan(row['path'],original,'source path',row['name'])
    # Preserve exact references in canonical notes and docs where present.
    for path in sorted((ROOT.parent/'docs').glob('*.md'))+sorted((ROOT.parent/'notes').glob('*.md')):
        scan(os.path.relpath(path,ROOT),path.read_text(errors='replace'),'canonical note',path.name)

    scratch=[];scratch_index=['# Missing scratch references','','These pages locate surviving, exact path mentions. They are **not** reconstructed scratch-file contents. Some entries may be directory names, examples, executable paths or filenames mentioned in passing.','', '[Archive home](../../README.md)','','| Original reference | Surviving report references | Candidate filename matches |','|---|---:|---:|']
    for path,oldrow in sorted(targets.items()):
        key=hashlib.sha256(path.encode()).hexdigest()[:20]
        name=f'scratch-provenance/{key}.md'
        refs=sorted(references[path].values(),key=lambda r:(r['kind'],r['date'],r['path'],r['line']))
        candidates=oldrow['candidate_archive_paths']
        ts=sorted({t for r in refs for t in r['topics']})
        summary=f'{len(refs)} surviving exact-path report references; {len(candidates)} candidate filename matches. Original scratch bytes not established.'
        row={'title':path,'summary':summary,'page':f'scratch/{key}.html','markdown':name,'topics':ts,'references':refs,'candidate_archive_paths':candidates}
        scratch.append(row)
        lines=[f'# {path}','','[Scratch reference index](README.md) · [Archive home](../../README.md)','','**Recovery status:** original file bytes are not established. This page links historical reports that mention the exact path, rather than claiming to recreate the original file.','',f'{len(refs)} surviving exact-path references; {len(candidates)} possible archived filename matches.','']
        if refs:
            lines+=['## Surviving references','']
            for r in refs:
                lines.append(f"- {esc(r['kind'])}: {link(r['title'],r['path'],name,r['line'])}"+(f" ({r['date'][:10]})" if r['date'] else ''))
        else:lines+=['No exact path mention was found by this pass in the indexed public report collections. The original omission record is retained.']
        if candidates:
            lines+=['','## Possible archived filename matches','','These are filename-only leads, not evidence of identical historical bytes.','']
            for c in candidates:lines.append('- '+link(Path(c).name,c,name))
        emit(name,lines,check,errors)
        scratch_index.append(f'| [{esc(path)}]({key}.md) | {len(refs)} | {len(candidates)} |')
    emit('scratch-provenance/README.md',scratch_index,check,errors)
    emit_json('scratch-provenance.json',scratch,check,errors)

    history=[];label_index=['# Historical report labels outside the final ledger','','An explicit report label is not necessarily a distinct mathematical front. Some are older names, follow-up checks, aliases or one-off investigations. The final ledger still contains 750 fronts. This index makes the additional historical labels discoverable.','','[Archive home](../../README.md)','','| Label | Board messages | Related final ledger fronts |','|---|---:|---:|']
    ws=x['workspaces']
    for name,rows in sorted(labels.items()):
        rows=sorted(rows.values(),key=lambda b:(b['date'],b['id']))
        related=set(f for b in rows for f in b['fronts'])
        # Date suffixes sometimes identify a later commission of a ledger front.
        base=re.sub(r'-20\d{6}[a-z]*$','',name)
        alias=lower.get(base)
        if alias:related.add(alias)
        related=sorted(related)
        workspaces=[w for w in ws if Path(w['workspace']).name.lower()==name]
        key=hashlib.sha256(name.encode()).hexdigest()[:20]
        md=f'historical-labels/{key}.md'
        ts=sorted({ids[f]['topic'] for f in related})
        summary=f'{len(rows)} board message(s); {len(related)} linked final-ledger fronts; {len(workspaces)} exact-name workspace inventories.'
        history.append({'title':name,'summary':summary,'page':f'labels/{key}.html','markdown':md,'topics':ts,'board':rows,'related_fronts':related,'workspaces':[w['manifest'] for w in workspaces],'possible_date_alias':alias})
        lines=[f'# {name}','','[Historical label index](README.md) · [Archive home](../../README.md)','','This label appeared in an explicit historical board author or report heading but is not an exact ID in the final ledger. It may be an alias, earlier investigation or follow-up review; it is not automatically a new research front.','',summary,'']
        if alias:lines+=['Possible dated alias: '+link(alias,ids[alias]['path'],md)+'.','']
        lines+=['## Original board evidence','']
        for b in rows:
            lines.append(f"- {b['date'][:10]} — {link(b['title'],b['path'],md,b['line'])}")
            if b['verdict']:lines.append('  - Historical verdict marker: '+esc(b['verdict']))
        if related:lines+=['','## Linked ledger fronts','']+['- '+link(f,ids[f]['path'],md) for f in related]
        if workspaces:lines+=['','## Exact-name workspace inventories','']+['- '+link(w['workspace'],w['manifest'],md) for w in workspaces]
        emit(md,lines,check,errors)
        label_index.append(f'| [{esc(name)}]({key}.md) | {len(rows)} | {len(related)} |')
    emit('historical-labels/README.md',label_index,check,errors)
    emit_json('historical-labels.json',history,check,errors)
    print('Scratch paths:',len(scratch),'with surviving exact-path references:',sum(bool(r['references']) for r in scratch),'references:',sum(len(r['references']) for r in scratch))
    print('Historical labels outside final ledger:',len(history),'possible dated aliases:',sum(bool(r['possible_date_alias']) for r in history))
    if errors:print('Stale or missing outputs:',*errors[:20],sep='\n')
    return bool(errors)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true')
    raise SystemExit(build(p.parse_args().check))
