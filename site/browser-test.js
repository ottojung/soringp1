/* Browser smoke tests for the deployed site or a local static HTTP preview.
   Node 24+, Chromium, no npm packages. A fresh disposable browser profile
   is used; no account session or existing browser profile is accessed. */
"use strict";
const fs=require("node:fs");
const path=require("node:path");
const os=require("node:os");
const {spawn}=require("node:child_process");
const assert=require("node:assert/strict");
const dir=fs.mkdtempSync(path.join(os.tmpdir(),"soring-browser-"));
const profile=path.join(dir,"profile");
const base=(process.env.SORING_SITE_URL||"https://ottojung.github.io/soringp1/").replace(/\/?$/,"/");
const screenshotDir=process.env.SORING_SCREENSHOTS;
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
const args=["--headless","--disable-gpu","--disable-dev-shm-usage","--no-first-run","--no-default-browser-check","--disable-background-networking","--remote-debugging-port=0","--remote-debugging-address=127.0.0.1","--user-data-dir="+profile,"about:blank"];
if(process.env.CHROMIUM_NO_SANDBOX==="1")args.unshift("--no-sandbox");
const child=spawn(process.env.CHROMIUM||"chromium",args,{stdio:["ignore","ignore",fs.openSync(path.join(dir,"chromium.log"),"w")]});
let ws,nextID=0;
const pending=new Map(),errors=[];
let startupError;
child.on("error",e=>{startupError=e;});
async function waitFor(fn,timeout=45000){
  const end=Date.now()+timeout;
  while(Date.now()<end){
    if(startupError)throw startupError;
    try{const value=await fn();if(value)return value;}catch{}
    await sleep(200);
  }
  throw Error("Timed out waiting for browser state: "+String(fn).slice(0,150));
}
function send(method,params={}){
  const id=++nextID;
  return new Promise((resolve,reject)=>{
    const timer=setTimeout(()=>{pending.delete(id);reject(Error("CDP timeout: "+method));},45000);
    pending.set(id,{resolve:r=>{clearTimeout(timer);resolve(r);},reject:e=>{clearTimeout(timer);reject(e);}});
    ws.send(JSON.stringify({id,method,params}));
  });
}
async function evaluate(expression){
  const r=await send("Runtime.evaluate",{expression,returnByValue:true,awaitPromise:true});
  if(r.exceptionDetails)throw Error("Page JS exception: "+JSON.stringify(r.exceptionDetails).slice(0,300));
  return r.result.value;
}
async function navigate(url,ready){
  await send("Page.navigate",{url});
  await waitFor(()=>evaluate("document.readyState==='complete' && location.href.startsWith("+JSON.stringify(url.split("?")[0])+")"));
  if(ready)await waitFor(()=>evaluate(ready),90000);
}
async function metrics(width,height,mobile=false){
  await send("Emulation.setDeviceMetricsOverride",{width,height,deviceScaleFactor:1,mobile});
}
async function screenshot(name){
  if(!screenshotDir)return;
  fs.mkdirSync(screenshotDir,{recursive:true});
  const r=await send("Page.captureScreenshot",{format:"png",captureBeyondViewport:false});
  fs.writeFileSync(path.join(screenshotDir,name),Buffer.from(r.data,"base64"));
}
async function layout(label){
  const m=await evaluate("({w:innerWidth,scroll:document.documentElement.scrollWidth,h:innerHeight,title:document.querySelector('h1')?.textContent})");
  console.log(label,m);
  assert(m.scroll<=m.w+2,"horizontal overflow "+label);
  return m;
}
const resultsReady="/^[0-9,]+ results?/.test(document.getElementById('result-count')?.textContent||'')";
(async()=>{
  const port=await waitFor(()=>{
    const p=path.join(profile,"DevToolsActivePort");
    return fs.existsSync(p)?fs.readFileSync(p,"utf8").split("\n")[0]:null;
  });
  const tabs=await (await fetch("http://127.0.0.1:"+port+"/json/list")).json();
  ws=new WebSocket(tabs.find(t=>t.type==="page").webSocketDebuggerUrl);
  await new Promise((r,j)=>{ws.addEventListener("open",r,{once:true});ws.addEventListener("error",j,{once:true});});
  ws.addEventListener("message",event=>{
    const m=JSON.parse(event.data);
    if(m.id&&pending.has(m.id)){const p=pending.get(m.id);pending.delete(m.id);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result||{});}
    if(m.method==="Runtime.exceptionThrown")errors.push(m.params.exceptionDetails.text+" "+m.params.exceptionDetails.exception?.description);
  });
  await send("Page.enable");await send("Runtime.enable");
  await metrics(1440,1000);
  await navigate(base);
  assert((await layout("Desktop homepage")).title.includes("Understanding optimal sorting"));
  await screenshot("home-desktop.png");
  await navigate(base+"explore.html?q=cospectral+minimax&kind=front",resultsReady);
  const hit=await evaluate("({count:document.getElementById('result-count').textContent,items:document.querySelectorAll('#results-list article').length,first:document.querySelector('#results-list h3')?.textContent})");
  console.log("Live search:",hit);assert(hit.items>0);await screenshot("search-desktop.png");
  await navigate(base+"explore.html?q=cospectral-gap-span-alln&kind=front","document.querySelector('#results-list h3')?.textContent==='cospectral-gap-span-alln'");
  await evaluate("document.getElementById('query').value='';document.getElementById('status').value='blocked';document.getElementById('status').dispatchEvent(new Event('change'));true");
  await waitFor(()=>evaluate("document.getElementById('result-count').textContent==='33 results'"));
  assert.equal(await evaluate("document.querySelectorAll('#results-list article').length"),25);
  await evaluate("document.getElementById('next').click();true");
  await waitFor(()=>evaluate("document.getElementById('page-count').textContent==='Page 2 of 2'"));
  assert.equal(await evaluate("document.querySelectorAll('#results-list article').length"),8);
  console.log("Blocked filter and pagination passed");
  await evaluate("document.getElementById('query').value='cospectral';document.getElementById('clear').click();true");
  assert.equal(await evaluate("document.getElementById('query').value"),"cospectral");
  await evaluate("document.getElementById('query').value='';document.getElementById('evidence').value='formal';document.getElementById('evidence').dispatchEvent(new Event('change'));true");
  await waitFor(()=>evaluate("document.getElementById('result-count').textContent==='2 results'"));
  assert.equal(await evaluate("document.querySelectorAll('#results-list article').length"),2);
  console.log("Formal evidence filter and query-preserving clear passed");
  await evaluate("document.activeElement.blur();document.dispatchEvent(new KeyboardEvent('keydown',{key:'/',bubbles:true}));true");
  assert.equal(await evaluate("document.activeElement.id"),"query");
  await navigate(base+"results/index.html");await layout("Desktop results");await screenshot("results-desktop.png");
  await metrics(390,844,true);await send("Emulation.setEmulatedMedia",{features:[{name:"prefers-color-scheme",value:"dark"}]});
  await navigate(base);await layout("Mobile dark homepage");await screenshot("home-mobile-dark.png");
  await navigate(base+"explore.html?q=cospectral+minimax&kind=front",resultsReady);
  await layout("Mobile dark search");
  assert.equal(await evaluate("document.getElementById('filter-fields').hidden"),true);
  assert(await evaluate("document.querySelector('#results-list article').getBoundingClientRect().top<innerHeight"),"first mobile search result should be visible without scrolling");
  await screenshot("search-mobile-dark.png");
  await evaluate("document.getElementById('filter-toggle').click();true");
  assert.equal(await evaluate("document.getElementById('filter-fields').hidden"),false);
  await evaluate("document.getElementById('filter-toggle').click();true");
  assert.equal(await evaluate("document.getElementById('filter-fields').hidden"),true);
  await navigate(base+"fronts/cospectral-gap-span-alln.html");
  await layout("Mobile front");
  assert(await evaluate("document.querySelector('.article').getBoundingClientRect().top<document.querySelector('.sidebar').getBoundingClientRect().top"));
  assert(await evaluate("document.querySelector('.front-summary').getBoundingClientRect().top<innerHeight"));
  await screenshot("front-mobile-dark.png");
  const boardLink=await evaluate("[...document.querySelectorAll('.sidebar a')].find(a=>a.href.includes('/board/'))?.href");
  assert(boardLink);await navigate(boardLink);await layout("Mobile board");
  assert(await evaluate("[...document.querySelectorAll('.sidebar a')].some(a=>['Earlier message','Later message'].includes(a.textContent))"));
  assert.equal(errors.length,0,errors.join("; "));
  console.log("LIVE BROWSER CHECKS PASSED; JavaScript exceptions:",errors.length);
})().catch(e=>{console.error(e);process.exitCode=1;}).finally(async()=>{
  if(ws)ws.close();
  child.kill("SIGTERM");
  await Promise.race([new Promise(r=>child.once("exit",r)),sleep(2000)]);
  fs.rmSync(dir,{recursive:true,force:true});
});
