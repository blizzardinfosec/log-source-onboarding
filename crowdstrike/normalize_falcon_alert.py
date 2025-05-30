import json

with open("detection_event.json") as f:
    raw = json.load(f)

normalized = {
    "event_type": raw.get("event"),
    "timestamp": raw.get("metadata", {}).get("eventCreationTime"),
    "host": raw.get("device", {}).get("hostname"),
    "user": raw.get("device", {}).get("user_name"),
    "severity": raw.get("severity"),
    "tactic": raw.get("tactic"),
    "technique_id": raw.get("technique_id"),
    "behavior_id": raw.get("behavior_id"),
    "file_path": raw.get("file_path"),
    "command_line": raw.get("command_line")
}

with open("normalized_event.json", "w") as out:
    json.dump(normalized, out, indent=2)

print("✅ CrowdStrike Falcon alert normalized to normalized_event.json")
