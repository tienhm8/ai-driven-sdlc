# Kế hoạch triển khai (Deployment Plan)

## 1. Metadata
- Project/service:
- Release ID/version:
- Change/ticket:
- Repository:
- Commit SHA:
- Artifact URI and digest:
- Target environment/region:
- Deployment owner:
- Release Manager:
- Planned window and timezone:

## 2. Phạm vi và rủi ro
- Thay đổi bao gồm/loại trừ:
- Dependencies:
- Tác động dự kiến đến người dùng/downtime:
- Mức rủi ro và lý do:

## 3. Điều kiện tiên quyết
- G4 approval:
- G5 sign-off:
- CI/build/test/security evidence:
- Environment readiness:
- Access/approval:
- Backup/restore status:
- Monitoring readiness:

## 4. Chiến lược triển khai
- Strategy: Rolling / Blue-Green / Canary / Recreate / Other
- Lý do:
- Batch size / traffic percentages:
- Pause và evaluation windows:
- Tiêu chí health/success:
- Abort/rollback triggers:

## 5. Các bước thực thi
| # | Action | Expected result | Owner | Evidence/checkpoint |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## 6. Database và cấu hình
- Các bước migration:
- Backward compatibility:
- Feature flags:
- Tham chiếu config/secret:
- Data validation:

## 7. Xác minh
- Health endpoints:
- Smoke tests/critical journeys:
- Metrics/logs/traces:
- Ngưỡng error-rate/latency:
- Owner xác minh và thời lượng:

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

## 10. Phê duyệt
- DevOps review:
- QA confirmation:
- Release Manager G6 decision:
- Timestamp:
- Approved plan version:
