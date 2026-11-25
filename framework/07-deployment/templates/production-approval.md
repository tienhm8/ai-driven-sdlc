# Phê duyệt triển khai Production – G6

> Đây là nơi duy nhất ghi quyết định G6. Plan chỉ tham chiếu file này; việc thực thi, sai lệch, sự cố và bàn giao nằm trong deployment record dùng chung.

## 1. Gói review bất biến và ràng buộc phê duyệt
- Project/service:
- Release ID/version:
- Environment / canonical target (cluster/region/account/namespace):
- Commit SHA:
- Artifact digest (SHA-256):
- Deployment plan (link, version):
- Rollback plan (link, version):
- Immutable review package (link/URI) và SHA-256:
- G5 sign-off (link, version/SHA-256):
- Change record / tham chiếu ngoại lệ được duyệt (nếu có):
- Planned window/timezone:
- Release owner:

Phê duyệt chỉ hiệu lực cho đúng artifact digest, canonical target và review package SHA-256 ở trên. Bất kỳ thay đổi nào cần review/phê duyệt lại.

## 2. Evidence sẵn sàng
| Yêu cầu | Trạng thái | Evidence/link | Reviewer |
|---|---|---|---|
| G4 code review approval | | | |
| G5 QA sign-off | | | |
| CI/build/test | | | |
| Security checks | | | |
| Artifact provenance/integrity | | | |
| Environment/config readiness | | | |
| Backup/restore và migration review | | | |
| Monitoring/alert readiness | | | |
| Rollback plan đã review | | | |
| Communication/on-call readiness | | | |

## 3. Đánh giá rủi ro
- Tác động đến người dùng/nghiệp vụ:
- Downtime:
- Rủi ro dữ liệu/bảo mật:
- Dependencies:
- Known issues:
- Mitigations:
- Ngoại lệ và risk owner:

## 4. Quyết định
- [ ] Approved / Go
- [ ] Rejected / No-Go
- [ ] Blocked / Deferred

Lý do quyết định:
Điều kiện/giới hạn:

Triển khai khẩn cấp vẫn cần quyết định G6 hợp lệ, không phải một loại quyết định riêng. Nếu dùng ngoại lệ theo [gate policy](../../governance/human-review-gates/gate-policy.md#ngoại-lệ), ghi tham chiếu ngoại lệ đã duyệt và thời điểm hết hiệu lực (kèm múi giờ). Không thực thi sau khi ngoại lệ hết hạn.

## 5. Phê duyệt của con người
> Phân tích do AI tạo ra chỉ là evidence hỗ trợ. AI không được phê duyệt, ký hoặc điền quyết định G6; chỉ người có thẩm quyền ký phần này.

- Release Manager:
- Vai trò:
- Timestamp/timezone:
- Approval reference:
- Người phê duyệt bổ sung:

## 6. Liên kết bản ghi thực thi
- Tham chiếu biên bản đã điền theo mẫu [Deployment Record](../../templates/deployment/deployment-record.md):
- Deployment ID:

Không lặp lại chi tiết thực thi, kết quả hay bàn giao tại đây; chúng chỉ được ghi trong deployment record.
