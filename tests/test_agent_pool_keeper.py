"""Deterministic keeper contract: curated packets only, up to a target count."""
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
    def test_v2_curated_frontier_without_invented_fallback(self):
        plan = KEEPER.load_packet_plan()
        self.assertEqual(len(KEEPER.ROSTER), 8)
        self.assertEqual(len({id for id, _, _ in KEEPER.ROSTER}), 8)
        self.assertEqual(len(plan["agents"]), 8)
        seen = set()
        for agent_id, cwd, title in KEEPER.ROSTER:
            self.assertTrue(cwd.startswith("soring301-new-"))
            prompts = plan["agents"][agent_id]
            self.assertGreaterEqual(len(prompts), 1)
            for prompt in prompts:
                self.assertNotIn(prompt, seen)
                seen.add(prompt)
            delivered = [KEEPER.select_packet(agent_id, title, {agent_id: n}, plan)
                         for n in range(len(prompts))]
            self.assertEqual(len(set(delivered)), len(prompts))
            self.assertTrue(all("no" in p.lower() and "lean" in p.lower() for p in delivered))
            # Once curated packets are used, the track waits for curation.
            exhausted = {agent_id: len(prompts)}
            self.assertIsNone(KEEPER.select_packet(agent_id, title, exhausted, plan))
            self.assertIn(agent_id, KEEPER.awaiting_curation(exhausted, plan))

    def _tick_with_launch_capture(self, live, history, cursors, plan, target=5):
        launched = []
        def fake_execute(args, timeout=20):
            self.assertEqual(args[:3], [KEEPER.A, "agent", "run"])
            self.assertNotIn("--cwd", args)
            launched.append(args[args.index("--id") + 1])
            return mock.Mock(returncode=0, stdout=json.dumps({"state": "running"}), stderr="")
        with tempfile.TemporaryDirectory() as tmp:
            with (mock.patch.object(KEEPER, "STATE", Path(tmp) / "history.json"),
                  mock.patch.object(KEEPER, "CURSORS", Path(tmp) / "cursors.json"),
                  mock.patch.object(KEEPER, "AGENTS_DIR", Path(tmp) / "agents"),
                  mock.patch.object(KEEPER, "running", return_value=set(live)),
                  mock.patch.object(KEEPER.os.path, "isdir", return_value=True),
                  mock.patch.object(KEEPER, "agent_declares_cwd", return_value=True),
                  mock.patch.object(KEEPER, "execute", side_effect=fake_execute)):
                KEEPER.tick(history, cursors, plan, target)
                if launched:
                    self.assertEqual(json.loads((Path(tmp) / "cursors.json").read_text()), cursors)
        return launched

    def test_below_target_refills_with_next_curated_packet(self):
        plan = KEEPER.load_packet_plan()
        live = {aid for aid, _, _ in KEEPER.ROSTER[:4]}
        history = {aid: time.time() - 3600 for aid, _, _ in KEEPER.ROSTER}
        cursors = {}
        launched = self._tick_with_launch_capture(live, history, cursors, plan)
        self.assertEqual(len(launched), 1)
        self.assertEqual(cursors[launched[0]], 1)

    def test_recently_finished_agent_waits_for_cooldown(self):
        plan = KEEPER.load_packet_plan()
        live = {aid for aid, _, _ in KEEPER.ROSTER[:4]}
        history = {aid: time.time() for aid, _, _ in KEEPER.ROSTER}
        self.assertEqual(self._tick_with_launch_capture(live, history, {}, plan), [])

    def test_exhausted_tracks_are_not_relaunched_with_filler(self):
        plan = KEEPER.load_packet_plan()
        history = {aid: time.time() - 3600 for aid, _, _ in KEEPER.ROSTER}
        cursors = {aid: len(plan["agents"][aid]) for aid, _, _ in KEEPER.ROSTER}
        launched = self._tick_with_launch_capture(set(), history, cursors, plan)
        self.assertEqual(launched, [])  # Running below target is acceptable.
        # Curating one new packet makes exactly that track eligible again.
        agent_id = KEEPER.ROSTER[2][0]
        plan["agents"][agent_id] = plan["agents"][agent_id] + [
            "A newly curated all-n research question with a stated complexity consequence."]
        launched = self._tick_with_launch_capture(set(), history, cursors, plan)
        self.assertEqual(launched, [agent_id])

    def test_relaunch_respects_persisted_worktree_authority(self):
        agent_id, wd, _ = KEEPER.ROSTER[0]
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / agent_id
            base.mkdir()
            meta = base / "meta.json"
            with mock.patch.object(KEEPER, "AGENTS_DIR", Path(tmp)):
                self.assertFalse(KEEPER.agent_declares_cwd(agent_id, "/home/lubko/" + wd))
                meta.write_text(json.dumps({
                    "id": agent_id, "cwd": "/home/lubko/DIFFERENT"}))
                self.assertFalse(KEEPER.agent_declares_cwd(agent_id, "/home/lubko/" + wd))
                meta.write_text(json.dumps({
                    "id": agent_id, "cwd": "/home/lubko/" + wd}))
                self.assertTrue(KEEPER.agent_declares_cwd(agent_id, "/home/lubko/" + wd))

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

    def test_return_to_primary_after_actual_cooldown_and_quiet_period(self):
        plan = KEEPER.load_packet_plan()
        now = time.time()
        agent_id, wd, _ = KEEPER.ROSTER[0]
        live = {a for a, _, _ in KEEPER.ROSTER}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "agents" / agent_id
            path.mkdir(parents=True)
            meta_file = path / "meta.json"
            model_config = root / "model-config.json"
            model_config.write_text(json.dumps({"models": [
                {"model": "test/primary"}, {"model": "test/fallback"}]}))
            meta = {
                "state": "running", "cwd": "/home/lubko/" + wd,
                "started_at": now - 650,
                "model_failover": {
                    "selected_model": "test/fallback",
                    "cooldowns": [{"model": "test/primary",
                                   "reason": "quota_exhausted",
                                   "until": now + 15}],
                },
            }
            meta_file.write_text(json.dumps(meta))
            (path / "output.log").write_text("last response")
            import os
            os.utime(path / "output.log", (now - 650, now - 650))
            history = {agent_id: now - 650}
            cursors = {}
            with (mock.patch.object(KEEPER, "STATE", root / "history.json"),
                  mock.patch.object(KEEPER, "CURSORS", root / "cursors.json"),
                  mock.patch.object(KEEPER, "AGENTS_DIR", root / "agents"),
                  mock.patch.object(KEEPER, "MODELS_CONFIG", model_config),
                  mock.patch.object(KEEPER, "running", return_value=live),
                  mock.patch.object(KEEPER, "execute", return_value=mock.Mock(
                      returncode=0, stdout='{"state":"running"}', stderr="")) as execute,
                  mock.patch.object(KEEPER.time, "time", return_value=now)):
                KEEPER.tick(history, cursors, plan)
                execute.assert_not_called()  # Provider's reset has not passed.
                meta["model_failover"]["cooldowns"][0]["until"] = now - 30
                meta_file.write_text(json.dumps(meta))
                KEEPER.tick(history, cursors, plan)
                self.assertEqual(execute.call_count, 1)
                self.assertIn("--steer", execute.call_args.args[0])
                self.assertEqual(cursors[agent_id], 1)
                KEEPER.tick(history, cursors, plan)
                self.assertEqual(execute.call_count, 1)  # No rapid re-steer.

    def test_primary_recovery_does_not_interrupt_recent_fallback_output(self):
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
                "started_at": now - 650,
                "model_failover": {
                    "selected_model": "test/fallback",
                    "cooldowns": [{"model": "test/primary",
                                   "reason": "quota_exhausted",
                                   "until": now - 1}],
                },
            }))
            (path / "output.log").write_text("recent actual output")
            cfg = root / "config.json"
            cfg.write_text(json.dumps({"models": [
                {"model": "test/primary"}, {"model": "test/fallback"}]}))
            with (mock.patch.object(KEEPER, "AGENTS_DIR", root / "agents"),
                  mock.patch.object(KEEPER, "MODELS_CONFIG", cfg),
                  mock.patch.object(KEEPER, "running", return_value=live),
                  mock.patch.object(KEEPER, "execute") as execute,
                  mock.patch.object(KEEPER.time, "time", return_value=now)):
                KEEPER.tick({agent_id: now - 650}, {}, plan)
                execute.assert_not_called()

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
