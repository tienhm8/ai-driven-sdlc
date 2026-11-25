# Kế hoạch triển khai (Deployment Plan)

> Template chuẩn của Stage 07. [File trong thư viện dùng chung](../../templates/deployment/deployment-plan.md) chỉ trỏ về mẫu này.
> Plan mô tả cách thực hiện và chỉ tham chiếu [hồ sơ phê duyệt G6](production-approval.md); không ghi quyết định G6 tại đây.

## 1. Metadata
- Deployment ID: `DEP-{{NUMBER}}`
- Plan version / Status: Draft / Reviewed / Approved-for-G6-review / Superseded
- Project/service:
- Release ID/version:
- Change/ticket/PR:
- Repository:
- Commit SHA:
- Artifact URI and digest (SHA-256):
- Target environment/region:
- Deployment owner:
- Release Manager:
- Planned window and timezone:

## 2. Phạm vi và rủi ro
- Thay đổi bao gồm:
- Thay đổi loại trừ:
- Requirement liên quan:
- Dependencies:
- Tác động dự kiến đến người dùng/downtime:
- Mức rủi ro và lý do:
- Rủi ro đã biết và biện pháp giảm thiểu:

## 3. Điều kiện tiên quyết (readiness)
- G4 approval (link):
- G5 sign-off (link):
- CI/build/test/security evidence:
- Artifact đã xác minh và promote từ pipeline tin cậy:
- Environment readiness:
- Access/approval:
- Backup/restore status:
- Monitoring/alerting readiness:
- Rollback plan đã review/test (link, phiên bản):
- Stakeholder đã được thông báo:

## 4. Chiến lược triển khai
- Strategy: Rolling / Blue-Green / Canary / Recreate / Other
- Lý do:
- Batch size / traffic percentages:
- Pause và evaluation windows:
- Tiêu chí health/success:

## 5. Checkpoint theo thứ tự (migration, rollout, traffic)
Liệt kê theo đúng thứ tự thực hiện; đánh dấu bước phải hoàn tất trước rollout hoặc trước chuyển traffic, và bước được thực hiện sau rollout. Chỉ đi tiếp khi điều kiện của checkpoint hiện tại đạt.

| # | Loại (migration / config / rollout / traffic / verify) | Action | Owner | Điều kiện đi tiếp | Tiêu chí dừng (stop) | Phục hồi nếu dừng | Evidence |
|---:|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

- Tiêu chí dừng toàn cục (ngưỡng đo được, cửa sổ, người quyết định):
- Phục hồi: rollback ứng dụng, forward-fix hoặc restore dữ liệu; tham chiếu bước cụ thể trong rollback plan.
- Lưu ý: rollback ứng dụng không tự động rollback dữ liệu.

## 6. Database và cấu hình
- Thứ tự migration và loại migration:
- Backward compatibility (app cũ/mới với schema):
- Feature flags:
- Tham chiếu config/secret (không ghi giá trị):
- Data validation:

## 7. Xác minh và theo dõi
- Health endpoints:
- Smoke tests/critical journeys:
- Metrics/logs/traces, queue/background job:
- Ngưỡng error-rate/latency, KPI nghiệp vụ:
- Owner xác minh và observation window:

## 8. Rollback / phương án dự phòng
- Tham chiếu rollback plan/version:
- Owner quyết định:
- Trigger:
- Recovery time objective (nếu đã định nghĩa):
- Ràng buộc khôi phục dữ liệu:

## 9. Truyền thông
- Stakeholders/kênh:
- Thông báo bắt đầu/cập nhật/hoàn tất:
- Liên hệ escalation sự cố:

## 10. Review kế hoạch
- DevOps review:
- QA confirmation:
- Plan version được đưa vào G6 review:
- Tham chiếu hồ sơ G6 đã điền (chỉ Production):
- Tham chiếu biên bản đã điền theo mẫu [Deployment Record](../../templates/deployment/deployment-record.md):
