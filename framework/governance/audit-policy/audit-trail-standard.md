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

## Integrity và privacy
Dùng centralized logging/kho audit được duyệt; hạn chế sửa/xóa, ưu tiên append-only/immutable khi phù hợp; đồng bộ thời gian; phát hiện mất log/tampering. Không ghi credential, secret, private key hoặc raw sensitive payload; mask/redact trước khi lưu.

## Review và alert
Cảnh báo tool ngoài allowlist, quyền bị từ chối lặp lại, production/destructive action thiếu approval, Gate chuyển trạng thái thiếu approver/evidence, thay đổi policy/quyền/audit config và audit pipeline gián đoạn.

Project owner xác định log store; Security/Compliance yêu cầu kiểm soát; platform owner vận hành; auditor truy cập theo nhiệm vụ.
