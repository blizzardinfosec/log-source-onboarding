# 💻 FleetDM Onboarding Checklist

Fleet is an open-source osquery manager providing real-time visibility into laptops and servers. This guide outlines how to onboard Fleet log data.

---

## 🔧 Setup

- [ ] Install [Fleet](https://fleetdm.com/) and enroll hosts with osquery
- [ ] Configure log shipping to SIEM (via Kafka, Firehose, syslog)
- [ ] Enable results, status, and snapshot logs

---

## 🎯 Key Tables to Monitor

- `process_events`
- `scheduled_queries`
- `users`
- `crontab`, `launchd`
- `listening_ports`
- `browser_extensions`
- `authentications`

---

## 🧱 Normalize to ECS

| osquery Field        | ECS Field              |
|----------------------|------------------------|
| `name`               | `process.name`         |
| `cmdline`            | `process.command_line` |
| `uid` / `user`       | `user.name`            |
| `hostname`           | `host.hostname`        |
| `time`               | `@timestamp`           |
| `action` (Fleet log) | `event.action`         |

---

## ✅ Validation

- [ ] Deploy known test queries (e.g., netcat, new user)
- [ ] Confirm Fleet logs parsed in SIEM
- [ ] Check field mapping for `process.*`, `user.*`, `event.*`
