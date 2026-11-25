# 07 – Deployment

## Mục tiêu
Chuẩn bị, phê duyệt, phát hành và triển khai phần mềm vào môi trường mục tiêu an toàn, lặp lại được, có thể quan sát và khôi phục. Giai đoạn này tiếp nhận sản phẩm từ Development, Code Review và Testing & QA; không thay thế phê duyệt của các giai đoạn trước.

## Phạm vi
- Xác định release scope, version và artifact bất biến.
- Kiểm tra cấu hình môi trường, secrets, quyền và dependencies.
- Xây dựng/duy trì CI/CD pipeline.
- Chọn chiến lược Rolling, Blue-Green, Canary hoặc Recreate.
- Lập deployment plan, rollback plan và release notes.
- Thực hiện pre-check, deployment, smoke test, post-deployment verification.
- Ghi nhận G6 và bàn giao Monitoring & Maintenance.

## Vai trò
- **AI/Deployment Assistant:** phân tích đầu vào, đề xuất pipeline/strategy, tạo bản nháp, kiểm tra cấu hình, tổng hợp evidence.
- **Developer/Release Engineer:** chuẩn bị artifact, cấu hình và xử lý lỗi kỹ thuật.
- **DevOps Engineer:** xác minh hạ tầng, pipeline, quyền, observability và rollback.
- **QA Lead:** xác nhận G5, test evidence và smoke-test criteria.
- **Release Manager:** quyết định Go/No-Go và phê duyệt G6.
- **SRE/Operations:** xác nhận readiness, theo dõi sau triển khai và tiếp nhận bàn giao.

## Cấu trúc
- `workflow.md`: luồng triển khai.
- `ai-instructions.md`: chỉ dẫn và giới hạn AI.
- `human-review.md`: trách nhiệm, G6 và audit record.
- `inputs/`: dữ liệu bàn giao và thông tin release.
- `templates/`: biểu mẫu release/deployment/rollback/approval.
- `checklists/`: kiểm tra trước, trong và sau triển khai.
- `ci-cd/`: tiêu chuẩn pipeline và chiến lược deployment.
- `outputs/`: báo cáo và bằng chứng triển khai.

## Human Review Gate G6
G6 chỉ áp dụng cho Production, sau readiness và trước khi cấp quyền thực thi. Release Manager phê duyệt đúng artifact đã qua G5, môi trường đích và gói review đã chốt. AI chỉ hỗ trợ, không được phê duyệt G6. Dùng [checklist quyền thực thi](checklists/production-authorization-checklist.md) ngay trước khi chạy.

## Mức tự chủ L1–L4
- **L1:** tạo release note nháp, tổng hợp pipeline status, chạy kiểm tra read-only.
- **L2:** chuẩn bị pipeline/plan và deploy non-production trong phạm vi quyền được giao.
- **L3:** thay đổi pipeline dùng chung, IAM, network, production config hoặc migration cần con người review/phê duyệt.
- **L4:** Go/No-Go Production, chấp nhận rủi ro cao, rollback rủi ro cao và G6 do con người quyết định.

L1 vẫn cần log, kiểm tra tự động, quyền tối thiểu và truy vết.

## Nguyên tắc
1. Build once, promote the same immutable artifact.
2. Không đưa secret vào source, log, artifact hoặc tài liệu.
3. Ưu tiên least privilege và credential ngắn hạn.
4. Production deployment phải có approval và audit trail.
5. Đánh giá backward compatibility, backup/restore và migration.
6. Rollback ứng dụng không đồng nghĩa rollback dữ liệu.
7. Chỉ báo thành công khi health checks và verification đạt.
8. Thiếu evidence hoặc còn rủi ro chưa xử lý thì Blocked/No-Go.

## Đầu ra
Deployment plan, release notes, checklist, rollback plan, hồ sơ G6 (chỉ Production), pipeline evidence và [Deployment Record](../templates/deployment/deployment-record.md) chứa kết quả xác minh và bàn giao. Chỉ triển khai Production thành công đã xác minh mới chuyển Stage 08; rollback hoặc bàn giao thông tin sự cố không hoàn thành Stage 07.
