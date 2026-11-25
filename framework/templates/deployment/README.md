# Template Deployment

Dành cho giai đoạn 07 – Deployment. Production change phải tuân thủ access control, change management và Gate G6.

## Canonical
| Tài liệu | Template chuẩn |
|---|---|
| Deployment plan | [`07-deployment/templates/deployment-plan.md`](../../07-deployment/templates/deployment-plan.md) |
| Rollback plan | [`07-deployment/templates/rollback-plan.md`](../../07-deployment/templates/rollback-plan.md) |
| Release notes | [`07-deployment/templates/release-note.md`](../../07-deployment/templates/release-note.md) |
| G6 approval | [`07-deployment/templates/production-approval.md`](../../07-deployment/templates/production-approval.md) |
| Deployment record | `deployment-record.md` (thư mục này, canonical dùng chung) |

`deployment-plan.md`, `rollback-plan.md`, `release-notes.md` ở thư mục này chỉ là file liên kết.

## Quan hệ
Plan và rollback plan được review trước G6. G6 chỉ ghi quyết định Go/No-Go và liên kết tới deployment record; việc thực thi, sai lệch, sự cố và bàn giao Stage 08 chỉ ghi trong `deployment-record.md`.

Không lưu secret hoặc credential trong tài liệu.
