# Scripts

## Scripts

| Script | Trách nhiệm |
|---|---|
| `init-project.py` | Tạo Project Instance mới. Tham số: `--name`, `--slug` (bắt buộc), `--tools` (mặc định `claude`), `--no-project-management`. |
| `validate-project.py` | Kiểm tra cấu trúc và cấu hình dự án. Tham số: `--project` (bắt buộc), `--framework`. |
| `sync-framework.py` | Cập nhật template và tài nguyên theo phiên bản Framework mới, không ghi đè tài liệu dự án đã phát sinh. Tham số: `--framework`, `--project` (bắt buộc), `--apply`, `--overwrite`. |
| `build-guide.py` | Nhúng `framework/guide/guide-data.yml` vào `framework/guide/index.html`. Tham số: `--check` để kiểm tra index đã cập nhật chưa. |
| `guide-server.py` | Chạy server local, chỉ đọc, phục vụ guide và tiến độ dự án. Tham số: `--port` (mặc định `8765`), `--state-dir`. |

> **Nguyên tắc:** `init-project.py` không sinh source code Backend/Frontend. Các repository code được tạo riêng theo công nghệ và quy trình khởi tạo tương ứng. Script này chỉ chịu trách nhiệm tạo workspace, cấu trúc tài liệu và cấu hình AI-Driven SDLC.

## Phân biệt tài nguyên AI

| Vị trí | Phạm vi | Ghi chú |
|---|---|---|
| `rules/`, `skills/` (trong Project Instance) | Riêng của từng dự án | Có thể bổ sung hoặc tùy chỉnh. |
| `shared-ai/rules/`, `shared-ai/skills/` | Dùng chung giữa các dự án | Quản lý tập trung tại một nơi. |
| `.ai-sdlc/project.yaml` | Riêng của từng dự án | Manifest chính thức: `project.id`, `project.name`, framework version, technology stack, tài nguyên AI và autonomy. Xem [manifest mẫu](../config-examples/project.yaml). |

Đường dẫn `ai.local_resources.rules_path` và `skills_path` tính từ gốc project. Init trỏ hai trường này tới thư mục của công cụ đầu tiên trong `--tools`. Validator kiểm tra cả hai thư mục được khai báo và [approval policy](../approval-engine/README.md) nếu có. Project mới có thể báo `STACK_UNDEFINED` cho đến khi điền technology stack.

**Project được tạo bằng bản cũ:** sao lưu cấu hình, chuyển `config.yml` sang `.ai-sdlc/project.yaml` và đổi `project.slug` thành `project.id`. Giữ các đường dẫn local hiện có vì chúng vẫn tính từ gốc project. Chạy validator để kiểm tra trước khi bỏ file cũ. Init không sửa hoặc ghi đè project đã có.

## Cách chạy script

Từ gốc repo, cài platform và các dependency (Python 3.10+) trước khi chạy:

```bash
python3 -m pip install -e ./platform
```

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

## Hồ sơ Project Management

Mặc định, init tạo charter `Draft`, hướng dẫn và các register `No entries` trong `docs/project-management/`. Dùng `_templates/` cho hồ sơ chi tiết, báo cáo trạng thái và closeout. `.ai-sdlc/project.yaml` là nguồn cấu hình platform; phạm vi, KPI, baseline và thẩm quyền thuộc charter đã duyệt. `--no-project-management` bỏ qua toàn bộ phần này. Xem [Project Management](../../framework/project-management/README.md).

## Outputs của QA, Deployment và Monitoring

Khi khởi tạo, ba stage dưới đây có thư mục `outputs/` chứa README hướng dẫn và các file `*-example.md` từ framework. File ví dụ không phải kết quả kiểm thử, phê duyệt hay bằng chứng vận hành. Thư mục con thực tế chỉ được tạo khi có đợt kiểm thử, triển khai hoặc vận hành tương ứng:

| Stage | Đường dẫn lưu hồ sơ thực tế |
|---|---|
| `06-testing-qa` | `docs/06-testing-qa/outputs/<project>/<release-or-cycle>/` |
| `07-deployment` | `docs/07-deployment/outputs/<project>/<release-ID>/` |
| `08-monitoring-maintenance` | `docs/08-monitoring-maintenance/outputs/<service>/<env>/<period-or-incident-id>/` |

## Kiểm tra và đồng bộ

Từ gốc repo, sau khi tạo Project CRM:

```bash
python3 platform/scripts/validate-project.py --project projects/Project-CRM --framework framework
python3 platform/scripts/sync-framework.py --framework framework --project projects/Project-CRM
```

### Chế độ đồng bộ

| Chế độ | Hành vi |
|---|---|
| Dry run (mặc định) | Liệt kê file dự kiến chép, bỏ qua hoặc conflict; không ghi tài nguyên, manifest hay nhật ký. |
| `--apply` | Ghi thay đổi vào `.ai-sdlc/framework-resources/` và cập nhật manifest. Không cập nhật các bản template theo stage đã được init chép vào `docs/`. |
| `--overwrite` | Cho phép thay file đích khác nội dung, kể cả file chưa được quản lý. Dùng riêng để xem trước; chỉ ghi khi kèm `--apply`. Không bỏ qua file chỉ đọc hoặc mục recovery chưa xác minh được. |

**Cập nhật mẫu cho dự án cũ:** Tra [danh mục mẫu chuẩn](../../framework/templates/README.md) trong repo framework. Khi cần dùng mẫu mới, đối chiếu bản chuẩn với bản tại `docs/<stage>/_templates/`, rồi cập nhật thủ công phần mẫu chưa điền và giữ tùy chỉnh cần thiết. Không sửa hồ sơ đã điền hoặc baseline đã duyệt. Các file chỉ dẫn trong `.ai-sdlc/framework-resources/templates/` không phải bản mẫu để điền.

### Checksum và xử lý conflict

- `.ai-sdlc/framework-sync.json` lưu SHA-256 của tài nguyên do sync quản lý. Nếu file đích khác nguồn và đã khác checksum mốc, sync mặc định giữ nguyên file và checksum mốc, đồng thời báo conflict (exit code `2`). File khác nội dung chưa được quản lý được bỏ qua. Hãy đối chiếu, sao lưu thay đổi cần giữ và xem dry run trước khi quyết định dùng `--apply --overwrite`.
- Nếu bản sync cũ đã ghi sai checksum mốc, bản mới không tự suy đoán nội dung từng được cài; hãy đối chiếu file với nguồn trước khi xử lý conflict và chạy lại.
- Sync kiểm tra lại đích trước khi thay file, nhưng kiểm tra checksum và thay file không phải một thao tác nguyên tử chung. Không chạy sync đồng thời với trình sửa file hoặc lần sync khác.

### Quyền file và thư mục staging

- Sync giữ quyền truy cập của manifest và tài nguyên đích đã có; tài nguyên mới lấy quyền từ nguồn, còn manifest mới có quyền `0600` trên POSIX. Trên Linux, sync giữ POSIX access ACL và chủ sở hữu/nhóm của đích đã có; manifest mới không kế thừa access ACL. Nếu không thể giữ quyền cần thiết, sync báo conflict và không thay file. Quản trị quyền sở hữu và nhóm ở thư mục cha của workspace dùng chung.
- Sync đặt file tạm trong thư mục staging riêng cùng filesystem. File tài nguyên giữ timestamp và các thuộc tính `user.*` của nguồn nếu được hỗ trợ, nhưng không nhập quyền nguồn vào file đích đã có. Trên Windows, kiểm tra quyền dựa vào cờ read-only và ACL của staging phụ thuộc cấu hình máy.

### Khôi phục lần sync bị gián đoạn

- Trước khi thay tài nguyên, sync chuẩn bị manifest và kiểm tra quyền. Mỗi thay đổi được ghi trước vào `.ai-sdlc/framework-sync.pending.json`; nhật ký giữ quyền của manifest hoặc dùng quyền riêng khi chưa có manifest. Trên POSIX, sync flush các thư mục chứa file đổi tên và các thư mục mới tạo.
- Nếu bị gián đoạn hoặc không ghi được manifest cuối, giữ nguyên nhật ký và `.ai-sdlc/framework-sync.proofs/`, rồi chạy lại. Sync chỉ cập nhật checksum mốc khi inode của file đích trùng liên kết cứng proof và cả checksum nội dung lẫn mốc cũ đều khớp. Nếu filesystem không hỗ trợ liên kết cứng giữa staging và `.ai-sdlc/`, sync không thay tài nguyên.
- Mục không xác minh được vẫn nằm trong nhật ký và được báo conflict. Nếu không đọc được nhật ký, dùng tài khoản đã chạy sync hoặc khôi phục quyền nhóm bảo trì. Nếu nhật ký không hợp lệ hoặc thiếu proof, đối chiếu thủ công trước khi dọn nhật ký và chạy lại.

## AI-Driven SDLC Platform

Các script init/validate/sync không thực hiện phê duyệt hoặc cấp quyền merge/deploy. Xem [Platform README](../README.md) để biết phạm vi hiện có và [Architecture](../docs/architecture.md) trước khi nối platform với hệ thống bên ngoài.

## Guide theo vai trò, giai đoạn và dự án

```bash
python3 platform/scripts/build-guide.py          # nhúng framework/guide/guide-data.yml vào index.html (--check để kiểm tra)
python3 platform/scripts/guide-server.py         # http://127.0.0.1:8765/framework/guide/index.html, thêm --port và --state-dir nếu cần
```

- Tab **Theo vai trò** và **Theo giai đoạn** chỉ cần mở `framework/guide/index.html`. Dữ liệu khung nằm ở `framework/guide/guide-data.yml`; sửa file này rồi chạy `build-guide.py`.
- Link trong guide mở tài liệu `.md` dưới dạng trang đã render (bảng, danh sách, code block) khi xem qua `guide-server.py`; mở `index.html` trực tiếp bằng `file://` thì link hiện Markdown thô. Server chỉ phục vụ `framework/` và `shared-ai/`, và hiển thị HTML nhúng trong Markdown như văn bản.
- Tab **Theo dự án** cần `guide-server.py`. Mỗi lần chọn dự án, server đọc ngay trạng thái hiện tại. Server chỉ nghe ở `127.0.0.1`, chỉ có API đọc, và không ghi vào dự án hay governance store.
- Trạng thái workflow và gate lấy từ SQLite của Workflow Engine tại `--state-dir` (mặc định `~/.ai-sdlc/state`), cùng thư mục mà service ghi phê duyệt dùng. Đầu ra bắt buộc được xác định bằng việc file trong `docs/<giai-đoạn>/` có tồn tại và đã khác bản template gốc. Chưa có execution trong store thì dự án hiện là "chưa bắt đầu workflow".
