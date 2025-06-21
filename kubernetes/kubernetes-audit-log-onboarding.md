# ☸️ Kubernetes Audit Log Onboarding Checklist

Kubernetes audit logs provide a detailed trail of API server activity — useful for detection of privilege escalation, lateral movement, and cluster abuse.

---

## 🔧 Enable Audit Logging

- [ ] Edit `kube-apiserver` to include `--audit-log-path` and `--audit-policy-file`
- [ ] Use [default or hardened policy](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/#audit-policy) for event filtering
- [ ] Forward audit logs via Fluentd or Filebeat to SIEM

---

## 🎯 Key Detection Use Cases

- Pod exec into sensitive namespaces
- Privileged pod launches
- Secrets accessed or modified
- HostPath mounted volumes
- Service Account misuse

---

## 🧱 Normalize to ECS

| Raw Field               | ECS Field                 |
|-------------------------|---------------------------|
| `user.username`         | `user.name`               |
| `verb`                  | `event.action`            |
| `objectRef.namespace`   | `kubernetes.namespace`    |
| `objectRef.name`        | `kubernetes.resource.name`|
| `sourceIPs[]`           | `source.ip`               |
| `stage`                 | `event.stage`             |

---

## ✅ Validation

- [ ] Trigger test events: `kubectl exec`, `create pod`, etc.
- [ ] Verify `verb`, `namespace`, `user.name`, `source.ip` mapped
- [ ] Confirm ingest into SIEM (e.g. Splunk, Elastic, Datadog)
