# Example – Code Review Report

> Dữ liệu minh họa, không phải kết quả review một repository thực tế.

## Metadata
- Repository: `sample-service`
- PR: `#123`
- Base SHA: `abc0000`
- Head SHA: `def1111`
- Report version: `1`
- Human reviewer: `Pending`

## Summary
- Recommendation: **Request Changes**
- Findings: Critical 0 / High 1 / Medium 1 / Low 0 / Info 1
- CI: Not verified in this example
- Limitation: Không có repository/diff thực tế để xác minh.

## Findings

### [CR-001] [High] – Endpoint thiếu kiểm tra quyền trên resource
- Category: Authorization
- Location: `src/example/ResourceController.cs` (minh họa)
- Status: Open
- Evidence: Minh họa tình huống endpoint nhận `resourceId` từ request nhưng không thể hiện kiểm tra resource ownership/permission.
- Impact: Người dùng có thể truy cập resource ngoài phạm vi quyền nếu không có kiểm soát ở tầng khác.
- Recommendation: Thực hiện authorization server-side trên resource và bổ sung test truy cập chéo user/tenant.
- Verification: Cần kiểm tra implementation và integration test thực tế.

### [CR-002] [Medium] – Thiếu test cho trường hợp input rỗng
- Category: Testing
- Location: `tests/example` (minh họa)
- Status: Open
- Evidence: Bộ test giả định input hợp lệ; chưa có test empty/null.
- Impact: Regression có thể không được phát hiện.
- Recommendation: Bổ sung test boundary và validation failure.

### [CR-003] [Info] – Bổ sung mô tả rollback
- Category: Release
- Location: PR description
- Status: Need Clarification
- Evidence: Mẫu PR chưa có hướng dẫn rollback cho thay đổi có migration.
- Impact: Khó phục hồi nếu release gặp lỗi.
- Recommendation: Ghi rõ migration/rollback nếu thay đổi thực tế yêu cầu.

## Decision
- AI recommendation: Request Changes
- Human G4 decision: Pending
- Approver / timestamp: Pending
