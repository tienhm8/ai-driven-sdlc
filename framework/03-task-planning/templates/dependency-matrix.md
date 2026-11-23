# Mẫu Dependency Matrix
| Dự án/kế hoạch | Phiên bản/ngày | Người lập | Baseline |
|---|---|---|---|

| Dependency ID | Tiền nhiệm (predecessor) | Kế nhiệm (successor) | Loại | Mô tả/interface | Có chặn không? | Cần trước ngày | Owner | Trạng thái | Biện pháp giảm thiểu |
|---|---|---|---|---|---|---|---|---|---|
| DEP-001 | | | `Internal/External/Technical/Data/Resource/Approval` | | | | | `Open/At risk/Resolved` | |

Dependency bên ngoài:
| Team/vendor/hệ thống | Deliverable | Owner/liên hệ | Lead time | Hạn chót | Leo thang | Trạng thái |
|---|---|---|---|---|---|---|

Thứ tự thực hiện/critical path:  
Công việc có thể song song:  
Task bị chặn:  
Rủi ro:
| Risk ID | Dependency | Xác suất | Tác động | Dấu hiệu kích hoạt | Phương án dự phòng | Owner |
|---|---|---|---|---|---|---|

Rà soát: mọi blocker đều có owner/hạn; lead time bên ngoài đã xác nhận; dependency vòng tròn đã giải quyết; thứ tự khớp với architecture/contract; dependency tác động lớn đều có biện pháp giảm thiểu.
