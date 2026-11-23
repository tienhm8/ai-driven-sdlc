# Human Review – Monitoring & Maintenance

> **Giai đoạn:** 08 – Monitoring & Maintenance  
> **Mục đích:** Bảo đảm hệ thống được giám sát, bảo trì và xử lý sự cố an toàn; cảnh báo và phân tích của AI được xác minh trước các hành động có tác động lớn.  
> **Review Gate:** G7 – Incident Approval (kích hoạt theo sự kiện đối với sự cố nghiêm trọng); các thay đổi thông thường tuân thủ change control và Gate tương ứng.  
> **Người phê duyệt chính:** Incident Commander (IC) đối với quyết định xử lý sự cố nghiêm trọng

## 1. Nguyên tắc review

- AI có thể phát hiện bất thường, tương quan tín hiệu và đề xuất Root Cause Analysis; đây là giả thuyết cho đến khi được xác minh.
- Phân biệt rõ **phát hiện**, **khuyến nghị**, **hành động tự động có giới hạn** và **quyết định của Incident Commander**.
- Ưu tiên an toàn con người, bảo vệ dữ liệu, giới hạn blast radius và khôi phục dịch vụ.
- Không cho AI tự thực hiện hành động phá hủy dữ liệu, thay đổi quyền, tắt kiểm soát bảo mật hoặc thay đổi production ngoài policy.
- Postmortem tập trung vào cải thiện hệ thống và quy trình, không quy kết cá nhân; các kết luận phải dựa trên bằng chứng.

## 2. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm review / quyết định |
|---|---|
| SRE / Operations Engineer | Review alert, health, telemetry, capacity; xác minh tác động và thực hiện runbook trong phạm vi được ủy quyền. |
| Incident Commander – **Approver G7** | Điều phối sự cố nghiêm trọng, xác lập mức độ, ưu tiên, phân công và phê duyệt phương án xử lý theo incident policy. |
| Service / System Owner | Đánh giá ảnh hưởng dịch vụ, dependency, business impact và xác nhận phương án phục hồi. |
| Tech Lead / Engineering Lead | Review giả thuyết kỹ thuật, hotfix, rollback, mitigation và rủi ro thay đổi. |
| Security Incident Lead (khi liên quan) | Điều phối đánh giá/ứng phó sự cố bảo mật, bảo toàn bằng chứng và nghĩa vụ thông báo theo policy. |
| Database / Data Owner | Phê duyệt hành động ảnh hưởng dữ liệu, restore, replay, migration hoặc data correction. |
| Product / Business Owner | Đánh giá tác động nghiệp vụ, thông báo stakeholder và quyết định trade-off nghiệp vụ trong thẩm quyền. |
| Communications Lead (khi cần) | Kiểm tra thông tin cập nhật nội bộ/khách hàng, bảo đảm chính xác và đúng thẩm quyền công bố. |

## 3. Trách nhiệm review của con người

1. **Alert validation:** Xác minh alert, nguồn telemetry, phạm vi ảnh hưởng và khả năng false positive.
2. **Severity & impact:** Xác định severity theo tiêu chí tổ chức; đánh giá người dùng, dịch vụ, dữ liệu, vùng địa lý và business impact.
3. **Incident command:** Với sự cố nghiêm trọng, xác định IC, incident team, kênh liên lạc, mục tiêu và nhịp cập nhật.
4. **AI RCA validation:** Kiểm tra giả thuyết root cause bằng log, metrics, traces, deploy/change history và bằng chứng độc lập; phân biệt fact với inference.
5. **Mitigation safety:** Đánh giá tác động phụ, blast radius, reversibility, data integrity, security và khả năng làm tình hình xấu hơn.
6. **Action authorization:** Xác định ai có quyền phê duyệt và thực hiện restart, failover, rollback, traffic shift, disable feature, restore hoặc thay đổi production.
7. **Data protection:** Không xóa/ghi đè dữ liệu, reset state hoặc chạy script sửa dữ liệu nếu chưa có approval, backup và phương án phục hồi phù hợp.
8. **Security/privacy response:** Bảo toàn bằng chứng, giới hạn truy cập, xử lý credential/token và tuân thủ quy trình báo cáo sự cố.
9. **Recovery validation:** Xác minh service health, error rate, latency, data consistency và trải nghiệm người dùng sau mitigation.
10. **Communication:** Xác nhận nội dung, tần suất và đối tượng nhận thông báo; không công bố nguyên nhân chưa được xác minh như sự thật.
11. **Post-incident review:** Đánh giá timeline, contributing factors, detection/response gap và action items có owner/deadline.
12. **Maintenance/change review:** Đánh giá patch, upgrade, capacity tuning và thay đổi vận hành theo change management; kích hoạt các Gate khác nếu thay đổi thuộc phạm vi của chúng.

## 4. Review theo Autonomy Level

| Level | Cách con người tham gia |
|---|---|
| L1 | AI có thể phân loại log, tổng hợp dashboard, phát hiện bất thường và gửi cảnh báo. Tác vụ tự động chỉ được phép khi đã định nghĩa rõ phạm vi, giới hạn, log và cơ chế dừng/hoàn tác. |
| L2 | AI có thể đề xuất hoặc thực hiện runbook rủi ro thấp đã được phê duyệt trước; SRE review theo điều kiện, sampling hoặc khi có dấu hiệu bất thường. |
| L3 | Bắt buộc người có thẩm quyền review và phê duyệt hành động production có tác động đáng kể, thay đổi cấu hình, failover hoặc remediation vượt phạm vi tự động cho phép. |
| L4 | IC/owner quyết định ứng phó sự cố nghiêm trọng, hành động không thể đảo ngược, xử lý dữ liệu quan trọng, security incident và trade-off ảnh hưởng lớn; AI chỉ tư vấn. |

**Quy tắc:** G7 không phải approval cho mọi alert. G7 được kích hoạt khi incident đạt ngưỡng nghiêm trọng theo incident policy hoặc khi hành động ứng phó có rủi ro cao yêu cầu IC phê duyệt.

## 5. Checklist G7 – Sự cố nghiêm trọng

- [ ] Incident được xác nhận và severity được phân loại theo policy.
- [ ] Incident Commander và người chịu trách nhiệm kỹ thuật đã được chỉ định.
- [ ] Impact, affected services/users/data và phạm vi ảnh hưởng đã được đánh giá.
- [ ] Bằng chứng telemetry/log/change history được bảo toàn phù hợp.
- [ ] Giả thuyết AI được phân biệt với dữ kiện đã xác minh.
- [ ] Các phương án mitigation, rủi ro và blast radius được đánh giá.
- [ ] Hành động ảnh hưởng dữ liệu/bảo mật có approval chuyên môn cần thiết.
- [ ] Người phê duyệt, người thực hiện và điều kiện dừng/rollback đã rõ.
- [ ] Recovery criteria và cách xác minh dịch vụ phục hồi đã xác định.
- [ ] Stakeholder/customer communication đúng thẩm quyền.
- [ ] Timeline, quyết định và action được ghi nhận.
- [ ] Postmortem và corrective actions được lên kế hoạch.

## 6. Điều kiện quyết định G7

**Approve mitigation** khi IC xác nhận phương án phù hợp với severity, mục tiêu khôi phục, rủi ro và thẩm quyền; các owner chuyên môn cần thiết đã tham gia; có tiêu chí theo dõi/dừng và ghi nhận quyết định.

**Reject / Request alternative** khi phương án có nguy cơ làm mất dữ liệu, mở rộng sự cố, phá vỡ bằng chứng, tạo lỗ hổng bảo mật hoặc vượt thẩm quyền.

Trong tình huống khẩn cấp, tổ chức có thể quy định quy trình emergency action riêng với người có thẩm quyền, phạm vi hành động tối thiểu và hậu kiểm bắt buộc. Không mặc định AI có quyền hành động khẩn cấp. Mọi ngoại lệ phải được audit theo policy.

## 7. Khi yêu cầu AI phân tích lại

Cung cấp incident ID, khoảng thời gian, nguồn telemetry được phép, thay đổi gần nhất và câu hỏi cụ thể. AI phải tách:
- Facts: dữ liệu quan sát được và nguồn.
- Hypotheses: giả thuyết, mức độ tin cậy và bằng chứng cần kiểm tra.
- Recommendations: hành động đề xuất, rủi ro và khả năng hoàn tác.

SRE/owner xác minh giả thuyết. IC quyết định phương án đối với incident nghiêm trọng.

## 8. Bằng chứng và hồ sơ review

Lưu alert/incident ID, severity, timeline, telemetry references, AI analysis version, facts/hypotheses, quyết định IC, người thực hiện, command/change log, approval timestamp, recovery evidence, communication log và postmortem/action items. Tuân thủ retention và access policy; không sao chép dữ liệu nhạy cảm không cần thiết vào báo cáo.

## 9. Trách nhiệm cuối cùng

SRE/Operations chịu trách nhiệm giám sát và vận hành trong phạm vi được giao. Incident Commander chịu trách nhiệm điều phối và quyết định ứng phó sự cố nghiêm trọng theo thẩm quyền. Service, Security và Data Owner chịu trách nhiệm đối với đánh giá chuyên môn tương ứng. AI không tự xác nhận root cause, không tự phê duyệt G7 và không được vượt quyền hành động đã cấp.
