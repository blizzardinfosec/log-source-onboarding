import json

# Load raw CloudTrail log
with open("cloudtrail_sample.json") as f:
    raw = json.load(f)

# Extract normalized fields
normalized = {
    "event_type": raw.get("eventName"),
    "username": raw.get("userIdentity", {}).get("userName"),
    "user_arn": raw.get("userIdentity", {}).get("arn"),
    "account_id": raw.get("userIdentity", {}).get("accountId"),
    "source_ip": raw.get("sourceIPAddress"),
    "region": raw.get("awsRegion"),
    "user_agent": raw.get("userAgent"),
    "timestamp": raw.get("eventTime")
}

# Write normalized JSON
with open("normalized_event.json", "w") as out:
    json.dump(normalized, out, indent=2)

print("✅ Normalized CloudTrail log saved to normalized_event.json")
