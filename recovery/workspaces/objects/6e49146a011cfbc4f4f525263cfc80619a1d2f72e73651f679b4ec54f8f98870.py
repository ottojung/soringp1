#!/usr/bin/env python3
"""Evidence to Legislature; no judicial policy proposals or modifications.

Act 18 §5 (Board Reporting Act) mandates that the independent Judiciary add
board-trail completeness to its observability/audit lens and report it each
measurement window. The deterministic board/Git cross-check is scripted in
POSIX /bin/sh (government/board-trail-check.sh); this file aggregates its facts
into the durable measurement report. The same-model / measurement-reliability
limitation is reported, not hidden.
"""
import hashlib, json, os, shutil, subprocess, time
from pathlib import Path

root=Path(os.environ.get('VICHE_STATE_ROOT','/var/lib/lubko/wd/viche-state'))
town=Path(os.environ.get('VICHE_TOWN_ROOT','/var/lib/lubko/wd/viche'))
now=int(os.environ.get('VICHE_BRANCH_NOW',time.time()))
a=root/'oversight/random'
cases=list((a/'cases').glob('*.json')) if (a/'cases').exists() else []
counts={'sampled':len(cases),'reported':0,'unreported':0,'finding':0,'unreadable':0}
for p in cases:
    try:
        x=json.loads((a/'outcomes'/p.name).read_text())
        counts['reported']+=1
        counts['finding']+=int(x.get('verdict')=='finding')
    except FileNotFoundError:
        counts['unreported']+=1
    except (ValueError,TypeError):
        counts['unreadable']+=1


def board_trail():
    """Act 18 §5 board-trail completeness lens (facts only; no proposals)."""
    cycle=int(os.environ.get('VICHE_BOARD_TRAIL_CYCLE','86400'))
    script=town/'government/board-trail-check.sh'
    mapping=town/'records/board-trail/originating.tsv'
    index=town/'records/board-trail/index.json'
    out={'authority':'Act 18 §5','criteria':'records/PREREGISTERED-CRITERIA-2026-10-19.md (W2)',
         'status':'not_measured','executive_index_present':index.exists(),
         'measurement_reliability':'not_established',
         'caveat':'same-model procedural check; classification is a deterministic heuristic, not proof'}
    if os.environ.get('VICHE_BOARD_TRAIL_CHECKS','1')=='0':
        out['reason']='disabled by VICHE_BOARD_TRAIL_CHECKS=0'; return out
    if not script.exists():
        out['reason']='cross-check script absent'; return out
    if not mapping.exists():
        out['reason']='no Git cross-check mapping (records/board-trail/originating.tsv)'; return out
    if shutil.which('antonina') is None:
        out['reason']='antonina CLI unavailable'; return out
    try:
        done=subprocess.run(['/bin/sh',str(script)],capture_output=True,text=True,timeout=30)
    except (subprocess.TimeoutExpired,OSError) as err:
        out['reason']='cross-check unavailable: '+str(err)[:160]; return out
    if done.returncode!=0:
        out['reason']='cross-check failed: '+done.stderr.strip()[-160:]; return out
    rows=[]
    for line in done.stdout.splitlines():
        line=line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            continue
    completed=[r for r in rows if int(r.get('enacted_epoch',0))>0 and r.get('type') in ('law','task')]
    # Act 18 §2/§7: a failed board call is unreadable, never evidence of a gap.
    # Exclude unreadable issues from the gap/rate computation and report them
    # separately, so a transient board error cannot fabricate a Git-only gap.
    unreadable=[r for r in completed if r.get('board_readable') is False]
    readable=[r for r in completed if r.get('board_readable') is not False]
    terminal=[r for r in readable if r.get('terminal')==1]
    gaps=[r for r in readable if int(r.get('post_completion') or 0)==0]
    no_stage=[r for r in readable if not r.get('stage_markers')]
    dangling=[r for r in readable if r.get('terminal')!=1 and now-int(r['enacted_epoch'])>cycle]
    ages=[now-int(r['enacted_epoch']) for r in readable if r.get('terminal')!=1]
    out.update({
        'status':'measured',
        'originating_total':len(rows),
        'completed_total':len(completed),
        'readable_total':len(readable),
        'terminal_reached':len(terminal),
        'fraction_terminal':(round(len(terminal)/len(readable),4) if readable else None),
        'git_only_gaps':[{'issue':r['issue'],'work':r['work'],'act':r.get('act')} for r in gaps],
        'board_unreadable':[{'issue':r['issue'],'work':r['work']} for r in unreadable],
        'stage_marker_missing':[{'issue':r['issue'],'work':r['work']} for r in no_stage],
        'dangling_trails':len(dangling),
        'oldest_gap_age_seconds':(max(ages) if ages else 0),
        'content_standard_failures':sum(int(r.get('chatter') or 0) for r in rows),
        'cycle_seconds':cycle,
        'per_issue':rows,
    })
    return out


try:
    institutional_outcomes=json.loads(
        (root/'institutional-outcomes/latest.json').read_text())
except (OSError,ValueError,TypeError):
    institutional_outcomes={'telemetry':'unavailable','not_a_clean_result':True}

def suite_compliance():
    script=town/'government/suite-compliance-check.sh'
    if not script.exists():
        return {'status':'unreadable','reason':'suite compliance check absent'}
    try:
        done=subprocess.run(['/bin/sh',str(script),str(town)],capture_output=True,text=True,timeout=60)
        data=json.loads(done.stdout)
        if done.returncode:
            return {'status':'unreadable','reason':done.stderr.strip()[-200:]}
        # The full per-change audit can be large. Preserve it as a durable,
        # separately addressable detail record; keep this prompt-facing summary
        # bounded so the Clerk's next boot dispatch remains within argv limits.
        per_change=data.pop('per_change',None)
        if per_change is not None:
            red_changes=data.pop('changes_reaching_main_red',[])
            red_unknown=data.pop('red_chronology_unresolved_changes',[])
            detail=root/'branches'/('suite-compliance-%d.json' % now)
            full={'observed_at':now,'summary':data,
                  'changes_reaching_main_red':red_changes,
                  'red_chronology_unresolved_changes':red_unknown,
                  'per_change':per_change}
            blob=(json.dumps(full,
                             sort_keys=True,indent=2)+'\n').encode()
            detail.parent.mkdir(parents=True,exist_ok=True)
            tmp=detail.with_suffix('.json.tmp')
            tmp.write_bytes(blob)
            tmp.replace(detail)
            data['per_change_count']=len(per_change)
            data['red_change_count']=len(red_changes)
            data['red_chronology_unresolved_count']=len(red_unknown)
            data['details_ref']=str(detail)
            data['details_sha256']=hashlib.sha256(blob).hexdigest()
        return data
    except (subprocess.TimeoutExpired,OSError,ValueError) as err:
        return {'status':'unreadable','reason':str(err)[:200]}


payload={'observed_at':now,'destination':'Legislature', 'kind':'Judiciary measurement, not legislation', 'counts':counts, 'false_positive_rate':None,'false_negative_rate':None,'measurement_reliability':'not_established','judiciary_independence':'non-voting independent measurement office (Act 15, enacted 2026-10-17)', 'no_proposals':True, 'institutional_outcomes':institutional_outcomes, 'board_trail':board_trail(), 'suite_compliance':suite_compliance()}
p=root/'branches/judiciary-measurements.json'
p.parent.mkdir(parents=True,exist_ok=True)
tmp=p.with_suffix('.json.tmp')
tmp.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
tmp.replace(p)
print('Judiciary measurement report:',counts)
