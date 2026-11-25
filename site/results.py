"""A curated, evidence-graded view of the existing Markdown result register.

The categories describe the evidence recorded in RESULTS.md. They are not
new formal verification or a promotion of historical reports to theorems.
"""
import re
from render import cells

CATEGORIES={
 'formal':'Lean kernel theorem',
 'literature':'Literature baseline',
 'argument':'Paper / algorithm argument',
 'structural':'Historical structural deduction',
 'finite':'Finite computational evidence',
 'conditional':'Conditional argument',
 'corrected':'Corrected proof scope',
}
FINITE={'P01','P03','P04','P05','D04','D05','D07','D09','C03'}
TOPICS={
 'K':'Logic, complexity and encodings',
 'A':'Space, search and exact algorithms',
 'B':'Logic, complexity and encodings',
 'C':'Certificates and strategy representations',
 'P':'Profiles, decks and lookahead',
 'D':'Information, balance, entropy and defect',
 'E':'Information, balance, entropy and defect',
 'S':'Poset decomposition, symmetry and quotient',
 'L':'Sorting schedules and asymptotic arithmetic',
}

def evidence(ident):
    if ident.startswith('K'):return 'formal'
    if ident.startswith('L'):return 'literature'
    if ident=='C05':return 'conditional'
    if ident=='D03':return 'corrected'
    if ident in FINITE:return 'finite'
    if ident in {'P02','D01','D02','D06','D08','D10','C04','E01','E02'}:return 'structural'
    return 'argument'

def plain(text):
    return re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',text).replace('**','').replace('`','')

def parse(text):
    rows=[]
    section=''
    for i,line in enumerate(text.splitlines(),1):
        if line.startswith('## '):section=line[3:]
        if not re.match(r'^\| [A-Z]\d\d \|',line):continue
        ident,title,scope=cells(line)
        rows.append({'id':ident,'title':plain(title),'scope':scope,'evidence':evidence(ident),'topic':TOPICS[ident[0]],'line':i,'section':section})
    if len({r['id'] for r in rows})!=len(rows):raise ValueError('duplicate result ID')
    return rows
