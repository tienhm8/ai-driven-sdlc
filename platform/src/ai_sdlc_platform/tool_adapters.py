from pathlib import Path
from .config import load_yaml

class ToolAdapterRegistry:
    # Registry/discovery only. Actual integrations must implement a secured adapter interface.
    def __init__(self, configs_root: Path): self.root = configs_root
    def get(self, name):
        path=self.root/name/"adapter.yaml"
        if not path.exists(): raise FileNotFoundError(path)
        cfg=load_yaml(path,required=True)
        if cfg.get("enabled") is not True: raise PermissionError(f"Adapter disabled: {name}")
        return cfg
    def list_enabled(self):
        if not self.root.exists(): return []
        return sorted(p.parent.name for p in self.root.glob("*/adapter.yaml") if load_yaml(p).get("enabled") is True)
