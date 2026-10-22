"""Keep Antonina research context small and informative."""
import importlib.util
from pathlib import Path
import unittest
from unittest import mock

FILE = Path(__file__).resolve().parents[1] / "scripts/board_digest.py"
SPEC = importlib.util.spec_from_file_location("board_digest", FILE)
DIGEST = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(DIGEST)


class BoardDigestTests(unittest.TestCase):
    def setUp(self):
        self.messages = [
            {"createdAt": "2026-10-22T15:00:00Z", "author": "Reviewer",
             "body": "A serious optimal policy lemma."},
            {"createdAt": "2026-10-22T15:01:00Z", "author": "Reviewer",
             "body": "A serious optimal policy lemma."},
            {"createdAt": "2026-10-22T15:02:00Z", "author": "Worker",
             "body": "Only a finite witness."},
            {"createdAt": "2026-10-22T15:03:00Z", "author": "Worker",
             "body": "An all-n OPTIMAL policy claim."},
        ]

    def test_latest_first_and_deduplicate(self):
        selected = DIGEST.select_messages(self.messages, 3, "")
        self.assertEqual([x[0] for x in selected], [
            "2026-10-22T15:03:00Z",
            "2026-10-22T15:02:00Z",
            "2026-10-22T15:01:00Z",
        ])

    def test_keyword_filter_casefold_and_limit(self):
        selected = DIGEST.select_messages(self.messages, 1, "optimal")
        self.assertEqual(selected[0][0], "2026-10-22T15:03:00Z")
        selected = DIGEST.select_messages(self.messages, 3, "REVIEWER")
        self.assertEqual(len(selected), 1)

    def test_error_exits_cleanly(self):
        with (mock.patch.object(DIGEST, "fetch_messages", side_effect=OSError("offline")),
              mock.patch("sys.argv", ["board_digest.py"])):
            self.assertEqual(DIGEST.main(), 1)


if __name__ == "__main__":
    unittest.main()
