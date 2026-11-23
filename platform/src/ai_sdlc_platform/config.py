from pathlib import Path
import yaml

def load_yaml(path: Path, required=False):
    if not path.exists():
        if required: raise FileNotFoundError(path)
        return {}
    value = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(value, dict): raise ValueError(f"YAML root must be a mapping: {path}")
    return value

def deep_merge(base, override):
    out = dict(base)
    for key, value in override.items():
        out[key] = deep_merge(out[key], value) if isinstance(value, dict) and isinstance(out.get(key), dict) else value
    return out
