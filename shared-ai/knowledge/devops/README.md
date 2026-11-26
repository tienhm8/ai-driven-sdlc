# Knowledge: devops

Chỉ mục tra cứu theo câu hỏi; không chép lại standards hay checklist.

| Câu hỏi | Đọc chuẩn | Dùng skill |
|---|---|---|
| Phát hành và hạ tầng theo chuẩn nào? | [Triển khai](../../../framework/07-deployment/README.md), [Vận hành](../../../framework/08-monitoring-maintenance/README.md) | [docker](../../skills/devops/docker/SKILL.md), [kubernetes](../../skills/devops/kubernetes/SKILL.md), [terraform](../../skills/devops/terraform/SKILL.md) |
| Khi nào cần phê duyệt phát hành? | [G6](../../../framework/governance/human-review-gates/G6-production-approval.md) và [quyền theo môi trường](../../../framework/07-deployment/ai-instructions.md) | Không có skill thay thế phê duyệt của con người |

**Gợi ý:** phát hành artifact bất biến giữa các môi trường; xác nhận version, health check, telemetry, người trực; định nghĩa điều kiện dừng theo tỷ lệ lỗi/độ trễ và diễn tập phục hồi trước thay đổi rủi ro.

**Ghi kết quả ở đâu:** Ghi bằng chứng phát hành trong [deployment record](../../../framework/07-deployment/outputs/README.md) và kết quả theo dõi trong [hồ sơ vận hành](../../../framework/08-monitoring-maintenance/outputs/README.md).
