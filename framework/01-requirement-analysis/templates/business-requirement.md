# Tài liệu yêu cầu nghiệp vụ (Business Requirements Document — BRD)

## 1. Thông tin tài liệu

| Trường | Giá trị |
|---|---|
| Mã tài liệu | BRD-0001 |
| Dự án | [Tên dự án] |
| Phiên bản | 0.1 |
| Trạng thái | Draft |
| Owner nghiệp vụ | [Owner] |
| Nguồn | [Tài liệu/yêu cầu nguồn] |
| Ngày cập nhật | [YYYY-MM-DD] |

## 2. Tóm tắt nghiệp vụ

- Bối cảnh và vấn đề:
- Nhu cầu nghiệp vụ:
- Giải pháp/sản phẩm được xem xét:

## 3. Mục tiêu nghiệp vụ

| ID | Mục tiêu | Chỉ số thành công | Giá trị mục tiêu | Nguồn/Owner |
|---|---|---|---|---|
| BO-0001 | [Mục tiêu] | [Chỉ số] | [Mục tiêu] | [Nguồn/Owner] |

## 4. Stakeholder và nhu cầu

| Stakeholder ID/nhóm | Nhu cầu/yêu cầu | Vai trò/thẩm quyền | Nguồn |
|---|---|---|---|
| STK-0001 | [Nhu cầu] | [Vai trò] | [Nguồn] |

## 5. Business Requirements (BRQ)

| BRQ ID | Tên | Mô tả | Mục tiêu liên quan | Ưu tiên | Nguồn | Owner | Trạng thái |
|---|---|---|---|---|---|---|---|
| BRQ-0001 | [Tên] | [Mô tả] | BO-0001 | [Mức] | [Nguồn] | [Owner] | Draft |

### BRQ-0001 — [Tên yêu cầu]

- Mô tả:
- Lý do/giá trị nghiệp vụ:
- Kết quả mong đợi:
- Stakeholder/nguồn:
- Business Rules liên quan (BR IDs; nội dung chuẩn nằm ở Business Rules Catalogue):
- Scope Definition tham chiếu: `../outputs/02-scope-definition/scope-definition.md`
- Related IDs (FR/NFR/US/UC/AC):
- Ưu tiên:
- Owner:
- Trạng thái: Draft

## 6. Tham chiếu Scope Definition

Scope Definition là nguồn chuẩn duy nhất cho phạm vi. BRD chỉ tóm tắt hoặc dẫn chiếu, không sao chép in-scope/out-of-scope:

- Scope Definition/version: [Liên kết]
- Tóm tắt nghiệp vụ (nếu cần): [Tóm tắt ngắn]

## 7. Tham chiếu Business Rules

Business Rules Catalogue là nguồn chuẩn duy nhất cho nội dung BR. BRD chỉ ghi liên kết bằng ID:

| BR ID | Tên quy tắc | BRQ áp dụng |
|---|---|---|
| [BR ID] | [Tên quy tắc] | [BRQ ID] |

## 8. Yêu cầu liên quan

- FRS: [Artifact/IDs]
- NFR: [Artifact/IDs]
- Assumptions/Constraints/Dependencies/Risks: [Artifact/IDs]
- RTM: [Artifact]

## 9. Lịch sử thay đổi

| Phiên bản | Ngày | Người cập nhật | Mô tả thay đổi |
|---|---|---|---|
| 0.1 | [Ngày] | [Owner] | Bản nháp ban đầu |

**Hướng dẫn:** BRD chứa mục tiêu, nhu cầu và BRQ. Không nhúng nội dung chi tiết của Scope, BR, NFR, risks hoặc quyết định G1; tham chiếu artifact chuẩn bằng ID/path. AI không được đánh dấu nội dung là Approved.
