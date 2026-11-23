# Kế hoạch Triển khai (Deployment Plan)

## Metadata
- Deployment ID: `DEP-{{NUMBER}}`
- Project / Service:
- Release version:
- Environment: Development / Staging / Production
- Change / PR references:
- Deployment owner:
- Thời gian dự kiến bắt đầu/kết thúc (timezone):
- Status: Draft / Reviewed / Approved / Executing / Completed / Failed

## 1. Phạm vi phát hành
- Thay đổi được đưa vào:
- Thay đổi không đưa vào:
- Requirement liên quan:
- Dependencies:

## 2. Mức độ sẵn sàng (Readiness)
- [ ] Release artifact/version đã được xác minh.
- [ ] Kiểm tra CI/build/test đã pass.
- [ ] Đã hoàn tất kiểm tra bảo mật và cấu hình.
- [ ] Database migration đã được review (nếu có).
- [ ] Monitoring và alerting đã sẵn sàng.
- [ ] Đã xác nhận sẵn sàng backup/recovery khi cần.
- [ ] Rollback plan đã được review/test.
- [ ] Stakeholder đã được thông báo.

## 3. Các bước triển khai
| Thứ tự | Bước | Owner | Kết quả kỳ vọng | Kiểm tra |
|---:|---|---|---|---|
| 1 | {{STEP}} | {{OWNER}} | {{RESULT}} | {{CHECK}} |

## 4. Health check
- Smoke test:
- Endpoint quan trọng:
- Error rate / latency:
- Queue / background job:
- KPI nghiệp vụ:
- Khoảng thời gian theo dõi (observation window):

## 5. Truyền thông
- Stakeholder/kênh:
- Thông báo bắt đầu:
- Thông báo hoàn tất:
- Liên hệ escalation:

## 6. Rủi ro và phương án dự phòng
- Rủi ro đã biết:
- Biện pháp giảm thiểu:
- Tham chiếu rollback plan:

## 7. Phê duyệt G6
| Vai trò | Tên | Quyết định | Timestamp | Bằng chứng |
|---|---|---|---|---|
| Release Manager | {{NAME}} | Pending | | |
| Approver kỹ thuật/bảo mật bắt buộc | {{NAME}} | Pending | | |
