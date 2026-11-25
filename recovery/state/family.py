import sys
sys.path.insert(0,'/tmp/opencode/t5verify')
from verify import count_ext, succ_from_pred, minimax_succ, closure_pred
for n in range(1,9):
    pred=[0]+[(1<<(i-1))-1 for i in range(1,n)]
    pred=closure_pred(pred)
    e=count_ext(pred); m=minimax_succ(succ_from_pred(pred))
    print(f"F_{n}: pred={list(pred)} e={e} m={m}")
