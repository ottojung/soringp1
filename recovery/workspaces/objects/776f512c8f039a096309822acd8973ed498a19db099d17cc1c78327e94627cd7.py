import sys, json, random
sys.path.insert(0, '/home/lubko/soring-fronts/fibonacci-threshold-20261111')
from solve_fib import m_extension_set
classes = [tuple(x) for x in json.load(open('classes_n8.json'))]
recs = {}
for line in open('checkpoint_n8_ordered.jsonl'):
    line=line.strip()
    if line:
        r = json.loads(line); recs[int(r['idx'])] = r
# stratified sample by e, e<=3000, seed fixed, exclude nothing (fresh draw across all done)
random.seed(20261111)
cands = [(i,r) for i,r in recs.items() if r['e']<=3000]
cands.sort(key=lambda t:(t[1]['e'],t[0]))
# stratify: split into 5 e-bands, take 6 each
bands=[[],[],[],[],[]]
for i,r in cands:
    e=r['e']
    b=0 if e<=12 else 1 if e<=40 else 2 if e<=150 else 3 if e<=800 else 4
    bands[b].append((i,r))
sample=[]
for b in bands:
    k=min(6,len(b))
    sample.extend(random.sample(b,k))
sample.sort(key=lambda t:(t[1]['e'],t[0]))
print(f'SAMPLE n={len(sample)} bandsizes={[len(b) for b in bands]}', flush=True)
agree=0; total=0
for i,r in sample:
    m_ext = int(m_extension_set(classes[i], 8))
    ok = (m_ext==r['m'])
    total+=1; agree+=ok
    print(f'XCHECK idx={i} e={r["e"]} m_state={r["m"]} m_ext={m_ext} {"OK" if ok else "MISMATCH"}', flush=True)
print(f'XCHECK_AGREE {agree}/{total}', flush=True)
