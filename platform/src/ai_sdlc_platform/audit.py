from datetime import datetime, timezone
from pathlib import Path
import json, uuid

def new_execution_id():
    return "exec-" + uuid.uuid4().hex[:12]

def emit_event(project, execution_id, event_type, **data):
    event = {"timestamp": datetime.now(timezone.utc).isoformat(),
             "execution_id": execution_id, "event_type": event_type, **data}
    folder = project / ".ai-sdlc" / "audit"
    folder.mkdir(parents=True, exist_ok=True)
    with (folder / "events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False, default=str) + "\n")
    return event
