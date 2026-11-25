#include <bits/stdc++.h>
static const int MYN = 12;
static int N;
typedef unsigned __int128 Key;
#include "canon.hpp"
int main(){
    N=3;
    uint16_t a[MYN]={}; a[0]=4; // 0<2
    Key k; uint16_t r[MYN];
    canon_key_rows(a,k,r);
    printf("canon key rows: ");
    for(int i=0;i<N;i++) printf(" %d",r[i]);
    printf("\n");
    // manual: what does rec2 see? replicate groups quickly by copying internals
    return 0;
}
