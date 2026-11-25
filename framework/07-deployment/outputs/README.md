# Outputs – Deployment

## Kiến trúc
Thư mục lưu **hồ sơ phát hành và bằng chứng triển khai**. Hiện chỉ chứa file mẫu để minh họa định dạng; trong vận hành thật, hồ sơ được tổ chức theo project/service/release ID.

```
outputs/
├── README.md                          → quy ước lưu trữ và metadata bắt buộc
├── deployment-report-example.md       → mẫu báo cáo sau triển khai
└── release-note-example.md            → mẫu release note

Trong vận hành:  outputs/<project>/<release-ID>/   (ví dụ: outputs/CRM/REL-2026.04/)
```

Nguyên tắc: không ghi đè lịch sử; khi plan, artifact hoặc kết quả thay đổi thì tạo revision mới.

## Biểu mẫu và ví dụ

Dùng [Deployment Record](../../templates/deployment/deployment-record.md) làm biên bản chuẩn cho thực thi, xác minh, sự cố/rollback và bàn giao. Hồ sơ [phê duyệt G6](../templates/production-approval.md) giữ quyết định phê duyệt và chỉ tham chiếu biên bản thực thi; không sao chép kết quả sang hồ sơ G6.
| File | Vai trò |
|---|---|
| `README.md` | Quy định cách tổ chức thư mục theo release, danh sách metadata bắt buộc và cấm lưu secret/dữ liệu production nhạy cảm. |
| `deployment-report-example.md` | Mẫu báo cáo sau triển khai: metadata, kết quả, bảng bước thực thi kèm evidence, issues và phần bàn giao. Dữ liệu là minh họa. |
| `release-note-example.md` | Mẫu release note: tóm tắt, thay đổi, tương thích, rollback và truy vết (version, commit, digest, approval). Dữ liệu là minh họa. |

## Lưu trữ
Trong vận hành, tổ chức theo project/service/release ID. Không ghi đè lịch sử; tạo revision mới khi plan, artifact hoặc kết quả thay đổi.

## Metadata bắt buộc
Project/service, release ID, môi trường đích, commit SHA, artifact digest, pipeline run, plan version, timestamp, người thực thi, kết quả và bằng chứng xác minh, phiên bản đang chạy và trạng thái bàn giao. Với Production, ghi tham chiếu hồ sơ G6, authorization và lượt bắt đầu. Phân biệt bàn giao release đã xác minh thành công với bàn giao thông tin sự cố; bàn giao sự cố không chuyển stage.

Không lưu secret, token hoặc dữ liệu production nhạy cảm trong outputs.
