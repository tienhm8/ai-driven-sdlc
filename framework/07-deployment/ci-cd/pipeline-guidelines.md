# Hướng dẫn CI/CD Pipeline

## 1. Nguyên tắc
- Build once; promote cùng một artifact bất biến qua các môi trường.
- Fail safely: thiếu approval, check thất bại hoặc trạng thái không rõ đều phải chặn promotion.
- Tách biệt build identity và deployment identity.
- Áp dụng least privilege, credential ngắn hạn và protected environments.
- Làm cho pipeline run có thể tái lập, quan sát được và audit được.
- Giữ secrets ngoài source, logs, artifacts và caches.

## 2. Các stage khuyến nghị
1. **Source validation:** chính sách branch/tag và commit metadata.
2. **Quality:** format, lint, static analysis và unit test.
3. **Security:** secret scan, SAST, dependency/SCA và container/IaC scan tùy theo phạm vi.
4. **Build/package:** build deterministic, versioning, SBOM/provenance khi nền tảng hỗ trợ.
5. **Artifact publication:** registry bất biến, ghi nhận digest và kiểm soát truy cập.
6. **Non-production deploy:** dev/staging/test.
7. **Verification:** integration, smoke, contract và environment checks.
8. **Approval gate:** con người phê duyệt cho protected environment/Production.
9. **Production deploy:** chiến lược đã duyệt, có health checks và rollout được kiểm soát.
10. **Post-deploy:** verification, evidence, thông báo và bàn giao.

Điều chỉnh stage theo công nghệ và mức rủi ro; không bao giờ ghi nhận một stage đã pass khi chưa có kết quả.

## 3. Trigger và kiểm soát branch
- Định nghĩa trusted triggers (PR, protected branch, signed tag, release event).
- Không để privileged secrets lộ cho code từ fork/PR không tin cậy.
- Bảo vệ release branches/tags và yêu cầu review/status checks.
- Pin third-party actions/plugins/build images vào version tin cậy hoặc reference bất biến theo policy.
- Không deploy từ tên branch tùy ý hoặc commit ref chưa xác minh.

## 4. Tính toàn vẹn và promotion của artifact
- Gán version duy nhất và digest bất biến.
- Ghi nhận source commit, builder identity, build run và metadata dependency.
- Promote đúng artifact đã test; không build lại riêng cho Production.
- Xác minh chữ ký/attestation khi policy yêu cầu.
- Lưu giữ artifact theo chính sách release/audit.

## 5. Môi trường và secrets
- Tách cấu hình môi trường khỏi application artifact.
- Dùng secret manager được phê duyệt và identity có phạm vi giới hạn.
- Che (mask) secrets; tránh shell tracing có thể lộ credential.
- Giới hạn truy cập Production và yêu cầu phê duyệt rõ ràng.
- Review config drift và ngăn deploy chéo môi trường.

## 6. Độ tin cậy
- Thêm timeout, retry có giới hạn và kiểm soát concurrency.
- Dùng deployment lock để tránh các release xung đột.
- Định nghĩa health checks và ngưỡng abort.
- Làm các bước idempotent khi khả thi.
- Giữ logs/evidence khi có lỗi.
- Cung cấp cơ chế hủy an toàn và hành vi khi lỗi từng phần.

## 7. Quản trị và anti-pattern
Ghi nhận actor, timestamp, commit SHA, artifact digest, môi trường, version định nghĩa pipeline, approvals, checks, kết quả và hành động rollback. AI có thể soạn bản nháp thay đổi pipeline, nhưng workflow có đặc quyền và production gate bắt buộc con người review.

Tránh: dùng `latest` làm định danh artifact duy nhất; plaintext secrets; deploy Production từ branch chưa review; tắt check/approval để gỡ kẹt release; build lại artifact khác sau QA; retry không giới hạn; rollback mù quáng với thay đổi stateful.
