import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "python" / "01_dedupe_events.py"
spec = importlib.util.spec_from_file_location("dedupe_events_module", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class DedupeEventsTest(unittest.TestCase):
    def test_keeps_latest_and_rejects_bad_rows(self):
        lines = [
            '{"event_id":"1","event_ts":"2026-01-01T00:00:00Z","v":1}',
            'bad json',
            '{"event_id":"1","event_ts":"2026-01-02T00:00:00Z","v":2}',
            '{"event_id":"2","event_ts":"2026-01-01T12:00:00Z","v":1}',
            '{"event_id":"3"}',
        ]
        records, rejected = module.dedupe_events(lines)
        self.assertEqual(rejected, 2)
        self.assertEqual([r["event_id"] for r in records], ["2", "1"])
        self.assertEqual(records[1]["v"], 2)

    def test_later_input_wins_timestamp_tie(self):
        lines = [
            '{"event_id":"1","event_ts":"2026-01-01T00:00:00Z","v":1}',
            '{"event_id":"1","event_ts":"2026-01-01T00:00:00Z","v":2}',
        ]
        records, rejected = module.dedupe_events(lines)
        self.assertEqual(rejected, 0)
        self.assertEqual(records[0]["v"], 2)


if __name__ == "__main__":
    unittest.main()
