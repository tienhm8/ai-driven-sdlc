---
name: gitlab-ci
description: "Design or review GitLab CI validation, build, and release jobs; verify runner and branch rules; collect merge-request checks for G4. Includes on-demand guidance for aisoft-backend and base-web."
---

# GitLab CI

1. Inspect the effective `.gitlab-ci.yml`, its includes, and the repository's required checks. Identify what runs on merge requests (MRs), branch pushes, and tags. Do not infer a job from a stage name or a comment.
2. Separate validation from publishing and deployment. MR checks should compile or test the change without pushing an image, deploying, or uploading release assets. Reuse the repository's checked-in lockfile, runtime, and approved registry. Keep credentials out of untrusted jobs, logs, images, and reports.
3. Add a test or lint job only after confirming its command, dependencies, and runner prerequisites. Use non-fixing checks. A missing runner or suite is not a passing check; do not mask failures or loosen required checks to make a pipeline pass.
4. Attach evidence to the reviewed revision: MR, head SHA, tested SHA if different, pipeline and job, result, and report if available. Follow the [G4 policy](../../../../framework/governance/human-review-gates/G4-code-approval.md); green CI is not human approval.

| Task | Open only what applies |
|---|---|
| Inspect or design NestJS CI | [Backend pipeline](references/backend-pipeline.md) |
| Inspect or design Umi Max CI | [Frontend pipeline](references/frontend-pipeline.md) |
| Change pipeline triggers, job concurrency, or validation/publish/deploy boundaries | [Pipeline patterns](references/pipeline-patterns.md) |
| Prepare or verify evidence for G4 | [G4 evidence](references/g4-evidence.md) |

Treat YAML examples as guidance, not permission to change a pipeline, start CI, publish, or deploy.
