import itertools, math, random, time, sys
from collections import deque

# R_3 definition
# elements indices: 0:y, 1:a1,2:a2,3:a3, 4:x, 5:b1,6:c1,7:b2,8:c2,9:b3,10:c3
names = ['y','a1','a2','a3','x','b1','c1','b2','c2','b3','c3']
idx = {n:i for i,n in enumerate(names)}
n = 11
# base relations (u < v)
less = [[False]*n for _ in range(n)]
# y below all B
for v in ['x','b1','c1','b2','c2','b3','c3']:
    less[idx['y']][idx[v]] = True
for i in [1,2,3]:
    for v in [f'b{i}', f'c{i}']:
        less[idx[f'a{i}']][idx[v]] = True

def closure(mat):
    # transitive closure
    m = [row[:] for row in mat]
    for k in range(n):
        for i in range(n):
            if m[i][k]:
                rowi = m[i]
                rowk = m[k]
                for j in range(n):
                    if rowk[j]: rowi[j] = True
    return m

base = closure(less)
print('base comparabilities count (ordered pairs u<v):', sum(sum(r) for r in base))
# check incomparable pairs count
inc = []
for i in range(n):
    for j in range(i+1,n):
        if not base[i][j] and not base[j][i]:
            inc.append((i,j))
print('incomparable pairs:', len(inc))

# e(P) via subset DP counting linear extensions consistent with poset matrix
# e(S)=number of linear extensions of subposet induced by S (bitmask)
# e(empty)=1, e(S)=sum_{x in S and x minimal in S} e(S without x)
# but need minimal among S given all relations

def count_extensions(mat):
    # precompute for speed? n<=11 2048 subsets easy
    # allowed[x] as bitmask of elements above x (or related?) easier use mat
    # dp[mask] = number of linear extensions
    dp = [0]*(1<<n)
    dp[0]=1
    # to get minimal in mask: x in mask and no y in mask with y<x (mat[y][x])
    # precompute below masks? not necessary
    allmask = (1<<n)-1
    for mask in range(1,1<<n):
        m = mask
        total = 0
        while m:
            lsb = m & -m
            x = (lsb.bit_length()-1)
            m -= lsb
            # is x minimal in mask? no y in mask with mat[y][x]
            ok = True
            mm = mask ^ lsb
            # check predecessors
            t = mm
            while t:
                lsb2 = t & -t
                y = (lsb2.bit_length()-1)
                t -= lsb2
                if mat[y][x]:
                    ok = False
                    break
            if ok:
                total += dp[mask ^ lsb]
        dp[mask]=total
    return dp[allmask]

e_base = count_extensions(base)
print('e(R3)=', e_base, 'C=', (e_base-1).bit_length())
# automorphisms: permute copies 1-3 and swap b_i,c_i
def apply_perm(mat, perm):
    # perm is list where new index of old i is perm[i]? easier build
    nm = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                nm[perm[i]][perm[j]] = True
    return nm

# generate automorphisms
auts = []
copy_perms = list(itertools.permutations([1,2,3]))
for cp in copy_perms:
    # cp maps copy slot? say original a1->a_{cp0} etc by positions
    for swaps in itertools.product([0,1],[0,1],[0,1]):
        # define mapping from old element to new
        # copies in order 1,2,3 correspond to (a1,b1,c1),(a2,b2,c2),(a3,b3,c3)
        old_groups = {1:('a1','b1','c1'),2:('a2','b2','c2'),3:('a3','b3','c3')}
        mapping = {}
        mapping[idx['y']] = idx['y']
        mapping[idx['x']] = idx['x']
        for orig_c in [1,2,3]:
            new_c = cp[orig_c-1]
            oa,ob,oc = old_groups[orig_c]
            na,nb,nc = old_groups[new_c]
            mapping[idx[oa]] = idx[na]
            if swaps[orig_c-1]==0:
                mapping[idx[ob]] = idx[nb]
                mapping[idx[oc]] = idx[nc]
            else:
                mapping[idx[ob]] = idx[nc]
                mapping[idx[oc]] = idx[nb]
        perm_arr = [0]*n
        for old,new in mapping.items():
            perm_arr[old]=new
        auts.append(tuple(perm_arr))
print('automorphisms:', len(set(auts)))

def mat_key(mat):
    # tuple of ints bitmasks per row
    rows = []
    for i in range(n):
        r=0
        row = mat[i]
        for j in range(n):
            if row[j]: r |= 1<<j
        rows.append(r)
    return tuple(rows)

def canon_key(mat):
    best = None
    for p in auts:
        nm = [[False]*n for _ in range(n)]
        for i in range(n):
            pi = p[i]
            row = mat[i]
            for j in range(n):
                if row[j]: nm[pi][p[j]] = True
        k = mat_key(nm)
        if best is None or k < best: best = k
    return best

# add relation and closure
def add_rel(mat,i,j):
    # add i<j
    m = [row[:] for row in mat]
    if m[i][j]: return m
    # closure: any x with x<=i (including i) gets < j and < all >j
    desc_j = 0
    for y in range(n):
        if y==j or m[j][y]: desc_j |= 1<<y
    for x in range(n):
        if x==i or m[x][i]:
            # add desc_j
            rowx = m[x]
            dj = desc_j
            while dj:
                lsb = dj & -dj
                y = lsb.bit_length()-1
                dj -= lsb
                rowx[y] = True
    return m

def incomparables(mat):
    res=[]
    for i in range(n):
        for j in range(i+1,n):
            if not mat[i][j] and not mat[j][i]:
                res.append((i,j))
    return res

# quick test e after adding a comparison
pairs = incomparables(base)
print('first pair', pairs[0], names[pairs[0][0]], names[pairs[0][1]])
m1 = add_rel(base, pairs[0][0], pairs[0][1])
m2 = add_rel(base, pairs[0][1], pairs[0][0])
print(count_extensions(m1), count_extensions(m2), count_extensions(m1)+count_extensions(m2))
print('done init')

NODE_CAP = 300000
WALL_CAP = 180.0
ATTEMPT_NODE_CAP = 60000
ATTEMPT_TIME_CAP = 45.0

class Search:
    def __init__(self, start_time):
        self.nodes = 0
        self.start = start_time
        self.attempt_start = start_time
        self.memo = {} # (key,budget)->bool
        self.strategy = {} # (key,budget)->(i,j)
        self.hit = None
    def time_up(self):
        now = time.time()
        return (now-self.start) > WALL_CAP or (now-self.attempt_start) > ATTEMPT_TIME_CAP

def can_solve(mat,budget,search,rng,depth=0):
    if search.hit: return False
    if search.nodes >= NODE_CAP or search.nodes >= ATTEMPT_NODE_CAP:
        search.hit = 'node_cap'
        return False
    if search.time_up():
        search.hit = 'time_cap'
        return False
    e = count_extensions(mat)
    if e <= 1:
        return True
    if budget <= 0:
        return False
    if (e-1).bit_length() > budget:
        return False
    key = canon_key(mat)
    mkey = (key,budget)
    if mkey in search.memo:
        return search.memo[mkey]
    search.nodes += 1
    inc = incomparables(mat)
    # heuristic ordering: evaluate children e
    cand = []
    for (i,j) in inc:
        m1 = add_rel(mat,i,j)
        m2 = add_rel(mat,j,i)
        e1 = count_extensions(m1)
        e2 = count_extensions(m2)
        # must satisfy info bound
        if (e1-1).bit_length() > budget-1 or (e2-1).bit_length() > budget-1:
            continue
        score = max(e1,e2)
        bal = abs(e1-e2)
        cand.append((score, bal, rng.random(), i,j,m1,m2))
    cand.sort()
    for _,_,_,i,j,m1,m2 in cand:
        # try
        if can_solve(m1,budget-1,search,rng,depth+1) and can_solve(m2,budget-1,search,rng,depth+1):
            search.memo[mkey]=True
            search.strategy[mkey]=(i,j)
            return True
        if search.hit: return False
    search.memo[mkey]=False
    return False

if __name__ == '__main__':
    start=time.time()
    # try to find complete strategy
    bestD=None
    best_info=None
    results=[]
    for D in [24,23]:
        print('\nTrying D=',D, flush=True)
        for attempt in range(5):
            if time.time()-start > WALL_CAP:
                break
            rng = random.Random(1000*D+attempt)
            search = Search(start)
            search.attempt_start = time.time()
            ok = can_solve(base,D,search,rng)
            rec = (D,attempt,ok,search.nodes,search.hit,len(search.memo),round(time.time()-search.attempt_start,2))
            results.append(rec)
            print(' attempt',attempt,'ok',ok,'nodes',search.nodes,'hit',search.hit,'memo',len(search.memo),'time',rec[-1], flush=True)
            if ok:
                bestD=D
                root = search.strategy.get((canon_key(base),D))
                best_info={'D':D,'attempt':attempt,'nodes':search.nodes,'root_pair':root,'strategy_size':len(search.strategy)}
                print('FOUND complete strategy for D=',D,'root',root, flush=True)
                break
        if bestD==D:
            break
    print('\nBEST', bestD, best_info, flush=True)
    print('RESULTS', results, flush=True)
    print('total time', round(time.time()-start,2), flush=True)


