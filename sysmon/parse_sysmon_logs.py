import xml.etree.ElementTree as ET
import json

tree = ET.parse("raw_event.xml")
root = tree.getroot()

ns = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}

def get_text(tag):
    el = root.find(f".//ns:Data[@Name='{tag}']", ns)
    return el.text if el is not None else None

normalized = {
    "event_type": "ProcessCreate",
    "timestamp": get_text("UtcTime"),
    "host": root.find(".//ns:Computer", ns).text,
    "user": get_text("User"),
    "image": get_text("Image"),
    "command_line": get_text("CommandLine"),
    "parent_image": get_text("ParentImage"),
    "process_id": get_text("ProcessId"),
    "parent_pid": get_text("ParentProcessId")
}

with open("parsed_event.json", "w") as out:
    json.dump(normalized, out, indent=2)

print("✅ Sysmon Event ID 1 normalized to parsed_event.json")
