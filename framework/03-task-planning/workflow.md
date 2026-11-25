# Workflow — Task Planning

> Tài liệu workflow cấp framework cho giai đoạn này. Tuân thủ governance, standards và template dùng chung trong `framework/`; các cấu hình riêng của dự án được kế thừa từ `projects/<Project>/.ai-sdlc/`.

# 3. Giai đoạn 03 — Task Planning

## 3.1 Purpose — Mục đích

Phân rã requirement và design baseline thành backlog, work packages và tasks có thể giao, ước lượng, theo dõi và nghiệm thu. Xác định thứ tự, phụ thuộc, nguồn lực, tiêu chí hoàn thành và kế hoạch kiểm soát rủi ro trước khi phát triển.

## 3.2 Workflow Overview — Tổng quan luồng xử lý

```text
Approved Requirement + Design
        ↓
Scope & Delivery Strategy
        ↓
Breakdown into Epics / Stories / Tasks
        ↓
Estimate, Sequence & Dependency Analysis
        ↓
Assign Owners & Define DoR / DoD
        ↓
Plan Review
        ↓
G3 — Approve Execution Readiness
        ↓
Handoff to Development
```

## 3.3 Entry Criteria — Điều kiện bắt đầu

- G1 đã được phê duyệt; G2 `Passed` cho đúng phiên bản design package đã chốt làm baseline, kèm bằng chứng hợp lệ.
- Có requirement/design baseline và danh sách rủi ro/phụ thuộc.
- Xác định được delivery approach, team/role và công cụ quản lý backlog.
- Các constraint về ngân sách, thời hạn, môi trường và nguồn lực đã được cung cấp ở mức phù hợp.

## 3.4 Workflow Steps — Các bước thực hiện

1. **Xác nhận phạm vi release/iteration:** thống nhất mục tiêu, deliverables, in-scope/out-of-scope và giới hạn.
2. **Phân rã backlog:** tạo epic/feature/story/work package; liên kết về requirement ID và design component.
3. **Phân rã technical tasks:** tạo task cho code, database, API, integration, security, infrastructure, documentation và testing.
4. **Xác định tiêu chí sẵn sàng:** áp dụng Definition of Ready (DoR) cho story/task; làm rõ acceptance criteria và dependency.
5. **Ước lượng:** sử dụng phương pháp phù hợp (story points, ideal days, t-shirt sizing hoặc effort range); ghi rõ độ tin cậy và giả định.
6. **Phân tích phụ thuộc:** xác định thứ tự, critical path, external dependency, environment/data dependency và integration sequence.
7. **Lập kế hoạch kiểm thử:** liên kết task với test level, test data, automation và non-functional validation.
8. **Phân công và capacity planning:** xác định owner, reviewer, skill requirement và workload; không giao task vượt quyền AI agent.
9. **Lập kế hoạch rủi ro:** đánh giá risk, mitigation, contingency và trigger.
10. **Thiết lập Definition of Done (DoD):** quy định code, test, review, documentation, security và traceability cần có.
11. **Lập milestone/release plan:** xác định mốc, deliverable, acceptance, buffer và reporting.
12. **Kiểm tra tính khả thi:** rà soát scope, estimate, capacity, dependency và risk; điều chỉnh kế hoạch.
13. **Trình G3:** phê duyệt execution baseline và lưu kế hoạch.

## 3.5 Input — Đầu vào

- Requirement baseline, RTM, acceptance criteria.
- Design baseline, ADR, component/API/data contracts.
- Release objective, deadline, budget và capacity.
- Team structure, skill matrix, lịch nghỉ và availability.
- Risk register, dependency list, environment constraints.
- Testing strategy và Definition of Done cấp tổ chức/dự án.

## 3.6 AI Activities — Hoạt động AI

- Đề xuất backlog breakdown và mapping requirement → epic/story/task.
- Phát hiện task thiếu acceptance criteria, owner, dependency hoặc test coverage.
- Đề xuất estimate range dựa trên dữ liệu lịch sử được phép; nêu rõ độ tin cậy.
- Đề xuất sequencing, milestone và critical path.
- Tạo draft sprint/release plan, risk register và dependency matrix.
- Kiểm tra tính nhất quán giữa backlog, design và RTM.
- Đề xuất DoR/DoD theo chuẩn framework.
- Không tự cam kết deadline, capacity hoặc estimate chính thức thay cho delivery owner.

## 3.7 Human Activities — Hoạt động con người

- PM/Delivery Lead chịu trách nhiệm kế hoạch, capacity, tiến độ và rủi ro.
- PO quyết định ưu tiên và trade-off phạm vi.
- SA/Tech Lead xác nhận phân rã kỹ thuật và dependency.
- Developer/QA/DevOps xác nhận effort, feasibility và điều kiện thực hiện.
- Team thống nhất DoR/DoD và cách theo dõi tiến độ.

## 3.8 Output — Đầu ra

- Product/Engineering Backlog (epic, story, task).
- Work Breakdown Structure và task-to-requirement mapping.
- Estimate, capacity plan và resource assignment.
- Dependency matrix, milestone/release plan.
- Risk register và mitigation plan.
- DoR/DoD, sprint/iteration plan.
- Test task mapping và execution readiness checklist.
- G3 approval record.

## 3.9 Quality Check — Kiểm tra chất lượng

- Mỗi task truy vết được tới requirement hoặc technical objective.
- Task đủ nhỏ để giao và theo dõi; có owner và acceptance/ completion criteria.
- Dependency, external blocker và critical path được nhận diện.
- Estimate có giả định và độ tin cậy; capacity không bị tính trùng.
- Có task cho testing, security, migration, documentation và operations khi cần.
- DoR/DoD rõ và phù hợp.
- Rủi ro high/critical có owner, mitigation và contingency.

## 3.10 Human Review Gate — Điểm phê duyệt bắt buộc

**G3 — Planning & Execution Readiness Approval**

Người phê duyệt: Project Manager/Delivery Lead và Product Owner; Tech Lead/SA xác nhận tính khả thi kỹ thuật.

Điều kiện duyệt:
- Scope, priority, estimate và milestone được thống nhất.
- Team/capacity và dependency khả thi.
- DoR/DoD, test work và risk mitigation đã được xác định.
- Không có blocker critical chưa có kế hoạch xử lý.

## 3.11 Exit Criteria — Điều kiện hoàn thành

- G3 được Approved.
- Backlog và kế hoạch thực thi được baseline.
- Task đầu tiên đạt DoR; môi trường/công cụ cần thiết sẵn sàng hoặc có kế hoạch.
- Owner và reporting cadence được xác định.

## 3.12 Exception Handling — Xử lý ngoại lệ

- **Estimate thiếu dữ liệu:** tạo spike/timebox, dùng range và ghi confidence thấp.
- **Capacity không đủ:** giảm scope, đổi milestone hoặc bổ sung nguồn lực qua quyết định của PO/PM.
- **Dependency chưa sẵn sàng:** tạo blocker có owner và ngày cần; điều chỉnh sequencing.
- **Yêu cầu thay đổi sau baseline:** change request và impact analysis; cập nhật backlog sau phê duyệt.
- **Task không đạt DoR:** trả về làm rõ, không đưa vào execution chỉ vì áp lực tiến độ.

## 3.13 Next Stage — Chuyển sang giai đoạn tiếp theo

Bàn giao execution baseline, backlog, task ownership, DoR/DoD, dependency và test mapping cho **04 — Development**.

---
