"""Compact deterministic full-text search index for the static explorer."""
from array import array
from collections import defaultdict
import json
import re

TOKEN = re.compile(r'[a-z0-9]+')
STOP = frozenset('the and for from that this with are was were have has had but not can could would should will shall into also only there their they our you your its his her she him them then than when where which what who how why each any all been being some these those of to in on is as at by an or it be if'.split())
SINGLE = frozenset('s n f p e g l d k t r m a b c h'.split())

def tokens(text):
    return [t for t in TOKEN.findall(text.lower()) if t not in STOP and (len(t)>1 or t in SINGLE) and len(t)<=48 and not (t.isdigit() and len(t)>8)]

def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')

class SearchIndex:
    def __init__(self):
        self.records=[]
        self.postings=defaultdict(lambda:array('I'))

    def add(self,record,body=''):
        ident=len(self.records)
        self.records.append(record)
        text=' '.join([record.get('title',''),record.get('summary',''),record.get('source',''),record.get('date',''),record.get('status',''),' '.join(record.get('topics',[])),body])
        for token in set(tokens(text)):
            self.postings[token].append(ident)
        return ident

    def write(self,out):
        shards=defaultdict(dict)
        for token in sorted(self.postings):
            shards[token[:2]][token]=list(self.postings[token])
        for name,data in shards.items():
            write_json(out/'search'/f'{name}.json',data)
        write_json(out/'search'/'records.json',self.records)
        write_json(out/'search'/'manifest.json',{'records':len(self.records),'terms':len(self.postings),'shards':sorted(shards),'stop':sorted(STOP),'single':sorted(SINGLE),'max_body_bytes':1048576})
        print('Search records:',len(self.records),'terms:',len(self.postings),'shards:',len(shards),flush=True)
