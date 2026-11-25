import json

# Generate merge-sort framed strategy certificate for n=5 as explicit tree.
# We track concrete slot contents as element ids 0..4 (arbitrary labels) to know
# which comparisons merge sort would make, but certificate only has slot compares/perms.
# Relations are over slots and checker propagates them; our perms must move the same
# logical elements so relations stay attached.

def id_perm(n):
    return list(range(n))

def rot_left_block(perm_block):
    # helper not needed
    pass

def apply_perm_to_array(arr, perm):
    # perm maps old slot -> new slot. element at old i moves to new perm[i]
    out = [None]*len(arr)
    for i,v in enumerate(arr):
        out[perm[i]] = v
    return out

n=5
nodes=[]

def add(node):
    nodes.append(node)
    return len(nodes)-1

# We'll represent merge sort procedure on array 'arr' representing current slot contents.
# Returns node index for this procedure, mutating nothing globally except nodes.
# But to build a single tree we follow one path? No, need both outcomes: function must
# branch only at compare nodes we create, and recursively build both children given
# the resulting array states.

def merge(arr, lo, mid, hi):
    # arr is list of length n
    left = lo
    right = mid
    out_start = lo
    # standard merge but we must emit comparison nodes following adaptive process.
    # State defined by (left,right,out_start?) with arr having: [lo..out_start-1] output sorted,
    # [out_start..left-1]? easier: simulate by always keeping elements in place except
    # we conceptually take from left/right. But to realize as in-place slot comparisons,
    # use the rotation method: when taking from right, rotate [left_index_of_head..right] right by 1.
    # Maintain indices.
    # We'll work on a copy per branch.
    def rec(a, i, j, out_pos):
        # i index of head of left run within [out_pos, j), j index of head of right run within [j, hi)
        # remaining left count = j-i? no: left run currently occupies out_pos..j-1? simpler:
        # use standard merge logic on array segments.
        # invariant: a[out_pos .. i-1] is merged prefix (sorted, < all in [i,j) and [j,hi_end?])
        # left remaining in a[i .. j-1], right remaining in a[j .. hi-1], both sorted.
        ii, jj = i, j
        if ii == j: # left exhausted, right already in place
            return add({"leaf": True})
        if jj == hi: # right exhausted
            return add({"leaf": True})
        # compare heads a[ii] vs a[jj] at slots ii,jj
        node = add(None)
        # lt: a[ii] < a[jj], element at ii stays, prefix grows
        a_lt = a[:] # no move
        lt_child = rec(a_lt, ii+1, jj, out_pos+1)
        # gt: a[jj] < a[ii], move element at jj to ii by rotating block ii..jj right
        perm = list(range(n))
        # rotate: old jj -> new ii, old k -> new k+1 for k in ii..jj-1
        for k in range(ii, jj):
            perm[k] = k+1
        perm[jj] = ii
        a_gt = apply_perm_to_array(a, perm)
        # after rotation, left run elements shifted right: now occupy ii+1 .. jj+1? yes count same (j-ii)
        # right head was at jj, now prefix at ii done, right remaining head at jj+1
        gt_child = rec(a_gt, ii+1, jj+1, out_pos+1)
        nodes[node] = {"compare":[ii,jj], "lt":{"next":lt_child,"perm":id_perm(n)}, "gt":{"next":gt_child,"perm":perm}}
        return node
    return rec(arr, lo, mid, mid)

# Full merge sort
def msort(arr, lo, hi):
    if hi-lo <= 1:
        return add({"leaf": True})
    mid = (lo+hi)//2
    # need to sequence: sort left, then sort right, then merge.
    # Build by: create sort-left subtree, but its leaves must become roots of sort-right etc.
    # So implement with continuation.
    def build(a, lo2, hi2, cont):
        if hi2-lo2 <= 1:
            return cont(a)
        mid2=(lo2+hi2)//2
        def after_left(a2):
            def after_right(a3):
                return merge_then(a3, lo2, mid2, hi2, cont)
            return build(a2, mid2, hi2, after_right)
        return build(a, lo2, mid2, after_left)
    return build(arr, lo, hi, lambda a: add({"leaf": True}))

def merge_then(arr, lo, mid, hi, cont):
    # like merge but when merge completes (a run exhausted) call cont on resulting array
    def rec(a,i,j):
        ii,jj=i,j
        if ii==j:
            return cont(a)
        if jj==hi:
            return cont(a)
        node=add(None)
        a_lt=a[:]
        lt_child=rec(a_lt, ii+1, jj)
        perm=list(range(n))
        for k in range(ii,jj): perm[k]=k+1
        perm[jj]=ii
        a_gt=apply_perm_to_array(a,perm)
        gt_child=rec(a_gt, ii+1, jj+1)
        nodes[node]={"compare":[ii,jj],"lt":{"next":lt_child,"perm":id_perm(n)},"gt":{"next":gt_child,"perm":perm}}
        return node
    return rec(arr, lo, mid)

root = msort(list(range(n)), 0, n)
cert = {"n":n, "budget":8, "nodes":nodes} # merge sort n=5 uses <=8? compute later
open('/tmp/opencode/ms5.json','w').write(json.dumps(cert))
print('nodes',len(nodes),'root',root)
