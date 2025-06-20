# ☁️ Netskope Onboarding Checklist

Netskope provides CASB visibility and DLP telemetry across SaaS, web, and cloud applications. This guide helps onboard Netskope into your detection pipeline.

---

## 🔧 Setup

- [ ] Enable **Tenant Logging API** or SIEM Forwarder
- [ ] Authenticate using a service account or API token
- [ ] Choose log types: `alert`, `audit`, `application`, `incident`, `webtx`
- [ ] Forward to Splunk HEC, Datadog, or intermediary syslog

---

## 📄 Key Fields to Normalize

| Raw Field            | ECS Field             |
|----------------------|-----------------------|
| `app`                | `app.name`            |
| `ur_normalized`      | `url.full`            |
| `mime_type`          | `file.mime_type`      |
| `user`               | `user.email`          |
| `device`             | `host.name`           |
| `dst_country`        | `geo.country`         |
| `event`              | `event.action`        |
| `activity`           | `event.category`      |

---

## 🛡️ Recommended Detections

- [ ] Unusual OAuth grants
- [ ] Bulk downloads from sanctioned apps
- [ ] Executable/script downloads
- [ ] Sensitive file sharing to public
- [ ] Concurrent logins from different countries

---

## ✅ Validation

- [ ] Ingest test event from browser/download
- [ ] Confirm `user.email`, `event.action`, `mime_type` are mapped
- [ ] Run test Sigma rules for public share, executable download
