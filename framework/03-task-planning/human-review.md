# Human Review – Task Planning

> **Giai đoạn:** 03 – Task Planning  
> **Mục đích:** Bảo đảm backlog có thể thực hiện, ưu tiên đúng giá trị, phản ánh phụ thuộc/rủi ro và có tiêu chí hoàn thành rõ ràng trước khi bắt đầu coding.  
> **Review Gate:** G3 – Task Approval (trước khi bắt đầu coding)  
> **Người phê duyệt G3:** Tech Lead; PM xác nhận lịch và nguồn lực, PO xác nhận ưu tiên và trade-off sản phẩm

## 1. Nguyên tắc review

- AI có thể đề xuất phân rã, effort và thứ tự; estimate của AI là dữ liệu tham khảo, không phải cam kết nguồn lực.
- Task phải truy vết được tới requirement và design đã duyệt.
- Không bắt đầu coding khi task nằm ngoài phạm vi kế hoạch đã được G3 phê duyệt.
- Ước lượng phải nêu giả định, độ bất định và phụ thuộc; không tạo cảm giác chính xác giả.
- Thay đổi phạm vi, ưu tiên hoặc dependency có tác động đáng kể phải được đánh giá lại.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| Tech Lead – **Approver G3** | Phê duyệt một phiên bản kế hoạch và phạm vi task; xem xét tính khả thi kỹ thuật, dependency và Definition of Done. |
| Project Manager (PM) | Review kế hoạch, milestone, tiến độ, nguồn lực, rủi ro và điều phối phụ thuộc. |
| Product Owner | Xác nhận thứ tự ưu tiên và giá trị nghiệp vụ; quyết định trade-off phạm vi/sản phẩm. |
| Developer / Engineering Lead | Review tính khả thi, effort, độ phức tạp, cách tiếp cận và các task kỹ thuật bị bỏ sót. |
| QA Lead / QA Engineer | Review khả năng kiểm thử, test task, test data, môi trường và tiêu chí chất lượng. |
| Architect / Security / DevOps (khi cần) | Xác nhận task liên quan đến kiến trúc, bảo mật, hạ tầng hoặc vận hành không bị bỏ sót. |

## 3. Trọng tâm review của con người

Tiêu chí kiểm tra chi tiết nằm ở [checklist G3](checklists/g3-planning-approval-checklist.md) và các checklist [readiness](checklists/planning-readiness-checklist.md), [estimate](checklists/estimation-review-checklist.md), [dependency](checklists/dependency-review-checklist.md); không chép lại ở đây. Reviewer tập trung vào phán đoán mà checklist không thay thế được:

- Task có thật sự truy vết được và đủ nhỏ để giao, hay chỉ đã điền đủ ô.
- Estimate có cơ sở và nêu độ bất định; không chấp nhận con số AI tạo ra như cam kết mặc định.
- Priority phản ánh giá trị, rủi ro và dependency; PO xác nhận ưu tiên sản phẩm.
- Capacity và kỹ năng đủ; không phân bổ vượt năng lực đã thống nhất.
- Task không dựa trên yêu cầu/thiết kế chưa duyệt.
- Thay đổi sau duyệt có owner, lý do và đánh giá tác động.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể sắp xếp/định dạng backlog, gắn nhãn hoặc phát hiện task trùng; không tự thay đổi cam kết hoặc ưu tiên đã duyệt. |
| L2 | PM/Tech Lead review theo mẫu đối với đề xuất phân rã/estimate có rủi ro thấp; kiểm tra các trường hợp ngoại lệ hoặc độ lệch lớn. |
| L3 | Tech Lead review tác động kỹ thuật của task đến logic nghiệp vụ, API, schema, security, kiến trúc hoặc dữ liệu trong gói trình G3. G3 duyệt phiên bản kế hoạch và phạm vi task, không tạo thêm quyết định G3 cho từng task. |
| L4 | PO quyết định ưu tiên và trade-off sản phẩm; PM quyết định/đề xuất kế hoạch nguồn lực theo thẩm quyền; AI chỉ tư vấn. |

## 5. Checklist

Dùng [checklist G3](checklists/g3-planning-approval-checklist.md) để kiểm tra; ghi quyết định trong [mẫu approval record chung](../templates/review/approval-record.md).

## 6. Điều kiện quyết định G3

**Approved** khi phiên bản kế hoạch và phạm vi task đã ghi đạt checklist G3: đầu vào đã duyệt, owner, tiêu chí hoàn thành, dependency và kế hoạch phù hợp. Tech Lead ra quyết định.

**Changes requested / Not ready** khi task mơ hồ, thiếu AC/DoD, estimate không có cơ sở, dependency chưa giải quyết hoặc có quyết định nghiệp vụ/thiết kế còn chờ.

G3 duyệt **một phiên bản kế hoạch với phạm vi task xác định**, không thay thế G1/G2 và không đồng nghĩa PO đã chấp thuận mọi thay đổi phạm vi. Trước coding, Stage 04 xác minh task thuộc phạm vi đó và đạt DoR (xem [development readiness](../04-development/checklists/development-readiness.md)); đó là xác minh, không phải duyệt lại.

## 7. Khi yêu cầu AI làm lại

Reviewer chỉ rõ task/subtask, nội dung thiếu hoặc sai, dependency/constraint cần bổ sung và tiêu chí Ready. AI cập nhật backlog; PM/Tech Lead kiểm tra lại. Nếu thay đổi priority hoặc scope sản phẩm, cần PO xác nhận trước khi cập nhật baseline.

## 8. Bằng chứng và hồ sơ review

Lưu backlog snapshot/version, task ID, liên kết requirement/design, estimate và giả định, dependency, owner, quyết định G3, reviewer, timestamp và lịch sử thay đổi sau phê duyệt.

## 9. Trách nhiệm cuối cùng

Tech Lead chịu trách nhiệm về quyết định G3; Stage 04 kiểm tra readiness từng task trước coding. PM chịu trách nhiệm điều phối kế hoạch và nguồn lực trong phạm vi được giao. PO chịu trách nhiệm ưu tiên và trade-off sản phẩm. Estimate do AI đề xuất không phải cam kết delivery nếu chưa được người có thẩm quyền xác nhận.
