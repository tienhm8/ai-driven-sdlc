# Thiết kế module

Khai báo controller trong `controllers`, service trong `providers`, và chỉ `exports` contract được module khác dùng. Module tiêu thụ import module sở hữu provider. Nếu có vòng phụ thuộc, tách orchestration hoặc contract trước khi cân nhắc `forwardRef`.
