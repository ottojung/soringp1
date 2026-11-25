#!/usr/bin/env python3
"""Black-box regression tests for mail, evidence and publication invariants."""
import concurrent.futures
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

POST=Path(__file__).resolve().parents[1]/"government/post.py"

class PostTest(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.env=dict(os.environ,VICHE_POST_DB=str(Path(self.temp.name)/"post.sqlite3"))

    def cli(self,*argv,ok=True):
        if argv and argv[0]=="send":
            argv=(*argv,"--public")
        r=subprocess.run(["python3",str(POST),*argv],env=self.env,
                         text=True,capture_output=True)
        if ok:
            self.assertEqual(r.returncode,0,r.stderr)
            return json.loads(r.stdout)
        self.assertNotEqual(r.returncode,0,r.stdout)
        return r.stderr

    def send(self,*additional):
        return self.cli("send","--sender","statistics-bureau","--to","judiciary",
                        "--subject","Review","--body","Please investigate",*additional)

    def test_durable_mail_transition(self):
        mid=self.send("--key","unique1")["id"]
        self.assertEqual(len(self.cli("inbox","--office","judiciary","--new")),1)
        self.assertEqual(self.send("--key","unique1")["id"],mid)
        self.assertEqual(len(self.cli("inbox","--office","judiciary","--new")),1)
        self.assertIn("different content",self.cli("send","--sender","statistics-bureau",
            "--to","judiciary","--subject","Review","--body","New payload",
            "--key","unique1",ok=False))
        self.cli("read","--office","judiciary","--id",mid)
        self.cli("ack","--office","judiciary","--id",mid)
        self.assertIn("required",self.cli("resolve","--office","judiciary",
                            "--id",mid,ok=False))
        self.cli("resolve","--office","judiciary","--id",mid,"--reason",
                 "Examined separately; cannot verify the claimed remediation")
        self.assertEqual(self.cli("inbox","--office","judiciary")[0]["status"],"resolved")
        self.assertEqual(self.cli("health")["integrity"],"ok")

    def test_public_mail_requires_explicit_acknowledgement(self):
        r=subprocess.run(["python3",str(POST),"send","--sender","office-a",
            "--to","office-b","--subject","Message","--body","Message"],
            env=self.env,text=True,capture_output=True)
        self.assertNotEqual(r.returncode,0)
        self.assertIn("--public",r.stderr)

    def test_gazette_opt_in_no_autowake(self):
        self.cli("subscribe","--office","judiciary","--topic","statistics/resources")
        self.cli("subscribe","--office","foresight","--topic","statistics/resources",
                 "--mode","alert")
        pub=self.cli("publish","--sender","statistics-bureau",
                     "--topic","statistics/resources","--subject","Resource trend",
                     "--body","Observed","--kind","observation",
                     "--source","probe:disk-20261119","--condition","disk_used_percent",
                     "--priority","urgent")
        self.assertEqual(pub["delivered"],2)
        self.assertEqual(self.cli("wake","--office","foresight")["urgent_unread"],0)
        self.assertEqual(self.cli("inbox","--office","foresight")[0]["alert"],1)
        self.assertEqual(self.cli("inbox","--office","judiciary")[0]["alert"],0)
        self.assertEqual(len(self.cli("inbox","--office","strategy")),0)
        self.assertEqual(len(self.cli("inbox","--office","judiciary")),1)
        self.assertEqual(len(self.cli("feed","--topic","statistics/resources")),1)

    def test_causal_attention_budget_and_loop(self):
        first=self.send("--priority","urgent")
        self.assertEqual(self.cli("wake","--office","judiciary")["urgent_unread"],0)
        second=self.send("--priority","urgent","--caused-by",first["id"])
        third=self.send("--priority","urgent","--caused-by",second["id"])
        self.assertEqual(third["causal_depth"],2)
        self.assertEqual(self.cli("wake","--office","judiciary")["urgent_unread"],0)
        self.send("--priority","urgent")
        self.send("--priority","urgent")
        self.send("--priority","urgent")
        self.assertEqual(self.cli("wake","--office","judiciary")["urgent_unread"],0)
        self.assertEqual(len(self.cli("inbox","--office","judiciary")),6)

    def test_provenance_deduplicates_repeated_summaries(self):
        root=self.cli("publish","--sender","statistics-bureau",
                      "--topic","statistics/resources","--subject","Root",
                      "--body","Disk data","--kind","observation",
                      "--condition","bytes used as of timestamp",
                      "--source","measurement:disk:uuid-1")["id"]
        two=self.cli("publish","--sender","foresight","--topic","foresight/risks",
                      "--subject","Restatement","--body","Extrapolation",
                      "--based-on",root)["id"]
        three=self.cli("publish","--sender","strategy","--topic","strategy/plans",
                        "--subject","More analysis","--body","No new measurement",
                        "--based-on",root,"--based-on",two)["id"]
        self.assertEqual(self.cli("lineage","--id",three)["count"],1)

    def test_reject_epistemically_underspecified_claims(self):
        base=("publish","--sender","statistics-bureau",
              "--topic","statistics/resources","--subject","Data","--body","Data")
        self.assertIn("original sources",self.cli(*base,"--kind","observation",ok=False))
        self.assertIn("Act 22",self.cli(*base,"--kind","forecast",
            "--condition","no intervention","--baseline","50%","--resolution-rule",
            "observe outcomes by 2027",ok=False))
        self.assertIn("alternative explanation",self.cli("publish","--sender","spying",
            "--topic","founder/signals","--subject","Interest","--body","Observed",
            "--kind","founder-inference","--source","antonina:302",ok=False))

    def test_committed_forecast_registry_cannot_be_faked(self):
        import hashlib
        import time
        town=Path(self.temp.name)/"town"
        (town/"records/predictions").mkdir(parents=True)
        subprocess.run(["git","init","-q",str(town)],check=True)
        at=int(time.time())-600
        entry={"id":"trial-registration-1","kind":"registration",
               "bill_id":"trial","proposition":"Capacity falls before deadline",
               "probability":0.4,"resolution_date":"2026-12-31",
               "evidence_source":"collector:capacity","author":"foresight",
               "registered_at":at}
        fields=("bill_id","proposition","probability","resolution_date",
                "evidence_source","author","registered_at")
        canon={k:entry[k] for k in fields}
        blob=json.dumps(canon,sort_keys=True,separators=(",",":")).encode()
        entry["content_hash"]="sha256:"+hashlib.sha256(blob).hexdigest()
        (town/"records/predictions/ledger.json").write_text(
            json.dumps({"entries":[entry],"resolutions":[]}))
        subprocess.run(["git","-C",str(town),"add","records/predictions/ledger.json"],check=True)
        subprocess.run(["git","-C",str(town),"-c","user.name=Test",
            "-c","user.email=test@example.invalid","commit","-qm","Register forecast"],
            check=True)
        self.env["VICHE_TOWN_ROOT"]=str(town)
        good=("publish","--sender","foresight","--topic","foresight/forecasts",
              "--subject",entry["proposition"],"--body","Conditional forecast",
              "--kind","forecast","--source","act22:"+entry["id"],
              "--condition","No intervention","--baseline","0.5",
              "--resolution-rule","collector:capacity")
        self.assertEqual(self.cli(*good)["delivered"],0)
        fake=list(good)
        fake[fake.index("--source")+1]="act22:not-registered"
        self.assertIn("committed Act 22 registration",self.cli(*fake,ok=False))
        forged=list(good)
        forged[forged.index("--subject")+1]="A different prediction"
        self.assertIn("committed Act 22 registration",self.cli(*forged,ok=False))

    def test_thread_trace_search_and_immutability(self):
        a=self.send("--key","thread-root")["id"]
        b=self.cli("send","--sender","judiciary","--to","statistics",
                   "--subject","Response","--body","Contrary evidence",
                   "--caused-by",a)["id"]
        c=self.cli("send","--sender","statistics","--to","judiciary",
                   "--subject","Follow-up","--body","Research reply",
                   "--caused-by",b)["id"]
        t=self.cli("thread","--id",b)
        self.assertEqual([x["id"] for x in t["messages"]],[a,b,c])
        self.assertEqual(self.cli("trace","--id",a)["deliveries"][0]["recipient"],"judiciary")
        self.assertEqual(len(self.cli("search","--text","Contrary evidence")),1)
        import sqlite3
        with sqlite3.connect(self.env["VICHE_POST_DB"]) as db:
            with self.assertRaises(sqlite3.DatabaseError):
                db.execute("DELETE FROM messages WHERE id=?",(a,))
            with self.assertRaises(sqlite3.DatabaseError):
                db.execute("UPDATE messages SET body=? WHERE id=?",("tampered",a))

    def test_concurrent_receipts_monotonic(self):
        # Read and acknowledgement may race across separate agent invocations.
        # The final state cannot ever move backward.
        for i in range(8):
            mid=self.send("--key","receipt-"+str(i))["id"]
            def action(cmd):
                return subprocess.run(["python3",str(POST),cmd,
                    "--office","judiciary","--id",mid],env=self.env,
                    capture_output=True,text=True)
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                results=list(pool.map(action,("read","ack")))
            self.assertTrue(all(x.returncode==0 for x in results),results)
            status=self.cli("trace","--id",mid)["deliveries"][0]["status"]
            self.assertEqual(status,"acknowledged")
        older=self.cli("read","--office","judiciary","--id",mid)
        self.assertEqual(older["status"],"acknowledged")
        self.assertTrue(older["already_advanced"])

    def test_urgent_mail_not_buried(self):
        self.cli("subscribe","--office","judiciary","--topic","statistics/outcomes")
        for i in range(6):
            self.cli("publish","--sender","statistics","--topic","statistics/outcomes",
                     "--subject","Low-priority "+str(i),"--body","Derived report")
        urgent=self.cli("send","--sender","executive","--to","judiciary",
                        "--subject","Real urgent letter","--body","Please investigate",
                        "--priority","urgent")["id"]
        first=self.cli("inbox","--office","judiciary","--new","--limit","1")[0]
        self.assertEqual(first["id"],urgent)
        self.assertEqual(self.cli("wake","--office","judiciary")["urgent_unread"],0)

    def test_subscriber_agent_ids(self):
        ident="Qwe2S9z-AbCd3"
        self.cli("subscribe","--office",ident,"--topic","statistics/outcomes",
                 "--mode","alert")
        pub=self.cli("publish","--sender","statistics","--topic","statistics/outcomes",
                     "--subject","Observed","--body","Collector updated",
                     "--kind","observation","--source","collector:hash",
                     "--condition","daily window")
        self.assertEqual(pub["delivered"],1)
        self.assertEqual(self.cli("inbox","--office",ident)[0]["alert"],1)
        self.assertEqual(self.cli("wake","--office",ident)["urgent_unread"],0)

    def test_atomic_concurrent_idempotency(self):
        def action(_):
            return self.send("--key","same-concurrent")
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            responses=list(pool.map(action,range(16)))
        self.assertEqual(len({x["id"] for x in responses}),1)
        self.assertEqual(len(self.cli("inbox","--office","judiciary")),1)
        backup=Path(self.temp.name)/"backup.sqlite3"
        self.cli("backup","--destination",str(backup))
        self.assertTrue(backup.exists())

if __name__=="__main__":
    unittest.main()
