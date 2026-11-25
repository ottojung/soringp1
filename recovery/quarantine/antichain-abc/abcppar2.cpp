// abcppar2: corrected parallel F/H census.
// Fixes vs abc.cpp (the 2026-11-10 binary):
//  (a) slaveCount/A-test now uses the CURRENT state's downsets (abc.cpp read a
//      downMask clobbered by the last child ext() call);
//  (b) nauty canon is mutex-guarded so threads can run ext/cert work in
//      parallel safely;
//  (c) level-synchronous processing (densest relation count first) so child
//      memo lookups are always final.
// F must reproduce all8.out/all9.out exactly; H may legitimately differ.
#include <bits/stdc++.h>
#include <thread>
#include <atomic>
#include <mutex>
#include "nauty.h"
static const int MYN = 12;
static const int MYM = (MYN + WORDSIZE - 1) / WORDSIZE;
static int N;
static const int INF = 1000000;
typedef unsigned __int128 Key;
struct HKey { size_t operator()(const Key& k) const { uint64_t lo=(uint64_t)k, hi=(uint64_t)(k>>64); return std::hash<uint64_t>()(lo^(hi*0x9e3779b97f4a7c15ULL)); } };
static std::unordered_map<Key,std::pair<int,int>,HKey> memo;
static std::mutex nautyMutex;

static Key canon_key(const uint16_t up[MYN], uint16_t out[MYN]) {
    std::lock_guard<std::mutex> lk(nautyMutex);
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

// ext: fills downOut with the downset masks of up, returns e(up)
static long long ext(const uint16_t up[MYN], uint16_t downOut[MYN], long long* dp){
    for(int i=0;i<N;i++) downOut[i]=0;
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(up[i]>>j&1) downOut[j]|=1u<<i;
    int full=(1<<N)-1; dp[0]=1;
    for(int mask=1;mask<=full;mask++){ long long s=0; for(int v=0;v<N;v++){ if(!(mask>>v&1)) continue; if(downOut[v]&~mask) continue; s+=dp[mask^(1<<v)]; } dp[mask]=s; }
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
static int slaveCount(const uint16_t up[MYN],const uint16_t downP[MYN],int x,int y){
    uint16_t freeY=~(up[y]|downP[y]|(1u<<y)); uint16_t freeX=~(up[x]|downP[x]|(1u<<x));
    return __builtin_popcount((unsigned)(up[x]&freeY))+__builtin_popcount((unsigned)(downP[y]&freeX));
}

struct ThreadScratch {
    long long dp[1<<MYN];
    uint16_t downP[MYN], downT[MYN];
};

static void solveOne(const uint16_t in[MYN], ThreadScratch& sc, int& Fo, int& Ho){
    uint16_t up[MYN]; Key key;
    key=canon_key(in,up);
    { auto it=memo.find(key); if(it!=memo.end()){ Fo=it->second.first; Ho=it->second.second; return; } }
    long long* dp=sc.dp; uint16_t* downP=sc.downP; uint16_t* downT=sc.downT;
    long long total=ext(up,downP,dp);
    std::vector<std::pair<int,int>> pairs;
    for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(!(up[i]>>j&1)&&!(up[j]>>i&1)) pairs.push_back({i,j});
    if(pairs.empty()){ memo[key]={0,0}; Fo=0; Ho=0; return; }
    std::vector<std::pair<int,int>> cpairs;
    for(auto pr:pairs){
        int x=pr.first,y=pr.second; uint16_t t[MYN]; long long a=-1,b=-1;
        if(addRel(up,x,y,t)) a=ext(t,downT,dp);
        if(addRel(up,y,x,t)) b=ext(t,downT,dp);
        bool cert=false;
        for(int o=0;o<2&&!cert;o++){ int u=o?y:x,v=o?x:y; long long eu=(u==x)?a:b; int sl=slaveCount(up,downP,u,v); if(sl<=1&&2*eu>=total) cert=true; if(2*eu==total) cert=true; }
        if(!cert){
            for(int o=0;o<2&&!cert;o++){
                int u=o?y:x,v=o?x:y; long long evu=(u==x)?b:a;
                for(int z=0;z<N&&!cert;z++){
                    if(z==x||z==y) continue; uint16_t t1[MYN],t2[MYN];
                    if(!addRel(up,u,v,t1)) continue;
                    if(!addRel(t1,v,z,t2)) continue;
                    long long a1=ext(t2,downT,dp); uint16_t tz[MYN]; long long ezv=0;
                    if(addRel(up,z,v,tz)) ezv=ext(tz,downT,dp);
                    long long bound=std::max(evu,ezv);
                    if(2*bound<=total&&a1<=bound) cert=true;
                }
            }
        }
        if(cert) cpairs.push_back(pr);
    }
    int bestF=INF;
    for(auto pr:pairs){ int x=pr.first,y=pr.second; uint16_t t[MYN],c1[MYN]; Key k1,k2; int f1,f2,h1,h2;
        if(addRel(up,x,y,t)){ k1=canon_key(t,c1); auto it=memo.find(k1); if(it!=memo.end()){f1=it->second.first;h1=it->second.second;} else {f1=h1=INF;} } else {f1=h1=INF;}
        if(addRel(up,y,x,t)){ k2=canon_key(t,c1); auto it=memo.find(k2); if(it!=memo.end()){f2=it->second.first;h2=it->second.second;} else {f2=h2=INF;} } else {f2=h2=INF;}
        bestF=std::min(bestF,1+std::max(f1,f2)); }
    int bestH=INF;
    for(auto pr:cpairs){ int x=pr.first,y=pr.second; uint16_t t[MYN],c1[MYN]; Key k1,k2; int h1,h2;
        if(addRel(up,x,y,t)){ k1=canon_key(t,c1); auto it=memo.find(k1); if(it!=memo.end()){h1=it->second.second;} else h1=INF; } else h1=INF;
        if(addRel(up,y,x,t)){ k2=canon_key(t,c1); auto it=memo.find(k2); if(it!=memo.end()){h2=it->second.second;} else h2=INF; } else h2=INF;
        bestH=std::min(bestH,1+std::max(h1,h2)); }
    memo[key]={bestF,bestH}; Fo=bestF; Ho=bestH;
}

int main(int argc,char**argv){
    if(argc<4){ fprintf(stderr,"usage: abcppar2 pN.txt out nthreads\n"); return 1; }
    FILE* f=fopen(argv[1],"r"); if(!f){perror("open");return 1;}
    if(fscanf(f,"%d",&N)!=1) return 1;
    std::vector<std::array<uint16_t,MYN>> roots;
    for(;;){ std::array<uint16_t,MYN> a{}; int ok=1; for(int i=0;i<N;i++){ long long v; if(fscanf(f,"%lld",&v)!=1){ok=0;break;} a[i]=(uint16_t)v; } if(!ok) break; roots.push_back(a); }
    fclose(f);
    fprintf(stderr,"n=%d roots=%zu\n",N,roots.size());
    int nthreads=atoi(argv[3]);
    int maxL=0; std::vector<int> level(roots.size());
    for(size_t r=0;r<roots.size();r++){ int L=0; for(int i=0;i<N;i++) L+=__builtin_popcount((unsigned)roots[r][i]); level[r]=L; maxL=std::max(maxL,L); }
    std::vector<std::vector<int>> byLevel(maxL+1);
    for(size_t r=0;r<roots.size();r++) byLevel[level[r]].push_back((int)r);
    std::vector<int> Fr(roots.size()),Hr(roots.size());
    memo.reserve(4000000);
    std::atomic<size_t> cursor(0);
    std::atomic<int> doneLevels(0);
    auto start=std::chrono::steady_clock::now();
    for(int L=maxL;L>=0;L--){
        auto& v=byLevel[L]; if(v.empty()) continue;
        cursor.store(0);
        std::vector<std::thread> th;
        for(int t=0;t<nthreads;t++) th.emplace_back([&](){
            ThreadScratch sc;
            size_t i;
            while((i=cursor.fetch_add(1))<v.size()){
                int r=v[i]; int Fo,Ho;
                solveOne(roots[r].data(),sc,Fo,Ho);
                Fr[r]=Fo; Hr[r]=Ho;
            }
        });
        for(auto&t:th) t.join();
        doneLevels++;
        { auto el=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
          fprintf(stderr,"level %d done (%zu classes, memo=%zu, %.0fs)\n",L,v.size(),memo.size(),el); fflush(stderr); }
    }
    FILE* g=fopen(argv[2],"w");
    for(size_t r=0;r<roots.size();r++){ fprintf(g,"ROW %zu %d %d up=",(size_t)r,Fr[r],Hr[r]); for(int i=0;i<N;i++) fprintf(g,"%s%d",i?",":"",roots[r][i]); fprintf(g,"\n"); }
    fclose(g);
    long long over=0; for(auto&kv:memo) if(kv.second.second>kv.second.first) over++;
    auto el=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    fprintf(stderr,"states=%zu over=%lld time=%.0fs\n",memo.size(),over,el);
    return 0;
}
