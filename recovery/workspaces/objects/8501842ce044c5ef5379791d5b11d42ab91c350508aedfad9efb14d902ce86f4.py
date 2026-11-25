#!/usr/bin/env python3
"""Viche Post: durable institutional correspondence and opt-in Gazette.

Transport is NOT authority: all sender labels are claims on a shared Unix UID.
No message constitutes a ballot, Founder instruction, or independently verified fact.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
import time
import uuid

NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$")
TOPIC = re.compile(r"^[a-z][a-z0-9/-]{0,127}$")
KINDS = ("letter", "request", "observation", "forecast", "scenario",
         "strategy", "intervention", "founder-inference", "report")
SCHEMA = """
CREATE TABLE IF NOT EXISTS messages(
  id TEXT PRIMARY KEY, channel TEXT NOT NULL CHECK(channel IN ('mail','gazette')),
  sender TEXT NOT NULL, recipient TEXT, topic TEXT, kind TEXT NOT NULL,
  subject TEXT NOT NULL, body TEXT NOT NULL, created_at INTEGER NOT NULL,
  idempotency_key TEXT, caused_by TEXT REFERENCES messages(id),
  chain_depth INTEGER NOT NULL, priority TEXT NOT NULL,
  sources TEXT NOT NULL, based_on TEXT NOT NULL, conditions TEXT NOT NULL,
  baseline TEXT NOT NULL, resolution_rule TEXT NOT NULL, alternative TEXT NOT NULL,
  UNIQUE(sender,idempotency_key));
CREATE TABLE IF NOT EXISTS deliveries(
  message_id TEXT NOT NULL REFERENCES messages(id), recipient TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('new','read','acknowledged','resolved')),
  alert INTEGER NOT NULL, created_at INTEGER NOT NULL, read_at INTEGER,
  ack_at INTEGER, resolved_at INTEGER, resolution TEXT,
  PRIMARY KEY(message_id,recipient));
CREATE TABLE IF NOT EXISTS subscriptions(
  subscriber TEXT NOT NULL, topic TEXT NOT NULL, mode TEXT NOT NULL
  CHECK(mode IN ('digest','alert')), created_at INTEGER NOT NULL,
  PRIMARY KEY(subscriber,topic));
CREATE TABLE IF NOT EXISTS events(
  event_id INTEGER PRIMARY KEY AUTOINCREMENT, at INTEGER NOT NULL,
  actor TEXT NOT NULL, action TEXT NOT NULL, message_id TEXT, details TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS msg_channel_topic ON messages(channel,topic,created_at);
CREATE INDEX IF NOT EXISTS delivery_inbox ON deliveries(recipient,status,created_at);
CREATE TRIGGER IF NOT EXISTS immutable_messages_update BEFORE UPDATE ON messages
BEGIN SELECT RAISE(ABORT,'message content is immutable'); END;
CREATE TRIGGER IF NOT EXISTS immutable_messages_delete BEFORE DELETE ON messages
BEGIN SELECT RAISE(ABORT,'message deletion is forbidden'); END;
CREATE TRIGGER IF NOT EXISTS immutable_events_update BEFORE UPDATE ON events
BEGIN SELECT RAISE(ABORT,'event history is immutable'); END;
CREATE TRIGGER IF NOT EXISTS immutable_events_delete BEFORE DELETE ON events
BEGIN SELECT RAISE(ABORT,'event history deletion is forbidden'); END;
"""

def clock():
    return int(time.time())

def location():
    return Path(os.environ.get("VICHE_POST_DB",
         str(Path(os.environ.get("VICHE_STATE_ROOT", "/var/lib/lubko/wd/viche-state"))
             / "post" / "post.sqlite3")))

def connect():
    path = location()
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    db = sqlite3.connect(str(path), timeout=15)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    db.execute("PRAGMA busy_timeout=15000")
    db.execute("PRAGMA journal_mode=WAL")
    db.execute("PRAGMA synchronous=FULL")
    db.executescript(SCHEMA)
    return db

def event(db, actor, action, message_id=None, **details):
    db.execute("INSERT INTO events(at,actor,action,message_id,details) VALUES(?,?,?,?,?)",
               (clock(),actor,action,message_id,json.dumps(details,sort_keys=True)))

def valid_name(value):
    if not NAME.fullmatch(value):
        raise ValueError("invalid institutional identity: " + str(value))
    return value

def valid_topic(value):
    if not TOPIC.fullmatch(value) or "//" in value or value.endswith("/"):
        raise ValueError("invalid Gazette topic: " + str(value))
    return value

def output(obj):
    print(json.dumps(obj,sort_keys=True,ensure_ascii=False))

def msg_dict(row):
    result = dict(row)
    for key in ("sources","based_on"):
        result[key] = json.loads(result[key])
    result["sender_authenticated"]=False
    result["confidential"]=False
    return result

def source_roots(db, message_id, visited=None):
    """Union original cited sources; never count repeated summaries as new evidence."""
    seen = visited if visited is not None else set()
    if message_id in seen:
        return set()
    seen.add(message_id)
    row = db.execute("SELECT sources,based_on FROM messages WHERE id=?",
                     (message_id,)).fetchone()
    if row is None:
        raise ValueError("unknown source message " + message_id)
    roots = set(json.loads(row["sources"]))
    for parent in json.loads(row["based_on"]):
        roots.update(source_roots(db,parent,seen))
    return roots

def verify_committed_act22(sources, proposition):
    """A scoreable forecast must cite its exact committed, hashed registration.

    Even this is not proof of independently observed resolution; the existing
    Act 22 resolver/scorer remains responsible for that separate judgment.
    """
    import subprocess
    ids=[s[6:] for s in sources if s.startswith("act22:")]
    if not ids:
        return False
    town=Path(os.environ.get("VICHE_TOWN_ROOT",
               "/var/lib/lubko/wd/viche"))
    try:
        result=subprocess.run(
            ["git","-C",str(town),"show","HEAD:records/predictions/ledger.json"],
            check=True,capture_output=True,text=True,timeout=15)
        data=json.loads(result.stdout)
    except (OSError,ValueError,subprocess.SubprocessError):
        return False
    for entry in data.get("entries",[]):
        if (entry.get("id") not in ids or entry.get("kind")!="registration"
                or entry.get("proposition")!=proposition
                or int(entry.get("registered_at",0))>clock()):
            continue
        fields=("bill_id","proposition","probability","resolution_date",
                "evidence_source","author","registered_at")
        canon={k:entry.get(k) for k in fields}
        blob=json.dumps(canon,sort_keys=True,separators=(",",":")).encode()
        digest="sha256:"+hashlib.sha256(blob).hexdigest()
        if entry.get("content_hash")==digest:
            return True
    return False

def publish(db, args):
    sender = valid_name(args.sender)
    if args.command == "send" and not args.public:
        raise ValueError("addressed correspondence is PUBLIC; explicitly pass --public")
    recipient = valid_name(args.to) if args.command == "send" else None
    topic = valid_topic(args.topic) if args.command == "publish" else None
    channel = "mail" if recipient else "gazette"
    kind = args.kind
    text = Path(args.body_file).read_text() if args.body_file else args.body
    if not text or not args.subject.strip():
        raise ValueError("message subject and body are required")
    sources = sorted(set(args.source))
    based_on = sorted(set(args.based_on))
    if kind == "observation" and (not sources or not args.conditions):
        raise ValueError("observations require original sources and metric definition (--condition)")
    if kind == "forecast" and (not args.conditions or not args.baseline
        or not args.resolution_rule or not any(s.startswith("act22:") for s in sources)):
        raise ValueError("scoreable forecasts require conditions, baseline, resolution rule and Act 22 registration")
    if kind == "forecast" and not verify_committed_act22(sources,args.subject):
        raise ValueError("forecast must exactly match a hash-verified, committed Act 22 registration")
    if kind in ("scenario","report","strategy","intervention") and not (sources or based_on):
        raise ValueError("substantive publications require cited evidence or prior claims")
    if kind == "scenario" and (not args.conditions or not args.alternative):
        raise ValueError("scenarios require their assumptions and competing scenario")
    if kind == "intervention" and (not sources or not based_on or
        not args.conditions or not args.alternative):
        raise ValueError("interventions require action evidence, forecast/plan references and alternatives")
    if kind == "founder-inference" and (not sources or not args.alternative or not args.conditions):
        raise ValueError("Founder inferences require authorized sources, alternative explanation and observation context")
    if kind == "founder-inference" and not all(
        s.startswith("antonina:") or s.startswith("github:public:") for s in sources):
        raise ValueError("Founder inferences require publicly attributable Antonina/GitHub source identifiers")
    if kind == "strategy" and (not args.conditions or not args.alternative):
        raise ValueError("strategies require the proposed intervention and a baseline alternative")
    if kind == "request" and not recipient:
        raise ValueError("requests require a particular recipient, not Gazette broadcast")
    if len(sources)+len(based_on)>64:
        raise ValueError("too many provenance edges; publish a linked report")
    if len(text.encode())>1_000_000:
        raise ValueError("message exceeds 1 MiB; link a durable artifact instead")
    with db:
        db.execute("BEGIN IMMEDIATE")
        for ancestor in based_on:
            if not db.execute("SELECT 1 FROM messages WHERE id=?",(ancestor,)).fetchone():
                raise ValueError("unknown based-on reference "+ancestor)
        depth = 0
        if args.caused_by:
            row=db.execute("SELECT chain_depth FROM messages WHERE id=?",(args.caused_by,)).fetchone()
            if row is None:
                raise ValueError("unknown causal predecessor")
            depth=row["chain_depth"]+1
        if args.key:
            prior=db.execute("SELECT * FROM messages WHERE sender=? AND idempotency_key=?",
                             (sender,args.key)).fetchone()
            if prior:
                fingerprint = (channel, recipient,topic,kind,args.subject,text,
                               sources,based_on,args.conditions,args.baseline,
                               args.resolution_rule,args.alternative,args.caused_by,args.priority)
                old=(prior["channel"],prior["recipient"],prior["topic"],prior["kind"],
                     prior["subject"],prior["body"],json.loads(prior["sources"]),
                     json.loads(prior["based_on"]),prior["conditions"],prior["baseline"],
                     prior["resolution_rule"],prior["alternative"],prior["caused_by"],
                     prior["priority"])
                if fingerprint != old:
                    raise ValueError("idempotency-key reuse with different content")
                return {"id":prior["id"],"duplicate":True,"delivered":db.execute(
                    "SELECT COUNT(*) FROM deliveries WHERE message_id=?",(prior["id"],)).fetchone()[0]}
        mid=uuid.uuid4().hex
        now=clock()
        db.execute("""INSERT INTO messages VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                   (mid,channel,sender,recipient,topic,kind,args.subject,text,now,
                    args.key,args.caused_by,depth,args.priority,
                    json.dumps(sources),json.dumps(based_on),args.conditions,
                    args.baseline,args.resolution_rule,args.alternative))
        recipients=[(recipient,"direct")] if recipient else db.execute(
            "SELECT subscriber,mode FROM subscriptions WHERE topic=?",(topic,)).fetchall()
        delivered=0
        for item in recipients:
            office,mode=item
            # Alert is only an inbox-presentation hint. It never summons an AI
            # agent: unauthenticated mail must have no dispatch authority.
            alert=int((channel=="mail" and args.priority=="urgent") or
                      (channel=="gazette" and mode=="alert"))
            db.execute("""INSERT INTO deliveries(message_id,recipient,status,alert,created_at)
                          VALUES(?,?,'new',?,?)""",(mid,office,alert,now))
            delivered+=1
        event(db,sender,"sent" if recipient else "published",mid,
              destination=recipient or topic, delivered=delivered, causal_depth=depth)
    return {"id":mid,"duplicate":False,"delivered":delivered,"causal_depth":depth}

def subscriptions(db, args):
    subscriber=valid_name(args.office)
    topic=valid_topic(args.topic)
    with db:
        db.execute("BEGIN IMMEDIATE")
        existing=db.execute("SELECT mode FROM subscriptions WHERE subscriber=? AND topic=?",
                            (subscriber,topic)).fetchone()
        if args.command=="subscribe" and existing and existing["mode"]==args.mode:
            return {"office":subscriber,"topic":topic,"action":"unchanged"}
        if args.command=="unsubscribe" and not existing:
            return {"office":subscriber,"topic":topic,"action":"unchanged"}
        if args.command=="subscribe":
            db.execute("""INSERT INTO subscriptions(subscriber,topic,mode,created_at)
                          VALUES(?,?,?,?) ON CONFLICT(subscriber,topic)
                          DO UPDATE SET mode=excluded.mode""",
                       (subscriber,topic,args.mode,clock()))
            event(db,subscriber,"subscribe",topic=topic,mode=args.mode)
        else:
            db.execute("DELETE FROM subscriptions WHERE subscriber=? AND topic=?",
                       (subscriber,topic))
            event(db,subscriber,"unsubscribe",topic=topic)
    return {"office":subscriber,"topic":topic,"action":args.command}

def inbox(db, args):
    office=valid_name(args.office)
    statuses="AND d.status='new'" if args.new else ""
    rows=db.execute("""SELECT m.*, d.status,d.alert,d.ack_at,d.resolved_at,d.resolution
       FROM deliveries d JOIN messages m ON m.id=d.message_id
       WHERE d.recipient=? """+statuses+"""
       ORDER BY CASE
         WHEN m.channel='mail' AND d.status='new' THEN 0
         WHEN d.status='new' THEN 1 ELSE 2 END,
         m.created_at,m.id LIMIT ?""",(office,min(max(args.limit,1),200))).fetchall()
    return [msg_dict(row) for row in rows]

def feed(db,args):
    rows=db.execute("""SELECT * FROM messages WHERE channel='gazette'
      AND (?='' OR topic=?) ORDER BY created_at DESC,id DESC LIMIT ?""",
      (args.topic or "",args.topic or "",args.limit)).fetchall()
    return [msg_dict(r) for r in rows]

def transition(db,args):
    office=valid_name(args.office)
    # Serialize the status read with the update. Previously a late "read"
    # could overwrite a concurrent "acknowledged" or "resolved" receipt.
    db.execute("BEGIN IMMEDIATE")
    row=db.execute("SELECT status FROM deliveries WHERE message_id=? AND recipient=?",
                   (args.id,office)).fetchone()
    if row is None:
        raise ValueError("message not delivered to office")
    status=row["status"]
    steps=["new","read","acknowledged","resolved"]
    requested={"read":"read","ack":"acknowledged","resolve":"resolved"}[args.command]
    if steps.index(requested)<steps.index(status):
        return {"id":args.id,"status":status,"already_advanced":True}
    if requested=="resolved" and not args.reason:
        raise ValueError("resolutions require a reason; not proof of task success")
    if requested==status:
        return {"id":args.id,"status":status,"duplicate":True}
    at=clock()
    with db:
        if requested=="read":
            db.execute("UPDATE deliveries SET status='read',read_at=? WHERE message_id=? AND recipient=?",
                       (at,args.id,office))
        elif requested=="acknowledged":
            db.execute("""UPDATE deliveries SET status='acknowledged',read_at=COALESCE(read_at,?),
                          ack_at=? WHERE message_id=? AND recipient=?""",
                       (at,at,args.id,office))
        else:
            db.execute("""UPDATE deliveries SET status='resolved',read_at=COALESCE(read_at,?),
              ack_at=COALESCE(ack_at,?),resolved_at=?,resolution=?
              WHERE message_id=? AND recipient=?""",
              (at,at,at,args.reason,args.id,office))
        event(db,office,requested,args.id,reason=getattr(args,"reason",""))
    return {"id":args.id,"status":requested}

def wake(db,args):
    office=valid_name(args.office)
    # Compatibility with older dispatch runners, intentionally CONSTANT.
    # Mail cannot authenticate senders on the shared Unix UID. Consequently
    # no correspondence is permitted to cause an automatic model dispatch.
    # Agents inspect inbox during their regularly scheduled working sessions.
    return {"office":office,"urgent_unread":0,
            "fingerprint":hashlib.sha256(b"").hexdigest(),
            "ids":[],"automatic_dispatch":False,
            "reason":"public untrusted correspondence cannot awaken agents"}

def health(db,args):
    check=db.execute("PRAGMA integrity_check").fetchone()[0]
    counts={row[0]:row[1] for row in db.execute(
        "SELECT status,COUNT(*) FROM deliveries GROUP BY status")}
    pubs=db.execute("SELECT COUNT(*) FROM messages WHERE channel='gazette'").fetchone()[0]
    msg=db.execute("SELECT COUNT(*) FROM messages").fetchone()[0]
    pending=db.execute("""SELECT MIN(created_at) FROM deliveries
       WHERE status IN ('new','read','acknowledged')""").fetchone()[0]
    return {"healthy":check=="ok","integrity":check,"messages":msg,
            "publications":pubs,"delivery_status":counts,
            "oldest_unresolved_age_s":clock()-pending if pending else None,
            "db_bytes":location().stat().st_size,
            "public_correspondence":True,"sender_authentication":False,
            "mail_triggered_model_dispatch":False,
            "receipt_status_is_authoritative":False}
def lineage(db,args):
    roots=sorted(source_roots(db,args.id))
    return {"message_id":args.id,"distinct_cited_source_ids":roots,
            "count":len(roots),"caveat":"Distinct IDs are not independently verified observations"}

def thread(db,args):
    row=db.execute("SELECT id,caused_by FROM messages WHERE id=?",(args.id,)).fetchone()
    if row is None: raise ValueError("unknown message")
    while row["caused_by"]:
        row=db.execute("SELECT id,caused_by FROM messages WHERE id=?",
                       (row["caused_by"],)).fetchone()
        if row is None: raise ValueError("broken thread ancestry")
    root=row["id"]
    found=[];queue=[root];seen=set()
    while queue and len(found)<args.limit:
        mid=queue.pop(0)
        if mid in seen:continue
        seen.add(mid)
        r=db.execute("SELECT * FROM messages WHERE id=?",(mid,)).fetchone()
        if r: found.append(msg_dict(r))
        queue.extend(x[0] for x in db.execute(
            "SELECT id FROM messages WHERE caused_by=? ORDER BY created_at,id",(mid,)))
    return {"root_id":root,"messages":found,
            "truncated":bool(queue),"note":"Thread links do not establish evidence independence"}

def trace(db,args):
    row=db.execute("SELECT * FROM messages WHERE id=?",(args.id,)).fetchone()
    if row is None:raise ValueError("unknown message")
    deliveries=[dict(x) for x in db.execute(
        "SELECT * FROM deliveries WHERE message_id=? ORDER BY recipient",(args.id,))]
    events=[dict(x) for x in db.execute(
        "SELECT * FROM events WHERE message_id=? ORDER BY event_id",(args.id,))]
    return {"message":msg_dict(row),"deliveries":deliveries,
            "events":events,"lineage":lineage(db,args)}

def search(db,args):
    q="%"+args.text.replace("%",r"\%").replace("_",r"\_")+"%"
    rows=db.execute("SELECT * FROM messages WHERE "
       "(subject LIKE ? ESCAPE '\\' OR body LIKE ? ESCAPE '\\') "
       "ORDER BY created_at DESC,id DESC LIMIT ?",(q,q,args.limit)).fetchall()
    return [msg_dict(r) for r in rows]

def parser():
    p=argparse.ArgumentParser(description=__doc__)
    s=p.add_subparsers(dest="command",required=True)
    for action in ("send","publish"):
        q=s.add_parser(action)
        if action=="send":
            q.add_argument("--public",action="store_true",
                           help="acknowledge that addressed correspondence is PUBLIC")
        q.add_argument("--sender",required=True)
        q.add_argument("--to",required=action=="send")
        q.add_argument("--topic",required=action=="publish")
        q.add_argument("--kind",choices=KINDS,default="letter")
        q.add_argument("--subject",required=True)
        b=q.add_mutually_exclusive_group(required=True)
        b.add_argument("--body")
        b.add_argument("--body-file")
        q.add_argument("--key",help="idempotency key for retries")
        q.add_argument("--caused-by",help="predecessor message in causal chain")
        q.add_argument("--source",action="append",default=[],help="original evidence identifier")
        q.add_argument("--based-on",action="append",default=[],help="previous Post message ID")
        q.add_argument("--condition",dest="conditions",default="")
        q.add_argument("--baseline",default="")
        q.add_argument("--resolution-rule",default="")
        q.add_argument("--alternative",default="")
        q.add_argument("--priority",choices=("normal","urgent"),default="normal")
    for action in ("subscribe","unsubscribe"):
        q=s.add_parser(action);q.add_argument("--office",required=True)
        q.add_argument("--topic",required=True)
        if action=="subscribe": q.add_argument("--mode",choices=("digest","alert"),default="digest")
    q=s.add_parser("inbox");q.add_argument("--office",required=True)
    q.add_argument("--new",action="store_true");q.add_argument("--limit",type=int,default=50)
    q=s.add_parser("feed");q.add_argument("--topic",default="")
    q.add_argument("--limit",type=int,default=50)
    for action in ("read","ack","resolve"):
        q=s.add_parser(action);q.add_argument("--office",required=True);q.add_argument("--id",required=True)
        if action=="resolve":q.add_argument("--reason",required=True)
    q=s.add_parser("wake");q.add_argument("--office",required=True)
    q=s.add_parser("lineage");q.add_argument("--id",required=True)
    s.add_parser("health")
    for name in ("thread","trace"):
        q=s.add_parser(name);q.add_argument("--id",required=True)
        if name=="thread":q.add_argument("--limit",type=int,default=200)
    q=s.add_parser("search");q.add_argument("--text",required=True)
    q.add_argument("--limit",type=int,default=50)
    q=s.add_parser("backup");q.add_argument("--destination",required=True)
    return p

def main():
    args=parser().parse_args()
    db=connect()
    try:
        if args.command in ("send","publish"): result=publish(db,args)
        elif args.command in ("subscribe","unsubscribe"): result=subscriptions(db,args)
        elif args.command=="inbox": result=inbox(db,args)
        elif args.command=="feed": result=feed(db,args)
        elif args.command in ("read","ack","resolve"): result=transition(db,args)
        elif args.command=="wake": result=wake(db,args)
        elif args.command=="lineage": result=lineage(db,args)
        elif args.command=="health": result=health(db,args)
        elif args.command=="thread": result=thread(db,args)
        elif args.command=="trace": result=trace(db,args)
        elif args.command=="search": result=search(db,args)
        elif args.command=="backup":
            destination=Path(args.destination)
            if destination.exists(): raise ValueError("backup destination already exists")
            with sqlite3.connect(str(destination)) as dst: db.backup(dst)
            result={"backup":str(destination),"integrity":"check with post.py health on backup"}
        else: raise ValueError("unknown command")
        output(result)
    except (ValueError,sqlite3.Error,OSError) as exc:
        print("viche-post: "+str(exc),file=sys.stderr)
        return 1
    finally:
        db.close()
    return 0

if __name__=="__main__":
    sys.exit(main())
