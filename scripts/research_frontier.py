#!/usr/bin/env python3
"""Durable claim-once research fronts; independent curator replenishes on depletion."""
import fcntl, json, os, re, subprocess, tempfile, time
from pathlib import Path
HOME=Path('/home/lubko')
REPO=HOME/'soring301'
SOURCE=Path(os.getenv('SORING_FRONTIER_SOURCE',str(REPO/'docs/research-frontier.json')))
STATE=Path(os.getenv('SORING_FRONTIER_STATE',str(HOME/'.local/state/soringp1/frontier-ledger.json')))
WORK=Path(os.getenv('SORING_FRONTIER_WORK',str(HOME/'soring-fronts')))
CLI=str(HOME/'.local/bin/antonina')
BASE=('On billy-dev ONLY, study AGENTS.md, docs/problem.md and current board #301. '
      'Study the primary literature, attack a precise all-n falsifiable mathematical '
      'claim about complexity of EXACT unary S(n), and try seriously to DISPROVE it. '
      'Distinguish general-poset results and certificate SOUNDNESS from completeness. '
      'Do not create Lean or repository changes without a genuinely substantive, '
      'independently checkable new theorem or counterexample. Report honest limits. ')
def call(args,timeout=50):
    return subprocess.run(list(map(str,args)),capture_output=True,text=True,timeout=timeout)
def save(d):
    STATE.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(dir=STATE.parent,prefix='.frontier-')
    try:
        with os.fdopen(fd,'w') as f:
            json.dump(d,f,indent=2,sort_keys=True)
            f.write('\n');f.flush();os.fsync(f.fileno())
        os.replace(tmp,STATE)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)
def valid(x):
    return isinstance(x,dict) and bool(re.fullmatch('[a-z][a-z0-9-]{5,62}',str(x.get('id','')))) and all(
        isinstance(x.get(k),str) and len(x[k])>=n for k,n in
        [('question',75),('falsifier',40),('implication',40),('basis',35)])
def load():
    if STATE.exists():
        d=json.loads(STATE.read_text())
    else:
        x=json.loads(SOURCE.read_text())
        assert x['version']==1 and all(valid(y) for y in x['fronts'])
        d={'version':1,'fronts':[dict(y,status='ready',origin='reviewed_seed') for y in x['fronts']],
           'curator':{}}
        save(d)
    assert d['version']==1 and all(valid(x) for x in d['fronts'])
    ids=[x['id'] for x in d['fronts']]
    assert len(ids)==len(set(ids))
    return d
def live():
    p=call([CLI,'agent','list','--running','--page',1,'--limit',500,'--json'])
    if p.returncode:raise RuntimeError(p.stderr[-300:])
    obj=json.loads(p.stdout)
    if obj.get('unreadable'):raise RuntimeError('incomplete inventory')
    return {x['id'] for x in obj['agents']}
def status(aid):
    p=call([CLI,'agent','status','--id',aid,'--json'])
    return json.loads(p.stdout).get('state') if p.returncode==0 else 'unavailable'
def excerpt(aid):
    p=HOME/'.local/state/antonina/agents'/aid/'output.log'
    if not p.exists():return 'No readable output; no verified result'
    pieces=[]
    for line in p.open(errors='replace'):
        try:x=json.loads(line)
        except ValueError:continue
        part=x.get('part')
        if x.get('type')=='text' and isinstance(part,dict) and isinstance(part.get('text'),str):
            pieces.append(part['text'])
            if len(pieces)>8:pieces.pop(0)
    return '\n'.join(pieces)[-3500:] or 'No final text; audit needed'
def workspace(slug):
    p=WORK/slug
    if p.exists():
        if not (p/'.git').exists():raise RuntimeError('unowned path '+str(p))
    else:
        WORK.mkdir(parents=True,exist_ok=True)
        r=call(['git','clone','--local','--shared','--quiet',REPO,p],90)
        if r.returncode:raise RuntimeError(r.stderr[-250:])
        call(['git','-C',p,'remote','set-url','origin','git@github.com:ottojung/soringp1.git'])
    return p
def new(path,title):
    r=call([CLI,'agent','new','--cwd',path,'--title',title,'--json'])
    if r.returncode:raise RuntimeError(r.stderr[-250:])
    x=json.loads(r.stdout)
    aid=x.get('id') or x.get('agent_id')
    if not aid:raise RuntimeError('missing agent id')
    return aid
def run(aid,path,prompt):
    r=call([CLI,'agent','run','--id',aid,'--cwd',path,'--prompt',prompt,'--detach','--json'],65)
    if r.returncode:raise RuntimeError(r.stderr[-300:])
def reconcile(d,active):
    for q in d['fronts']:
        if q['status'] not in ('running','launching') or q.get('agent_id') in active:continue
        s=status(q['agent_id']) if q.get('agent_id') else 'unavailable'
        if s=='idle' and q['status']=='launching':
            q['status']='ready'  # interrupted launch, reuse the reserved agent id
            continue
        if s not in ('succeeded','failed','stopped','killed'):continue
        q.update(status='investigated' if s=='succeeded' else 'blocked',
                 exit_state=s,finished_at=time.time(),finding_unverified=excerpt(q['agent_id']))
        print('research result',q['id'],s,flush=True)
def curate_done(d,active):
    c=d.get('curator',{})
    if not c.get('agent_id') or c['agent_id'] in active:return
    s=status(c['agent_id'])
    if s not in ('succeeded','failed','stopped','killed'):return
    path=WORK/'curator'/'frontier-candidates.json'
    try:
        proposals=json.loads(path.read_text()).get('fronts',[]) if s=='succeeded' else []
    except (OSError,ValueError):proposals=[]
    known={q['id'] for q in d['fronts']}
    questions={re.sub(r'\W+','',q['question'].lower()) for q in d['fronts']}
    added=0
    for q in proposals if isinstance(proposals,list) else []:
        if not valid(q) or q['id'] in known:continue
        fingerprint=re.sub(r'\W+','',q['question'].lower())
        if fingerprint in questions:continue
        d['fronts'].append(dict({k:q[k] for k in ('id','question','falsifier','implication','basis')},
                                status='ready',origin='ai_proposal_unverified'))
        known.add(q['id']);questions.add(fingerprint);added+=1
    d['curator']={'last_finished_at':time.time(),'added':added,'exit_state':s}
    print('curator',s,'new fronts',added,flush=True)
def dispatch(d,q):
    path=workspace(q['id'])
    if not q.get('agent_id'):
        q['agent_id']=new(path,'SoringP1 frontier: '+q['id'])
        q['status']='launching'
        save(d)
    prompt=(BASE+'\nFRONT: '+q['question']+'\nFALSIFIER: '+q['falsifier']+
            '\nCOMPLEXITY IMPLICATION: '+q['implication']+'\nEVIDENCE: '+q['basis']+
            '\nOn completion report a mathematical finding, concrete failed '
            'approach or exact obstruction; do not confuse process success with a proof.')
    run(q['agent_id'],path,prompt)
    q.update(status='running',started_at=time.time())
    save(d)
    print('dispatched',q['id'],q['agent_id'],flush=True)
def curate(d):
    path=workspace('curator')
    output=path/'frontier-candidates.json'
    if output.exists():output.unlink()
    aid=new(path,'SoringP1 autonomous research-frontier curator')
    d['curator']={'agent_id':aid,'started_at':time.time()}
    save(d)
    old=[{'id':q['id'],'status':q['status'],'finding':q.get('finding_unverified','')[-600:]}
         for q in d['fronts'][-20:]]
    prompt=(BASE+'\nCURATOR ROLE: propose genuinely NEW independent all-n falsifiable '
            'research questions grounded in newest board #301, repository docs and '
            'independently checked mathematical evidence. Refuse duplicate investigations. '
            'If no defensible new direction is available, output an empty list. '
            'Write ONLY a JSON object with fronts array to '+str(output)+'. '
            'Each front has id (6..63 character lowercase slug), question (>=75 chars), '
            'falsifier (>=40 chars), implication (>=40 chars), basis (>=35 chars). '
            'Never claim proof or verification. PREVIOUS: '+json.dumps(old)[-15000:])
    run(aid,path,prompt)
    print('curation started',aid,flush=True)
def tick(d,dry=False):
    active=live()
    reconcile(d,active)
    curate_done(d,active)
    ready=[q for q in d['fronts'] if q['status']=='ready']
    if dry:
        print('dry-run ready',len(ready),'active',len(active));return
    for q in ready:
        try:dispatch(d,q)
        except Exception as exc:
            q['launch_error']=str(exc)[-300:]
            print('launch failed',q['id'],q['launch_error'],flush=True)
    save(d)
    useful=any(q['status'] in ('ready','running','launching') for q in d['fronts'])
    c=d.get('curator',{})
    if not useful and not c.get('agent_id') and time.time()-c.get('last_finished_at',0)>=1800:
        try:curate(d)
        except Exception as exc:print('curation failed',str(exc)[-300:],flush=True)
    print('frontier ready',sum(q['status']=='ready' for q in d['fronts']),
          'active',sum(q['status'] in ('running','launching') for q in d['fronts']),
          'curator_running',bool(d.get('curator',{}).get('agent_id')),flush=True)
def main():
    import argparse
    a=argparse.ArgumentParser()
    a.add_argument('--once',action='store_true')
    a.add_argument('--dry-run',action='store_true')
    args=a.parse_args()
    if os.uname().nodename!='billy-dev' and not args.dry_run:raise SystemExit('billy-dev only')
    STATE.parent.mkdir(parents=True,exist_ok=True)
    with (STATE.parent/'frontier.lock').open('w') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        while True:
            try:tick(load(),args.dry_run)
            except Exception as exc:
                print('frontier error',repr(exc),flush=True)
                if args.once:raise
            if args.once or args.dry_run:break
            time.sleep(30)
if __name__=='__main__':main()
