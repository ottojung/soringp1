// Parallel level-synchronous F/H census over all unlabeled posets.
// Same definitions as abc.cpp (validated on n<=9, Executive-verified #301),
// but canon is a self-contained refinement+color-class-permutation search
// (complete invariant: any isomorphism preserves refined colors), and levels
// (by relation count) are processed from densest to sparsest so that every
// child lookup hits the already-final memo. No nauty, no locks except at
// level barriers.
#include <bits/stdc++.h>
#include <thread>
#include <atomic>

static const int MYN = 12;
static int N;
static const int INF = 1000000;
typedef unsigned __int128 Key;
struct HKey { size_t operator()(const Key& k) const { uint64_t lo=(uint64_t)k, hi=(uint64_t)(k>>64); return std::hash<uint64_t>()(lo^(hi*0x9e3779b97f4a7c15ULL)); } };
static std::unordered_map<Key,std::pair<int,int>,HKey> memo;

static thread_local long long tdp[1<<MYN];
static thread_local uint16_t tdown[MYN];

static long long ext(const uint16_t up[MYN]){
    for(int i=0;i<N;i++) tdown[i]=0;
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(up[i]>>j&1) tdown[j]|=1u<<i;
    int full=(1<<N)-1; tdp[0]=1;
    for(int mask=1;mask<=full;mask++){ long long s=0; for(int v=0;v<N;v++){ if(!(mask>>v&1)) continue; if(tdown[v]&~mask) continue; s+=tdp[mask^(1<<v)]; } tdp[mask]=s; }
    return tdp[full];
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
    uint16_t freeY=~(up[y]|tdown[y]|(1u<<y)); uint16_t freeX=~(up[x]|tdown[x]|(1u<<x));
    return __builtin_popcount((unsigned)(up[x]&freeY))+__builtin_popcount((unsigned)(tdown[y]&freeX));
}

// ---- canon: 2D color refinement + min encoding over color-class permutations
static void canon_key_rows(const uint16_t in[MYN], Key& keyOut, uint16_t rows[MYN]){
    int color[MYN], ncolor[MYN];
    for(int i=0;i<N;i++) color[i]=__builtin_popcount((unsigned)in[i]);
    while(true){
        int dn[MYN][MYN], dnN[MYN], uv[MYN][MYN], uvN[MYN];
        for(int i=0;i<N;i++){ dnN[i]=0; uvN[i]=0;
            for(int j=0;j<N;j++) if(in[i]>>j&1) dn[i][dnN[i]++]=color[j];
            for(int j=0;j<N;j++) if(in[j]>>i&1) uv[i][uvN[i]++]=color[j];
            std::sort(dn[i],dn[i]+dnN[i]); std::sort(uv[i],uv[i]+uvN[i]); }
        std::vector<std::array<int,2*MYN+1>> sigv(N);
        for(int i=0;i<N;i++){ auto&s=sigv[i]; s[0]=color[i]; for(int k=0;k<dnN[i];k++) s[1+k]=dn[i][k]; for(int k=0;k<uvN[i];k++) s[1+MYN+k]=uv[i][k]; for(int k=dnN[i];k<MYN;k++) s[1+k]=7777; for(int k=uvN[i];k<MYN;k++) s[1+MYN+k]=7777; }
        std::vector<std::array<int,2*MYN+1>> sorted=sigv;
        std::sort(sorted.begin(),sorted.end());
        sorted.erase(std::unique(sorted.begin(),sorted.end()),sorted.end());
        for(int i=0;i<N;i++) ncolor[i]=std::lower_bound(sorted.begin(),sorted.end(),sigv[i])-sorted.begin();
        bool same=true; for(int i=0;i<N;i++) if(ncolor[i]!=color[i]){same=false;break;}
        if(same) break;
        for(int i=0;i<N;i++) color[i]=ncolor[i];
    }
    // color classes
    std::vector<std::vector<int>> groups;
    { std::vector<std::pair<int,int>> v; for(int i=0;i<N;i++) v.push_back({color[i],i});
      std::sort(v.begin(),v.end());
      for(int i=0;i<N;i++){ if(groups.empty()||color[v[i].second]!=color[groups.back()[0]]) groups.push_back({}); groups.back().push_back(v[i].second); } }
    // product of permutations per group, min encoding (complete invariant:
    // every isomorphism preserves refined colors, so the admissible perm sets
    // of isomorphic inputs correspond bijectively and have equal minima)
    int perm[MYN]; for(int i=0;i<N;i++) perm[i]=i;
    Key best=~(Key)0; int bestPerm[MYN];
    std::function<void(int)> rec2 = [&](int g){
        if(g==(int)groups.size()){
            Key k=0;
            for(int a=0;a<N;a++){ uint16_t row=0; uint16_t src=in[perm[a]];
                for(int b=0;b<N;b++) if(src>>perm[b]&1) row|=1u<<b;
                k|=((Key)row)<<(N*a); }
            if(k<best){ best=k; for(int i=0;i<N;i++) bestPerm[i]=perm[i]; }
            return;
        }
        std::vector<int> saved;
        for(int e:groups[g]) saved.push_back(perm[e]);
        std::vector<int> gE=groups[g]; std::sort(gE.begin(),gE.end());
        do{
            int idx=0; for(int e:groups[g]) perm[e]=gE[idx++];
            rec2(g+1);
            int j=0; for(int e:groups[g]) perm[e]=saved[j++]; // restore before next perm? not needed but harmless
        }while(std::next_permutation(gE.begin(),gE.end()));
    };
    rec2(0);
    keyOut=best;
    for(int a=0;a<N;a++){ uint16_t row=0; uint16_t src=in[bestPerm[a]];
        for(int b=0;b<N;b++) if(src>>bestPerm[b]&1) row|=1u<<b;
        rows[a]=row; }
}

struct CertOut { std::vector<std::pair<int,int>> cpairs; };
static void solveOne(const uint16_t in[MYN], int& Fo, int& Ho){
    uint16_t up[MYN]; Key key;
    canon_key_rows(in,key,up);
    // memo lookup (children levels already final; duplicates within level recompute harmlessly)
    { auto it=memo.find(key); if(it!=memo.end()){ Fo=it->second.first; Ho=it->second.second; return; } }
    for(int i=0;i<N;i++) tdown[i]=0;
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(up[i]>>j&1) tdown[j]|=1u<<i;
    std::vector<std::pair<int,int>> pairs;
    for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(!(up[i]>>j&1)&&!(up[j]>>i&1)) pairs.push_back({i,j});
    if(pairs.empty()){ memo[key]={0,0}; Fo=0; Ho=0; return; }
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
    for(auto pr:pairs){ int x=pr.first,y=pr.second; uint16_t t[MYN],c1[MYN],c2[MYN]; Key k1,k2; int f1,f2,h1,h2;
        if(addRel(up,x,y,t)){ canon_key_rows(t,k1,c1); auto it=memo.find(k1); if(it!=memo.end()){f1=it->second.first;h1=it->second.second;} else {f1=h1=INF;} } else {f1=h1=INF;}
        if(addRel(up,y,x,t)){ canon_key_rows(t,k2,c2); auto it=memo.find(k2); if(it!=memo.end()){f2=it->second.first;h2=it->second.second;} else {f2=h2=INF;} } else {f2=h2=INF;}
        bestF=std::min(bestF,1+std::max(f1,f2)); }
    int bestH=INF;
    for(auto pr:cpairs){ int x=pr.first,y=pr.second; uint16_t t[MYN],c1[MYN],c2[MYN]; Key k1,k2; int h1,h2;
        if(addRel(up,x,y,t)){ canon_key_rows(t,k1,c1); auto it=memo.find(k1); if(it!=memo.end()){h1=it->second.second;} else h1=INF; } else h1=INF;
        if(addRel(up,y,x,t)){ canon_key_rows(t,k2,c2); auto it=memo.find(k2); if(it!=memo.end()){h2=it->second.second;} else h2=INF; } else h2=INF;
        bestH=std::min(bestH,1+std::max(h1,h2)); }
    memo[key]={bestF,bestH}; Fo=bestF; Ho=bestH;
}

int main(int argc,char**argv){
    if(argc<4){ fprintf(stderr,"usage: abcppar pN.txt out nthreads\n"); return 1; }
    FILE* f=fopen(argv[1],"r"); if(!f){perror("open");return 1;}
    if(fscanf(f,"%d",&N)!=1) return 1;
    std::vector<std::array<uint16_t,MYN>> roots;
    for(;;){ std::array<uint16_t,MYN> a{}; int ok=1; for(int i=0;i<N;i++){ long long v; if(fscanf(f,"%lld",&v)!=1){ok=0;break;} a[i]=(uint16_t)v; } if(!ok) break; roots.push_back(a); }
    fclose(f);
    fprintf(stderr,"n=%d roots=%zu\n",N,roots.size());
    int nthreads=atoi(argv[3]);
    // group by relation count
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
            size_t i;
            while((i=cursor.fetch_add(1))<v.size()){
                int r=v[i]; int Fo,Ho;
                solveOne(roots[r].data(),Fo,Ho);
                Fr[r]=Fo; Hr[r]=Ho;
            }
        });
        for(auto&t:th) t.join();
        doneLevels++;
        if(doneLevels%50==0||L%10==0){ auto el=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
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
