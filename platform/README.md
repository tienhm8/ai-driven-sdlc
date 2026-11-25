# Platform – Execution & Orchestration Core

Platform là lõi điều phối local cho [Project Instance](../README.md): cung cấp CLI để chuẩn bị workspace và API để quản lý trạng thái, review và phê duyệt. Các CLI và API là những điểm vào riêng; chưa có một bộ điều phối tự gọi tất cả các thành phần từ đầu đến cuối.

## Đã triển khai

| Thành phần | Trạng thái | Phạm vi hiện tại |
|---|---|---|
| [CLI](scripts/README.md) | Đã có | Khởi tạo Project Instance, kiểm tra workspace, đồng bộ tài nguyên Framework và phục vụ guide local. |
| [Rule Loader](rule-loader/README.md), [Skill Loader](skill-loader/README.md) | Đã có API | Nạp tài nguyên dùng chung và tài nguyên riêng của project theo cấu hình. Caller gọi loader, không phải Workflow Engine. |
| [Model Router](model-router/README.md) | Đã có API | Chọn profile tĩnh theo loại task, tính effort theo mức yêu cầu và ngưỡng tối thiểu của rủi ro, rồi trả về các profile dự phòng tương thích. Không đọc autonomy policy của project và không gọi model. |
| [Workflow Engine](workflow-engine/README.md), [Approval Engine](approval-engine/README.md) | Đã có API | Quản lý trạng thái stage và thực thi gate; ghi các sự kiện như review, quyết định và chuyển stage vào SQLite khi chúng xảy ra. Engine không tự tạo artifact, gọi loader/router/validator hay thực thi hành động bên ngoài. |
| [Validators](validators/README.md) | Đã có project validator | Kiểm tra manifest, cấu trúc workspace, đường dẫn tài nguyên và approval policy. Chưa xác minh nội dung artifact, chất lượng hay traceability. |
| [Tool Adapters](tool-adapters/README.md) | Mới có registry/contract | Nhận diện công cụ được cấu hình. Tích hợp xác thực, AI provider, repository, CI/CD và các hệ thống bên ngoài chưa có sẵn. |

## Kiến trúc đích — chưa tích hợp end-to-end

![Kiến trúc platform đề xuất](../framework/assets/platform-architecture.png)

Ở kiến trúc đích, lớp tích hợp nhận context từ Project Instance, nạp rule/skill cho stage và task, áp dụng autonomy policy khi chọn model/công cụ, rồi điều phối công việc và thu thập bằng chứng. Validator kiểm tra nội dung artifact và traceability trước khi gửi review tại gate cần thiết. Audit được ghi theo sự kiện trong quá trình thực thi, không phải bước cuối của luồng.

Xem [kiến trúc và ranh giới tin cậy](docs/architecture.md) để biết phần việc thuộc về core và phần do adapter thực hiện. Xem [Framework gate policy](../framework/governance/human-review-gates/gate-policy.md) để biết điều kiện và vai trò G1–G7.

## Cấu trúc thư mục

```text
platform/
├── README.md
├── pyproject.toml
├── requirements.txt
├── docs/                 # Kiến trúc và ranh giới tin cậy
├── config-examples/      # Manifest, autonomy policy và approval policy mẫu
├── src/ai_sdlc_platform/ # Mã Python của platform
├── tests/                # Test của platform
├── scripts/              # CLI init, validate, sync và guide
├── tool-adapters/        # Hướng dẫn thành phần, không phải vị trí mã Python
├── skill-loader/
├── rule-loader/
├── model-router/
├── workflow-engine/
├── approval-engine/
└── validators/
```

- Để khởi tạo và kiểm tra workspace, xem [hướng dẫn CLI](scripts/README.md).
- Để thử luồng phê duyệt local, xem [ví dụ G1](workflow-engine/README.md#run-a-local-g1-example).
- Tài nguyên đầu vào: [Framework](../framework/README.md) và [Shared AI resources](../shared-ai/).
