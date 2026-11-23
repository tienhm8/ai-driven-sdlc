# Outputs – Code Review

Thư mục lưu sản phẩm được tạo trong giai đoạn Code Review.

## Artifact
- `review-report-example.md`: ví dụ báo cáo review có finding và kết luận.
- `review-summary-example.md`: ví dụ tóm tắt ngắn cho PR/dashboard.

Trong vận hành thực tế, tạo thư mục theo project/PR hoặc quy ước lưu trữ của tổ chức, ví dụ `outputs/CRM/PR-123/`. Không ghi đè báo cáo cũ; tạo version mới khi head SHA thay đổi.

## Metadata bắt buộc
Repository, PR, base/head SHA, thời gian, reviewer, report version, CI evidence, finding status và quyết định human G4.

Không xem ví dụ trong thư mục này là kết quả review thực tế hoặc bằng chứng phê duyệt.

## Kiến trúc

```
outputs/
├── README.md                          # Quy ước lưu trữ, metadata bắt buộc
├── review-report-example.md           # Ví dụ báo cáo review (chỉ để tham khảo)
└── review-summary-example.md          # Ví dụ tóm tắt PR/dashboard (chỉ để tham khảo)
```

## Vai trò từng file

| File | Vai trò |
|---|---|
| `README.md` | Quy định cách tổ chức thư mục output theo project/PR, metadata bắt buộc và nguyên tắc version hóa khi head SHA thay đổi. |
| `review-report-example.md` | Minh họa cấu trúc báo cáo review: finding, mức độ, disposition và kết luận. Không phải kết quả review thực tế. |
| `review-summary-example.md` | Minh họa bản tóm tắt ngắn cho PR hoặc dashboard. Không phải bằng chứng phê duyệt. |
