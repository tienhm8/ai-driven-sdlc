"""Transactional local event store for governance decisions and state."""
from contextlib import contextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
import uuid


def new_execution_id():
    return "exec-" + uuid.uuid4().hex


class EventStore:
    def __init__(self, state_dir: Path, *, project: Path):
        self.path = state_dir / "governance.sqlite3"
        self.project = project
        self._check_location()

    def _check_location(self):
        for path in (self.path, *(self.path.with_name(self.path.name + suffix)
                                  for suffix in ("-journal", "-wal", "-shm"))):
            resolved = path.resolve()
            if resolved != path or resolved.is_relative_to(self.project):
                raise ValueError("Governance database paths must be outside the project workspace and not use symlinks")

    @contextmanager
    def transaction(self):
        self._check_location()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._check_location()
        connection = sqlite3.connect(self.path)
        try:
            with connection:
                connection.execute("BEGIN IMMEDIATE")
                connection.execute("""
                    CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY,
                        execution_id TEXT NOT NULL,
                        event TEXT NOT NULL
                    )
                """)
                connection.execute("CREATE INDEX IF NOT EXISTS events_execution ON events (execution_id)")
                yield connection
        finally:
            connection.close()

    @staticmethod
    def read(connection, execution_id):
        return [json.loads(row[0]) for row in connection.execute(
            "SELECT event FROM events WHERE execution_id = ? ORDER BY id", (execution_id,)
        )]

    @staticmethod
    def append(connection, execution_id, event_type, **data):
        event = {
            "event_id": uuid.uuid4().hex,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "execution_id": execution_id,
            "event_type": event_type,
            **data,
        }
        connection.execute("INSERT INTO events (execution_id, event) VALUES (?, ?)",
                           (execution_id, json.dumps(event, ensure_ascii=False)))
        return event
