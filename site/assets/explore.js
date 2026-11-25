/* The explorer is a static client, with no analytics or external requests. */
(() => {
  "use strict";
  const $ = id => document.getElementById(id);
  const form=$("search-form"), query=$("query"), kind=$("kind"), topic=$("topic"), status=$("status"), evidence=$("evidence"), sort=$("sort");
  const list=$("results-list"), count=$("result-count"), pageCount=$("page-count"), prev=$("prev"), next=$("next");
  const names={result:"Curated result",guide:"Reading guide",front:"Research front",board:"Board message",source:"Source file",session:"Agent report",commission:"Task commission",mixed:"Cross-project report",github:"GitHub discussion",patch:"Commit patch",workspace:"Workspace",scratch:"Scratch reference",label:"Historical label"};
  const evidenceNames={formal:"Lean kernel theorem",literature:"Literature baseline",argument:"Paper / algorithm argument",structural:"Historical structural deduction",finite:"Finite computational evidence",conditional:"Conditional argument",corrected:"Corrected proof scope"};
  let records, manifest, generation=0, timer, currentPage=1, match={ids:[],terms:[]};
  const cache = new Map(), pageSize=25;
  function el(tag, text, cls) {
    const node=document.createElement(tag);
    if(text!==undefined)node.textContent=text;
    if(cls)node.className=cls;
    return node;
  }
  function safeURL(path) {
    if(typeof path!=="string")return "#";
    if(path.startsWith("https://github.com/ottojung/soringp1/"))return path;
    if(/^[a-z0-9_][a-z0-9_./-]*\.html$/i.test(path) && !path.split("/").includes(".."))return path;
    return "#";
  }
  function anchor(url,text,cls) {
    const a=el("a",text,cls);a.href=safeURL(url);return a;
  }
  function highlight(node,text,terms) {
    if(!text)return;
    const visibleTerms=terms.filter(t=>t.length>1);
    if(!visibleTerms.length){node.textContent=text;return;}
    const pattern=new RegExp(visibleTerms.slice(0,16).sort((a,b)=>b.length-a.length).join("|"),"gi");
    let start=0;
    for(const m of text.matchAll(pattern)) {
      node.append(document.createTextNode(text.slice(start,m.index)),el("mark",m[0]));
      start=m.index+m[0].length;
    }
    node.append(document.createTextNode(text.slice(start)));
  }
  function filters(){return {kind:kind.value,topic:topic.value,status:status.value,evidence:evidence.value,sort:sort.value};}
  function syncURL(push=false) {
    const params=new URLSearchParams();
    if(query.value.trim())params.set("q",query.value.trim());
    for(const [k,v] of Object.entries(filters()))if(v && !(k==="sort" && v==="relevance"))params.set(k,v);
    if(currentPage>1)params.set("page",String(currentPage));
    const url=location.pathname+(params.toString()?"?"+params:"");
    if(url!==location.pathname+location.search)history[push?"pushState":"replaceState"]({}, "",url);
  }
  function loadURL() {
    const p=new URLSearchParams(location.search);
    query.value=p.get("q")||"";
    for(const control of [kind,topic,status,evidence,sort]) {
      const v=p.get(control.id);
      control.value=v && [...control.options].some(o=>o.value===v)?v:(control.id==="sort"?"relevance":"");
    }
    currentPage=Math.max(1,Number.parseInt(p.get("page"),10)||1);
  }
  async function json(url) {
    const r=await fetch(url);
    if(!r.ok)throw new Error("Could not load "+url);
    return r.json();
  }
  function shard(name){
    if(!cache.has(name))cache.set(name,json("search/"+name+".json").catch(err=>{cache.delete(name);throw err;}));
    return cache.get(name);
  }
  function render(){
    const total=match.ids.length,pages=Math.max(1,Math.ceil(total/pageSize));
    currentPage=Math.min(currentPage,pages);
    list.replaceChildren();
    count.textContent=total.toLocaleString()+" "+(total===1?"result":"results")+(match.prefix?" (prefix matches)":"");
    pageCount.textContent=total?"Page "+currentPage+" of "+pages:"";
    prev.disabled=currentPage===1;next.disabled=currentPage>=pages;
    if(!total){
      const box=el("div",undefined,"note");
      box.append(el("strong","No matching records."),el("p","Try fewer words, a broader term, or clear the collection and topic filters."));
      list.append(box);return;
    }
    const fragment=document.createDocumentFragment();
    for(const i of match.ids.slice((currentPage-1)*pageSize,currentPage*pageSize)){
      const r=records[i],item=el("article",undefined,"result"),meta=el("div",undefined,"result-meta");
      meta.append(el("span",names[r.kind]||r.kind,"pill"));
      if(r.evidence)meta.append(el("span",evidenceNames[r.evidence]||r.evidence,"pill accent"));
      if(r.status)meta.append(el("span",r.status==="review"?"Historical verdict marker":r.status,"pill"));
      if(r.date)meta.append(el("span",r.date.slice(0,10)));
      if(r.topics?.length)meta.append(el("span",r.topics.join(" · ")));
      const heading=el("h3"),a=anchor(r.url||r.source,"");
      highlight(a,r.title,match.terms);heading.append(a);
      const summary=el("p");highlight(summary,r.summary||"",match.terms);
      item.append(meta,heading,summary);
      if(r.outcome){
        const detail=el("p");detail.append(el("strong","Historical reported outcome: "));
        const span=el("span");highlight(span,r.outcome,match.terms);detail.append(span);item.append(detail);
      }
      item.append(anchor(r.source,"Original evidence on GitHub"));
      fragment.append(item);
    }
    list.append(fragment);
  }
  async function search({reset=true,push=false}={}){
    if(!records || !manifest)return;
    const own=++generation;
    if(reset)currentPage=1;
    count.textContent="Searching…";prev.disabled=true;next.disabled=true;
    try{
      const result=await SoringSearch.find(records,manifest,query.value,filters(),shard);
      if(own!==generation)return;
      match=result;render();syncURL(push);
    }catch(e){
      if(own!==generation)return;
      count.textContent="Search could not load.";
      list.replaceChildren(el("p","The static search index could not be loaded. Reload or browse the topic and collection indexes.","note"));
    }
  }
  form.addEventListener("submit",e=>{e.preventDefault();clearTimeout(timer);search({push:true});});
  query.addEventListener("input",()=>{clearTimeout(timer);timer=setTimeout(()=>search(),250);});
  for(const control of [kind,topic,status,evidence,sort])control.addEventListener("change",()=>search({push:true}));
  $("clear").addEventListener("click",()=>{query.value="";kind.value="";topic.value="";status.value="";evidence.value="";sort.value="relevance";search({push:true});query.focus();});
  prev.addEventListener("click",()=>{currentPage--;render();syncURL(true);count.scrollIntoView({block:"start"});});
  next.addEventListener("click",()=>{currentPage++;render();syncURL(true);count.scrollIntoView({block:"start"});});
  window.addEventListener("popstate",()=>{loadURL();search({reset:false});});
  document.addEventListener("keydown",e=>{
    const editing=/^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName)||document.activeElement?.isContentEditable;
    if((e.key==="/"&&!editing)||((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==="k")){e.preventDefault();query.focus();}
    if(e.key==="Escape"&&document.activeElement===query)query.blur();
  });
  loadURL();
  Promise.all([json("search/records.json"),json("search/manifest.json")]).then(([r,m])=>{
    records=r;manifest=m;search({reset:false});
  }).catch(()=>{
    count.textContent="Search index unavailable.";
    list.replaceChildren(el("p","Reload this page or use the topic and collection indexes. The rest of the site works without the search index.","note"));
  });
})();
