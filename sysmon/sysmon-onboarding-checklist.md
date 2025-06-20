# 🧩 Sysmon Onboarding Checklist

Sysmon provides rich Windows telemetry and is essential for host-level detection engineering. This guide helps deploy and ingest Sysmon data properly.

---

## 🛠️ Setup

- [ ] Install Sysmon (latest version) on target hosts
- [ ] Use [SwiftOnSecurity config](https://github.com/SwiftOnSecurity/sysmon-config) or hardened variant (e.g., [olafhartong/sysmon-modular](https://github.com/olafhartong/sysmon-modular))
- [ ] Ensure logs are sent to Event Log: `Microsoft-Windows-Sysmon/Operational`
- [ ] Forward logs to SIEM via:
  - Winlogbeat (Elastic)
  - Splunk UF
  - NXLog

---

## 📄 Key Event IDs

| Event ID | Description               | ECS Event Action          |
|----------|---------------------------|---------------------------|
| 1        | Process Create            | `process_create`          |
| 3        | Network Connection        | `network_connection`      |
| 11       | File Created              | `file_create`             |
| 12–13    | Registry Set/Create       | `registry_add`            |
| 7        | Image Load                | `image_load`              |
| 8        | CreateRemoteThread        | `thread_injection`        |

---

## 📦 ECS Mappings

| Raw Field        | ECS Field               |
|------------------|-------------------------|
| `CommandLine`    | `process.command_line`  |
| `ParentImage`    | `process.parent.executable` |
| `DestinationIp`  | `destination.ip`        |
| `User`           | `user.name`             |

---

## ✅ Validation

- [ ] Deploy test Sysmon config
- [ ] Validate logs in SIEM
- [ ] Confirm field mappings for `process.*`, `user.*`, `network.*`
- [ ] Trigger test events (e.g., `calc.exe`, netcat, regedit)
