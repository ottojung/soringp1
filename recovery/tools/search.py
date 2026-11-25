#!/usr/bin/env python3
"""Browse and verify the SoringP1 archive using only Python's standard library."""
import argparse
from collections import defaultdict
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))

def read(path):
    return (ROOT/path).read_text(encoding='utf-8',errors='replace')

def short(s,n=200):
    s=' '.join(str(s).split())
    return s if len(s)<=n else s[:n-1]+'…'

def select(rows,key,value):
    exact=[r for r in rows if r[key]==value]
    if exact:return exact[0]
    found=[r for r in rows if value.lower() in r[key].lower()]
    if len(found)==1:return found[0]
    if not found:raise ValueError(f'No match: {value}')
    raise ValueError(f'Ambiguous: {value}\n'+'\n'.join(r[key] for r in found[:20]))

def message_text(row,cache):
    p=row['path']
    if p not in cache:cache[p]=read(p).splitlines()
    lines=cache[p]; start=row['line']-1; end=len(lines)
    for i in range(start+1,len(lines)):
        if re.match(r'^## \d{4}-\d\d-\d\dT[^ ]+ — ',lines[i]):
            end=i;break
    return '\n'.join(lines[start:end])

def search(index,args):
    terms=[x.casefold() for x in args.terms if x]
    kinds=set(args.kind or ['front','board','source','session','commission','mixed','github','patch','docs','supplement'])
    result=[]; cache={}; visited=set()
    def consider(kind,title,path,body=None,line=1,meta=''):
        key=(kind,path,line)
        if key in visited:return
        t=(title+' '+meta).casefold()
        if args.metadata:
            full=t
        else:
            if body is None:body='' if path.endswith('.gz') else read(path)
            full=t+'\n'+body.casefold()
        if not all(term in full for term in terms):return
        visited.add(key)
        rank=sum((10 if term in t else 0)+min(full.count(term),5) for term in terms)
        excerpt=''
        if body:
            for n,l in enumerate(body.splitlines()):
                if any(x in l.casefold() for x in terms):
                    excerpt=short(l,180);line+=n;break
        result.append((rank,kind,title,path,line,excerpt))
    if 'front' in kinds:
        for f in index['fronts']:
            consider('front',f['id'],f['path'],meta=f['topic']+' '+f['question']+' '+f['status'])
    if 'board' in kinds:
        for b in index['board']:
            consider('board',b['date']+' '+b['author']+' '+b['title'],b['path'],
                     body=None if args.metadata else message_text(b,cache),line=b['line'],
                     meta=b['id']+' '+b['verdict']+' '+' '.join(b['fronts']))
    if 'source' in kinds:
        for s in index['sources']:
            consider('source',s['name'],s['path'],meta=' '.join(s['origins']))
    if 'session' in kinds:
        for s in index['sessions']:
            consider('session',s['id'],s['path'],meta=s['workspace']+' '+' '.join(s['fronts']))
    if 'commission' in kinds:
        for c in index.get('commissions',[]):
            consider('commission',c['title'],c['path'],meta=' '.join(c['workspaces']+c['fronts']))
    if 'mixed' in kinds:
        for r in index.get('mixed_reports',[]):
            consider('mixed',r['title'],r['path'],meta=' '.join(r['workspaces']+r['sessions']+r['fronts']))
    if 'github' in kinds:
        for i in index.get('github',[]):
            consider('github',i.get('kind','issue')+' #'+i['id']+' '+i['title'],i['path'],meta=i['state'])
    if 'patch' in kinds:
        for p in index['commits']:
            consider('patch',p['subject'],p['path'],meta=p['id'])
    if 'docs' in kinds:
        paths=[ROOT.parent/'README.md',ROOT.parent/'AGENTS.md',ROOT.parent/'SoringP1.lean']
        for folder in ('docs','notes','SoringP1','scripts','tests'):
            paths.extend(p for p in (ROOT.parent/folder).rglob('*') if p.is_file() and p.suffix in {'.md','.lean','.py','.go','.cpp','.hpp','.txt'} and '__pycache__' not in p.parts)
        for p in sorted(set(paths)):
            if not p.is_file():continue
            rel=str(p.relative_to(ROOT.parent))
            consider('docs',p.stem,'../'+rel,p.read_text(encoding='utf-8',errors='replace'))
        for p in sorted(ROOT.glob('*.md')):
            if p.name in ('THEMES.md','BOARD-INDEX.md'):continue
            consider('docs',p.stem,p.name)
    if 'supplement' in kinds:
        for p in sorted((ROOT/'quarantine').rglob('*')):
            if p.is_file() and p.suffix in {'.md','.py','.cpp','.hpp','.log','.err','.txt','.out'}:
                consider('supplement',p.name,str(p.relative_to(ROOT)))
        for p in sorted((ROOT/'state').glob('*')):
            if p.is_file():consider('supplement',p.name,str(p.relative_to(ROOT)))
        for p in sorted((ROOT/'followup').glob('*.json')):
            consider('supplement',p.name,str(p.relative_to(ROOT)))
    result.sort(key=lambda x:(-x[0],x[1],x[3],x[4]))
    print(f'{len(result)} matches; showing {min(args.limit,len(result))}')
    for rank,kind,title,path,line,excerpt in result[:args.limit]:
        print(f'[{kind}] {short(title,150)}\n  {path}:{line}')
        if excerpt:print('  '+excerpt)

def front(index,ident):
    f=select(index['fronts'],'id',ident)
    print(f['id'],f'({f["status"]})',f['topic'],sep=' — ')
    print(f['question'],'\nOriginal full report:',f['path'])
    for key,label in [('falsifier','Intended test or falsifier'),('implication','Proposed implication'),('reported_excerpt','Historical reported excerpt (unverified)')]:
        if f.get(key):print(label+': '+f[key])
    print('\nBoard links (matching title, opening text or explicit author):')
    rows={b['id']:b for b in index['board']}
    for mid in f['board']:
        b=rows[mid]
        print(f'  {b["date"]} {b["path"]}:{b["line"]} {short(b["verdict"] or b["title"],125)}')
    print('\nRelated workspace manifests:')
    for p in f['workspaces']:print('  '+p)
    print('\nRelated assistant reports:')
    for p in f['sessions']:print('  '+p)
    if f.get('commissions'):
        print('\nHistorical task commissions:')
        for p in f['commissions']:print('  '+p)
    if f.get('mixed_reports'):
        print('\nRelated mixed-project research reports:')
        for p in f['mixed_reports']:print('  '+p)
    if f.get('mentions'):
        print('\nAdditional board mentions (not necessarily findings about this front):')
        for mid in f['mentions']:
            if mid in f['board']:continue
            b=rows[mid];print(f'  {b["date"]} {b["path"]}:{b["line"]} {short(b["title"],100)}')

def workspace(index,ident):
    w=select(index['workspaces'],'workspace',ident)
    print(w['workspace'],'\nManifest:',w['manifest'],'\nHEAD:',w['head'])
    for source,obj in sorted(load(w['manifest'])['files'].items()):
        print(f'  {source} → workspaces/objects/{obj}')

def extract(index,ident,dest):
    w=select(index['workspaces'],'workspace',ident)
    d=Path(dest).resolve()
    if d.exists() and (not d.is_dir() or any(d.iterdir())):
        raise ValueError('Destination must be absent or an empty directory')
    mappings=load(w['manifest'])['files']
    targets=[]
    for source,obj in mappings.items():
        relative=Path(source)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError(f'Unsafe archived path: {source}')
        p=d/relative
        q=(ROOT/'workspaces/objects'/obj).resolve()
        if not q.is_relative_to((ROOT/'workspaces/objects').resolve()) or not q.is_file():
            raise ValueError(f'Invalid archive object: {obj}')
        targets.append((p,q))
    d.mkdir(parents=True,exist_ok=True)
    for p,q in targets:
        p.parent.mkdir(parents=True,exist_ok=True)
        with p.open('xb') as f:f.write(q.read_bytes())
    print(f'Extracted {len(targets)} archived changed/additional files to {d}.')
    print('Not a full historical checkout. No code was executed.')

def verify(index):
    errors=[]; notices=[]
    def exists(p):
        if not (ROOT/p).is_file():errors.append('missing file '+p)
    def unique(rows,key,label):
        seen=set()
        for row in rows:
            val=row[key]
            if val in seen:errors.append(f'duplicate {label}: {val}')
            seen.add(val)
        return seen
    front_ids=unique(index['fronts'],'id','front')
    board_ids=unique(index['board'],'id','board message')
    unique(index['workspaces'],'workspace','workspace')
    unique(index['sessions'],'path','session path')
    unique(index['commits'],'id','patch')
    if len(front_ids)!=750:errors.append(f'expected 750 original fronts; got {len(front_ids)}')
    if len(board_ids)<3725:errors.append(f'expected at least 3725 original board messages; got {len(board_ids)}')
    for f in index['fronts']:
        exists(f['path'])
        for mid in f['board']+f.get('mentions',[]):
            if mid not in board_ids:errors.append('missing referenced board ID '+mid)
        for p in f['sessions']+f['workspaces']+f.get('commissions',[])+f.get('mixed_reports',[]):exists(p)
    for s in index['sessions']+index['commits']+index['sources']+index.get('commissions',[])+index.get('mixed_reports',[])+index.get('github',[]):exists(s['path'])
    cache={}
    for b in index['board']:
        exists(b['path'])
        if (ROOT/b['path']).is_file() and 'Message ID: '+b['id'] not in message_text(b,cache):
            errors.append('incorrect message anchor '+b['id'])
    for w in index['workspaces']:
        exists(w['manifest'])
        for obj in load(w['manifest'])['files'].values():exists('workspaces/objects/'+obj)
    for obj in load('supplement/manifest.json').values():exists('supplement/objects/'+obj)
    for audit in ('followup/file-audit.json','followup/marceline-audit.json'):
        if (ROOT/audit).is_file():
            for row in load(audit)['mappings']:exists(row['path'])
    if (ROOT/'followup/ledger.json').is_file():
        actual={f['id'] for f in load('followup/ledger.json')['fronts']}
        if actual!=front_ids:errors.append('machine-readable ledger front IDs differ')
    # Original archive file names encode the initially sanitized content.
    # Additional line redactions explicitly recorded during first recovery
    # can legitimately change the bytes; no hash mismatch is silently ignored.
    redacted={r['path'] for r in load('workspaces/additional-redactions.json')}
    for folder in ['workspaces/objects','supplement/objects','followup/objects','followup/orphan-blobs','followup/dangling-drafts/objects','followup/task-commissions/objects','followup/mixed-reports/objects']:
        for p in sorted((ROOT/folder).glob('*')):
            if not p.is_file():continue
            stem=p.name.split('.')[0]
            if not re.fullmatch('[0-9a-f]{64}',stem):continue
            if hashlib.sha256(p.read_bytes()).hexdigest()!=stem:
                if folder=='workspaces/objects' and 'objects/'+p.name in redacted:
                    notices.append('recorded redaction '+p.name)
                else:errors.append('unexplained content hash mismatch '+str(p.relative_to(ROOT)))
    print('Counts:',{k:len(v) for k,v in index.items()})
    for n in notices:print('NOTE:',n)
    for e in errors[:30]:print('ERROR:',e,file=sys.stderr)
    print(f'Archive integrity: {len(errors)} errors')
    return 1 if errors else 0

def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    s=sub.add_parser('search',help='Search metadata and full research text')
    s.add_argument('terms',nargs='+',help='All terms must match; quote phrases')
    s.add_argument('--kind',action='append',choices=['front','board','source','session','commission','mixed','github','patch','docs','supplement'])
    s.add_argument('--metadata',action='store_true',help='Search only titles, IDs and source paths')
    s.add_argument('--limit',type=int,default=25)
    for name,helptext in [('front','Show a research front and all linked evidence'),('board','Print one original board message by ID or unique prefix'),('workspace','List original files and archive objects')]:
        q=sub.add_parser(name,help=helptext);q.add_argument('id')
    q=sub.add_parser('extract',help='Extract archived changed files of one workspace without executing them')
    q.add_argument('id');q.add_argument('destination')
    sub.add_parser('verify',help='Check catalogue references, message anchors, coverage and object hashes')
    a=p.parse_args();index=load('catalog/index.json')
    try:
        if a.command=='search':
            if a.limit<=0:raise ValueError('--limit must be positive')
            search(index,a)
        elif a.command=='front':front(index,a.id)
        elif a.command=='board':print(message_text(select(index['board'],'id',a.id),{}))
        elif a.command=='workspace':workspace(index,a.id)
        elif a.command=='extract':extract(index,a.id,a.destination)
        elif a.command=='verify':return verify(index)
    except (ValueError,OSError,KeyError) as e:
        print(str(e),file=sys.stderr);return 2
    return 0

if __name__=='__main__':sys.exit(main())
