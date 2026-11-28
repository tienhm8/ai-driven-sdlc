# Delivery Modes — Chế độ triển khai

Chế độ triển khai quy định **thời điểm** các gate trước coding (G1, G2, G3) chặn việc phát triển. Chế độ không bỏ gate nào, không đổi approver và không nới điều kiện của từng gate.

Project chọn chế độ trong `.ai-sdlc/project.yaml`, khóa `delivery`. Không khai báo thì dùng `standard`.

| Chế độ | Khi nào dùng | G1/G2/G3 | G4–G7 |
|---|---|---|---|
| `standard` | Mặc định. Yêu cầu và thiết kế được chốt trước khi code. | Chặn bắt đầu coding theo [development readiness](../../04-development/checklists/development-readiness.md). | Chặn như [gate policy](../human-review-gates/gate-policy.md). |
| [`prototype_first`](prototype-first.md) | Đã có prototype hoặc SRS đủ để code. | Vẫn lập hồ sơ và duyệt, nhưng **song song** với coding; không chặn bắt đầu code. Phải được duyệt trước G5. | Chặn như `standard`; tùy chọn thêm điều kiện cho G4 qua `merge_policy`. |

## Ai được bật

- Bật hoặc tắt `prototype_first` là quyết định quản trị của project owner hoặc người được ủy quyền. Ghi vào decision log của project (`DEC-xxxx`, trạng thái `Accepted`) và dẫn ID đó trong `delivery.decision_ref`.
- AI có thể soạn đề xuất và sửa `project.yaml` khi được yêu cầu, nhưng không tự bật chế độ và không đổi trạng thái quyết định sang `Accepted`.
- Đây là tùy chọn do framework định nghĩa, không phải project tự hạ yêu cầu bắt buộc. Project không được mở rộng sang G4–G7 hoặc bỏ điều kiện trong [prototype-first](prototype-first.md).

## Cấu hình

```yaml
delivery:
  mode: prototype_first          # standard | prototype_first
  decision_ref: DEC-0002          # quyết định Accepted trong decision log
  prototype_first:
    sources:
      prototype: docs/inputs/prototype-v7.html   # ít nhất một trong prototype / srs
      srs: docs/inputs/srs-v4.xlsx
      ui_base: fe                  # alias trong technology_stack.repositories
    deferred_gates: [G1, G2, G3]   # tập con của G1, G2, G3; mặc định cả ba
    ux_improvements: apply_and_record   # apply_and_record | propose_only
    merge_policy: after_g4         # after_g4 | after_deferred_gates
```

Đường dẫn trong `sources` là đường dẫn tương đối trong project. Platform kiểm tra cấu trúc khi chạy `validate_project`; nội dung prototype và SRS không được kiểm tra tự động.
