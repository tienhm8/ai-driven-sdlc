# Pipeline patterns

Open when changing CI triggers, concurrency, or release boundaries. The sample repositories illustrate decisions, not templates or defaults for aisoft-backend and base-web.

## Selective lessons from the samples

| Pattern | Observed in the samples | What to reuse |
|---|---|---|
| Separate validation from publishing | `1group-be` (`8be133b7`) and `1group-fe` (`b2f6a017`) declare `validate → build → deploy`. Both have `validate:compose`; BE also has MR `check:build` for selected changes, building a Docker target without tagging or pushing. Neither pipeline defines lint or test jobs. | A distinct MR validation job can check Compose or compile the application without publication. `docker compose config` checks configuration, not service startup. Verify trigger coverage before declaring any required check. |
| Cancel obsolete checks | Both samples use `workflow:auto_cancel:on_new_commit: interruptible` and mark eligible validation/build jobs `interruptible: true`. Deploy jobs are not marked interruptible. | Cancel only work that can stop safely. Do not mark a job interruptible if interruption can leave a publish, migration, or deployment incomplete; evaluate side effects rather than copying the flag. |
| Serialize conflicting jobs | The samples use `resource_group` for shared build or deploy targets. Their deployment scripts also coordinate through a shared host `flock` when available. | [`resource_group`](https://docs.gitlab.com/ci/resource_groups/) serializes jobs with the same key within one GitLab project, not across repos. A host lock covers only cooperating processes using the same lock; do not assume it exists or is enforced. Report any unprotected shared target. |
| Keep release paths explicit | `1group-be` has a manual production deployment job for release tags. `1group-fe` uses GitLab for develop deployment, with production handled outside GitLab by Amplify. | Separate validate/build/publish/deploy and record the actual target. A tag or manual button is not framework approval. Do not copy the sample's deploy scripts, runner tags, host Docker setup, Prisma commands, Next.js/Amplify settings, or SSH configuration into the bases. |

## Review triggers and runner trust

- Check the effective `workflow:rules`, job `rules`, `changes`, and `needs` for MR, branch push, tag, and protected release. Verify a push to an open MR does not create unwanted duplicate pipelines. If a required job is conditional, make sure its absence on a relevant diff is visible; do not use a successful publish job as a substitute.
- Validate untrusted changes on an approved runner without deployment credentials or host-Docker access. Select runners, images, and package sources from repository policy; the sample tags are not portable.
- Keep caches for reproducible dependency downloads separate from artifacts used as evidence. Scope artifacts to outputs needed by reviewers; do not archive credentials, environment files, or production data.

See the [GitLab CI/CD YAML reference](https://docs.gitlab.com/ci/yaml/) and [G4 evidence](g4-evidence.md).
