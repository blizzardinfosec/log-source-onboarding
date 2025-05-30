import json

with open("unified_audit_log.json") as f:
    raw = json.load(f)

# Extract target object from Parameters if it exists
target = None
for p in raw.get("Parameters", []):
    if p.get("Name") in ("SendOnBehalfTo", "TargetObjectId"):
        target = p.get("Value")
        break

normalized = {
    "event_type": raw.get("Operation"),
    "user": raw.get("UserId"),
    "client_ip": raw.get("ClientIP"),
    "user_agent": raw.get("UserAgent"),
    "timestamp": raw.get("CreationTime"),
    "record_type": raw.get("RecordType"),
    "workload": raw.get("Workload"),
    "target_object": target or raw.get("ObjectId"),
    "result": raw.get("ResultStatus")
}

with open("normalized_event.json", "w") as out:
    json.dump(normalized, out, indent=2)

print("✅ O365 audit log normalized to normalized_event.json")
