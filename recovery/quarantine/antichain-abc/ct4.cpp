#include <bits/stdc++.h>
static const int MYN = 12;
static int N;
typedef unsigned __int128 Key;
#include "canon_dbg.hpp"
int main(){
    N=3;
    uint16_t a[MYN]={}; a[0]=4;
    Key k; uint16_t r[MYN];
    canon_key_rows(a,k,r);
    printf("canon rows:"); for(int i=0;i<N;i++) printf(" %d",r[i]); printf("\n");
    return 0;
}
