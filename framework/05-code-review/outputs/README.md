# Outputs – Code Review

Thư mục lưu sản phẩm được tạo trong giai đoạn Code Review.

## Artifact
- `review-report-example.md`: ví dụ báo cáo review có finding và kết luận.
- `review-summary-example.md`: ví dụ tóm tắt ngắn cho PR/dashboard.

Trong vận hành thực tế, tạo thư mục theo project/PR hoặc quy ước lưu trữ của tổ chức, ví dụ `outputs/CRM/PR-123/`. Không ghi đè báo cáo cũ; tạo version mới khi head SHA thay đổi.

## Metadata bắt buộc
Repository, PR, base/head SHA, thời gian, reviewer, report version, CI evidence, finding status, quyết định human G4, merge commit SHA, link bằng chứng merge và rủi ro bàn giao QA.

Không xem ví dụ trong thư mục này là kết quả review thực tế hoặc bằng chứng phê duyệt.

## Đầu ra

| Đầu ra | Mức | Ghi chú |
|---|---|---|
| [Review report](../templates/review-report.md) | **Bắt buộc** mọi PR | Gồm findings và quyết định G4; bổ sung merge commit SHA, link bằng chứng merge và rủi ro bàn giao QA sau khi merge |
| Review summary | Khuyến nghị | Bản ngắn cho PR/dashboard, trỏ về report |
| [Security review](../templates/security-review.md) | Khi thuộc phạm vi bảo mật | Phụ lục của report |
| Risk acceptance / exception record | Khi có accepted risk | Nêu approver, lý do, hạn |
| Cập nhật risk/technical debt register | Khi có follow-up | Mỗi follow-up có owner/deadline |

Bản ghi G4 và bằng chứng merge nằm trong mục *Human decision & G4* của review report. Rủi ro chuyển sang QA nằm cùng mục này và được bàn giao theo [workflow.md](../workflow.md#513-next-stage--chuyển-sang-giai-đoạn-tiếp-theo).

## Ví dụ
- [`review-report-example.md`](review-report-example.md), [`review-summary-example.md`](review-summary-example.md): chỉ để tham khảo.
