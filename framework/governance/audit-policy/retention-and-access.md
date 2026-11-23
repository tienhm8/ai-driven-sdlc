# Audit Retention & Access

## Retention
Thời hạn lưu phải căn cứ luật/quy định, hợp đồng/khách hàng, data classification, mục đích xử lý, nhu cầu điều tra/audit và legal hold. Không áp dụng một thời hạn mặc định cho mọi loại log. Project owner cùng Legal/Compliance/Security xác nhận retention schedule trước production.

## Access control
- Least privilege và role-based access.
- Tách quyền xem, export, cấu hình retention và xóa/disposition.
- Quyền có thời hạn và được review định kỳ.
- Truy cập audit record nhạy cảm phải được ghi nhận.
- Agent đang bị audit không được sửa/xóa bằng chứng của chính nó.

## Protection
Mã hóa khi truyền/lưu theo security baseline; mask secret/PII; backup và kiểm tra restore theo criticality; phân tách audit data với workspace log khi cần.

## Disposal
Khi hết retention và không có legal hold, disposition theo quy trình được duyệt; xử lý replica/bản sao theo khả năng; lưu bằng chứng disposition phù hợp. Không xóa hồ sơ đang phục vụ incident, investigation hoặc legal hold.

## Periodic review
Kiểm tra retention schedule, access list/privileged access, log completeness/integrity/alerting, khả năng truy xuất Gate/incident evidence và data minimization/disposal.

## Project configuration
- Audit store/system:
- Data classification:
- Retention schedule reference:
- Legal hold owner:
- Access roles:
- Export approver:
- Disposal owner:
- Review frequency:
