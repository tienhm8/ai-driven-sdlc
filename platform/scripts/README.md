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

## Outputs của QA, Deployment và Monitoring

Khi khởi tạo, ba stage dưới đây có thư mục `outputs/` chứa README hướng dẫn và các file `*-example.md` từ framework. File ví dụ không phải kết quả kiểm thử, phê duyệt hay bằng chứng vận hành. Thư mục con thực tế chỉ được tạo khi có đợt kiểm thử, triển khai hoặc vận hành tương ứng:

| Stage | Đường dẫn lưu hồ sơ thực tế |
|---|---|
| `06-testing-qa` | `docs/06-testing-qa/outputs/<project>/<release-or-cycle>/` |
| `07-deployment` | `docs/07-deployment/outputs/<project>/<release-ID>/` |
| `08-monitoring-maintenance` | `docs/08-monitoring-maintenance/outputs/<service>/<period>/` hoặc `docs/08-monitoring-maintenance/outputs/<service>/<incident-id>/` |

## Kiểm tra và đồng bộ

Từ gốc repo, sau khi tạo Project CRM:

```bash
python3 platform/scripts/validate-project.py --project projects/Project-CRM --framework framework
python3 platform/scripts/sync-framework.py --framework framework --project projects/Project-CRM
```

Sync mặc định chỉ xem trước. Manifest hiện có giữ quyền truy cập của đích, bao gồm POSIX access ACL trên Linux. Manifest mới mặc định `0600` và không kế thừa access ACL. Đối với workspace dùng chung, quản trị quyền sở hữu và nhóm ở thư mục cha. Thêm `--apply` để cập nhật tài nguyên dùng chung trong `.ai-sdlc/framework-resources/`; lệnh này không cập nhật các bản template theo stage đã được init chép vào `docs/`. Khi phát hiện file do sync quản lý đã bị chỉnh, sync báo conflict (exit code 2), không chép đè và giữ checksum mốc cũ. Sau khi xử lý conflict, chạy lại. Nếu bản sync cũ đã ghi sai checksum mốc, bản mới không tự suy đoán phiên bản từng được cài; hãy đối chiếu file với nguồn và xử lý conflict thủ công. File khác nội dung chưa từng được sync quản lý không bị chép đè hoặc nhận vào manifest trừ khi dùng `--apply --overwrite`. Chỉ dùng cờ ghi đè sau khi đã xem dry run và sao lưu thay đổi cần giữ. Sync từ chối thay file chỉ đọc, kể cả khi dùng `--overwrite`, và kiểm tra lại đích trước khi thay file. Tài nguyên đã có giữ nguyên quyền đọc/ghi/thực thi của đích; tài nguyên mới lấy các quyền này từ nguồn. Trên Linux, sync cũng giữ POSIX access ACL từ cùng file tham chiếu và giữ chủ sở hữu/nhóm của file đích hiện có. Nếu không thể giữ các quyền đó, sync báo conflict và không thay tài nguyên. Tài nguyên được chép giữ timestamp của nguồn và các thuộc tính `user.*` mà filesystem hỗ trợ, không nhập quyền truy cập của nguồn vào file đích đã có. Hành vi này không áp dụng cho các định dạng ACL khác. Không chạy sync đồng thời với trình sửa file hoặc một lần sync khác: kiểm tra checksum và thay file không phải một thao tác nguyên tử chung.

Trước khi thay tài nguyên, sync chuẩn bị file manifest mới và kiểm tra khả năng giữ quyền/ACL. Mỗi lần thay tài nguyên được ghi trước vào `.ai-sdlc/framework-sync.pending.json`. Nếu lần chạy bị gián đoạn hoặc không ghi được manifest cuối, để nguyên nhật ký rồi chạy lại. Sync kiểm tra checksum trong manifest trước khi ghi. Khi phục hồi, sync chỉ nhận mốc mới nếu file đích có cùng inode hiện tại với liên kết cứng trong `.ai-sdlc/framework-sync.proofs/`, và cả checksum nội dung lẫn mốc cũ đều khớp. Không xóa hoặc chỉnh sửa thư mục proof trong khi còn nhật ký. Cơ chế này cần filesystem hỗ trợ hard link giữa khu vực staging và `.ai-sdlc/`; nếu không tạo được proof, sync không thay tài nguyên. Trên POSIX, `--apply` flush thư mục chứa file được đổi tên; thư mục mới được ghi bền vững khi tạo. Mục chưa xác minh được vẫn nằm trong nhật ký và được báo conflict. Dry run chỉ đọc. Nhật ký dùng quyền của manifest hiện có hoặc quyền private khi chưa có manifest. Nếu nhật ký không đọc được, dùng tài khoản đã chạy sync hoặc khôi phục quyền cho nhóm bảo trì; nếu nhật ký không hợp lệ hoặc thiếu proof, đối chiếu thủ công trước khi dọn nhật ký và chạy lại. `--overwrite` không bỏ qua mục recovery chưa xác minh được. Windows chỉ kiểm tra cờ read-only và không có bước flush thư mục này; ACL của thư mục staging dựa vào cấu hình máy.

## AI-Driven SDLC Platform

Platform có các thành phần tải cấu hình, skills/rules, model routing và tool adapter. [Workflow Engine](../workflow-engine/README.md) thực thi gate qua API và ghi các sự kiện vào SQLite trong thư mục trạng thái do service bảo vệ, nằm ngoài workspace. Các script init/validate/sync không thực hiện phê duyệt hoặc cấp quyền merge/deploy.

Đây là nền tảng điều phối, không phải tích hợp API của nhà cung cấp. Việc thực thi model/tool, xác thực danh tính, triển khai production và trạng thái multi-user bền vững cần các adapter và biện pháp bảo mật được cấu hình riêng.

## Guide theo vai trò, giai đoạn và dự án

```bash
python3 platform/scripts/build-guide.py          # nhúng framework/guide/guide-data.yml vào index.html (--check để kiểm tra)
python3 platform/scripts/guide-server.py         # http://127.0.0.1:8765/framework/guide/index.html, thêm --port và --state-dir nếu cần
```

- Tab **Theo vai trò** và **Theo giai đoạn** chỉ cần mở `framework/guide/index.html`. Dữ liệu khung nằm ở `framework/guide/guide-data.yml`; sửa file này rồi chạy `build-guide.py`.
- Link trong guide mở tài liệu `.md` dưới dạng trang đã render (bảng, danh sách, code block) khi xem qua `guide-server.py`; mở `index.html` trực tiếp bằng `file://` thì link hiện Markdown thô. Server chỉ phục vụ `framework/` và `shared-ai/`, và hiển thị HTML nhúng trong Markdown như văn bản.
- Tab **Theo dự án** cần `guide-server.py`. Mỗi lần chọn dự án, server đọc ngay trạng thái hiện tại. Server chỉ nghe ở `127.0.0.1`, chỉ có API đọc, và không ghi vào dự án hay governance store.
- Trạng thái workflow và gate lấy từ SQLite của Workflow Engine tại `--state-dir` (mặc định `~/.ai-sdlc/state`), cùng thư mục mà service ghi phê duyệt dùng. Đầu ra bắt buộc được xác định bằng việc file trong `docs/<giai-đoạn>/` có tồn tại và đã khác bản template gốc. Chưa có execution trong store thì dự án hiện là "chưa bắt đầu workflow".
