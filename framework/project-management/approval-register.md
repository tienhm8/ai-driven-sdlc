# Approval Register
Sổ đăng ký phê duyệt và Human Review Gates. Mỗi approval gắn với đúng artifact version hoặc commit SHA.

| ID | Gate / Subject | Artifact version / SHA | Requested by | Approver | Decision | Timestamp | Evidence | Notes |
|---|---|---|---|---|---|---|---|---|
| APR-001 | G1 / Requirement | | | Product Owner | Pending | | | |

## Gate reference
| Gate | Control point | Approver |
|---|---|---|
| G1 | Sau phân tích yêu cầu | Product Owner |
| G2 | Sau thiết kế | Solution Architect |
| G3 | Trước coding | Tech Lead |
| G4 | Trước merge | Reviewer / Tech Lead |
| G5 | Trước nghiệm thu | QA Lead / Product Owner |
| G6 | Trước production | Release Manager |
| G7 | Sự cố nghiêm trọng | Incident Commander |

Ghi approver là người có thẩm quyền, timestamp, quyết định, artifact version/SHA và evidence. Từ chối phải có lý do/action. Không sửa/xóa approval cũ. Tuân thủ gate-policy chính thức của framework.
