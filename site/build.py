#!/usr/bin/env python3
"""Build the SoringP1 static research library. Never executes archive content."""
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
import hashlib
import json
import os
import posixpath
import re
import shutil
import subprocess

from render import esc, markdown, slug, inline
from results import CATEGORIES, parse as parse_results, plain
from search_index import SearchIndex, write_json
from gazette import home as gazette_home

ROOT=Path(__file__).resolve().parent.parent
ARCH=ROOT/'recovery'
OUT=ROOT/'site/_site'
DATA=json.loads((ARCH/'catalog/index.json').read_text())
REV=subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'],text=True).strip()
REPO='https://github.com/ottojung/soringp1'
SOURCE=REPO+'/blob/'+REV+'/'
KINDS={
 'result':('Curated results','Principal claims with explicit evidence type and scope'),
 'guide':('Reading guides','Curated and canonical mathematical documents'),
 'front':('Research fronts','Questions, conjectures and historical findings'),
 'board':('Board messages','Original dated reports and referee discussions'),
 'source':('Source files','Archived experimental code and original filename mappings'),
 'session':('Agent reports','Historical assistant-visible reports'),
 'commission':('Task commissions','Original mathematical task descriptions'),
 'mixed':('Cross-project reports','Research texts recovered from mixed sessions'),
 'github':('GitHub discussions','Issue and pull-request bodies and comments'),
 'patch':('Commit patches','Historical changes and commit provenance'),
 'workspace':('Workspaces','Original source path inventories'),
 'scratch':('Scratch references','Missing original paths and surviving evidence'),
 'label':('Historical labels','Named report directions outside the final ledger'),
}
GUIDES=[
 ('recovery/SYNTHESIS.md','Research synthesis','Main findings, negative results and lessons'),
 ('recovery/RESULTS.md','Results and evidence','Theorems, computations and their exact scope'),
 ('recovery/OPEN-QUESTIONS.md','Open questions','Conjectures and what would settle them'),
 ('recovery/CORRECTIONS.md','Corrections','Refuted claims, proof gaps and qualifications'),
 ('docs/problem.md','The problem','Precise comparison model and input encodings'),
 ('docs/kernel-results.md','Formal theorem inventory','Lean-checked results in the maintained library'),
 ('recovery/README.md','Archive guide','Coverage, scope and recovery boundaries'),
 ('recovery/followup/README.md','Recovery audit','Recovery provenance and known omissions'),
 ('recovery/followup/VERIFICATION.md','Verification','Reproducible integrity and test checks'),
 ('recovery/tools/README.md','Offline tools','Search, extract and verify the repository locally'),
]
def compact(s,n=300):
    s=' '.join(str(s or '').split())
    return s if len(s)<=n else s[:n-1]+'…'

def read(p,limit=1048576):
    with (ROOT/p).open('rb') as f:return f.read(limit).decode('utf-8','replace')

def repo_link(p,anchor=''):
    return SOURCE+quote(str(p),safe='/')+anchor

def rel(page,path):
    return posixpath.relpath(path,posixpath.dirname(page) or '.')

def link(page,path,label,cls=''):
    return '<a'+(' class="'+esc(cls)+'"' if cls else '')+' href="'+esc(rel(page,path))+'">'+esc(label)+'</a>'

def external(url,label,cls=''):
    return '<a'+(' class="'+esc(cls)+'"' if cls else '')+' href="'+esc(url)+'">'+esc(label)+'</a>'

def write(path,text):
    target=OUT/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text,encoding='utf-8')

def page(path,title,body,description='',active='',script=False):
    home=rel(path,'index.html')
    nav=[('Home','index.html'),('Explore','explore.html'),('Topics','topics/index.html'),('Results','results/index.html'),('About','guides/archive-guide.html')]
    links=[]
    for label,dest in nav:
        links.append('<a href="'+esc(rel(path,dest))+'"'+(' aria-current="page"' if active==label else '')+'>'+label+'</a>')
    links.append(external(REPO,'GitHub'))
    out='''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="'''+esc(description or 'SoringP1 research archive — exact optimal comparison sorting.')+'''">
<title>'''+esc(title)+''' · SoringP1</title><link rel="stylesheet" href="'''+esc(rel(path,'assets/style.css'))+'''">
<link rel="icon" type="image/svg+xml" href="'''+esc(rel(path,'assets/favicon.svg'))+'''"></head><body>
<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="header-inner">
<a class="brand" href="'''+esc(home)+'''"><span class="brand-mark" aria-hidden="true">S(n)</span>SoringP1</a><nav aria-label="Main navigation">'''+''.join(links)+'''</nav></div></header>
<main id="main">'''+body+'''</main><footer class="site-footer">Research archive · Suspended 24 November 2026 · Revision '''+external(REPO+'/commit/'+REV,REV[:8])+''' · '''+external(REPO,'Source on GitHub')+'''</footer>'''
    if path=='index.html':out=out.replace('</head>','<link rel="stylesheet" href="assets/gazette.css"></head>')
    if script:out+='<script defer src="'+esc(rel(path,'assets/search-core.js'))+'"></script>'+'<script defer src="'+esc(rel(path,'assets/explore.js'))+'"></script>'
    write(path,out+'</body></html>\n')

def crumb(path,label,parents=()):
    return '<div class="crumb">'+link(path,'index.html','Home')+''.join(' / '+link(path,p,t) for p,t in parents)+' / '+esc(label)+'</div>'

def tile(path,target,title,summary,count=None):
    return '<a class="tile" href="'+esc(rel(path,target))+'"><h3>'+esc(title)+'</h3><p>'+esc(summary)+'</p>'+('<div class="count">'+esc(count)+'</div>' if count else '')+'</a>'

def searchform(path,value=''):
    return '<form class="searchbar" role="search" action="'+esc(rel(path,'explore.html'))+'" method="get"><input type="search" name="q" value="'+esc(value)+'" aria-label="Search research" placeholder="Search e.g. cospectral, FO(TC), defect-free"><button class="btn primary" type="submit">Search</button></form>'

fronts={f['id']:f for f in DATA['fronts']}
topics=defaultdict(list)
for f in fronts.values():topics[f['topic']].append(f)
front_pages={f['id']:'fronts/'+f['id']+'.html' for f in fronts.values()}
board_by_id={b['id']:b for b in DATA['board']}
board_pages={b['id']:'board/'+b['id'].split(':')[-1]+'.html' for b in DATA['board']}
board_by_file=defaultdict(list)
for b in DATA['board']:board_by_file[b['path']].append(b)
threads=defaultdict(list)
for b in DATA['board']:threads[b['path'].split('/')[1]].append(b)
neighbors={}
for rows in threads.values():
    rows.sort(key=lambda b:(b['date'],b['id']))
    for i,b in enumerate(rows):
        neighbors[b['id']]=(rows[i-1]['id'] if i else None,rows[i+1]['id'] if i+1<len(rows) else None)

guide_pages={}
for source,title,summary in GUIDES:
    name=Path(source).stem.lower()
    if source=='recovery/README.md':name='archive-guide'
    elif source=='recovery/followup/README.md':name='recovery-audit'
    elif source=='recovery/tools/README.md':name='offline-tools'
    elif source=='recovery/RESULTS.md':name='results'
    guide_pages[source]='guides/'+name+'.html'
for p in sorted((ROOT/'docs').glob('*.md'))+sorted((ROOT/'notes').glob('*.md')):
    source=str(p.relative_to(ROOT))
    guide_pages.setdefault(source,'guides/'+p.parent.name+'-'+p.stem+'.html')
def evidence_route(kind,p,title):
    key=hashlib.sha256((kind+'|'+p+'|'+title).encode()).hexdigest()[:20]
    return f'evidence/{kind}/{key}.html'

def file_entries():
    for row in DATA['sources']:
        yield dict(kind='source',title=row['name'],summary='; '.join(row['origins'][:3]),p=row['path'],extra=' '.join(row['origins']),origins=row['origins'])
    for row in DATA['sessions']:
        yield dict(kind='session',title=row['workspace']+' · '+row['id'],summary=f"{row['outputs']} historical assistant report outputs",p=row['path'],related=row['fronts'])
    for row in DATA['commissions']:
        yield dict(kind='commission',title=compact(row['title'],150),summary='; '.join(row['workspaces'][:3]),p=row['path'],related=row['fronts'],origins=row['workspaces'])
    for row in DATA['mixed_reports']:
        yield dict(kind='mixed',title=compact(row['title'],150),summary='; '.join(row['workspaces'][:3]),p=row['path'],related=row['fronts'],origins=row['workspaces'])
    for row in DATA['github']:
        yield dict(kind='github',title=row['kind']+' #'+row['id']+' · '+row['title'],summary=f"{row['comments']} discussion entries",p=row['path'])
    for row in DATA['commits']:
        yield dict(kind='patch',title=row['subject'] or row['id'],summary=row['id'],p=row['path'])
    for row in DATA['workspaces']:
        yield dict(kind='workspace',title=row['workspace'],summary=f"{row['files']} archived source entries · {row['head']}",p=row['manifest'],related=row['fronts'])

FILE_ENTRIES=list(file_entries())
source_pages={**guide_pages,**{'recovery/'+f['path']:front_pages[f['id']] for f in fronts.values()}}
for entry in FILE_ENTRIES:
    source_pages.setdefault('recovery/'+entry['p'],evidence_route(entry['kind'],entry['p'],entry['title']))
for file in ('scratch-provenance.json','historical-labels.json'):
    if (ARCH/'followup'/file).is_file():
        for row in json.loads((ARCH/'followup'/file).read_text()):
            source_pages['recovery/followup/'+row['markdown']]=row['page']

def evidence_link(page,source,label):
    return link(page,source_pages[source],label) if source in source_pages else external(repo_link(source),label)

anchor_cache={}
def known_anchor(source,fragment):
    if source not in source_pages:return False
    if source not in anchor_cache:
        rendered,_=markdown(read(source),lambda _:None,omit_h1=True)
        anchor_cache[source]=set(re.findall(r' id="([^"]+)"',rendered))|{'main'}
    return fragment in anchor_cache[source]


def resolver(page_path,original):
    def resolve(url):
        parts=urlsplit(url)
        if parts.scheme:return url if parts.scheme in ('https','http') else None
        if parts.netloc:return None
        if not parts.path:
            fragment=unquote(parts.fragment)
            if not fragment:return None
            if known_anchor(original,fragment):return '#'+quote(fragment,safe='-_')
            return repo_link(original,'#'+quote(fragment,safe='-_'))

        path=posixpath.normpath(posixpath.join(posixpath.dirname(original),unquote(parts.path)))
        if path.startswith('../') or path.startswith('/'):return None
        if path in source_pages and (not parts.fragment or known_anchor(path,unquote(parts.fragment))):
            return rel(page_path,source_pages[path])+('#'+quote(unquote(parts.fragment),safe='-_') if parts.fragment else '')
        match=re.match(r'L(\d+)',parts.fragment)
        if match and path.startswith('recovery/'):
            rows=board_by_file.get(path.removeprefix('recovery/'),[])
            line=int(match.group(1))
            candidates=[b for b in rows if b['line']<=line]
            if candidates:return rel(page_path,board_pages[max(candidates,key=lambda b:b['line'])['id']])
        if not (ROOT/path).exists():return None
        return repo_link(path,('#'+parts.fragment) if parts.fragment else '')
    return resolve

def source_button(source,anchor=''):
    return external(repo_link(source,anchor),'Original source on GitHub','btn')

def toc_html(toc):
    if not toc:return ''
    return '<h3>On this page</h3><ul>'+''.join('<li><a href="#'+esc(anchor)+'">'+esc(compact(label,80))+'</a></li>' for label,anchor in toc[:40])+'</ul>'

def article(path,title,original,text,side='',intro='',parents=(),anchor='',active=''):
    rendered,toc=markdown(text,resolver(path,original),omit_h1=True)
    actions='<div class="article-actions">'+external(repo_link(original,anchor),'Original source')+' · <a href="#site-related-evidence">Jump to related evidence</a></div>'
    body=crumb(path,title,parents)+'<div class="article-layout"><article class="article"><h1>'+esc(title)+'</h1>'+actions+intro+rendered+'</article><aside id="site-related-evidence" class="sidebar" aria-label="Related evidence"><h2>Source &amp; navigation</h2>'+source_button(original,anchor)+side+toc_html(toc)+'</aside></div>'
    page(path,title,body,compact(intro or title,160),active)

def item_record(path,record):
    url=record.get('url')
    if url and not url.startswith('https://'):url=rel(path,url)
    else:url=url or record['source']
    pills=[KINDS[record['kind']][0]]
    if record.get('status'):pills.append(record['status'])
    if record.get('evidence'):pills.append(CATEGORIES[record['evidence']])
    extra=''.join('<span class="pill">'+esc(p)+'</span>' for p in pills)
    if record.get('date'):extra+='<span>'+esc(record['date'][:10])+'</span>'
    if record.get('topics'):extra+='<span>'+esc(' · '.join(record['topics']))+'</span>'
    return '<div class="result"><div class="result-meta">'+extra+'</div><h3><a href="'+esc(url)+'">'+esc(record['title'])+'</a></h3><p>'+esc(record.get('summary',''))+'</p>'+external(record['source'],'Original evidence')+'</div>'

def make_home(index):
    page('index.html','The SoringP1 Gazette',
         gazette_home(index,fronts,DATA['board'],searchform),
         description='Mathematical curiosities from the SoringP1 research archive: surprising counterexamples, the mysteries of optimal sorting, logic, and computational complexity.',
         active='Home')

def make_explorer(index):
    path='explore.html'
    counts=Counter(r['kind'] for r in index.records)
    kind_options='<option value="">All collections</option>'+''.join(f'<option value="{k}">{esc(KINDS[k][0])} ({counts[k]:,})</option>' for k in KINDS if counts[k])
    evidence_options='<option value="">Any evidence type</option>'+''.join(f'<option value="{k}">{esc(v)}</option>' for k,v in CATEGORIES.items())
    topic_options='<option value="">All topics</option>'+''.join(f'<option value="{esc(t)}">{esc(t)}</option>' for t in sorted(topics))
    body=crumb(path,'Explore')+'''<span class="kicker">Research explorer</span><h1>Find a result, question or source.</h1><p class="muted">Search full indexed text, titles, original paths, and historical reports. Combine terms to narrow results.</p>
<form id="search-form" class="searchbar" role="search"><input id="query" type="search" name="q" aria-label="Search research archive" placeholder="e.g. cospectral minimax" autocomplete="off"><button class="btn primary" type="submit">Search</button></form>
<p class="muted"><small><span class="desktop-hint">Press / or Ctrl+K to focus search. </span>No tracking. Large text files are indexed up to 1 MiB.</small></p>
<div class="search-layout"><aside class="filters" aria-label="Search filters">
<button id="filter-toggle" class="btn filter-toggle" type="button" aria-expanded="true" aria-controls="filter-fields"><span>Filters</span><span id="filter-count" class="muted"></span><span aria-hidden="true">⌄</span></button>
<div id="filter-fields" class="filter-fields">
<div><label for="kind">Collection</label><select id="kind">'''+kind_options+'''</select></div>
<div><label for="topic">Topic (linked records)</label><select id="topic">'''+topic_options+'''</select></div>
<div><label for="status">Historical workflow status</label><select id="status"><option value="">Any status</option><option value="investigated">Investigated</option><option value="blocked">Blocked</option><option value="review">Board review / verdict marker</option></select></div>
<div><label for="evidence">Curated evidence type</label><select id="evidence">'''+evidence_options+'''</select></div>
<button id="clear" class="btn" type="button">Clear filters</button></div></aside>
<section class="results" aria-label="Search results"><div class="results-header"><p id="result-count" role="status" aria-live="polite">Loading index…</p><label>Sort <select id="sort"><option value="relevance">Relevance</option><option value="newest">Newest dated evidence</option><option value="title">Title A–Z</option></select></label></div>
<div id="results-list"></div><div class="pagination"><button id="prev" class="btn" type="button" disabled>Previous</button><span id="page-count"></span><button id="next" class="btn" type="button" disabled>Next</button></div></section></div>
<noscript><div class="note">Search requires JavaScript. '''+link(path,'browse/index.html','Browse all evidence without JavaScript')+' or '+link(path,'topics/index.html','browse by topic')+'.</div></noscript>'
    page(path,'Explore research',body,active='Explore',script=True)

def make_browse(index):
    path='browse/index.html';group=defaultdict(list)
    for r in index.records:group[r['kind']].append(r)
    body=crumb(path,'Evidence collections')+'<h1>Evidence collections</h1><p class="muted">Every collection is browsable without JavaScript. Use the explorer for full-text search.</p><div class="cards">'
    for kind,rows in group.items():
        body+=tile(path,'browse/'+kind+'/001.html',*KINDS[kind],f'{len(rows):,} records')
    page(path,'Evidence collections',body+'</div>',active='Explore')
    size=75
    for kind,rows in group.items():
        if kind=='board':rows=sorted(rows,key=lambda r:r.get('date',''),reverse=True)
        else:rows=sorted(rows,key=lambda r:r['title'].casefold())
        pages=(len(rows)+size-1)//size
        for i in range(pages):
            path=f'browse/{kind}/{i+1:03}.html';title=KINDS[kind][0]
            def pager():
                prev=link(path,f'browse/{kind}/{i:03}.html','Previous','btn') if i else '<span></span>'
                nxt=link(path,f'browse/{kind}/{i+2:03}.html','Next','btn') if i+1<pages else '<span></span>'
                return '<div class="pagination">'+prev+f'<span>Page {i+1} of {pages} · {len(rows):,} records</span>'+nxt+'</div>'
            body=crumb(path,title,[('browse/index.html','Collections')])+f'<h1>{esc(title)}</h1><p class="muted">{esc(KINDS[kind][1])}</p>'+pager()+''.join(item_record(path,r) for r in rows[i*size:(i+1)*size])+pager()
            page(path,title+' · '+str(i+1),body,active='Explore')

def build():
    if OUT.exists():shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(ROOT/'site/assets',OUT/'assets')
    write('.nojekyll','')
    index=SearchIndex()
    result_text=read('recovery/RESULTS.md')
    result_rows=parse_results(result_text)
    result_path='results/index.html'
    result_body=crumb(result_path,'Curated results')+'<span class="kicker">Evidence register</span><h1>What was learned</h1><p class="muted">The principal mathematical claims in the curated archive, with their evidence and limits. These categories describe the historical evidence; they are not new proof assessments.</p><div class="actions">'+link(result_path,'guides/results.html','Full results register','btn')+link(result_path,'guides/corrections.html','Corrections','btn')+link(result_path,'guides/open-questions.html','Open questions','btn')+'</div>'
    groups=defaultdict(list)
    for r in result_rows:groups[r['evidence']].append(r)
    result_body+='<div class="actions">'+''.join('<a class="pill" href="#'+k+'">'+esc(CATEGORIES[k])+' · '+str(len(groups[k]))+'</a>' for k in CATEGORIES if groups[k])+'</div>'
    for k in CATEGORIES:
        rows=groups[k]
        if not rows:continue
        result_body+='<section class="section"><h2 id="'+k+'">'+esc(CATEGORIES[k])+'</h2><div class="cards">'
        for r in rows:
            path='results/'+r['id'].lower()+'.html';source='recovery/RESULTS.md'
            detail=crumb(path,r['id'],[('results/index.html','Results')])+'<div class="article-layout"><article class="article"><div class="result-meta"><span class="pill">'+esc(r['id'])+'</span><span class="pill accent">'+esc(CATEGORIES[k])+'</span></div><h1>'+esc(r['title'])+'</h1><h2>Evidence and scope</h2><p>'+inline(r['scope'],resolver(path,source))+'</p><div class="note">This is a curated historical result entry, not a new verification. Read the original evidence and its limitations.</div><div class="actions">'+link(path,'guides/corrections.html','Corrections','btn')+link(path,'guides/open-questions.html','Open questions','btn')+'</div></article><aside class="sidebar"><h2>Source &amp; navigation</h2>'+source_button(source,'#L'+str(r['line']))+'<h3>Related topic</h3>'+link(path,'topics/'+slug(r['topic'])+'.html',r['topic'])+'</aside></div>'
            page(path,r['title'],detail,plain(r['scope']),active='Results')
            record={'kind':'result','id':r['id'],'title':r['title'],'summary':plain(r['scope']),'evidence':k,'url':path,'source':repo_link(source,'#L'+str(r['line'])),'topics':[r['topic']]}
            index.add(record,r['scope']+' '+r['id']+' '+CATEGORIES[k])
            result_body+=tile(result_path,path,r['title'],plain(r['scope']),r['id'])
        result_body+='</div></section>'
    page(result_path,'Curated results',result_body,active='Results')
    curated={p:(t,s) for p,t,s in GUIDES}
    print('Rendering guides and fronts…',flush=True)
    for source,path in guide_pages.items():
        text=read(source)
        title,summary=curated.get(source,('', ''))
        if not title:
            title=next((l[2:].strip() for l in text.splitlines() if l.startswith('# ')),Path(source).stem.replace('-',' '))
            summary=compact(' '.join(l for l in text.splitlines()[1:] if l and not l.startswith('#')),250)
        article(path,title,source,text,active='Results' if source=='recovery/RESULTS.md' else '')
        index.add({'kind':'guide','title':title,'summary':summary,'url':path,'source':repo_link(source),'topics':[]},text)
    for f in fronts.values():
        path=front_pages[f['id']];source='recovery/'+f['path'];topic=f['topic'];title=f['id']
        side='<h3>Topic</h3>'+link(path,'topics/'+slug(topic)+'.html',topic)
        side+='<h3>Original board evidence</h3>'
        ids=list(dict.fromkeys(f['board']+f.get('mentions',[])))
        if not ids:side+='<p class="muted">No direct board match in the catalogue.</p>'
        else:
            side+='<ul>'+''.join('<li>'+link(path,board_pages[mid],compact(board_by_id[mid].get('title') or board_by_id[mid]['author'],100))+'</li>' for mid in ids if mid in board_pages)+'</ul>'
        for key,name in [('sessions','Agent reports'),('workspaces','Workspace inventories'),('commissions','Task commissions'),('mixed_reports','Cross-project reports')]:
            values=f.get(key,[])
            if values:
                side+='<details><summary>'+name+f' ({len(values)})</summary><ul>'+''.join('<li>'+evidence_link(path,'recovery/'+v,Path(v).name)+'</li>' for v in values)+'</ul></details>'
        intro='<div class="result-meta"><span class="pill">'+esc(f['status'])+'</span><span>'+esc(topic)+'</span></div><section class="front-summary"><h2>Research question</h2><p>'+esc(f['question'])+'</p>'
        if f.get('reported_excerpt'):
            intro+='<h2>Reported outcome <span class="pill warm">Unverified excerpt</span></h2><p>'+esc(f['reported_excerpt'])+'</p>'
        if f.get('falsifier'):intro+='<details><summary>Intended falsifier</summary><p>'+esc(f['falsifier'])+'</p></details>'
        if f.get('implication'):intro+='<details><summary>Proposed implication</summary><p>'+esc(f['implication'])+'</p></details>'
        intro+='</section><div class="note">Historical workflow status, not a mathematical proof assessment. See the '+link(path,'guides/corrections.html','corrections')+' and original evidence.</div><h2>Full historical report</h2>'
        text=read(source)
        article(path,title,source,text,side,intro,[('topics/index.html','Topics'),('topics/'+slug(topic)+'.html',topic)])
        index.add({'kind':'front','title':title,'summary':f['question'],'url':path,'source':repo_link(source),'topics':[topic],'status':f['status'],'outcome':f.get('reported_excerpt','')},text)
    print('Rendering board messages…',flush=True)
    for source,rows in sorted(board_by_file.items()):
        lines=read('recovery/'+source,limit=16*1024*1024).splitlines()
        rows.sort(key=lambda r:r['line'])
        for i,b in enumerate(rows):
            start=b['line']-1;end=rows[i+1]['line']-1 if i+1<len(rows) else len(lines)
            text='\n'.join(lines[start:end])
            path=board_pages[b['id']];title=compact(b['title'] or b['author']+' · '+b['date'],170)
            related=[f for f in dict.fromkeys(b['fronts']+b.get('mentions',[])) if f in fronts]
            ts=sorted({fronts[f]['topic'] for f in related})
            side='<h3>Original message</h3><p>'+esc(b['id'])+'</p>'
            earlier,later=neighbors[b['id']]
            side+='<h3>Discussion chronology</h3><div class="evidence-list">'
            if earlier:side+=link(path,board_pages[earlier],'Earlier message')
            if later:side+=link(path,board_pages[later],'Later message')
            side+='</div>'
            if related:side+='<h3>Related ledger fronts</h3><ul>'+''.join('<li>'+link(path,front_pages[f],f)+'</li>' for f in related)+'</ul>'
            intro='<div class="result-meta"><span class="pill">Historical board message</span><span>'+esc(b['date'])+'</span><span>'+esc(b['author'])+'</span></div>'
            if b.get('verdict'):intro+='<div class="note"><strong>Historical verdict marker:</strong> '+esc(b['verdict'])+'<br>Not a new proof assessment.</div>'
            article(path,title,'recovery/'+source,text,side,intro,[('browse/board/001.html','Board messages')],anchor='#L'+str(b['line']))
            index.add({'kind':'board','title':title,'summary':compact(b.get('verdict') or b['title'],330),'url':path,'source':repo_link('recovery/'+source,'#L'+str(b['line'])),'topics':ts,'date':b['date'],'status':'review' if b.get('verdict') else ''},text)
    print('Indexing other evidence…',flush=True)
    def add_file(kind,title,summary,p,related=(),status='',date='',extra='',origins=()):
        source='recovery/'+p
        ts=sorted({fronts[f]['topic'] for f in related if f in fronts})
        route=evidence_route(kind,p,title)
        url=repo_link(source)
        size=(ROOT/source).stat().st_size
        body='' if p.endswith('.gz') else read(source)
        if '\x00' in body:body=''
        side=''
        if origins:
            side+='<details open><summary>Original locations ('+str(len(origins))+')</summary><ul>'+''.join('<li>'+esc(v)+'</li>' for v in origins)+'</ul></details>'
        if related:
            side+='<h3>Related ledger fronts</h3><ul>'+''.join('<li>'+link(route,front_pages[f],f)+'</li>' for f in dict.fromkeys(related) if f in fronts)+'</ul>'
        parents=[('browse/'+kind+'/001.html',KINDS[kind][0])]
        intro='<div class="result-meta"><span class="pill">'+esc(KINDS[kind][0])+'</span><span>'+f'{size:,} source bytes'+'</span></div><div class="note">Original archival evidence. Historical instructions and experimental claims are not live tasks or certified results.</div>'
        if size>1048576 and body:
            intro+='<p class="muted">Text preview is limited to the first 1 MiB; the full original is available on GitHub.</p>'
        if kind in ('session','commission','mixed','github') or (kind=='source' and p.endswith('.md')):
            article(route,title,source,body,side,intro,parents)
        else:
            main=crumb(route,title,parents)+'<div class="article-layout"><article class="article"><h1>'+esc(title)+'</h1><div class="article-actions">'+external(url,'Original source')+' · <a href="#site-related-evidence">Jump to related evidence</a></div>'+intro
            if kind=='workspace':
                manifest=json.loads((ROOT/source).read_text())
                main+='<h2>Recovered workspace</h2><p><strong>Original path:</strong> '+esc(manifest.get('source',''))+'</p><p><strong>HEAD:</strong> <code>'+esc(manifest.get('head',''))+'</code></p>'
                files=manifest.get('files',{})
                if files:
                    main+='<h2>Recovered changed and additional files ('+str(len(files))+')</h2><div class="table-wrap"><table><thead><tr><th scope="col">Original filename</th><th scope="col">Archived source</th></tr></thead><tbody>'
                    for original,obj in sorted(files.items()):
                        target='recovery/workspaces/objects/'+obj
                        main+='<tr><td><code>'+esc(original)+'</code></td><td>'+evidence_link(route,target,'Read file')+'</td></tr>'
                    main+='</tbody></table></div>'
                else:main+='<p>No changed/additional file entries in this inventory.</p>'
                main+='<details><summary>Full manifest, references and omissions</summary><pre><code>'+esc(body)+'</code></pre></details>'
            elif body:
                main+='<h2>Source text</h2><pre><code>'+esc(body)+'</code></pre>'
            else:
                main+='<h2>Original artifact</h2><p>This compressed or nontext artifact is indexed by its original filename and metadata. Open the original file on GitHub to inspect or download it.</p>'
            main+='</article><aside id="site-related-evidence" class="sidebar" aria-label="Related evidence"><h2>Source &amp; navigation</h2>'+source_button(source)+side+'</aside></div>'
            page(route,title,main,compact(summary,160))
        index.add({'kind':kind,'title':title,'summary':compact(summary,400),'url':route,'source':url,'topics':ts,'status':status,'date':date},extra+' '+body)
    for entry in FILE_ENTRIES:add_file(**entry)
    for kind,file in [('scratch','scratch-provenance.json'),('label','historical-labels.json')]:
        target=ARCH/'followup'/file
        if not target.is_file():continue
        for row in json.loads(target.read_text()):
            path=row['page'];source='recovery/followup/'+row['markdown']
            article(path,row['title'],source,read(source),parents=[('browse/'+kind+'/001.html',KINDS[kind][0])])
            index.add({'kind':kind,'title':row['title'],'summary':row['summary'],'url':path,'source':repo_link(source),'topics':row.get('topics',[])},read(source))
    print('Writing search index…',flush=True)
    index.write(OUT)
    make_home(index);make_explorer(index);make_browse(index)
    path='topics/index.html';body=crumb(path,'Topics')+'<h1>Browse research topics</h1><p class="muted">A thematic map of the 750 ledger questions. Grouping is a navigation aid, not a taxonomy of proved results.</p><div class="cards">'
    for topic,rows in sorted(topics.items()):body+=tile(path,'topics/'+slug(topic)+'.html',topic,'Browse all recorded questions and linked evidence',f'{len(rows)} fronts')
    page(path,'Research topics',body+'</div>',active='Topics')
    records={r['title']:r for r in index.records if r['kind']=='front'}
    for topic,rows in sorted(topics.items()):
        path='topics/'+slug(topic)+'.html'
        body=crumb(path,topic,[('topics/index.html','Topics')])+'<h1>'+esc(topic)+'</h1><p class="muted">'+str(len(rows))+' historical ledger fronts. The original questions and outcomes remain unverified unless explicitly documented otherwise.</p>'+link(path,'explore.html','Search and filter','btn')
        body+=''.join(item_record(path,records[f['id']]) for f in rows)
        page(path,topic,body,active='Topics')
    print('Built',sum(1 for p in OUT.rglob('*') if p.is_file()),'files',flush=True)

if __name__=='__main__':build()
