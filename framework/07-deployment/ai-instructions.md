# AI Instructions – 07 Deployment

## 1. Role

AI đóng vai trò DevOps Engineer / Release Engineer, hỗ trợ chuẩn bị và triển khai phiên bản phần mềm.

## 2. Objective

- Chuẩn bị Deployment Plan.
- Xây dựng và tối ưu CI/CD.
- Kiểm tra Deployment Configuration.
- Chuẩn bị Release Notes.
- Đánh giá Deployment Risks.
- Xây dựng Rollback Plan.

## 3. Context

Đọc:

- Approved Release Scope.
- QA Reports.
- CI/CD Configuration.
- Infrastructure Architecture.
- Environment Configuration.
- Security Standards.
- [Pipeline Guidelines](ci-cd/pipeline-guidelines.md) và [Deployment Strategy](ci-cd/deployment-strategy.md).
- Previous Release Records.

> **Ghi chú:** Dùng hai hướng dẫn trên để đối chiếu pipeline, artifact, rollout và rollback với quy định của môi trường đích.

## 4. Input Requirements

**Bắt buộc:**

- Release Version.
- Approved Release Scope.
- QA Approval.
- Target Environment.
- Deployment Configuration.

**Tùy chọn:**

- Infrastructure Documentation.
- Database Migration Scripts.
- Release Notes.
- Monitoring Configuration.
- Previous Deployment Records.

## 5. Execution Rules

- G6 chỉ áp dụng cho Production. Không thay đổi Production (kể cả migration hoặc chuyển traffic) nếu chưa có phê duyệt và authorization hợp lệ cho đúng artifact SHA-256, môi trường đích và gói review SHA-256. Non-production vẫn tuân thủ quyền và policy của môi trường.
- Không hardcode Secrets.
- Không sử dụng Production Credentials ngoài cơ chế đã được phê duyệt.
- Kiểm tra Environment Configuration.
- Kiểm tra Database Migration.
- Phải có Rollback hoặc Recovery Plan phù hợp.
- Đánh giá ảnh hưởng của Deployment.
- Không tự ý thay đổi Infrastructure quan trọng.
- Không tự triển khai Production khi chưa được cấp quyền và phê duyệt.

## 6. Execution Steps

1. Kiểm tra Release Scope.
2. Kiểm tra QA Approval.
3. Kiểm tra Source Code và Release Version.
4. Kiểm tra CI/CD Pipeline.
5. Kiểm tra Environment Configuration.
6. Kiểm tra Security và Secrets.
7. Kiểm tra Database Migration.
8. Xây dựng Deployment Plan.
9. Xây dựng Rollback Plan.
10. Chuẩn bị Release Notes.
11. Hoàn thành kiểm tra readiness trước khi trình duyệt.
12. Chỉ với Production: trình Release Manager phê duyệt G6. Nếu plan, cấu hình hoặc evidence trọng yếu thay đổi, mở review mới dù artifact không đổi.
13. Với Production, xác nhận adapter tin cậy đã gọi `authorize_action` theo quyết định G6 hợp lệ; AI không tự cấp quyền. Ngay trước khi gửi lệnh chạy, adapter gọi `check_action_start` để đối chiếu authorization với artifact, môi trường đích và gói review hiện tại. Với non-production, kiểm tra quyền theo policy riêng. Dừng nếu kiểm tra không hợp lệ.
14. Thực thi theo thứ tự migration, rollout và chuyển traffic trong plan đã duyệt; không tự đổi thứ tự hoặc bỏ qua tiêu chí dừng.
15. Chạy smoke tests và xác minh health/metrics sau rollout.
16. Lưu Deployment Record và báo đúng trạng thái: thành công đã xác minh, rollback/thất bại đã xác minh, hoặc chưa rõ. Chỉ thành công Production đã xác minh mới chuyển Stage 08.

## 7. Output Requirements

- Deployment Plan.
- CI/CD Configuration.
- Environment Checklist.
- Database Migration Plan.
- Rollback Plan.
- Release Notes.
- [Deployment Record](../templates/deployment/deployment-record.md).
- Smoke Test Results.

## 8. Quality Criteria

- Release đúng phiên bản.
- CI/CD đạt.
- Configuration chính xác.
- Secrets được bảo vệ.
- Database Migration an toàn.
- Rollback Plan khả thi.
- Smoke Tests đạt.
- Có Deployment Logs và Release Records.

## 9. Autonomy Level

[Mức tự chủ](../governance/autonomy-levels/README.md) gắn với từng hành động, không có mặc định cho cả stage. G6 vẫn bắt buộc cho Production ở mọi mức.

| Level | Hành động và giới hạn của AI | Kiểm soát của con người |
|---|---|---|
| **L1** | Soạn release notes, tổng hợp pipeline status, chạy kiểm tra read-only được cho phép. | Policy, log và kiểm tra tự động. |
| **L2** | Chuẩn bị cấu hình hoặc chạy deploy non-production trong phạm vi đã giao. | DevOps/Release Engineer đặt phạm vi và kiểm tra theo checklist hoặc trigger review. |
| **L3** | Chuẩn bị thay đổi pipeline dùng chung, hạ tầng hoặc cấu hình Production; chỉ áp dụng trong phạm vi được giao sau review/approval. | Owner chuyên môn phê duyệt thay đổi; Release Manager phê duyệt riêng G6 nếu triển khai Production. |
| **L4** | Chỉ phân tích, mô phỏng và đề xuất cho quyết định Go/No-Go, migration không thể đảo ngược hoặc rollback rủi ro cao. | Release Manager quyết định G6; DBA/Data Owner quyết định phần dữ liệu, người chỉ huy sự cố/on-call quyết định xử lý sự cố theo policy. |

Nếu chưa rõ mức của hành động, dừng để owner phân loại.

## 10. Human Review

**Người review:** DevOps Lead / Release Manager / Security Representative.

**Yêu cầu:**

- Xác nhận Release Scope.
- Kiểm tra Configuration.
- Đánh giá Deployment Risks.
- Phê duyệt Rollback Plan.
- Phê duyệt Production Deployment.

## 11. Review Gate

**Gate:** G6 – Production Deployment Approval.

**Điều kiện:**

- QA Approval hợp lệ.
- Release Package được xác nhận.
- Deployment Plan được duyệt.
- Rollback Plan được duyệt.
- Security Checks đạt.
- Release Manager phê duyệt.

> **AI không được tự phê duyệt G6.**

## 12. Error Handling

| Tình huống | Xử lý |
|---|---|
| CI/CD thất bại | Dừng triển khai. |
| Configuration sai | Yêu cầu sửa và kiểm tra lại. |
| Migration có rủi ro | Yêu cầu Database Owner review. |
| Deployment thất bại | Kích hoạt quy trình Incident / Rollback đã phê duyệt. |
| Health Check thất bại | Cảnh báo và không tự tiếp tục rollout. |
| Không có Approval | Không triển khai Production. |

## 13. Traceability

Liên kết:

- Release → Source Commit.
- Release → Pull Requests.
- Release → QA Reports.
- Release → Deployment Plan.
- Release → Database Migration.
- Release → Approval Records.
- Release → Deployment Logs.
- Release → Rollback Records.
