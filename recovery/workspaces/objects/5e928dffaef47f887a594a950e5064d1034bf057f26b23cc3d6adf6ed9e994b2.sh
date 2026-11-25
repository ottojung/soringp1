#!/bin/sh
# Act 21 §5: audit the exact resulting commit/tree using committed suite-status
# history and the pre-push receipt plus post-push publication event. The event is
# hash-bound to the receipt and must have a later high-resolution timestamp; a
# receipt alone is never chronology evidence. A suite-status record committed
# by the same change is not pre-change evidence. Usage: suite-compliance-check.sh [repo]
set -eu
repo=${1:-${VICHE_TOWN_ROOT:-/var/lib/lubko/wd/viche}}
state=${VICHE_STATE_ROOT:-/var/lib/lubko/wd/viche-state}
python3 - "$repo" "$state" <<'PY'
import datetime, glob, hashlib, json, os, re, subprocess, sys
repo,state=sys.argv[1:]
def git(*args):
    return subprocess.check_output(['git','-C',repo,*args], text=True).strip()
def recorded_result(data, expected_suite):
    """Accept only generated records with a run matching the reported result."""
    if (data.get('generated_by')!='government/suite-status.sh'
            or data.get('suite')!=expected_suite):
        return None
    runs=data.get('runs')
    if not isinstance(runs,list):
        return None
    def valid_run(run, number):
        return (isinstance(run,dict) and type(run.get('run')) is int
                and run.get('run')==number and type(run.get('exit')) is int
                and run.get('result') in ('green','red')
                and re.fullmatch(r'[0-9a-f]{64}',str(run.get('output_sha256',''))) is not None)
    if any(not valid_run(run,i+1) for i,run in enumerate(runs)):
        return None
    if data.get('result')=='green':
        if (len(runs)==1 and runs[0].get('result')=='green'
                and runs[0].get('exit')==0):
            return 'green'
        if (len(runs)==2 and runs[0].get('result')=='red'
                and runs[0].get('exit')!=0 and runs[1].get('result')=='green'
                and runs[1].get('exit')==0):
            return 'green'
    if (data.get('result')=='red' and len(runs)==2
            and all(run.get('result')=='red' and run.get('exit')!=0
                    for run in runs)):
        return 'red'
    return None
def timestamp(value):
    if not isinstance(value,str):
        return None
    try:
        d=datetime.datetime.fromisoformat(value.replace('Z','+00:00'))
        return d.timestamp() if d.tzinfo else None
    except ValueError:
        return None
def valid_act26_record(path, data):
    """Check complete prelanding evidence; neither an agent exit nor a pin
    alone proves the claimed run. Require an immutable Git copy on main."""
    if not isinstance(data,dict) or data.get('schema')!='act26-prelanding-record/v1':
        return None
    mandatory=('commit','tree','parent','reviewer','independence_basis',
               'phase','bill_id','landing_authorisation','main_at_verification')
    if any(not isinstance(data.get(k),str) or not data[k].strip() for k in mandatory):
        return None
    if data.get('verdict')!='pass' or data.get('status') in ('parent_mismatch','fail','failed'):
        return None
    if data.get('main_at_verification') != data['parent']:
        return None
    commands=data.get('commands')
    if (not isinstance(commands,list) or not commands
            or any(not isinstance(c,dict) or not isinstance(c.get('command'),str)
                   or not c['command'].strip() or
                   (c.get('exit') is not None and type(c['exit']) is not int)
                   for c in commands)):
        return None
    # An interrupted/unknown run may be preserved as exit=null, but it is
    # NEVER a green result. A real matching full or records suite must pass.
    if not any(c.get('exit')==0 and any(
            suite in c['command'] for suite in
            ('tests/run-all.sh','tests/records-smoke.sh')) for c in commands):
        return None
    assertions=data.get('content_assertions')
    if (not isinstance(assertions,list) or not assertions
            or any(not isinstance(a,dict) or any(
                not isinstance(a.get(k),str) or not a[k].strip()
                for k in ('expected','actual'))
                or not any(isinstance(a.get(k),str) and a[k].strip()
                    for k in ('basis','method'))
                for a in assertions)):
        return None
    pin=data.get('board_pin')
    if (not isinstance(pin,dict) or
            not isinstance(pin.get('message_id'),str) or not pin['message_id'].strip()):
        return None
    created=timestamp(data.get('created_at'))
    pinned=timestamp(pin.get('server_timestamp'))
    if created is None or pinned is None or created>pinned:
        return None
    # Historical v1 included sha256 in JSON; current v1 deliberately keeps
    # its detached digest separate, and the board pin is added after hashing.
    # Accept only these two explicitly specified canonical representations.
    embedded=data.get('sha256')
    if embedded is not None and (
            not isinstance(embedded,str) or re.fullmatch('[0-9a-f]{64}',embedded) is None):
        return None
    if embedded is None:
        content={k:v for k,v in data.items() if k not in ('sha256','board_pin')}
        canonical=json.dumps(content,sort_keys=True,separators=(',',':'),ensure_ascii=True)
    else:
        content={k:v for k,v in data.items() if k!='sha256'}
        canonical=json.dumps(content,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    actual=hashlib.sha256(canonical.encode()).hexdigest()
    if embedded is not None and embedded != actual:
        return None
    try:
        with open(path+'.sha256',encoding='utf-8') as f:
            detached=f.read().strip()
        with open(path,'rb') as f:
            raw=f.read()
        with open(path+'.sha256','rb') as f:
            detached_raw=f.read()
        if detached != actual:
            return None
        basename=os.path.basename(path)
        # Git-anchored postlanding copy (Act 26) must match the current state
        # receipt exactly, including the separately stored detached digest.
        repo_copy=subprocess.check_output(['git','-C',repo,'show',
              'main:records/investigations/'+basename],stderr=subprocess.DEVNULL)
        digest_copy=subprocess.check_output(['git','-C',repo,'show',
              'main:records/investigations/'+basename+'.sha256'],stderr=subprocess.DEVNULL)
        if raw != repo_copy or detached_raw != digest_copy:
            return None
    except (OSError,subprocess.CalledProcessError):
        return None
    return pinned
def git_batch_show(specs):
    """Read '<commit>:<path>' blobs in one invocation; miss/invalid -> skip."""
    if not specs:
        return {}
    proc=subprocess.run(['git','-C',repo,'cat-file','--batch'],
        input=('\n'.join(specs)+'\n').encode(),capture_output=True)
    out={}
    buf=proc.stdout
    for spec in specs:
        nl=buf.find(b'\n')
        if nl<0:
            break
        header=buf[:nl].decode(errors='replace'); buf=buf[nl+1:]
        if header.endswith(' missing'):
            continue
        try:
            size=int(header.rsplit(' ',1)[1])
        except (ValueError,IndexError):
            break
        blob=buf[:size]; buf=buf[size:]
        if buf[:1]==b'\n':
            buf=buf[1:]
        try:
            out[spec]=json.loads(blob.decode())
        except ValueError:
            continue
    return out
def first_parent_map():
    """One git invocation: commit -> (parent, tree, introduced paths).

    Equivalent to per-commit `rev-parse <c>^1` plus
    `diff(--root|--name-only --no-renames)`, without one subprocess per commit.
    """
    proc=subprocess.run(['git','-C',repo,'log','--first-parent','--reverse',
        '--no-renames','--name-only','--format=COMMIT %H %P %T',main],
        capture_output=True,text=True,check=True)
    info={}
    cur=None
    want_files=False
    for line in proc.stdout.splitlines():
        if line.startswith('COMMIT '):
            # Header shape: COMMIT <H> <P1>..<Pn> <T> (n=0 for root, where
            # the slot is empty; n=2 for merges). Tree is always last.
            parts=[t for t in line.split(' ') if t!='']
            if len(parts)<3 or parts[0]!='COMMIT':
                pass  # pathological path that happens to start with COMMIT
            else:
                _,h,rest,t=parts[0],parts[1],parts[2:-1],parts[-1]
                parents=list(rest)
                cur=h
                info[cur]=[parents[0] if parents else None,t,[]]
                want_files=False  # the header is followed by one blank line
                continue
        if line=='':
            # A blank line right after the header precedes the file list;
            # a blank line after files (or a second blank) ends the block.
            if cur is not None and not want_files and not info[cur][2]:
                want_files=True
            else:
                cur=None
            continue
        if cur is not None:
            info[cur][2].append(line)
            want_files=True
    return info
try:
    main=git('rev-parse','--verify','main')
    fp=first_parent_map()
    commits=list(fp)
    positions={c:i for i,c in enumerate(commits)}
    trees={c:t for c,(p,t,paths) in fp.items()}
    records=[]
    blobs=git_batch_show([c+':records/suite-status.json' for c in commits])
    for rec_commit in commits:
        try:
            data=blobs[rec_commit+':records/suite-status.json']
        except KeyError:
            continue
        recorded_commit=data.get('commit')
        # A status entry is evidence only if that commit itself introduced or
        # updated the status file; subsequent history snapshots aren't new runs.
        touched=fp[rec_commit][2]
        if 'records/suite-status.json' in touched:
            records.append((rec_commit,data,'git'))
    # reviewed-merge.sh stores an immutable receipt before publishing and emits
    # a bound event after a successful push. Both are outside Git; chronology is
    # therefore only as trustworthy as the delivery host, filesystem and writer.
    import glob
    publications={}
    for filename in sorted(glob.glob(os.path.join(state,'delivery','published-*.json'))):
        try:
            with open(filename,'rb') as f: raw=f.read()
            event=json.loads(raw)
            # Act 31: the integration queue emits the same bound event.
            if (event.get('generated_by') in ('government/reviewed-merge.sh','government/integrator.py')
                    and isinstance(event.get('commit'),str)
                    and type(event.get('published_at_ns')) is int
                    and re.fullmatch(r'[0-9a-f]{64}',str(event.get('receipt_sha256','')))):
                publications[event['commit']]=event
        except (OSError,ValueError):
            continue
    for filename in sorted(glob.glob(os.path.join(state,'delivery','verified-*.json'))):
        try:
            with open(filename,'rb') as f: raw=f.read()
            data=json.loads(raw)
            if (data.get('generated_by')=='government/suite-status.sh'
                    and data.get('suite') in ('tests/run-all.sh','tests/records-smoke.sh')
                    and type(data.get('recorded_at')) is int):
                # A pre-push receipt alone cannot establish chronology: it may
                # have been copied into state after main changed. Require the
                # post-push event emitted by reviewed-merge.sh, bound to this
                # exact receipt digest, and strict timestamp ordering.
                event=publications.get(data.get('commit'))
                digest=hashlib.sha256(raw).hexdigest()
                if (event is not None and event.get('receipt_sha256')==digest
                        and event.get('published_at_ns') > data.get('recorded_at') * 1000000000):
                    records.append((None,data,'pre-push-receipt'))
        except (OSError,ValueError):
            continue

    # Act 26's independent state receipt is separate from the old suite-status
    # shape. This is a bounded, explicitly reviewed additional evidence source.
    # The next first-parent commit provides a conservative landing upper bound.
    commit_times={}
    for line in git('log','--first-parent','--format=%H %ct',main).splitlines():
        fields=line.split()
        if len(fields)==2:
            try: commit_times[fields[0]]=int(fields[1])
            except ValueError: pass
    act26=[]
    for filename in sorted(glob.glob(os.path.join(state,'delivery','*.json'))):
        try:
            with open(filename,encoding='utf-8') as f:
                record=json.load(f)
            pinned=valid_act26_record(filename,record)
            if pinned is not None:
                act26.append((os.path.basename(filename),record,pinned))
        except (OSError,ValueError):
            continue
    changes=[]
    for i,commit in enumerate(commits):
        paths=[p for p in fp[commit][2] if p.startswith(('government/','tests/','records/'))]
        if not paths:
            continue
        expected_suite=('tests/records-smoke.sh'
                        if all(p.startswith('records/') for p in paths)
                        else 'tests/run-all.sh')
        tree=trees[commit]
        # Require the record commit to precede the main change. The record must
        # name that exact commit and its tree; a matching parent is insufficient
        # because it does not verify the resulting merge tree.
        prior=[]
        for rc,r,source in records:
            recorded=recorded_result(r,expected_suite)
            if recorded not in ('green','red') or r.get('tree') != tree:
                continue
            candidate=r.get('commit','')
            try:
                cand_tree=trees.get(candidate)
                if cand_tree is None:
                    cand_tree=git('rev-parse','--verify',candidate+'^{tree}')
                if cand_tree != tree:
                    continue
                if candidate != commit:
                    continue
                if source=='git' and positions.get(rc, i) >= i:
                    continue
                if source=='pre-push-receipt' and type(r.get('recorded_at')) is not int:
                    continue
            except (subprocess.CalledProcessError, OSError):
                continue
            prior.append((rc,r,source))
        reds=[(rc,r,source) for rc,r,source in prior
              if recorded_result(r,expected_suite)=='red']
        greens=[(rc,r,source) for rc,r,source in prior
                if recorded_result(r,expected_suite)=='green']
        parent=fp[commit][0]
        upper=commit_times.get(commits[i+1]) if i+1<len(commits) else None
        act26_matches=([name for name,r,pinned in act26
            if upper is not None and pinned<upper
            and r.get('commit')==commit and r.get('tree')==tree
            and r.get('parent')==parent and r.get('main_at_verification')==parent])
        if reds:
            status='violation'; reason='red suite recorded for exact commit/tree'
        elif greens or act26_matches:
            labels=set(source for _,_,source in greens)
            if act26_matches:labels.add('act26-prelanding-record')
            status='compliant'
            reason='preceding green record for exact commit/tree ('+','.join(sorted(labels))+')'
        elif any(recorded_result(r,expected_suite)=='red'
                 and r.get('commit')==commit and r.get('tree')==tree
                 for _,r,_source in records):
            status='red_chronology_unresolved'
            reason='exact red run exists but its pre-merge ordering is not established'
        else:
            status='unreadable'; reason='no preceding exact-commit/tree suite record'
        row={'commit':commit,'tree':tree,'paths':paths,'status':status,'reason':reason}
        if act26_matches and status=='compliant':
            row['source']=act26_matches[0]
            row['source_labels']=['act26-prelanding-record']
        changes.append(row)

    # Count distinct main changes with a recorded exact red result as episodes;
    # repeated status-file snapshots for the same main commit do not multiply it.
    red_events=len(set((x['commit'],x['tree']) for x in changes if x['status']=='violation'))
    total=len(changes)
    good=sum(x['status']=='compliant' for x in changes)
    print(json.dumps({'status':'measured','main_red_episodes':red_events,
      'change_count':total,'compliant':good,
      'unreadable':sum(x['status']=='unreadable' for x in changes),
      'violations':sum(x['status']=='violation' for x in changes),
      'red_chronology_unresolved':sum(x['status']=='red_chronology_unresolved' for x in changes),
      'green_suite_compliance_rate':(good/total if total else None),
      'changes_reaching_main_red':[x for x in changes if x['status']=='violation'],
      'red_chronology_unresolved_changes':[x for x in changes if x['status']=='red_chronology_unresolved'],
      'per_change':changes},sort_keys=True))
except (subprocess.CalledProcessError, OSError) as err:
    print(json.dumps({'status':'unreadable','reason':str(err)}))
PY
