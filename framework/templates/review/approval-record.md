# Biên bản Phê duyệt (Approval Record)

## Metadata
- Approval ID: `APR-{{NUMBER}}`
- Gate / subject: G1 / G2 / G3 / G4 / G5 / G6 / G7 / Other
- Project / workflow:
- Artifact ID / tham chiếu / version / commit SHA hoặc hash:
- Review package version / hash:
- Người yêu cầu / thời điểm yêu cầu:
- Vai trò approver bắt buộc:
- Phạm vi được duyệt / phần ngoài phạm vi (nếu có):
- Đích đã duyệt (nếu áp dụng, ví dụ PR/nhánh đích hoặc môi trường):
- Audit event ID / vị trí bản ghi kiểm toán:

## Tiêu chí phê duyệt
| Tiêu chí | Bằng chứng / link | Kết quả |
|---|---|---|
| {{CRITERION}} | {{EVIDENCE}} | Pass / Fail / N/A |

## Kết luận chuyên môn
| Phạm vi | Reviewer / vai trò | Kết luận / thời điểm | Bằng chứng | Phê duyệt chuyên môn bắt buộc (nếu áp dụng) |
|---|---|---|---|---|

Reviewer ghi kết luận trong phạm vi của mình; phê duyệt chuyên môn bắt buộc phải có bằng chứng theo policy hoặc phạm vi dự án.

## Quyết định
- Gate status: Pending / In Review / Approved / Rejected / Blocked / Changes Requested
- Lý do, điều kiện bắt buộc chưa đóng hoặc blocker / bằng chứng xử lý:

| Approver | Vai trò / thẩm quyền | Quyết định | Timestamp / múi giờ | Phiên bản artifact / review | Bằng chứng |
|---|---|---|---|---|---|

Quyết định của approver: `Approved / Rejected / Changes Requested / Blocked`. `Pending` và `In Review` là trạng thái, không phải quyết định. Điều kiện bắt buộc chưa đóng chặn approval: dùng `Changes Requested`, không dùng `Conditional` làm quyết định gate. Ghi đầy đủ các approver theo gate policy; G5 cần hai người riêng biệt theo vai trò yêu cầu.

## Action không chặn
Không dùng action mở để che giấu điều kiện gate chưa đáp ứng.

| Action / phạm vi | Owner | Hạn xử lý | Theo dõi / bằng chứng |
|---|---|---|---|

## Waiver / ngoại lệ
Ghi waiver hợp lệ, phạm vi, lý do, rủi ro, giảm thiểu, owner, người có thẩm quyền chấp nhận, bằng chứng và thời hạn. Ngoại lệ tuân theo gate policy, không tự thay thế quyết định approval hoặc xóa quyết định Reject/Blocked hiện hành.

| Waiver / phạm vi / lý do | Rủi ro / giảm thiểu | Owner | Người chấp nhận / bằng chứng | Hết hạn |
|---|---|---|---|---|

## Kiểm toán và toàn vẹn
- Version/hash của artifact đã review:
- Tham chiếu báo cáo review / bằng chứng CI/test:
- Người ghi nhận:
- Thay thế approval ID / trigger phê duyệt lại:

> Chỉ người có thẩm quyền được phê duyệt human gate. Approval chỉ có hiệu lực với đúng artifact version/SHA và trong phạm vi thẩm quyền; thay đổi trọng yếu cần review/phê duyệt lại theo `framework/governance/human-review-gates/gate-policy.md`.
