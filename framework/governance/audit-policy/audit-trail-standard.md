# Audit Trail Standard

## Event cần ghi
- Agent/session start/end và identity/model/tool version khi có thể.
- Quyền cấp, đổi, thu hồi.
- Task start/end, scope, result.
- Tool/action có tác động: command, repository, branch, file/resource, environment, outcome.
- Artifact tạo/sửa: path, version, commit/hash.
- Finding, review decision, Gate approval/rejection, exception.
- Deploy, rollback, incident action và post-incident review.

## Metadata tối thiểu
| Field | Ý nghĩa |
|---|---|
| event_id | ID duy nhất |
| timestamp | Thời gian chuẩn hóa, ưu tiên UTC |
| actor / actor_type | Human, AI Agent hoặc System |
| project/workflow | Project và workflow |
| action / target | Hành động và resource bị tác động |
| version | Commit, artifact version hoặc hash |
| authorization | Policy/permission context |
| result | Success / Failure / Denied / Pending |
| approval_ref | Gate/approval ID nếu có |
| evidence_ref | Link bằng chứng |
| correlation_id | Liên kết event cùng workflow |

## Chuỗi bằng chứng cho hành động được bảo vệ

Ghi các tham chiếu trực tiếp giữa từng mắt xích; `correlation_id` chỉ giúp nhóm sự kiện cùng workflow, không đủ để xác định quyết định hoặc lần thực thi cụ thể.

1. **Review và quyết định:** Lưu gói review đã chốt, phiên bản/hash, đích, quyết định và các phê duyệt hoặc ngoại lệ hợp lệ làm căn cứ.
2. **Cấp quyền thực thi:** Liên kết quyền với đúng gói review và quyết định làm căn cứ; ghi hành động, phiên bản/hash, đích và thời hạn nếu có. Phê duyệt không phải là bằng chứng hành động đã chạy.
3. **Bắt đầu thực thi:** Ngay trước khi chạy, kiểm tra quyền còn hiệu lực và khớp phạm vi; ghi lần bắt đầu gắn với đúng quyền đã dùng.
4. **Kết quả đã xác minh:** Ghi tham chiếu bằng chứng thực tế, liên kết về quyền và lần bắt đầu nếu có; đối chiếu hành động, phiên bản và đích. Phân biệt thành công, thất bại hoặc rollback; không đánh dấu hoàn tất chỉ vì đã cấp quyền hay đã gọi công cụ. Nếu không bắt đầu thực thi, ghi rõ điều đó thay vì tạo bằng chứng bắt đầu.

**Đối với release:** Kết quả merge đã xác minh tại [G4](../human-review-gates/G4-code-approval.md) xác định merge commit. [G5](../human-review-gates/G5-qa-approval.md) duyệt release candidate có bằng chứng build từ commit đó và digest xác định. [G6](../human-review-gates/G6-production-approval.md) tham chiếu hồ sơ G5 và chỉ triển khai đúng digest đã được duyệt vào đích Production đã xác nhận.

Xem [hợp đồng workflow engine](../../../platform/workflow-engine/README.md) để biết trường dữ liệu và cách kiểm tra từng mắt xích trong platform.

## Integrity và privacy
Dùng centralized logging/kho audit được duyệt; hạn chế sửa/xóa, ưu tiên append-only/immutable khi phù hợp; đồng bộ thời gian; phát hiện mất log/tampering. Không ghi credential, secret, private key hoặc raw sensitive payload; mask/redact trước khi lưu.

## Review và alert
Cảnh báo tool ngoài allowlist, quyền bị từ chối lặp lại, production/destructive action thiếu approval, Gate chuyển trạng thái thiếu approver/evidence, thay đổi policy/quyền/audit config và audit pipeline gián đoạn.

Project owner xác định log store; Security/Compliance yêu cầu kiểm soát; platform owner vận hành; auditor truy cập theo nhiệm vụ.
