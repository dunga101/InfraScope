import json
from datetime import datetime, UTC


class JsonWriter:
    def __init__(self, filepath="telemetry_log.json"):
        self.filepath = filepath

    def write(self, data: dict):
        timestamped_data = {
            "timestamp": datetime.now(UTC).isoformat(),
            "data": data
        }

        with open(self.filepath, "a") as f:
            f.write(json.dumps(timestamped_data) + "\n")