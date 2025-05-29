import json

with open("sample_event.json") as f:
    raw = json.load(f)

normalized = {
    "event_type": raw["eventType"],
    "user": raw["actor"]["displayName"],
    "result": raw["outcome"]["result"],
    "auth_method": raw["authenticationContext"]["authenticationMethod"],
    "ip": raw["client"]["ipAddress"],
    "user_agent": raw["client"]["userAgent"]["rawUserAgent"]
}

with open("normalized_event.json", "w") as out:
    json.dump(normalized, out, indent=2)

print("✅ Normalized log written to normalized_event.json")
