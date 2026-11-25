/* Pure search functions shared by the browser and Node regression tests. */
(function (root) {
  "use strict";
  function tokenize(text, manifest) {
    const stop = new Set(manifest.stop), single = new Set(manifest.single);
    return [...new Set((text.toLowerCase().match(/[a-z0-9]+/g) || []).filter(
      t => !stop.has(t) && (t.length > 1 || single.has(t)) &&
        t.length <= 48 && !(/^\d+$/.test(t) && t.length > 8)
    ))].slice(0, 16);
  }
  function intersection(a, b) {
    const result = [];
    let i = 0, j = 0;
    while (i < a.length && j < b.length) {
      if (a[i] === b[j]) { result.push(a[i]); i++; j++; }
      else if (a[i] < b[j]) i++;
      else j++;
    }
    return result;
  }
  function union(lists) {
    const out = new Set();
    for (const list of lists) for (const id of list) out.add(id);
    return [...out].sort((a,b) => a-b);
  }
  function metadata(record) {
    return [record.title, record.summary, record.outcome, record.source,
      record.status, record.evidence, record.date, ...(record.topics || [])].filter(Boolean).join(" ").toLowerCase();
  }
  function rank(record, terms, raw) {
    const title = record.title.toLowerCase();
    const summary = (record.summary || "").toLowerCase();
    const outcome = (record.outcome || "").toLowerCase();
    let score = record.kind === "guide" ? 7 : record.kind === "front" ? 5 : 0;
    if (raw && title === raw) score += 120;
    if (raw && title.includes(raw)) score += 35;
    for (const t of terms) {
      if (title.includes(t)) score += 14;
      if (summary.includes(t)) score += 5;
      if (outcome.includes(t)) score += 3;
      if ((record.topics || []).some(x => x.toLowerCase().includes(t))) score += 2;
    }
    return score;
  }
  async function find(records, manifest, query, filters, loadShard) {
    const raw = query.trim().toLowerCase(), terms = tokenize(raw, manifest);
    const known = new Set(manifest.shards);
    let ids, prefix = false;
    if (terms.length) {
      const groups = await Promise.all(terms.map(async t => {
        if (!known.has(t.slice(0,2))) return [];
        const shard = await loadShard(t.slice(0,2));
        return shard[t] || [];
      }));
      ids = groups.sort((a,b) => a.length-b.length).reduce(intersection);
      if (!ids.length) {
        // Prefix matching only when the exact-token query has no results.
        const expanded = await Promise.all(terms.map(async t => {
          if (!known.has(t.slice(0,2))) return [];
          const shard = await loadShard(t.slice(0,2));
          if (shard[t]) return shard[t];
          if (t.length < 3) return [];
          return union(Object.keys(shard).filter(k => k.startsWith(t)).slice(0,80).map(k => shard[k]));
        }));
        ids = expanded.sort((a,b) => a.length-b.length).reduce(intersection);
        prefix = ids.length > 0;
      }
    } else {
      ids = records.map((_,i) => i);
      if (raw) ids = ids.filter(i => metadata(records[i]).includes(raw));
    }
    ids = ids.filter(i => {
      const r=records[i];
      return (!filters.kind || r.kind===filters.kind) &&
        (!filters.topic || (r.topics||[]).includes(filters.topic)) &&
        (!filters.status || r.status===filters.status) &&
        (!filters.evidence || r.evidence===filters.evidence);
    });
    if (filters.sort==="title") ids.sort((a,b)=>records[a].title.localeCompare(records[b].title));
    else if (filters.sort==="newest") ids.sort((a,b)=>(records[b].date||"").localeCompare(records[a].date||"") || a-b);
    else if (raw) {
      const scores=new Map(ids.map(i=>[i,rank(records[i],terms,raw)]));
      ids.sort((a,b)=>scores.get(b)-scores.get(a)||a-b);
    }
    return {ids,terms,prefix};
  }
  const api={tokenize,intersection,union,rank,find};
  if (typeof module!=="undefined" && module.exports) module.exports=api;
  else root.SoringSearch=api;
})(globalThis);
