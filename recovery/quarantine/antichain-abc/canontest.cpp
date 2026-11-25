#include <bits/stdc++.h>
#include <cstdlib>
static const int MYN = 12;
static int N;
typedef unsigned __int128 Key;
#include "canon.hpp"
static void printkey(const char* tag, Key k){
    printf("%s: ", tag);
    for(int i=0;i<N;i++){ printf("%d,", (int)((k>>(N*i))&((1u<<N)-1))); }
    printf("\n");
}
int main(int argc,char**argv){
    N=atoi(argv[1]);
    uint16_t a[MYN]={};
    // read N ints
    for(int i=0;i<N;i++){ long long v; scanf("%lld",&v); a[i]=v; }
    Key k1; uint16_t r1[MYN];
    canon_key_rows(a,k1,r1);
    printkey("canon(a)",k1);
    // relabel: swap 0 and 1
    uint16_t b[MYN];
    for(int i=0;i<N;i++){ uint16_t m=0; uint16_t src=a[i==0?1:(i==1?0:i)];
        for(int j=0;j<N;j++){ int jj = (j==0?1:(j==1?0:j)); if(src>>jj&1) m|=1u<<j; }
        b[i]=m; }
    Key k2; uint16_t r2[MYN];
    canon_key_rows(b,k2,r2);
    printkey("canon(swap01(a))",k2);
    printf("equal: %s\n", k1==k2?"YES":"NO");
    // canon of canon
    Key k3; uint16_t r3[MYN];
    canon_key_rows(r1,k3,r3);
    printkey("canon(canon(a))",k3);
    printf("fixed: %s\n", k1==k3?"YES":"NO");
    return 0;
}
