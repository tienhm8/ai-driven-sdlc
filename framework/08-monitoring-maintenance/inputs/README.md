# Inputs – Monitoring & Maintenance

Giai đoạn 08 nhận tham chiếu từ SDLC 01–07 và dữ liệu runtime. Không cần sao chép toàn bộ tài liệu/source code; ưu tiên liên kết có version/commit, owner và timestamp.

## 1. Kiến trúc

```
inputs/
└── README.md    # Định nghĩa đầu vào, quy ước và intake record
```

Thư mục hiện chỉ chứa README. Đầu vào thực tế được tham chiếu bằng liên kết (repo, commit, dashboard, ticket), không lưu bản sao trong thư mục này.

Luồng đầu vào:

```
01–07 (tài liệu, quyết định, release)  ──┐
Runtime (logs, metrics, traces, alerts) ─┴──► Intake record ──► 08 Monitoring & Maintenance
```

## 2. Vai trò từng file

| File | Vai trò |
|---|---|
| `README.md` | Liệt kê nguồn đầu vào theo từng giai đoạn SDLC 01–07 và Runtime, mục đích sử dụng của từng nguồn; quy định cách tham chiếu (version/commit, owner, timestamp), quyền truy cập và dữ liệu thiếu; định nghĩa intake record mà mỗi đợt 08 phải ghi nhận trước khi bắt đầu |

## Quy ước
- Snapshot chỉ khi cần bảo toàn evidence; ghi source, timestamp/timezone, query và retention.
- Không lưu secret, credential, raw PII hoặc production dump trong repo.
- Giới hạn quyền theo data classification.
- Ghi rõ dữ liệu thiếu/stale; missing telemetry không đồng nghĩa healthy.

## Intake record
Service/project; environment; release/version; Service Owner/on-call; architecture/dependency references; SLI/SLO and RTO/RPO; runbook/rollback/DR; recent changes; telemetry links; known risks; missing inputs and owner; captured-at timestamp/timezone.
