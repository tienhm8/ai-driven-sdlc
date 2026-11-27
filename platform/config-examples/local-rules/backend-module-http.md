---
id: backend-module-http
scope:
  repos: [be]
  paths: ['src', 'src/modules', 'src/modules/**', 'src/app.module.ts', 'src/app.controller.ts', 'src/main.ts']
  tasks: [code-generation, code-review]
---

# Backend module and HTTP boundaries

- Keep HTTP input validation and request/response handling at the controller boundary. Keep business decisions and transaction boundaries in the service, and persistence in the repository. Use the module's registered providers; do not bypass the repository from a controller or service.
- Preserve the approved HTTP contract, including response shape, pagination, status codes, and error format. If it must change, record the proposed change and affected consumers, and confirm the contract before implementing it.
- If an existing module pattern conflicts with this rule or a higher-priority policy, do not copy it or silently refactor outside the task. Raise the conflict with the module owner and stop the affected change until it is resolved.
