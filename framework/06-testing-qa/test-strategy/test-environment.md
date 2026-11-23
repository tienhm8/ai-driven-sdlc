# Test Environment Strategy

## Mục tiêu
Bảo đảm môi trường phù hợp, tái lập được và an toàn để kết quả có ý nghĩa.

## Các môi trường tham khảo
| Environment | Mục đích | Kiểm soát |
|---|---|---|
| Local/Dev | Unit, component, debug | Data giả lập, không dùng secret thật |
| Integration/Test | API, DB, service integration | Version/config quản lý được |
| QA/Staging | System, regression, pre-release | Gần production, data kiểm soát |
| UAT | Nghiệm thu nghiệp vụ | User/PO được cấp quyền |
| Performance/Security isolated | Kiểm thử chuyên biệt | Tách biệt, giới hạn tải, có phê duyệt |

Không mặc định mọi dự án có đủ các môi trường này.

## Environment manifest
Ghi environment ID/owner/mục đích; build/version/commit; OS/runtime/browser/device; dependency versions; configuration version (không ghi secret); DB schema/migration version; external services/mock/sandbox; network/access; test data reference/reset time; monitoring/logging/trace.

## Readiness
- Build đúng và xác định được version.
- Config/dependency/schema tương thích; secret lấy từ secret manager.
- Account/role và test data sẵn sàng.
- Sandbox/mock hoạt động.
- Có log/metrics và cách reset/cleanup an toàn.
- Không có hoạt động khác gây nhiễu.

## Data safety
Ưu tiên synthetic/anonymized data. Tuân thủ classification, access, retention. Không copy production dump vào QA nếu chưa phê duyệt và bảo vệ/khử định danh theo policy. Không lưu credential trong repo/report.

## Environment issue & drift
Ghi thời điểm, build, component, triệu chứng, dependency và evidence. Phân biệt environment failure với product defect; không tính là Pass. Nếu environment thay đổi đáng kể, đánh giá kết quả cũ và chạy lại test bị ảnh hưởng.
