#!/usr/bin/env python3
"""Check the generated static site, including every link and index shard."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import posixpath
import re
import sys

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/_site'

class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]
        self.ids=set()
        self.duplicates=[]
        self.h1=0
        self.scripts=[]
        self.unsafe=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            ident=attrs['id']
            if ident in self.ids:self.duplicates.append(ident)
            self.ids.add(ident)
        if tag=='h1':self.h1+=1
        for key in ('href','src','action'):
            if attrs.get(key):self.links.append((tag,attrs[key]))
        if tag=='script':self.scripts.append(attrs.get('src'))
        if any(key.startswith('on') for key in attrs):self.unsafe.append(tag)
        if tag in ('iframe','object','embed'):self.unsafe.append(tag)

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def main():
    errors=[];docs={};count=0;externals=0;anchors=0
    files={str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file()}
    for path in sorted(OUT.rglob('*.html')):
        rel=str(path.relative_to(OUT));d=Document()
        d.feed(path.read_text(encoding='utf-8'))
        docs[rel]=d
        if d.h1!=1:errors.append(rel+f': expected one h1, found {d.h1}')
        if 'main' not in d.ids:errors.append(rel+': missing main landmark')
        if d.duplicates:errors.append(rel+': duplicate ids '+str(d.duplicates))
        if d.unsafe:errors.append(rel+': unsafe HTML '+str(d.unsafe))
        if any(not s or s.startswith(('http:','https:','//')) for s in d.scripts):
            errors.append(rel+': nonlocal or inline script')
    for rel,d in docs.items():
        for tag,url in d.links:
            parts=urlsplit(url)
            if parts.scheme in ('https','http'):
                externals+=1
                continue
            if parts.scheme or parts.netloc:
                errors.append(rel+': unsafe URL '+url)
                continue
            target=posixpath.normpath(posixpath.join(posixpath.dirname(rel),unquote(parts.path))) if parts.path else rel
            if target.startswith(('../','/')) or target=='..':
                errors.append(rel+': external filesystem path '+url);continue
            if target not in files and target+'/index.html' in files:target+='/index.html'
            count+=1
            if target not in files:errors.append(rel+': broken link '+url);continue
            if parts.fragment and target in docs:
                anchors+=1
                if unquote(parts.fragment) not in docs[target].ids:
                    errors.append(rel+': missing anchor '+url)
    records=load(OUT/'search/records.json')
    manifest=load(OUT/'search/manifest.json')
    expected=load(ROOT/'recovery/catalog/index.json')
    kinds=Counter(r['kind'] for r in records)
    for kind,name in [('front','fronts'),('board','board'),('source','sources'),('session','sessions'),('commission','commissions'),('mixed','mixed_reports'),('github','github'),('patch','commits'),('workspace','workspaces')]:
        if kinds[kind]!=len(expected[name]):errors.append(f'{kind} coverage: {kinds[kind]} != {len(expected[name])}')
    for kind,name in [('scratch','scratch-provenance.json'),('label','historical-labels.json')]:
        p=ROOT/'recovery/followup'/name
        if p.is_file() and kinds[kind]!=len(load(p)):errors.append(f'{kind} coverage mismatch')
    expected_results=sum(bool(re.match(r'^\| [A-Z]\d\d \|',line)) for line in (ROOT/'recovery/RESULTS.md').read_text().splitlines())
    if kinds['result']!=expected_results:errors.append('curated result coverage mismatch')
    if manifest['records']!=len(records):errors.append('record count mismatch')
    for i,r in enumerate(records):
        if not r.get('title'):errors.append(f'empty title at record {i}')
        if not r.get('source','').startswith('https://github.com/ottojung/soringp1/blob/'):errors.append(f'invalid source at record {i}')
        url=r.get('url','')
        if not url.startswith('https://') and url not in docs:errors.append(f'invalid route at record {i}: {url}')
    terms=0;posting_count=0
    for name in manifest['shards']:
        p=OUT/'search'/f'{name}.json'
        if not p.is_file():errors.append('missing shard '+name);continue
        for token,ids in load(p).items():
            terms+=1;posting_count+=len(ids)
            if token[:2]!=name or not re.fullmatch(r'[a-z0-9]{1,48}',token):
                errors.append('wrong shard for '+token)
            if not ids or ids[0]<0 or ids[-1]>=len(records) or any(a>=b for a,b in zip(ids,ids[1:])):
                errors.append('invalid postings for '+token)
    if terms!=manifest['terms']:errors.append('term count mismatch')
    print(f'Website: {len(docs):,} HTML pages; {count:,} local links, {anchors:,} anchors; {externals:,} external links.')
    print(f'Search: {len(records):,} records; {terms:,} terms; {posting_count:,} postings; {len(manifest["shards"]):,} shards.')
    print('Coverage:',dict(kinds))
    print(f'Errors: {len(errors)}')
    for e in errors[:80]:print(e,file=sys.stderr)
    return bool(errors)

if __name__=='__main__':sys.exit(main())
