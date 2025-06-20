# 🦅 CrowdStrike Falcon Onboarding Checklist

CrowdStrike Falcon provides endpoint detection telemetry via the Falcon Event Stream API. This guide outlines how to onboard CrowdStrike logs into your SIEM pipeline.

---

## 🔧 Setup

- [ ] Enable **Event Stream API** in Falcon Console
- [ ] Generate API client with `Event streams: Read` permission
- [ ] Note `Client ID`, `Client Secret`, and Base URL (`https://api.crowdstrike.com`)
- [ ] Install [falconpy](https://github.com/CrowdStrike/falconpy) or use Splunk/Datadog native integration

---

## 📄 Event Types to Ingest

- [ ] `DetectionSummaryEvent`
- [ ] `ProcessRollup2`
- [ ] `NetworkConnect`
- [ ] `AuthEvent`
- [ ] `DnsRequest`
- [ ] `FileWritten`

---

## 🎯 Field Normalization

| Raw Field              | ECS Field                   |
|------------------------|-----------------------------|
| `aid`                  | `host.id`                   |
| `ComputerName`         | `host.hostname`             |
| `UserName`             | `user.name`                 |
| `CommandLine`          | `process.command_line`      |
| `ParentCommandLine`    | `process.parent.command_line` |
| `DetectionName`        | `threat.name`               |
| `EventType`            | `event.action`              |

---

## ✅ Validation

- [ ] Confirm data flowing to SIEM
- [ ] Correlate test detection to log (e.g. EICAR or lolbin)
- [ ] Check ECS mappings for `process.*`, `host.*`, and `user.*`
