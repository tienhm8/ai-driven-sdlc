# Prototype-first — Code song song với gate

Chế độ cho phép bắt đầu Development khi đã có prototype hoặc SRS đủ để code, không chờ G1, G2, G3 được duyệt. Hồ sơ của từng giai đoạn vẫn được lập và trình duyệt song song; code được cập nhật theo kết quả duyệt.

Cấu hình và người được bật: xem [Delivery Modes](README.md).

## 1. Điều kiện áp dụng

- `delivery.mode: prototype_first` trong `.ai-sdlc/project.yaml` và `delivery.decision_ref` trỏ tới quyết định `Accepted` trong decision log. Quyết định còn `Proposed` thì vẫn áp dụng `standard`.
- Có ít nhất một nguồn: prototype hoặc SRS, khai báo trong `delivery.prototype_first.sources` và có phiên bản xác định.
- Lát cắt chức năng (màn hình hoặc mục) được xác định rõ trong nguồn.

Thiếu điều kiện nào thì quay về [development readiness](../../04-development/checklists/development-readiness.md) của chế độ `standard`.

## 2. Nguồn sự thật khi code

| Khía cạnh | Nguồn chính | Khi nguồn chính thiếu hoặc mâu thuẫn |
|---|---|---|
| Giao diện: layout, component, style, theme | Base frontend (`sources.ui_base`): component, pattern và convention có sẵn | Dùng component gần nhất trong base; không tự tạo design system mới. Ghi khác biệt so với prototype. |
| Thao tác và luồng người dùng | Prototype | Theo SRS; nếu cả hai không có thì ghi câu hỏi mở. |
| Chức năng, business rule, validation, thông báo | SRS | Theo prototype; ghi rõ "suy từ prototype". |
| Hợp đồng API, dữ liệu | Đề xuất trong hồ sơ G2 (Draft) | FE gọi mock theo hợp đồng đề xuất; hợp đồng chính thức chốt ở G2. |

Prototype chỉ là tham chiếu hành vi, không phải code để chép. Giá trị mẫu trong prototype hoặc SRS không dùng làm giá trị mặc định hay dữ liệu chuẩn.

## 3. Cải tiến trải nghiệm người dùng

Khi thao tác trong prototype có thể làm tốt hơn (ít bước hơn, phản hồi rõ hơn, tránh mất dữ liệu, dễ tiếp cận hơn, nhất quán với base frontend), AI đề xuất cải tiến và ghi vào implementation summary, mục "Đề xuất cải tiến UX".

| `ux_improvements` | Cách xử lý |
|---|---|
| `apply_and_record` (mặc định) | Áp dụng cải tiến không đổi nghiệp vụ, ghi lại và đưa vào hồ sơ G1 để PO xác nhận. PO từ chối thì hoàn về theo prototype. |
| `propose_only` | Code đúng prototype; cải tiến chỉ ghi dạng đề xuất. |

Cải tiến làm đổi business rule, quyền, dữ liệu hoặc kết quả nghiệp vụ luôn là câu hỏi mở cho PO, không tự áp dụng.

## 4. Xác nhận bổ sung trong lúc phát triển

Phát sinh trong lúc code được ghi vào artifact chuẩn của giai đoạn tương ứng, không lập sổ riêng:

| Loại thông tin | Ghi vào | Ai xác nhận |
|---|---|---|
| Câu hỏi nghiệp vụ, mâu thuẫn prototype/SRS | [Open questions](../../01-requirement-analysis/outputs/10-assumptions-constraints-risks/open-questions.md) của Stage 01, kèm nhóm và mức quyết định | Theo nhóm A–D trong sổ |
| Giả định để code tiếp | Sổ giả định, ràng buộc, rủi ro của Stage 01 | BA / PO |
| Quyết định kỹ thuật, hợp đồng API | ADR hoặc tài liệu thiết kế của Stage 02 | Tech Lead / Solution Architect |
| Câu trả lời đã có | Cập nhật hồ sơ của giai đoạn đó (Draft), rồi cập nhật code | Người được hỏi |

Mỗi câu trả lời cập nhật vào hồ sơ là một thay đổi của bản trình duyệt; không chỉ sửa code.

Khi còn câu hỏi mở: làm phần giao diện và đánh dấu chờ ở chỗ liên quan (ví dụ `TODO(OQ-0012)`), không tự điền logic nghiệp vụ. Phần đã rõ thì code bình thường.

## 5. Gate trong chế độ này

Gate không bị bỏ. Chỉ thời điểm chặn thay đổi:

| Gate | Chế độ `prototype_first` |
|---|---|
| G1, G2, G3 có trong `deferred_gates` | Không chặn bắt đầu hoặc tiếp tục coding. Hồ sơ vẫn lập theo template của từng stage, trạng thái `Draft` / `In Review`, và trình duyệt song song. Code coi hồ sơ đang trình là **baseline tạm** để triển khai. |
| G1, G2, G3 không có trong `deferred_gates` | Chặn như `standard`. |
| G4 | Chặn merge như `standard`. Với `merge_policy: after_deferred_gates`, thêm điều kiện các gate trong `deferred_gates` phải `Approved` cho phần thay đổi trước khi merge vào nhánh tích hợp. |
| G5 | Trước khi trình G5, G1/G2/G3 phải `Approved` cho đúng phạm vi phát hành và code phải khớp phiên bản đã duyệt. Không ngoại lệ trong chế độ này. |
| G6, G7 | Không đổi. |

Ràng buộc với AI giữ nguyên: AI không ghi `Approved`, không ghi quyết định gate, không đổi "baseline tạm" thành baseline đã duyệt. "Triển khai như đã duyệt" nghĩa là code tiếp tục theo bản đang trình, không phải bản đó được duyệt.

## 6. Khi gate duyệt có thay đổi

- Gate `approved`: đối chiếu phiên bản được duyệt với phiên bản code đã dùng. Có khác biệt thì cập nhật code và ghi trong implementation summary.
- Gate `changes_requested` hoặc `rejected`: cập nhật hồ sơ, sửa code theo; phần đã merge cần sửa thì mở PR mới qua G4. Chi phí làm lại đã được chấp nhận khi bật chế độ.
- Thay đổi sau approval vẫn theo quy tắc [gate policy](../human-review-gates/gate-policy.md#quy-tắc): approval chỉ có hiệu lực với đúng phiên bản.

## 7. Truy vết

Mỗi task ghi trong [implementation summary](../../04-development/outputs/implementation-summary-template.md):

- Chế độ `prototype_first`, `decision_ref`, phiên bản prototype, SRS và commit base frontend đã dùng.
- Trạng thái G1/G2/G3 tại thời điểm code (ví dụ `G2: In Review v0.3`).
- Câu hỏi mở và giả định đang chờ, cải tiến UX đã áp dụng hoặc đề xuất.

## 8. Giới hạn

- Không áp dụng cho thay đổi bảo mật trọng yếu, migration dữ liệu thật hoặc tích hợp hệ thống ngoài có tác động thật; các việc này vẫn cần G2 trước khi thực thi.
- Không cấp quyền mới cho AI. Mức autonomy theo [chính sách mức tự chủ](../ai-governance/ai-autonomy-levels.md).
- Platform local (`workflow_engine`) chưa hỗ trợ chế độ này và vẫn chạy thứ tự stage của `standard`; chế độ hiện được áp dụng ở mức quy trình và tài liệu.
