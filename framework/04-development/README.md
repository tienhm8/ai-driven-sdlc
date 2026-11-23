# 04 — Development

## Mục đích
Chuyển requirement, thiết kế và backlog đã duyệt thành code, tests, tài liệu và gói bàn giao cho Code Review. AI hỗ trợ phân tích, lập kế hoạch, sinh/chỉnh sửa code, test và tài liệu; Developer chịu trách nhiệm xác minh logic nghiệp vụ, tính đúng đắn, bảo mật, hiệu năng và khả năng bảo trì.

## Vị trí trong SDLC
- Inputs: kết quả 01 Requirement Analysis, 02 System Design, 03 Task Planning.
- Entry: G1, G2, G3 đã được phê duyệt; task đạt Definition of Ready.
- Outputs: code changes trong Git, test evidence, implementation summary, tài liệu cập nhật và handover cho 05 Code Review.
- Development `Done` không đồng nghĩa PR đã merge, QA nghiệm thu hoặc đã deploy.

## Cấu trúc
```text
04-development/
├── README.md, workflow.md, ai-instructions.md, human-review.md
├── inputs/                 # Approved baseline từ 01–03
├── coding-guidelines/      # General, error handling, logging, secure coding
├── templates/              # Development task, implementation plan, code documentation
├── checklists/             # Readiness, DoD, AI safety, handover
└── outputs/                # Summary, test evidence, handover artifacts
```

## Cách sử dụng
1. Kiểm tra input manifest và approval references.
2. Tạo task từ `templates/development-task.md`.
3. Hoàn tất `checklists/development-readiness.md`; thiếu G1/G2/G3 thì Blocked.
4. Lập plan, triển khai theo guidelines và autonomy policy.
5. Chạy kiểm tra, ghi evidence, tự review và cập nhật docs.
6. Hoàn tất DoD/handover checklist và bàn giao sang 05.

## Quy tắc
- Không tự sửa requirement, API, schema, authorization hoặc kiến trúc đã duyệt nếu chưa có change approval.
- Không đưa secrets, credentials, production data hoặc PII không cần thiết vào prompt/log/test.
- Không khai báo test pass nếu chưa chạy; ghi command, môi trường, commit và kết quả.
- AI không tự phê duyệt output của chính mình tại human review gates.
- Tuân thủ `framework/governance/`, `framework/standards/` và project-local rules; policy cấp framework có ưu tiên cao hơn tài liệu này.
