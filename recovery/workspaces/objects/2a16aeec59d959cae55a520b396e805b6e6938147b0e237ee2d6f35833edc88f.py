#!/usr/bin/env python3
"""Observational institutional feedback; no authority to govern or enact."""
import collections
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

TOWN=Path(os.getenv('VICHE_TOWN_ROOT','/var/lib/lubko/wd/viche'))
STATE=Path(os.getenv('VICHE_STATE_ROOT','/var/lib/lubko/wd/viche-state'))
CLI=os.getenv('VICHE_METRICS_ANTONINA','antonina')
NOW=int(os.getenv('VICHE_METRICS_NOW',time.time()))
WINDOW=86400

def shell(args, timeout=35):
    p=subprocess.run([str(x) for x in args],capture_output=True,text=True,timeout=timeout)
    if p.returncode:raise RuntimeError(p.stderr[-180:] or 'nonzero exit')
    return p.stdout

def js(path):
    try:return json.loads(Path(path).read_text())
    except (ValueError,OSError):return None

def agents():
    rows=[]
    for page in range(1,9):
        d=json.loads(shell([CLI,'agent','list','--finished','--page',page,
                            '--limit',500,'--json'],65))
        if d.get('unreadable'):raise ValueError('incomplete agent inventory')
        a=d['agents']
        rows.extend(a)
        if len(a)<500:break
        if a and all(float(x.get('finished_at') or 0)<NOW-WINDOW for x in a):break
    else:raise RuntimeError('inventory exceeds bounded observation window')
    recent=[x for x in rows if isinstance(x.get('finished_at'),(float,int))
            and NOW-WINDOW<=x['finished_at']<=NOW+5]
    projects=collections.Counter()
    outcomes=collections.Counter()
    for x in recent:
        title=x.get('title','')
        projects['Viche' if title.startswith('Viche') else
                 'SoringP1' if title.startswith('SoringP1') else 'other']+=1
        outcomes[x.get('state','unknown')]+=1
    return dict(window_seconds=WINDOW,total=len(recent),by_project=dict(projects),
                by_process_outcome=dict(outcomes),
                caveat='process success does NOT prove work delivery or verification')

def git_delivery():
    lines=shell(['git','-C',TOWN,'log','--first-parent',
                 '--since='+str(NOW-WINDOW),'--format=%ct%x09%H%x09%s'])
    recent=[]
    for line in lines.splitlines():
        fields=line.split('\t',2)
        if len(fields)==3 and fields[0].isdigit() and int(fields[0])<=NOW:
            recent.append(fields)
    return dict(main_head=shell(['git','-C',TOWN,'rev-parse','HEAD']).strip(),
                main_commits=len(recent),
                main_merge_commits=sum('Merge pull request' in x[2] for x in recent),
                most_recent=recent[0] if recent else None,
                caveat='merged history is not proof of independently verified impact')

def branches():
    result={}
    for b in ('legislature','executive','judiciary'):
        x=js(STATE/'branches'/f'{b}.json')
        result[b]=dict(telemetry='available' if isinstance(x,dict) else 'missing',
                       readiness=x.get('readiness') if isinstance(x,dict) else None,
                       age_seconds=max(0,NOW-int(x['observed_at']))
                       if isinstance(x,dict) and isinstance(x.get('observed_at'),(float,int))
                       else None)
    laws=(TOWN/'government/LAWS.md').read_text() if (TOWN/'government/LAWS.md').exists() else ''
    import re
    moved=bool(re.search(r'^## Act \d+ — Executive Innovation Office Act \(enacted ',laws,re.M))
    path=('executive/innovation-office/health.json' if moved else 'legislature/innovation-centre/health.json')
    ic=js(STATE/path)
    result['innovation_centre']=dict(telemetry='available' if isinstance(ic,dict) else 'missing',
                                    readiness=ic.get('readiness') if isinstance(ic,dict) else None,
                                    age_seconds=max(0,NOW-int(ic['observed_at']))
                                    if isinstance(ic,dict) and isinstance(ic.get('observed_at'),(float,int))
                                    else None)
    return result

def research():
    frontier=js(os.getenv('VICHE_SORING_FRONTIER',
             '/home/lubko/.local/state/soringp1/frontier-ledger.json'))
    if not isinstance(frontier,dict):return {'telemetry':'unavailable'}
    return dict(telemetry='available',
                states=dict(collections.Counter(x.get('status','unknown')
                                  for x in frontier.get('fronts',[]))),
                curator_running=bool(frontier.get('curator',{}).get('agent_id')),
                caveat='curator proposals are not verified research results')

def board():
    entries=json.loads(shell([CLI,'board','list','--state','open',
                              '--page','1','--json'],45))
    if not isinstance(entries,list):raise ValueError('invalid board inventory')
    return dict(open_first_page=len(entries),
                open_by_project=dict(collections.Counter(
                    'Viche' if x.get('title','').startswith('Viche')
                    else 'SoringP1' if x.get('title','').startswith('SoringP1')
                    else 'other' for x in entries)),
                caveat='first page only; do not infer issues missing on this page were closed')

def measure():
    result={'observed_at':NOW,'role':'descriptive evidence for independent branch review',
            'delivery_verified_by_this_probe':False,
            'no_prescriptive_quota':True}
    for key,fn in [('agents',agents),('git',git_delivery),
                   ('branches',branches),('research',research),('board',board)]:
        try:result[key]=fn()
        except (ValueError,RuntimeError,KeyError,TypeError,subprocess.TimeoutExpired) as e:
            result[key]={'telemetry':'unavailable','error':str(e)[-180:]}
    alerts=[]
    if any(v['telemetry']!='available' or v['readiness']=='unhealthy'
           for v in result.get('branches',{}).values()):
        alerts.append('branch_readiness_review')
    r=result.get('research',{})
    if r.get('telemetry')=='available' and not (r['states'].get('ready',0)
         or r['states'].get('running',0) or r['states'].get('launching',0)
         or r['curator_running']):
        alerts.append('research_frontier_not_being_replenished')
    if any(result[k].get('telemetry')=='unavailable' for k in ('agents','git','board')):
        alerts.append('outcome_measurement_incomplete')
    result['signals_for_inquiry_not_verdicts']=alerts
    return result

def atomic(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix='.outcomes-',dir=path.parent)
    try:
        with os.fdopen(fd,'w') as f:
            f.write(data);f.flush();os.fsync(f.fileno())
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)

def main():
    obj=measure()
    root=STATE/'institutional-outcomes'
    atomic(root/'latest.json',json.dumps(obj,indent=2,sort_keys=True)+'\n')
    marker=js(root/'last-history-minute.json')
    if not isinstance(marker,dict) or marker.get('minute')!=NOW//60:
        with (root/'history.jsonl').open('a') as f:
            f.write(json.dumps(obj,sort_keys=True)+'\n')
        atomic(root/'last-history-minute.json',json.dumps({'minute':NOW//60})+'\n')
    print('Viche outcome evidence:',json.dumps({
        'agent_exits':obj['agents'].get('total'),
        'main_commits':obj['git'].get('main_commits'),
        'signals':obj['signals_for_inquiry_not_verdicts']}))
if __name__=='__main__':main()
