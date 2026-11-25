import sys, json, random, time
sys.path.insert(0, '/home/lubko/soring-fronts/fibonacci-threshold-20261111')
from solve_fib import m_extension_set
classes = [tuple(x) for x in json.load(open('classes_n8.json'))]
recs = {}
for line in open('checkpoint_n8_ordered.jsonl'):
    line=line.strip()
    if line:
        r = json.loads(line); recs[int(r['idx'])] = r
random.seed(777)
cands = [(i,r) for i,r in recs.items() if 800 < r['e'] <= 2500]
print(f'candidates in (800,2500]: {len(cands)}', flush=True)
sample = random.sample(cands, min(10, len(cands)))
sample.sort(key=lambda t: t[1]['e'])
agree=0; total=0
t0=time.time()
for i,r in sample:
    if time.time()-t0 > 1500: print('TIMEBOX xcheck-hard'); break
    m_ext = int(m_extension_set(classes[i], 8))
    ok=(m_ext==r['m']); total+=1; agree+=ok
    print(f'XCHECK-H idx={i} e={r["e"]} m_state={r["m"]} m_ext={m_ext} {"OK" if ok else "MISMATCH"}', flush=True)
print(f'XCHECK-H-AGREE {agree}/{total}', flush=True)
