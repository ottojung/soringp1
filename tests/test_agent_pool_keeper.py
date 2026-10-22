"""Deterministic keeper contract: minimum five without a duplicate-task loop."""
import importlib.util
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("soring_agent_keeper", ROOT / "scripts/agent_pool_keeper.py")
KEEPER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(KEEPER)


class KeeperTests(unittest.TestCase):
    def test_v2_curated_frontier_and_nonrepeat_fallback(self):
        plan = KEEPER.load_packet_plan()
        self.assertEqual(len(KEEPER.ROSTER), 8)
        self.assertEqual(len({id for id, _, _ in KEEPER.ROSTER}), 8)
        self.assertEqual(len(plan["agents"]), 8)
        seen = set()
        for agent_id, cwd, title in KEEPER.ROSTER:
            self.assertTrue(cwd.startswith("soring301-new-"))
            prompts = plan["agents"][agent_id]
            self.assertEqual(len(prompts), 3)
            for prompt in prompts:
                self.assertNotIn(prompt, seen)
                seen.add(prompt)
            delivered = [KEEPER.select_packet(agent_id, title, {agent_id: n}, plan) for n in range(4)]
            self.assertEqual(len(set(delivered)), 4)
            self.assertTrue(all("no" in p.lower() and "lean" in p.lower() for p in delivered))
            self.assertIn("WITHOUT a board comment", delivered[-1])
        self.assertEqual(len(seen), 24)

    def test_below_five_bypasses_quality_cooldown(self):
        plan = KEEPER.load_packet_plan()
        now = time.time()
        live = {aid for aid, _, _ in KEEPER.ROSTER[:4]}
        history = {aid: now for aid, _, _ in KEEPER.ROSTER}
        launched = []
        def fake_execute(args, timeout=20):
            self.assertEqual(args[:3], [KEEPER.A, "agent", "run"])
            launched.append(args[args.index("--id") + 1])
            return mock.Mock(returncode=0, stdout=json.dumps({"state": "running"}), stderr="")
        with tempfile.TemporaryDirectory() as tmp:
            with (mock.patch.object(KEEPER, "STATE", Path(tmp) / "history.json"),
                  mock.patch.object(KEEPER, "CURSORS", Path(tmp) / "cursors.json"),
                  mock.patch.object(KEEPER, "AGENTS_DIR", Path(tmp) / "agents"),
                  mock.patch.object(KEEPER, "running", return_value=set(live)),
                  mock.patch.object(KEEPER.os.path, "isdir", return_value=True),
                  mock.patch.object(KEEPER, "execute", side_effect=fake_execute)):
                cursors = {}
                KEEPER.tick(history, cursors, plan)
                self.assertEqual(len(launched), 1)
                self.assertEqual(cursors[launched[0]], 1)
                self.assertEqual(json.loads((Path(tmp) / "cursors.json").read_text()), cursors)

    def test_above_five_respects_quality_cooldown(self):
        plan = KEEPER.load_packet_plan()
        now = time.time()
        live = {aid for aid, _, _ in KEEPER.ROSTER[:6]}
        history = {aid: now for aid, _, _ in KEEPER.ROSTER}
        with tempfile.TemporaryDirectory() as tmp:
            with (mock.patch.object(KEEPER, "STATE", Path(tmp) / "history.json"),
                  mock.patch.object(KEEPER, "CURSORS", Path(tmp) / "cursors.json"),
                  mock.patch.object(KEEPER, "AGENTS_DIR", Path(tmp) / "agents"),
                  mock.patch.object(KEEPER, "running", return_value=live),
                  mock.patch.object(KEEPER, "execute") as call):
                KEEPER.tick(history, {}, plan)
                call.assert_not_called()

    def test_stalled_agent_is_steered_once_without_losing_agent_slot(self):
        plan = KEEPER.load_packet_plan()
        now = time.time()
        agent_id, wd, _ = KEEPER.ROSTER[0]
        live = {a for a, _, _ in KEEPER.ROSTER}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            agent_path = root / "agents" / agent_id
            agent_path.mkdir(parents=True)
            (agent_path / "meta.json").write_text(json.dumps({
                "state": "running", "cwd": "/home/lubko/" + wd,
                "started_at": now - 4000,
            }))
            log = agent_path / "output.log"
            log.write_text("no further output")
            import os
            os.utime(log, (now - 4000, now - 4000))
            history = {agent_id: now - 4000}
            cursors = {}
            def fake_execute(args, timeout=20):
                self.assertEqual(args[:3], [KEEPER.A, "agent", "run"])
                self.assertEqual(args[args.index("--id") + 1], agent_id)
                self.assertIn("--steer", args)
                self.assertNotIn("--cwd", args)  # active-front API forbids --cwd
                self.assertIn("Research packet 1", args[args.index("--prompt") + 1])
                return mock.Mock(returncode=0, stdout='{"state":"running"}', stderr="")
            with (mock.patch.object(KEEPER, "STATE", root / "history.json"),
                  mock.patch.object(KEEPER, "CURSORS", root / "cursors.json"),
                  mock.patch.object(KEEPER, "AGENTS_DIR", root / "agents"),
                  mock.patch.object(KEEPER, "running", return_value=live),
                  mock.patch.object(KEEPER, "execute", side_effect=fake_execute) as execute):
                KEEPER.tick(history, cursors, plan)
                self.assertEqual(execute.call_count, 1)
                self.assertEqual(cursors[agent_id], 1)
                self.assertEqual(json.loads((root / "cursors.json").read_text()), cursors)
                KEEPER.tick(history, cursors, plan)
                self.assertEqual(execute.call_count, 1)  # restarted agent cooldown

    def test_recent_output_protects_long_running_research(self):
        plan = KEEPER.load_packet_plan()
        now = time.time()
        agent_id, wd, _ = KEEPER.ROSTER[0]
        live = {a for a, _, _ in KEEPER.ROSTER}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "agents" / agent_id
            path.mkdir(parents=True)
            (path / "meta.json").write_text(json.dumps({
                "state": "running", "cwd": "/home/lubko/" + wd,
                "started_at": now - 4000,
            }))
            (path / "output.log").write_text("recent substantive output")
            with (mock.patch.object(KEEPER, "AGENTS_DIR", root / "agents"),
                  mock.patch.object(KEEPER, "running", return_value=live),
                  mock.patch.object(KEEPER, "execute") as execute):
                KEEPER.tick({agent_id: now - 4000}, {}, plan)
                execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()
