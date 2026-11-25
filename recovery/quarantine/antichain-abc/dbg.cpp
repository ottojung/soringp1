#include <bits/stdc++.h>
static int N;
typedef unsigned __int128 Key;
static void refine_dbg(const uint16_t in[], int N_){
    std::vector<int> color(N_);
    for(int i=0;i<N_;i++) color[i]=__builtin_popcount((unsigned)in[i]);
    auto show=[&](const char*t){ printf("%s colors:",t); for(int i=0;i<N_;i++) printf(" %d",color[i]); printf("\n"); };
    show("init");
    while(true){
        std::vector<std::array<int,2*MYN_+1>> dummy; (void)dummy;
        int dn[12][12], dnN[12], uv[12][12], uvN[12];
        for(int i=0;i<N_;i++){ dnN[i]=0; uvN[i]=0;
            for(int j=0;j<N_;j++) if(in[i]>>j&1) dn[i][dnN[i]++]=color[j];
            for(int j=0;j<N_;j++) if(in[j]>>i&1) uv[i][uvN[i]++]=color[j];
            std::sort(dn[i],dn[i]+dnN[i]); std::sort(uv[i],uv[i]+uvN[i]); }
        std::vector<std::array<int,25>> sigv(N_);
        for(int i=0;i<N_;i++){ auto&s=sigv[i]; for(auto&x:s) x=7777; s[0]=color[i];
            for(int k=0;k<dnN[i];k++) s[1+k]=dn[i][k];
            for(int k=0;k<uvN[i];k++) s[13+k]=uv[i][k]; }
        std::vector<std::array<int,25>> sorted=sigv;
        std::sort(sorted.begin(),sorted.end());
        sorted.erase(std::unique(sorted.begin(),sorted.end()),sorted.end());
        int ncolor[12];
        for(int i=0;i<N_;i++) ncolor[i]=std::lower_bound(sorted.begin(),sorted.end(),sigv[i])-sorted.begin();
        bool same=true; for(int i=0;i<N_;i++) if(ncolor[i]!=color[i]){same=false;break;}
        for(int i=0;i<N_;i++) color[i]=ncolor[i];
        show("iter");
        if(same) break;
    }
}
static const int MYN_=12;
int main(){ 
    uint16_t a[12]={0,1,1,2,2,0,0,0,0,0,0,0};
    N_=5;
    refine_dbg(a,5);
    return 0; }
