# Skill Loader

Call `load_skills(shared_root, project_root, requested=None)` with the shared skills directory (normally `shared-ai/skills`) or `None`. Project-local skills come from `ai.local_resources.skills_path` in the project's `.ai-sdlc/project.yaml`, relative to the project root. If omitted, the default is `.ai-sdlc/local-skills`. A local `<name>/SKILL.md` overrides a shared skill of the same name. If `requested` is supplied, each requested name must exist. Skill content is instruction data, not executable code.
