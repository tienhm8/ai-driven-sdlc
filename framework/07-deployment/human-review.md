# Human Review – Deployment

> **Giai đoạn:** 07 – Deployment  
> **Mục đích:** Bảo đảm phiên bản được triển khai đúng, an toàn, có thể giám sát và có phương án phục hồi phù hợp với rủi ro.  
> **Review Gate:** G6 – Production Approval  
> **Người phê duyệt chính:** Release Manager / người có thẩm quyền phát hành

## 1. Nguyên tắc review

- Triển khai production là hành động có tác động thực tế; AI không được tự phê duyệt G6.
- Mức tự động hóa triển khai phải dựa trên risk profile, môi trường, khả năng rollback và policy tổ chức.
- Phải phân biệt deploy, release/enable feature và migration dữ liệu; mỗi hoạt động có thể có rủi ro và phê duyệt riêng.
- Không triển khai khi artifact, cấu hình, approval hoặc bằng chứng kiểm thử không khớp phiên bản phát hành.
- Rollback không phải lúc nào cũng an toàn, đặc biệt với thay đổi schema/data; phải có phương án recovery/forward-fix phù hợp.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| Release Manager – **Approver G6** | Điều phối release, xác nhận readiness, đánh giá rủi ro và phê duyệt production theo thẩm quyền. |
| DevOps / Platform Engineer | Review pipeline, artifact, environment, infrastructure, secrets, deployment strategy và rollback/recovery. |
| Tech Lead | Xác nhận nội dung kỹ thuật, compatibility, migration và known technical risks. |
| QA Lead | Xác nhận test evidence, QA sign-off và các known issues liên quan release. |
| Product Owner / Business Owner | Xác nhận thời điểm, phạm vi phát hành và tác động nghiệp vụ khi cần. |
| Security / Compliance | Phê duyệt security exception, thay đổi nhạy cảm hoặc yêu cầu tuân thủ theo policy. |
| SRE / Operations | Xác nhận monitoring, alert, capacity, on-call và operational readiness. |

## 3. Trách nhiệm review của con người

1. **Release scope:** Release version, commit/tag, artifact và danh sách thay đổi khớp release note.
2. **Approval status:** G1–G5 và các approval liên quan đã hoàn tất; waiver/exception có đúng người phê duyệt.
3. **Artifact integrity:** Artifact được build từ nguồn tin cậy, có version/checksum/provenance phù hợp và không bị thay đổi ngoài pipeline.
4. **Environment & configuration:** Environment, config, feature flags, secrets, permissions và network rules đúng; không lộ secret.
5. **CI/CD safety:** Pipeline có kiểm soát quyền, approval, separation of duties, log và cơ chế dừng khi check thất bại.
6. **Compatibility:** Tương thích giữa phiên bản ứng dụng, API, database, client và dịch vụ phụ thuộc.
7. **Migration safety:** Migration có rehearsal khi cần, đánh giá lock/downtime/data loss, backup/restore và backward compatibility.
8. **Deployment strategy:** Rolling, blue-green, canary hoặc phương án khác phù hợp; blast radius được giới hạn.
9. **Rollback/recovery:** Trigger rollback, người quyết định, bước thực hiện, giới hạn và phương án forward-fix/data recovery rõ ràng.
10. **Observability:** Dashboard, alert, health check, log, trace và baseline trước/sau deploy sẵn sàng.
11. **Operational readiness:** On-call, runbook, support, capacity, maintenance window và stakeholder communication đã chuẩn bị.
12. **Release risk:** Known issues, security findings, residual risks và business impact được công khai.
13. **Go/no-go:** Có quyết định go/no-go rõ ràng bởi người có thẩm quyền trước production.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể tạo release note nháp, kiểm tra cấu hình tĩnh hoặc tổng hợp trạng thái pipeline; không được tự cấp quyền production. |
| L2 | DevOps/Release Manager giới hạn phạm vi triển khai tự động ở non-production và kiểm tra theo checklist hoặc điều kiện kích hoạt review. Không áp dụng L2 để triển khai Production. |
| L3 | Bắt buộc review và phê duyệt trước thay đổi production có ảnh hưởng logic, API, schema, quyền, dữ liệu hoặc hạ tầng quan trọng. |
| L4 | Con người trực tiếp quyết định production release rủi ro cao, migration không thể đảo ngược, security exception hoặc release có blast radius lớn; AI chỉ tư vấn. |

**Quy tắc:** Mức tự chủ gắn với từng hành động. Tự động hóa pipeline không đồng nghĩa tự động hóa quyền phê duyệt; G6 chỉ áp dụng cho Production và vẫn bắt buộc ở mọi mức rủi ro.

## 5. Checklist G6

- [ ] Release scope, version, tag và artifact đã xác định.
- [ ] Các Gate/approval bắt buộc trước đó đã hoàn tất.
- [ ] QA sign-off và known issues được xác nhận.
- [ ] Artifact provenance/integrity được kiểm tra.
- [ ] Config, secrets, permissions và environment đã được kiểm tra.
- [ ] Security scan và policy checks đạt hoặc exception được duyệt.
- [ ] Migration/backup/restore/recovery plan được review.
- [ ] Deployment strategy và blast radius phù hợp.
- [ ] Rollback/forward-fix criteria và người quyết định đã rõ.
- [ ] Monitoring, alerting, dashboard và on-call sẵn sàng.
- [ ] Release communication và support plan đã chuẩn bị.
- [ ] Release Manager ghi nhận quyết định Go/No-Go.

## 6. Điều kiện quyết định G6

**Go / Approve** khi artifact đúng phiên bản, approval hợp lệ, kiểm tra an toàn đạt, kế hoạch triển khai và phục hồi khả thi, monitoring/on-call sẵn sàng và residual risk được chấp nhận đúng thẩm quyền.

**No-Go / Reject** khi thiếu approval, artifact không xác định được nguồn gốc, test/sign-off không hợp lệ, migration không an toàn, rollback/recovery không phù hợp hoặc có rủi ro vượt ngưỡng.

Nếu triển khai theo canary/progressive delivery, tiêu chí tiếp tục, dừng và rollback phải được định nghĩa trước. Việc mở rộng rollout là một quyết định release theo policy, không dựa riêng vào đánh giá của AI.

## 7. Khi yêu cầu AI làm lại

Reviewer nêu rõ release/version, cấu hình hoặc bước triển khai cần điều chỉnh, rủi ro và điều kiện đạt. AI có thể cập nhật tài liệu/pipeline đề xuất. DevOps kiểm tra thay đổi; Release Manager thực hiện lại đánh giá Go/No-Go. Không cho AI tự sửa production config rồi áp dụng ngoài cơ chế change control.

## 8. Bằng chứng và hồ sơ review

Lưu quyết định, approver, thời điểm và tham chiếu gói review trong [hồ sơ G6](templates/production-approval.md). Quyết định phải khớp artifact SHA-256, môi trường đích và SHA-256 của gói review; thay đổi trọng yếu thì review lại. Sau khi phê duyệt, dùng [checklist quyền thực thi](checklists/production-authorization-checklist.md) ngay trước khi chạy. Ghi sự kiện thực thi, kết quả xác minh và bàn giao riêng trong [Deployment Record](../templates/deployment/deployment-record.md).

## 9. Trách nhiệm cuối cùng

Release Manager chịu trách nhiệm quyết định Go/No-Go trong phạm vi được ủy quyền. DevOps chịu trách nhiệm triển khai theo quy trình và xác nhận kỹ thuật. Tech Lead, QA, Security và SRE chịu trách nhiệm đánh giá chuyên môn tương ứng. AI không được tự phê duyệt hoặc tự thực hiện hành động production vượt quyền.
