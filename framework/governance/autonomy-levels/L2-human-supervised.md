# L2 – Human-Supervised Execution

AI thực hiện trong phạm vi giới hạn; con người review theo checklist, sampling hoặc trigger trước khi chấp nhận.

**Ví dụ:** sinh unit test; refactor nhỏ không đổi behavior; đề xuất tối ưu cục bộ; sửa lỗi đã xác định trong sandbox/branch riêng.

**Điều kiện:** task/acceptance criteria rõ; diff review được; có test/validation; không thay đổi vùng nhạy cảm nếu chưa nâng level; giới hạn file/module/action khi cần.

Reviewer kiểm tra checklist và đào sâu trường hợp rủi ro. Nếu thay đổi behavior, quyền, schema hoặc dữ liệu, nâng lên L3/L4. L2 không cho phép AI tự approve Gate.
