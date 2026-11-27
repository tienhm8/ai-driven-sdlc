"""Read-only access to an explicitly registered checkout and its committed stack."""
import json
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import subprocess

COMMIT_ID = re.compile(r"(?:[a-f0-9]{40}|[a-f0-9]{64})")
PACKAGES = {"nestjs": "@nestjs/core", "umi-max": "@umijs/max", "react": "react", "antd": "antd"}


def relative_path(value: str) -> str:
    if (not isinstance(value, str) or not value or value.startswith("/") or "\\" in value
            or any(ord(char) < 32 for char in value)
            or any(part in {"", ".", "..", ".git"} for part in value.split("/"))):
        raise ValueError("Expected a normalized repository-relative path")
    return PurePosixPath(value).as_posix()


def within_scope(path: str, prefixes: tuple[str, ...]) -> bool:
    return any(path == prefix or path.startswith(prefix + "/") for prefix in prefixes)


class Checkout:
    def __init__(self, root: Path, revision: str):
        self.root = root.resolve(strict=True)
        self.revision = revision
        if not isinstance(revision, str) or not COMMIT_ID.fullmatch(revision):
            raise ValueError("Revision must be a full lowercase Git commit ID")
        if not self.root.is_dir() or not (self.root / ".git").exists():
            raise ValueError("The registered checkout is not a Git worktree root")
        top = self._git("rev-parse", "--show-toplevel")
        if not top or Path(os.fsdecode(top.removesuffix(b"\n"))).resolve() != self.root:
            raise ValueError("The registered checkout is not a Git worktree root")
        if (self._git("rev-parse", "--verify", f"{revision}^{{commit}}") != f"{revision}\n".encode("ascii")
                or self._git("cat-file", "-t", revision) != b"commit\n"):
            raise ValueError("Requested revision is not a locally available commit")

    def _git(self, *args: str) -> bytes | None:
        # Ignore session Git overrides and don't fetch missing objects or honor replace refs.
        env = {key: value for key, value in os.environ.items() if not key.startswith("GIT_")}
        env.update(GIT_NO_REPLACE_OBJECTS="1", GIT_NO_LAZY_FETCH="1", GIT_OPTIONAL_LOCKS="0", GIT_ALLOW_PROTOCOL="",
                   GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")
        result = subprocess.run(["git", "-C", str(self.root), *args], env=env, capture_output=True,
                                timeout=10, check=False)
        return result.stdout if result.returncode == 0 else None

    def read_blob(self, name: str) -> str | None:
        entry = self._git("ls-tree", self.revision, "--", name)
        if not entry or not entry.startswith((b"100644 blob ", b"100755 blob ")):
            return None
        data = self._git("cat-file", "blob", f"{self.revision}:{name}")
        try:
            return data.decode("utf-8") if data is not None else None
        except UnicodeDecodeError:
            return None

    def safe_scope(self, paths: tuple[str, ...]) -> bool:
        # New paths are allowed, but paths under committed symlinks or submodules are not.
        prefixes = sorted({str(part) for path in paths for part in (PurePosixPath(path), *PurePosixPath(path).parents)
                           if str(part) != "."})
        if not prefixes:
            return True
        entries = self._git("--literal-pathspecs", "ls-tree", "-z", "-t", self.revision, "--", *prefixes)
        if entries is None:
            return False
        requested = {os.fsencode(path) for path in prefixes}
        return not any(line.partition(b"\t")[2] in requested and line.startswith((b"120000 ", b"160000 "))
                       for line in entries.split(b"\0"))

    def observed_versions(self, technologies) -> dict:
        result = {}
        if not set(technologies) & PACKAGES.keys():
            return result
        manifest = _json_document(self.read_blob("package.json"))
        dependencies = {}
        for key in ("dependencies", "devDependencies", "optionalDependencies"):
            if isinstance(manifest.get(key), dict):
                dependencies.update(manifest[key])
        npm = _json_document(self.read_blob("package-lock.json")) if "nestjs" in technologies else {}
        yarn = _yarn_versions(self.read_blob("yarn.lock")) if set(technologies) & {"umi-max", "react", "antd"} else {}
        for tech in sorted(set(technologies) & PACKAGES.keys()):
            package = PACKAGES[tech]
            selector = dependencies.get(package)
            if not isinstance(selector, str):
                continue
            if tech == "nestjs":
                packages = npm.get("packages", {})
                entry = packages.get(f"node_modules/{package}", {}) if isinstance(packages, dict) else {}
                root = packages.get("", {}) if isinstance(packages, dict) else {}
                if not isinstance(entry, dict) or not isinstance(root, dict) or not any(
                    isinstance(root.get(key), dict) and root[key].get(package) == selector
                    for key in ("dependencies", "devDependencies", "optionalDependencies")
                ):
                    continue
                exact = entry.get("version")
            else:
                exact = yarn.get(f"{package}@{selector}")
            if isinstance(exact, str) and re.fullmatch(r"[0-9]+(?:\.[0-9]+)+(?:[-+][0-9A-Za-z.+-]+)?", exact):
                result[tech] = exact
        return result


def _json_document(text) -> dict:
    try:
        data = json.loads(text) if text else {}
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}


def _yarn_versions(text: str | None) -> dict:
    """Read the selector/version subset of Yarn Classic, not the newest transitive version."""
    selectors, result = [], {}
    for line in (text or "").splitlines():
        if not line or line.startswith("#"):
            continue
        if not line[0].isspace():
            try:
                lexer = shlex.shlex(line[:-1], posix=True) if line.endswith(":") else None
                if lexer is not None:
                    lexer.whitespace += ","
                    lexer.whitespace_split = True
                selectors = list(lexer) if lexer is not None else []
            except ValueError:
                selectors = []
        elif selectors and (match := re.fullmatch(r'  version "([^"\s]+)"', line)):
            for selector in selectors:
                result[selector] = match[1] if selector not in result else None
            selectors = []
    return result
