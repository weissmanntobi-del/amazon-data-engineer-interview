from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable, TextIO


def parse_ts(value: str) -> datetime:
    """Parse common ISO-8601 timestamps, including a trailing Z."""
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def dedupe_events(lines: Iterable[str]) -> tuple[list[dict], int]:
    latest: dict[str, tuple[datetime, int, dict]] = {}
    rejected = 0

    for position, line in enumerate(lines):
        try:
            record = json.loads(line)
            event_id = record["event_id"]
            event_ts = record["event_ts"]
            if not event_id or not event_ts:
                raise ValueError("event_id and event_ts are required")
            parsed_ts = parse_ts(event_ts)
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            rejected += 1
            continue

        current = latest.get(str(event_id))
        candidate = (parsed_ts, position, record)
        if current is None or candidate[:2] >= current[:2]:
            latest[str(event_id)] = candidate

    output = [item[2] for item in latest.values()]
    output.sort(key=lambda r: (parse_ts(r["event_ts"]), str(r["event_id"])))
    return output, rejected


def run(path: Path, out: TextIO = sys.stdout) -> int:
    with path.open("r", encoding="utf-8") as handle:
        records, rejected = dedupe_events(handle)

    for record in records:
        out.write(json.dumps(record, sort_keys=True) + "\n")
    out.write(f"# rejected_rows={rejected}\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python 01_dedupe_events.py <events.jsonl>", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(run(Path(sys.argv[1])))
