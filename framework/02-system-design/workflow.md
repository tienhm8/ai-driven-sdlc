# Workflow — System Design

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 2. Giai đoạn 02 — System Design

## 2.1 Purpose — Mục đích

Chuyển yêu cầu đã duyệt thành thiết kế giải pháp có thể triển khai, bao gồm kiến trúc, thành phần, dữ liệu, API, tích hợp, bảo mật, triển khai và các quyết định kỹ thuật. Đảm bảo thiết kế đáp ứng FR/NFR và có thể truy vết về requirement baseline.

## 2.2 Workflow Overview — Tổng quan luồng xử lý

```text
Approved Requirements + NFR
        ↓
Architecture Drivers & Constraints
        ↓
Architecture Options & Trade-off
        ↓
Logical / Component / Data / API Design
        ↓
Security, Reliability & Deployment Design
        ↓
Architecture Review
        ↓
G2 — Approve Design Baseline
        ↓
Handoff to Task Planning
```

## 2.3 Entry Criteria — Điều kiện bắt đầu

- G1 đã được phê duyệt; requirement baseline có version rõ ràng.
- Có RTM, NFR, business rules, constraints và open issues.
- Có project technology context hoặc quy trình để đề xuất/lựa chọn công nghệ.
- Các tiêu chuẩn kiến trúc, API, database, security và documentation liên quan đã được xác định.

## 2.4 Workflow Steps — Các bước thực hiện

1. **Tiếp nhận yêu cầu:** rà soát requirement baseline, NFR, rủi ro và các điểm chưa đóng.
2. **Xác định architecture drivers:** phân loại yêu cầu chi phối kiến trúc như scale, latency, availability, security, cost và integration.
3. **Khảo sát hiện trạng và ràng buộc:** đánh giá hệ thống hiện có, nền tảng, kỹ năng đội ngũ, license, cloud/on-premise và compliance.
4. **Đề xuất phương án:** xây dựng một hoặc nhiều phương án kiến trúc; mô tả ưu/nhược điểm, chi phí, rủi ro và trade-off.
5. **Chọn kiến trúc mục tiêu:** xác định style/pattern phù hợp (monolith, modular monolith, microservices, event-driven...) dựa trên drivers, không chọn theo xu hướng.
6. **Thiết kế logical và component:** phân ranh giới module/service, trách nhiệm, dependency, interface và luồng tương tác.
7. **Thiết kế dữ liệu:** domain model, ERD/schema, ownership, lifecycle, migration, backup/retention và phân loại dữ liệu.
8. **Thiết kế API và integration:** contract, versioning, authentication, authorization, idempotency, error model, timeout/retry và event schema.
9. **Thiết kế security/privacy:** threat modeling, trust boundary, secrets, encryption, access control, audit và data minimization.
10. **Thiết kế reliability/operations:** capacity, scaling, failure mode, observability, backup/restore, DR, deployment topology và rollback.
11. **Đánh giá thiết kế:** kiểm tra traceability, NFR, security, operability, maintainability và chi phí.
12. **Ghi nhận ADR:** lưu Architecture Decision Records cho quyết định quan trọng và phương án bị loại.
13. **Review và phê duyệt:** tổ chức architecture review, xử lý findings và trình G2.

## 2.5 Input — Đầu vào

- Requirement baseline, RTM, NFR và acceptance criteria.
- Business/domain model, quy trình nghiệp vụ và integration landscape.
- Technology stack, platform constraints và tiêu chuẩn nội bộ.
- Security/compliance requirements, threat/risk register.
- Kiến trúc hiện trạng, dữ liệu và quyết định kỹ thuật đã có.

## 2.6 AI Activities — Hoạt động AI

- Phân tích architecture drivers và lập checklist coverage theo NFR.
- Đề xuất phương án kiến trúc, component boundaries và trade-off.
- Sinh sơ đồ C4/UML/sequence/data flow ở dạng văn bản hoặc mã nguồn sơ đồ.
- Đề xuất API contract, schema, data model và integration patterns.
- Thực hiện threat-model brainstorming và chỉ ra trust boundaries/attack surfaces.
- Kiểm tra consistency giữa design, requirement, API và data model.
- Soạn ADR, architecture review checklist và danh sách câu hỏi cần chuyên gia xác nhận.
- Không tự quyết định kiến trúc cuối cùng hoặc khẳng định thiết kế an toàn chỉ dựa trên phân tích AI.

## 2.7 Human Activities — Hoạt động con người

- SA chịu trách nhiệm lựa chọn kiến trúc và giải trình trade-off.
- BA/PO xác nhận thiết kế không làm sai lệch nghiệp vụ.
- Security/Compliance review threat model, dữ liệu và kiểm soát.
- Developer/QA/DevOps đánh giá khả năng triển khai, kiểm thử và vận hành.
- Các technical owner xác nhận contract, data ownership và dependency.

## 2.8 Output — Đầu ra

- Software/System Architecture Document.
- Architecture diagrams (context, container, component, deployment, sequence/data flow khi cần).
- Component/module design và interface contracts.
- ERD/data model, data dictionary và migration strategy.
- API specifications / event contracts.
- Security design và threat model.
- Deployment/operations design, reliability strategy.
- ADR set, design risks và updated RTM.
- Design Review Record và tham chiếu approval record G2.

## 2.9 Quality Check — Kiểm tra chất lượng

- Thành phần và ranh giới trách nhiệm rõ; dependency hợp lý.
- Thiết kế truy vết được tới requirement và NFR.
- API/data contract có versioning, validation, error handling và security.
- Data ownership, retention, migration và backup được xác định.
- Threat model bao phủ trust boundary và tài sản quan trọng.
- Có phương án quan sát, phục hồi, rollback và xử lý failure.
- ADR ghi rõ bối cảnh, quyết định, hệ quả và trạng thái.
- Không có critical design issue chưa có phương án xử lý.

## 2.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G2 — Architecture & Design Approval**

- **Approver G2:** Solution Architect được ủy quyền ra quyết định G2 và, khi G2 `Approved`, chốt đúng phiên bản design package làm baseline. Nếu thiếu người có thẩm quyền, gate `Blocked` theo policy.
- **Reviewer chuyên môn:** Tech Lead và các chuyên gia Security, Data, Compliance, vận hành hoặc lĩnh vực khác review và ghi kết luận, phạm vi, người review và bằng chứng. Họ không mặc nhiên là approver G2; phê duyệt chuyên môn là bắt buộc khi policy hoặc phạm vi dự án yêu cầu và phải hoàn tất trước G2 `Approved`.
- Quyết định chính thức được ghi trong approval record theo gate policy; checklist giữ tiêu chí và bằng chứng, package index chỉ tham chiếu hồ sơ quyết định.

Điều kiện duyệt:
- Kiến trúc đáp ứng requirement/NFR và constraints.
- Trade-off, chi phí, rủi ro và quyết định quan trọng minh bạch.
- Security, data, integration và operability đã được review.
- Findings critical/high đã đóng hoặc có risk acceptance hợp lệ.

## 2.11 Exit Criteria — Điều kiện hoàn thành

- G2 Approved; Solution Architect được ủy quyền chốt phiên bản design package đã duyệt làm baseline, ghi quyết định và phiên bản trong approval record; package index tham chiếu hồ sơ đó.
- Design baseline, ADR và contract được version hóa.
- Các dependency và technical risks có owner.
- Đủ thông tin để phân rã công việc, ước lượng và lập kế hoạch.

## 2.12 Exception Handling — Xử lý ngoại lệ

- **Không có phương án đáp ứng NFR:** quay lại làm rõ requirement/NFR hoặc đề xuất thay đổi phạm vi; không che giấu gap.
- **Phụ thuộc hệ thống ngoài chưa xác nhận:** đánh dấu dependency, lập spike/prototype và owner xác minh.
- **Thay đổi kiến trúc lớn:** tạo ADR mới, phân tích tác động và mở lại G2 nếu ảnh hưởng baseline.
- **Bất đồng kỹ thuật:** ghi nhận options và decision owner; không để AI tự phân xử.
- **Rủi ro bảo mật nghiêm trọng:** dừng phê duyệt phần liên quan cho tới khi có biện pháp hoặc risk acceptance hợp lệ.

## 2.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao design baseline, ADR, API/data contracts, dependency map, NFR và risk register cho **03 — Task Planning**.

---
