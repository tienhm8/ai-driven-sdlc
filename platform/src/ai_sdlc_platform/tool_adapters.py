from pathlib import Path
import re

from .config import load_yaml
from .manifest_schema import ID_PATTERN, strict_yaml_mapping

class ToolAdapterRegistry:
    # Registry/discovery only. Actual integrations must implement a secured adapter interface.
    def __init__(self, configs_root: Path): self.root = configs_root
    def get(self, name):
        path=self.root/name/"adapter.yaml"
        if not path.exists(): raise FileNotFoundError(path)
        cfg=load_yaml(path,required=True)
        if cfg.get("enabled") is not True: raise PermissionError(f"Adapter disabled: {name}")
        return cfg
    def require_outside(self, workspaces):
        root = self.root.resolve()
        if any(root.is_relative_to(path) or path.is_relative_to(root) for path in workspaces):
            raise ValueError("Managed adapter registry must not overlap a workspace")

    def managed(self, name):
        """Load only operator-registered, explicitly enabled managed adapter data."""
        if not isinstance(name, str) or not re.fullmatch(ID_PATTERN, name):
            raise ValueError("Invalid tool ID")
        root = self.root.resolve()
        path = root / name / "adapter.yaml"
        if path.resolve() != path:
            raise ValueError("Managed adapter entries must not use symlinks")
        config = strict_yaml_mapping(path.read_text(encoding="utf-8"))
        if config.get("enabled") is not True or config.get("name") != name:
            raise ValueError("Managed adapter is disabled or has a mismatched ID")
        return config

    def list_enabled(self):
        if not self.root.exists(): return []
        return sorted(p.parent.name for p in self.root.glob("*/adapter.yaml") if load_yaml(p).get("enabled") is True)
