import json
import argparse

class Ref:
    __slots__ = ('obj',)
    def __init__(self, obj):
        self.obj = obj

class Builder:
    def __init__(self, n):
        self.n = n
        self.id = list(range(n))

    def leaf(self):
        return Ref({"leaf": True})

    def sort_range(self, l, r, cont):
        size = r-l
        if size <= 1:
            return cont
        mid = l + size//2
        merge_entry = self.merge_range(l, mid-l, r-mid, cont)
        right_entry = self.sort_range(mid, r, merge_entry)
        left_entry = self.sort_range(l, mid, right_entry)
        return left_entry

    def merge_range(self, l, p, q, cont):
        n = self.n
        state = {}
        states_by_m = {}
        for m in range(0, p+q):
            s = p+q-m
            a_min = max(1, s-q)
            a_max = min(p, s-1)
            lst = []
            for a in range(a_min, a_max+1):
                lst.append((a, s-a))
            states_by_m[m] = lst
        for m in range(0, p+q):
            for (a,b) in states_by_m[m]:
                state[(a,b)] = Ref(None)
        for m in range(0, p+q):
            for (a,b) in states_by_m[m]:
                hL = l + m
                hR = l + m + a
                if a == 1:
                    next_lt = cont
                else:
                    next_lt = state[(a-1,b)]
                if b == 1:
                    next_gt = cont
                else:
                    next_gt = state[(a,b-1)]
                perm_gt = list(range(n))
                # move hR to hL, shift hL..hR-1 right by 1
                perm_gt[hR] = hL
                for k in range(hL, hR):
                    perm_gt[k] = k+1
                state[(a,b)].obj = {
                    "compare": [hL, hR],
                    "lt": {"next": next_lt, "perm": self.id},
                    "gt": {"next": next_gt, "perm": perm_gt},
                }
        return state[(p,q)]

    def build(self):
        leaf = self.leaf()
        entry = self.sort_range(0, self.n, leaf)
        return entry, leaf

def topo_number(root):
    seen = {}
    def visit(r):
        if id(r) in seen: return
        seen[id(r)] = r
        node = r.obj
        if node.get('leaf'):
            return
        visit(node['lt']['next'])
        visit(node['gt']['next'])
    visit(root)
    indeg = {rid:0 for rid in seen}
    children = {}
    for rid,r in seen.items():
        node=r.obj
        if node.get('leaf'):
            children[rid]=[]
            continue
        outs=[node['lt']['next'], node['gt']['next']]
        children[rid]=outs
        for c in outs:
            indeg[id(c)] += 1
    from collections import deque
    q=deque([rid for rid,d in indeg.items() if d==0])
    topo=[]
    while q:
        rid=q.popleft()
        topo.append(rid)
        for c in children.get(rid,[]):
            cid=id(c)
            indeg[cid]-=1
            if indeg[cid]==0:
                q.append(cid)
    if len(topo)!=len(seen):
        raise RuntimeError('cycle in numbering')
    idxmap={rid:i for i,rid in enumerate(topo)}
    nodes=[None]*len(topo)
    for rid,i in idxmap.items():
        r=seen[rid]
        node=r.obj
        if node.get('leaf'):
            nodes[i]={"leaf": True}
        else:
            nodes[i]={
                "compare": node['compare'],
                "lt": {"next": idxmap[id(node['lt']['next'])], "perm": node['lt']['perm']},
                "gt": {"next": idxmap[id(node['gt']['next'])], "perm": node['gt']['perm']},
            }
    return nodes

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=12)
    ap.add_argument('--budget', type=int, default=100)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    b=Builder(args.n)
    entry,leaf=b.build()
    nodes=topo_number(entry)
    cert={"n":args.n,"budget":args.budget,"nodes":nodes}
    with open(args.out,'w') as f:
        json.dump(cert,f,separators=(',',':'))
    nonleaf=sum(1 for nd in nodes if not nd.get('leaf'))
    leaves=sum(1 for nd in nodes if nd.get('leaf'))
    print(f"wrote {args.out} nodes={len(nodes)} compare={nonleaf} leaves={leaves} edges={2*nonleaf}")

if __name__=='__main__':
    main()
