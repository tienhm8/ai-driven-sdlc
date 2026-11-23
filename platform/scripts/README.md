# Scripts

## Scripts

| Script | Trách nhiệm |
|---|---|
| `init-project.py` | Tạo Project Instance mới. |
| `validate-project.py` | Kiểm tra cấu trúc và cấu hình dự án. |
| `sync-framework.py` | Cập nhật template và tài nguyên theo phiên bản Framework mới, không ghi đè tài liệu dự án đã phát sinh. |

> **Nguyên tắc:** `init-project.py` không sinh source code Backend/Frontend. Các repository code được tạo riêng theo công nghệ và quy trình khởi tạo tương ứng. Script này chỉ chịu trách nhiệm tạo workspace, cấu trúc tài liệu và cấu hình AI-Driven SDLC.

## Phân biệt tài nguyên AI

| Vị trí | Phạm vi | Ghi chú |
|---|---|---|
| `rules/`, `skills/` (trong Project Instance) | Riêng của từng dự án | Có thể bổ sung hoặc tùy chỉnh. |
| `shared-ai/rules/`, `shared-ai/skills/` | Dùng chung giữa các dự án | Quản lý tập trung tại một nơi. |
| `config.yaml` | Riêng của từng dự án | Khai báo project, framework version, technology stack, shared resources, autonomy và AI Tool. Không chứa nội dung chi tiết của Rules hoặc Skills. |

## Cách chạy script

### Trường hợp 1: Tạo Project Instance sử dụng Claude Code

```bash
python3 platform/scripts/init-project.py \
  --name "Project CRM" \
  --slug "Project-CRM"
```

### Trường hợp 2: Sử dụng Claude Code và Cursor

```bash
python3 platform/scripts/init-project.py \
  --name "Project CRM" \
  --slug "Project-CRM" \
  --tools claude,cursor
```

### Trường hợp 3: Sử dụng GitHub Copilot

```bash
python3 platform/scripts/init-project.py \
  --name "Project ERP" \
  --slug "Project-ERP" \
  --tools copilot
```

### Trường hợp 4: Không tạo Project Management

```bash
python3 platform/scripts/init-project.py \
  --name "Project CRM" \
  --slug "Project-CRM" \
  --tools claude \
  --no-project-management
```

## AI-Driven SDLC Platform

Lớp thực thi và điều phối trung lập với nhà cung cấp (provider-neutral) cho tám giai đoạn SDLC.

### Cài đặt

Yêu cầu Python 3.10+.

```bash
pip install -e .
python3 scripts/validate-project.py --project ../projects/Project-CRM --framework ../framework
python3 scripts/sync-framework.py --framework ../framework --project ../projects/Project-CRM
```

Platform tải cấu hình dự án, skills và rules (shared/local), profile định tuyến model và cấu hình tool adapter. Platform áp dụng các human gate đã cấu hình và ghi các sự kiện thực thi dạng append-only vào `.ai-sdlc/audit/`.

Đây là nền tảng điều phối, không phải tích hợp API của nhà cung cấp. Việc thực thi model/tool, xác thực danh tính, triển khai production và trạng thái multi-user bền vững cần các adapter và biện pháp bảo mật được cấu hình riêng.
