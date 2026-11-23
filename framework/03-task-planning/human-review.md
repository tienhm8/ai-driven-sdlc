# Human Review – Task Planning

> **Giai đoạn:** 03 – Task Planning  
> **Mục đích:** Bảo đảm backlog có thể thực hiện, ưu tiên đúng giá trị, phản ánh phụ thuộc/rủi ro và có tiêu chí hoàn thành rõ ràng trước khi bắt đầu coding.  
> **Review Gate:** G3 – Task Approval (trước khi bắt đầu coding)  
> **Người phê duyệt chính:** Tech Lead; PM/Project Manager phê duyệt kế hoạch và nguồn lực theo cơ chế dự án

## 1. Nguyên tắc review

- AI có thể đề xuất phân rã, effort và thứ tự; estimate của AI là dữ liệu tham khảo, không phải cam kết nguồn lực.
- Task phải truy vết được tới requirement và design đã duyệt.
- Không bắt đầu coding một task thuộc phạm vi G3 khi task chưa được người có thẩm quyền xác nhận.
- Ước lượng phải nêu giả định, độ bất định và phụ thuộc; không tạo cảm giác chính xác giả.
- Thay đổi phạm vi, ưu tiên hoặc dependency có tác động đáng kể phải được đánh giá lại.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| Tech Lead – **Approver G3** | Xác nhận task đủ rõ về kỹ thuật, phạm vi, dependency, Definition of Done và sẵn sàng coding. |
| Project Manager (PM) | Review kế hoạch, milestone, tiến độ, nguồn lực, rủi ro và điều phối phụ thuộc. |
| Product Owner | Xác nhận thứ tự ưu tiên và giá trị nghiệp vụ; quyết định trade-off phạm vi/sản phẩm. |
| Developer / Engineering Lead | Review tính khả thi, effort, độ phức tạp, cách tiếp cận và các task kỹ thuật bị bỏ sót. |
| QA Lead / QA Engineer | Review khả năng kiểm thử, test task, test data, môi trường và tiêu chí chất lượng. |
| Architect / Security / DevOps (khi cần) | Xác nhận task liên quan đến kiến trúc, bảo mật, hạ tầng hoặc vận hành không bị bỏ sót. |

## 3. Trách nhiệm review của con người

1. **Traceability:** Task liên kết với Requirement ID, Design/ADR và Acceptance Criteria tương ứng.
2. **Scope & outcome:** Mô tả rõ mục tiêu, phạm vi thực hiện, phần không làm và kết quả bàn giao.
3. **Granularity:** Task đủ nhỏ để theo dõi/review nhưng không chia vụn gây overhead; task lớn được phân rã thành subtask.
4. **Acceptance & DoD:** Có tiêu chí hoàn thành kiểm chứng được, bao gồm code, test, documentation, security và review khi phù hợp.
5. **Dependencies:** Phụ thuộc nội bộ/bên ngoài, thứ tự thực hiện, blocker và critical path được xác định.
6. **Effort & uncertainty:** Estimate có cơ sở, nêu giả định, độ tin cậy và yếu tố chưa biết; PM/Tech Lead không chấp nhận con số AI tạo ra như cam kết mặc định.
7. **Priority:** Thứ tự ưu tiên phản ánh giá trị, rủi ro, urgency và dependency; PO xác nhận ưu tiên sản phẩm.
8. **Capacity & ownership:** Có người/nhóm chịu trách nhiệm, năng lực phù hợp và không phân bổ vượt capacity đã thống nhất.
9. **Quality/security tasks:** Có task cho test, migration, observability, security, performance, documentation và rollout nếu cần.
10. **Risk & contingency:** Rủi ro delivery, tích hợp, môi trường, vendor và phương án dự phòng được ghi nhận.
11. **Readiness:** Task không phụ thuộc vào quyết định nghiệp vụ/thiết kế chưa được phê duyệt.
12. **Change impact:** Thay đổi backlog sau khi duyệt có owner, lý do và đánh giá tác động.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể sắp xếp/định dạng backlog, gắn nhãn hoặc phát hiện task trùng; không tự thay đổi cam kết hoặc ưu tiên đã duyệt. |
| L2 | PM/Tech Lead review theo mẫu đối với đề xuất phân rã/estimate có rủi ro thấp; kiểm tra các trường hợp ngoại lệ hoặc độ lệch lớn. |
| L3 | Tech Lead phải review và phê duyệt task trước coding khi task tác động logic nghiệp vụ, API, schema, security, kiến trúc hoặc dữ liệu. |
| L4 | PO quyết định ưu tiên và trade-off sản phẩm; PM quyết định/đề xuất kế hoạch nguồn lực theo thẩm quyền; AI chỉ tư vấn. |

## 5. Checklist review

- [ ] Task có liên kết tới requirement và design đã duyệt.
- [ ] Mục tiêu, phạm vi và deliverable rõ ràng.
- [ ] Task có kích thước phù hợp và owner dự kiến.
- [ ] Acceptance Criteria / Definition of Done kiểm chứng được.
- [ ] Dependency, blocker và thứ tự thực hiện đã được xác định.
- [ ] Estimate có giả định và mức độ bất định.
- [ ] Priority được PO hoặc người có thẩm quyền xác nhận.
- [ ] Capacity, kỹ năng và nguồn lực phù hợp.
- [ ] Task QA, security, migration, monitoring và documentation được tính đến khi cần.
- [ ] Không có task dựa trên yêu cầu/thiết kế chưa duyệt.
- [ ] Rủi ro và thay đổi phạm vi được ghi nhận.

## 6. Điều kiện quyết định G3

**Approve / Ready for Development** khi task rõ phạm vi, có đầu vào đã duyệt, owner, tiêu chí hoàn thành, dependency và kế hoạch phù hợp. Tech Lead xác nhận readiness trước khi coding.

**Changes requested / Not ready** khi task mơ hồ, thiếu AC/DoD, estimate không có cơ sở, dependency chưa giải quyết hoặc có quyết định nghiệp vụ/thiết kế còn chờ.

G3 phê duyệt readiness của task, không thay thế G1/G2 và không đồng nghĩa PO đã chấp thuận mọi thay đổi phạm vi.

## 7. Khi yêu cầu AI làm lại

Reviewer chỉ rõ task/subtask, nội dung thiếu hoặc sai, dependency/constraint cần bổ sung và tiêu chí Ready. AI cập nhật backlog; PM/Tech Lead kiểm tra lại. Nếu thay đổi priority hoặc scope sản phẩm, cần PO xác nhận trước khi cập nhật baseline.

## 8. Bằng chứng và hồ sơ review

Lưu backlog snapshot/version, task ID, liên kết requirement/design, estimate và giả định, dependency, owner, quyết định G3, reviewer, timestamp và lịch sử thay đổi sau phê duyệt.

## 9. Trách nhiệm cuối cùng

Tech Lead chịu trách nhiệm xác nhận task readiness về kỹ thuật trước coding. PM chịu trách nhiệm điều phối kế hoạch và nguồn lực trong phạm vi được giao. PO chịu trách nhiệm ưu tiên và trade-off sản phẩm. Estimate do AI đề xuất không phải cam kết delivery nếu chưa được người có thẩm quyền xác nhận.
