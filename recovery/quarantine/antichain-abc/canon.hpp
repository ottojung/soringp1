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

