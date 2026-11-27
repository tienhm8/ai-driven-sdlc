---
id: frontend-route-access-request
scope:
  repos: [fe]
  paths: ['config', 'config/routes.ts', 'src', 'src/app.tsx', 'src/access.ts', 'src/pages', 'src/pages/**', 'src/models', 'src/models/**', 'src/services', 'src/services/**', 'src/hooks', 'src/hooks/**', 'src/utils', 'src/utils/axios.ts']
  tasks: [code-generation, code-review]
---

# Frontend route, access, and request boundaries

- Keep route and menu declarations in the existing Umi route configuration and UI access decisions in the existing access layer. Hiding a route, menu, or button is not authorization; the server must enforce access to the operation and resource.
- Keep screen-level request state with the existing model or request owner and use the shared Axios client. Do not introduce a parallel client, duplicate interceptors, or change query/response semantics in the UI without confirming the API contract.
- If an existing screen conflicts with this rule or a higher-priority policy, do not copy it or silently refactor outside the task. Raise the conflict with the route or API owner and stop the affected change until it is resolved.
