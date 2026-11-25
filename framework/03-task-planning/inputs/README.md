# Inputs Stage 03
Inputs là baseline từ Stage 01/02 cộng với project context.

| Nguồn | Nội dung | Trạng thái cần có | Mục đích |
|---|---|---|---|
| Stage 01 | Scope, Epic/Story, FR/NFR, business rules, AC, open questions | Approved — G1 | Xác định việc cần làm |
| Stage 02 | Architecture, components, API, DB, ADR, constraints | Đúng phiên bản design package đã chốt làm baseline, có bằng chứng G2 hợp lệ cho phiên bản đó | Xác định cách làm và dependency |
| Project context | Team, capacity, calendar, release target, estimation policy | Confirmed | Lập lịch và phân bổ |

Ưu tiên tham chiếu path/URL, document ID, version, commit/hash và approval record. Chỉ snapshot khi cần audit hoặc khi nguồn không ổn định; ghi rõ nguồn và thời điểm snapshot.

| Input ID | Nguồn | Artifact/path | Version | Gate | Trạng thái | Owner |
|---|---|---|---|---|---|---|
| IN-REQ-01 | 01 | | | G1 | `Verified/Pending` | |
| IN-DES-01 | 02 | | | G2 | `Verified/Pending` | |
| IN-CTX-01 | Project | | | N/A | | |

Không dùng Draft/Rejected/Superseded làm baseline. Với design, đối chiếu ID/phiên bản gói và các phiên bản artifact trong package index với hồ sơ G2: gate Approved, quyết định Approved của Solution Architect, các phê duyệt chuyên môn bắt buộc, thời điểm và waiver hợp lệ (nếu có). Changes Requested hoặc Blocked chưa đủ để bàn giao chính thức; điều kiện phải được đóng và G2 được phê duyệt lại. Baseline là phiên bản gói đã chốt, không phải trạng thái artifact riêng. Requirement/design thay đổi sau khi planning bắt đầu phải đánh giá tác động và re-plan; phiên bản design mới cần review/phê duyệt phù hợp, không tự kế thừa G2 cũ.

## Kiến trúc
Luồng tiếp nhận đầu vào:

```text
Stage 01 (G1)                    ─┐
Stage 02 (G2 + design baseline)  ─┼→ Xác minh phiên bản/bằng chứng → Phiếu tiếp nhận → Stage 03 Planning → G3 → Stage 04 coding
Project context                  ─┘
```

Chỉ dùng requirement baseline đã Approved với bằng chứng G1 và đúng phiên bản design package đã chốt làm baseline với bằng chứng G2 hợp lệ cho phiên bản đó. Nếu thiếu hoặc có blocker, dừng phần kế hoạch bị ảnh hưởng và ghi owner, hạn xử lý. G2 cho phép tiếp nhận và lập kế hoạch, không thay thế G3: phải có phê duyệt G3 trước coding.

## Vai trò từng file
| File | Vai trò |
|---|---|
| `README.md` | Định nghĩa ba nguồn đầu vào, cách tham chiếu và bảng đăng ký Input ID (IN-REQ, IN-DES, IN-CTX). |
| `requirement-baseline.md` | Phiếu tiếp nhận requirement baseline từ Stage 01: scope, Epic/Story, FR/NFR, AC, business rules, open questions. Tham chiếu, không thay thế tài liệu gốc. |
| `design-baseline.md` | Phiếu tiếp nhận design baseline từ Stage 02: architecture/ADR, component, API, DB, bảo mật, hạ tầng, rủi ro. Tham chiếu, không thay thế tài liệu gốc. |
