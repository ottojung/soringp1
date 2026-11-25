#include <bits/stdc++.h>
#include "nauty.h"
static const int MYN = 12;
static const int MYM = (MYN + WORDSIZE - 1) / WORDSIZE;
static int N;
static const int INF = 1000000;
typedef unsigned __int128 Key;
struct HKey { size_t operator()(const Key& k) const { uint64_t lo=(uint64_t)k, hi=(uint64_t)(k>>64); return std::hash<uint64_t>()(lo^(hi*0x9e3779b97f4a7c15ULL)); } };
static std::unordered_map<Key,int,HKey> memoF, memoH;
static inline int popc(uint16_t x){ return __builtin_popcount((unsigned)x); }
static Key canon_key(const uint16_t up[MYN], uint16_t out[MYN]) {
    DEFAULTOPTIONS_GRAPH(options); options.getcanon=TRUE; options.digraph=TRUE; options.defaultptn=TRUE;
    graph g[MYM*MYN], cg[MYM*MYN]; int lab[MYN], ptn[MYN], orbits[MYN]; statsblk stats;
    memset(g,0,sizeof(g));
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(up[i]>>j&1) ADDONEARC(g,i,j,1);
    static std::vector<setword> ws(200000);
    nauty(g,lab,ptn,NULL,orbits,&options,&stats,ws.data(),(int)ws.size(),1,N,cg);
    Key k=0;
    for(int i=0;i<N;i++){ uint16_t row=0; for(int j=0;j<N;j++) if((cg[i]>>(WORDSIZE-1-j))&1UL) row|=1u<<j; out[i]=row; k|=((Key)row)<<(N*i); }
    return k;
}
static uint16_t downMask[MYN]; static long long dp[1<<MYN];
static long long ext(const uint16_t up[MYN]){
    for(int i=0;i<N;i++) downMask[i]=0;
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(up[i]>>j&1) downMask[j]|=1u<<i;
    int full=(1<<N)-1; dp[0]=1;
    for(int mask=1;mask<=full;mask++){ long long s=0; for(int v=0;v<N;v++){ if(!(mask>>v&1)) continue; if(downMask[v]&~mask) continue; s+=dp[mask^(1<<v)]; } dp[mask]=s; }
    return dp[full];
}
static bool addRel(const uint16_t up[MYN],int x,int y,uint16_t out[MYN]){
    if(up[x]>>y&1){ for(int i=0;i<N;i++) out[i]=up[i]; return true; }
    if(up[y]>>x&1) return false;
    uint16_t belowx=1u<<x; for(int a=0;a<N;a++) if(up[a]>>x&1) belowx|=1u<<a;
    uint16_t gain=(1u<<y)|up[y];
    for(int a=0;a<N;a++){ out[a]=up[a]; if(belowx>>a&1) out[a]|=gain; }
    return true;
}
static int slaveCount(const uint16_t up[MYN],int x,int y){
    uint16_t freeY=~(up[y]|downMask[y]|(1u<<y)); uint16_t freeX=~(up[x]|downMask[x]|(1u<<x));
    return popc(up[x]&freeY)+popc(downMask[y]&freeX);
}
static void solve(const uint16_t in[MYN],int &F,int &H,uint16_t canonOut[MYN]){
    Key key=canon_key(in,canonOut);
    auto it=memoF.find(key); if(it!=memoF.end()){ F=it->second; H=memoH[key]; return; }
    uint16_t up[MYN]; for(int i=0;i<N;i++) up[i]=canonOut[i];
    for(int i=0;i<N;i++) downMask[i]=0;
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(up[i]>>j&1) downMask[j]|=1u<<i;
    std::vector<std::pair<int,int>> pairs;
    for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(!(up[i]>>j&1)&&!(up[j]>>i&1)) pairs.push_back({i,j});
    if(pairs.empty()){ memoF[key]=0; memoH[key]=0; F=H=0; return; }
    long long total=ext(up);
    std::vector<std::pair<int,int>> cpairs;
    for(auto pr:pairs){
        int x=pr.first,y=pr.second; uint16_t t[MYN]; long long a=-1,b=-1;
        if(addRel(up,x,y,t)) a=ext(t);
        if(addRel(up,y,x,t)) b=ext(t);
        bool cert=false;
        for(int o=0;o<2&&!cert;o++){ int u=o?y:x,v=o?x:y; long long eu=(u==x)?a:b; int sl=slaveCount(up,u,v); if(sl<=1&&2*eu>=total) cert=true; if(2*eu==total) cert=true; }
        if(!cert){
            for(int o=0;o<2&&!cert;o++){
                int u=o?y:x,v=o?x:y; long long evu=(u==x)?b:a;
                for(int z=0;z<N&&!cert;z++){
                    if(z==x||z==y) continue; uint16_t t1[MYN],t2[MYN];
                    if(!addRel(up,u,v,t1)) continue;
                    if(!addRel(t1,v,z,t2)) continue;
                    long long a1=ext(t2); uint16_t tz[MYN]; long long ezv=0;
                    if(addRel(up,z,v,tz)) ezv=ext(tz);
                    long long bound=std::max(evu,ezv);
                    if(2*bound<=total&&a1<=bound) cert=true;
                }
            }
        }
        if(cert) cpairs.push_back(pr);
    }
    int bestF=INF;
    for(auto pr:pairs){ int x=pr.first,y=pr.second; uint16_t t[MYN],c1[MYN],c2[MYN]; int f1,f2,h1,h2;
        if(addRel(up,x,y,t)) solve(t,f1,h1,c1); else {f1=h1=INF;}
        if(addRel(up,y,x,t)) solve(t,f2,h2,c2); else {f2=h2=INF;}
        bestF=std::min(bestF,1+std::max(f1,f2)); }
    int bestH=INF;
    for(auto pr:cpairs){ int x=pr.first,y=pr.second; uint16_t t[MYN],c1[MYN],c2[MYN]; int f1,f2,h1,h2;
        if(addRel(up,x,y,t)) solve(t,f1,h1,c1); else {h1=INF;}
        if(addRel(up,y,x,t)) solve(t,f2,h2,c2); else {h2=INF;}
        bestH=std::min(bestH,1+std::max(h1,h2)); }
    F=bestF; H=bestH; memoF[key]=F; memoH[key]=H;
}
static void parse_up(const char* s,std::array<uint16_t,MYN>&a){ char* p=(char*)s; int k=0; while(p&&*p&&k<MYN){ a[k++]=(uint16_t)strtol(p,&p,10); if(*p==',') p++; } }
int main(int argc,char**argv){
    if(argc<2){ fprintf(stderr,"modes: all pN.txt out | reach n allout out\n"); return 1; }
    std::string mode=argv[1];
    if(mode=="all"){
        FILE* f=fopen(argv[2],"r"); if(!f){perror("open");return 1;} if(fscanf(f,"%d",&N)!=1) return 1;
        std::vector<std::array<uint16_t,MYN>> roots; for(;;){ std::array<uint16_t,MYN> a{}; int ok=1; for(int i=0;i<N;i++){ int v; if(fscanf(f,"%d",&v)!=1){ok=0;break;} a[i]=(uint16_t)v; } if(!ok) break; roots.push_back(a);} fclose(f);
        fprintf(stderr,"n=%d roots=%zu\n",N,roots.size()); nauty_check(WORDSIZE,MYM,MYN,NAUTYVERSIONID);
        memoF.reserve(400000); memoH.reserve(400000);
        FILE* g=fopen(argv[3],"w");
        for(size_t r=0;r<roots.size();r++){ uint16_t up[MYN],c[MYN]; for(int i=0;i<N;i++) up[i]=roots[r][i]; int F,H; solve(up,F,H,c);
            fprintf(g,"ROW %d %d %d up=",(int)r,F,H); for(int i=0;i<N;i++) fprintf(g,"%s%d",i?",":"",up[i]); fprintf(g,"\n"); }
        fclose(g);
        long long over=0; for(auto&kv:memoF) if(memoH[kv.first]>kv.second) over++;
        fprintf(stderr,"states=%zu over=%lld\n",memoF.size(),over);
        return 0;
    }
    if(mode=="reach"){
        N=atoi(argv[2]); FILE* f=fopen(argv[3],"r"); if(!f){perror("open");return 1;}
        std::vector<std::array<uint16_t,MYN>> rows; std::vector<int> Fs,Hs; std::unordered_map<Key,int,HKey> idx; char line[4096];
        while(fgets(line,sizeof line,f)){ if(strncmp(line,"ROW ",4)) continue; int r,F,H; char buf[2048]; if(sscanf(line,"ROW %d %d %d up=%2047s",&r,&F,&H,buf)!=4) continue; std::array<uint16_t,MYN> a{}; parse_up(buf,a); rows.push_back(a); Fs.push_back(F); Hs.push_back(H);} fclose(f);
        fprintf(stderr,"rows=%zu N=%d\n",rows.size(),N);
        for(size_t i=0;i<rows.size();i++){ uint16_t out[MYN]; Key key=canon_key(rows[i].data(),out); idx[key]=(int)i; }
        uint16_t anti[MYN]; for(int i=0;i<N;i++) anti[i]=0; uint16_t out[MYN]; Key ak=canon_key(anti,out); auto it=idx.find(ak); if(it==idx.end()){fprintf(stderr,"no anti\n");return 1;} int start=it->second;
        fprintf(stderr,"start=%d F=%d H=%d\n",start,Fs[start],Hs[start]);
        std::vector<char> seen(rows.size(),0); std::vector<int> par(rows.size(),-1); std::vector<int> q; q.push_back(start); seen[start]=1; size_t head=0; std::vector<int> badlist;
        while(head<q.size()){ int ii=q[head++]; if(Hs[ii]>Fs[ii]) badlist.push_back(ii); auto up=rows[ii].data();
            for(int x=0;x<N;x++) for(int y=x+1;y<N;y++){ if((up[x]>>y&1)||(up[y]>>x&1)) continue; uint16_t t1[MYN],t2[MYN],c1[MYN],c2[MYN]; int j1=-1,j2=-1;
                if(addRel(up,x,y,t1)){ Key k=canon_key(t1,c1); auto z=idx.find(k); if(z!=idx.end()) j1=z->second; }
                if(addRel(up,y,x,t2)){ Key k=canon_key(t2,c2); auto z=idx.find(k); if(z!=idx.end()) j2=z->second; }
                if(j1<0||j2<0) continue; if(std::max(Fs[j1],Fs[j2])!=Fs[ii]-1) continue; for(int j:{j1,j2}) if(!seen[j]){seen[j]=1;par[j]=ii;q.push_back(j);} }
        }
        fprintf(stderr,"reachable=%zu badreach=%zu\n",q.size(),badlist.size()); FILE* g=fopen(argv[4],"w");
        for(int ii:badlist){ std::vector<int> path; for(int z=ii;z>=0;z=par[z]) path.push_back(z); std::reverse(path.begin(),path.end());
            fprintf(g,"PATH"); for(int z:path) fprintf(g," %d(F=%d,H=%d)",z,Fs[z],Hs[z]); fprintf(g,"\n");
            fprintf(g,"BADREACH F=%d H=%d up=",Fs[ii],Hs[ii]); for(int i=0;i<N;i++) fprintf(g,"%s%d",i?",":"",rows[ii][i]); fprintf(g,"\n"); }
        fclose(g); return 0;
    }
    return 1;
}
