#include <bits/stdc++.h>
#include <cstdlib>
#include <random>
static const int MYN = 12;
static int N;
typedef unsigned __int128 Key;
#include "canon.hpp"

int main(int argc,char**argv){
    N=argc>2?atoi(argv[2]):6;
    unsigned seed=argc>1?atoi(argv[1]):1;
    std::mt19937 rng(seed);
    for(int trial=0;trial<2000;trial++){
        uint16_t a[MYN]={};
        // random DAG-ish relation set (not nec. transitive)
        for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(rng()%3==0) a[i]|=1u<<j;
        Key k1; uint16_t r1[MYN];
        canon_key_rows(a,k1,r1);
        // random relabeling
        int p[MYN]; for(int i=0;i<N;i++) p[i]=i;
        std::shuffle(p,p+N,rng);
        uint16_t b[MYN]={};
        for(int i=0;i<N;i++){ uint16_t m=0; uint16_t src=a[p[i]];
            for(int j=0;j<N;j++) if(src>>p[j]&1) m|=1u<<j;
            b[i]=m; }
        Key k2; uint16_t r2[MYN];
        canon_key_rows(b,k2,r2);
        if(k1!=k2){
            printf("MISMATCH trial %d\n canon(a)=",trial);
            for(int i=0;i<N;i++) printf("%d,",(int)((k1>>(N*i))&((1u<<N)-1)));
            printf("\n canon(b)=");
            for(int i=0;i<N;i++) printf("%d,",(int)((k2>>(N*i))&((1u<<N)-1)));
            printf("\n a:"); for(int i=0;i<N;i++) printf(" %d",a[i]);
            printf("\n p:"); for(int i=0;i<N;i++) printf(" %d",p[i]);
            printf("\n canon rows a:"); for(int i=0;i<N;i++) printf(" %d",r1[i]);
            printf("\n canon rows b:"); for(int i=0;i<N;i++) printf(" %d",r2[i]);
            printf("\n");
            return 1;
        }
    }
    printf("all consistent\n");
    return 0;
}
