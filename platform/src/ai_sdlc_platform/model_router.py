from pathlib import Path
from .config import load_yaml

class ModelRouter:
    def __init__(self, shared_ai: Path):
        root = shared_ai / "model-routing"
        self.mapping = load_yaml(root / "task-model-mapping.yaml")
        self.profiles = load_yaml(root / "model-profiles.yaml")
        self.effort = load_yaml(root / "effort-policy.yaml")
        self.fallback = load_yaml(root / "fallback-policy.yaml")

    def route(self, task_type, effort="medium"):
        profile_id = self.mapping.get("tasks", {}).get(task_type) or self.mapping.get("tasks", {}).get("default")
        if not profile_id: raise ValueError(f"No route for task type: {task_type}")
        profile = self.profiles.get("models", {}).get(profile_id)
        if not profile: raise ValueError(f"Undefined model profile: {profile_id}")
        allowed = self.effort.get("allowed_effort", ["low","medium","high"])
        if effort not in allowed: raise ValueError(f"Effort must be one of {allowed}")
        return {"task_type":task_type,"profile_id":profile_id,**profile,"effort":effort,
                "fallback":self.fallback.get("fallbacks",{}).get(profile_id,[])}
