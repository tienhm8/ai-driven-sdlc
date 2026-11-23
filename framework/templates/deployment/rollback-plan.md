# Kế hoạch Rollback / Recovery

## Metadata
- Plan ID: `RB-{{NUMBER}}`
- Release / Deployment ID:
- Service / Environment:
- Owner:
- Người review:
- Lần test gần nhất:

## 1. Trigger rollback
| Tín hiệu / điều kiện | Ngưỡng | Khoảng thời gian theo dõi | Người quyết định |
|---|---|---|---|
| Error rate | {{THRESHOLD}} | {{WINDOW}} | {{ROLE}} |

Đánh giá ngưỡng theo SLO và policy của dịch vụ; không dùng ngưỡng ví dụ làm mặc định cho production.

## 2. Tác động và phụ thuộc
- Thành phần bị ảnh hưởng:
- Tương thích database/schema:
- Dependency bên ngoài:
- Dữ liệu do phiên bản mới ghi ra:
- Thao tác không thể hoàn tác:

## 3. Quy trình recovery
| Bước | Hành động | Owner | Kết quả kỳ vọng | Kiểm tra |
|---:|---|---|---|---|
| 1 | {{ACTION}} | {{OWNER}} | {{RESULT}} | {{CHECK}} |

## 4. Khôi phục dữ liệu
- Tham chiếu backup/snapshot:
- Restore point:
- Đối soát dữ liệu:
- Khoảng thời gian mất dữ liệu:
- Yêu cầu phê duyệt:

## 5. Xác minh sau rollback
- [ ] Sức khỏe dịch vụ đã được khôi phục.
- [ ] Các user journey quan trọng pass.
- [ ] Tính nhất quán dữ liệu đã được kiểm tra.
- [ ] Monitoring ổn định trong khoảng thời gian theo dõi.
- [ ] Stakeholder đã được thông báo.

## 6. Truyền thông và escalation
- Kênh xử lý sự cố:
- Incident Commander:
- Liên hệ escalation:
- Người chịu trách nhiệm thông điệp gửi khách hàng/stakeholder:

## 7. Phê duyệt và bằng chứng test
- Người review kỹ thuật:
- Release Manager:
- Timestamp phê duyệt:
- Bằng chứng diễn tập rollback gần nhất:
