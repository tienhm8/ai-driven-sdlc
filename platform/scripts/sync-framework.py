#!/usr/bin/env python3
import argparse
from contextlib import contextmanager
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
from stat import S_IMODE, S_ISREG
from tempfile import NamedTemporaryFile

SYNC_DIRS = ("templates", "standards", "governance")


class SyncConflict(Exception):
    """The destination cannot be safely replaced."""


def sha(path):
    digest = sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


@contextmanager
def replacement(target):
    target.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(dir=target.parent, prefix=".sync-", delete=False) as stream:
        temporary = Path(stream.name)
    try:
        yield temporary
        temporary.replace(target)
    finally:
        temporary.unlink(missing_ok=True)


def write_manifest(manifest, data):
    try:
        mode = S_IMODE(manifest.stat().st_mode) & 0o777
    except FileNotFoundError:
        mode = 0o600
    with replacement(manifest) as temporary:
        temporary.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        temporary.chmod(mode)


def target_hash(path):
    if path.resolve() != path:
        raise SyncConflict("Destination uses a symlink")
    try:
        info = path.lstat()
        if not S_ISREG(info.st_mode):
            raise SyncConflict("Destination is not a regular file")
        return sha(path)
    except FileNotFoundError:
        return None


def require_writable(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return
    if not S_ISREG(info.st_mode) or not info.st_mode & 0o222 or not os.access(path, os.W_OK):
        raise SyncConflict("Destination is read-only or is not a regular file")


def copy_atomic(item, target, *, expected_hash):
    with replacement(target) as temporary:
        shutil.copy2(item, temporary)
        installed_hash = sha(temporary)
        require_writable(target)
        if target_hash(target) != expected_hash:
            raise SyncConflict("Destination changed while the replacement was prepared")
    return installed_hash


def sync(framework, project, apply=False, overwrite=False):
    framework, project = framework.resolve(), project.resolve()
    for root in (framework, project):
        if not root.is_dir():
            raise FileNotFoundError(root)

    base = project / ".ai-sdlc/framework-resources"
    manifest = project / ".ai-sdlc/framework-sync.json"
    for path in (base, manifest):
        if path.resolve() != path:
            raise ValueError(f"Sync path must not use symlinks: {path}")
    old = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else {}
    prior_files = old.get("files", {})
    # Retain the last known installed baseline for anything not updated here.
    new = {"framework_path": str(framework), "files": dict(prior_files)}
    copied, skipped, conflicts = [], [], []
    try:
        for folder in SYNC_DIRS:
            for item in sorted((framework / folder).rglob("*")):
                if not item.is_file() or ".git" in item.relative_to(framework).parts:
                    continue
                relative = item.relative_to(framework).as_posix()
                target = base / relative
                try:
                    if item.resolve() != item:
                        raise SyncConflict("Source uses a symlink")
                    source_hash = sha(item)
                    expected_hash = target_hash(target)
                    if expected_hash is not None:
                        prior_hash = prior_files.get(relative)
                        if expected_hash == source_hash:
                            skipped.append(relative)
                            new["files"][relative] = expected_hash
                            continue
                        if not overwrite and (not prior_hash or expected_hash != prior_hash):
                            (conflicts if prior_hash else skipped).append(relative)
                            continue
                        require_writable(target)
                    if apply:
                        new["files"][relative] = copy_atomic(item, target, expected_hash=expected_hash)
                except SyncConflict:
                    conflicts.append(relative)
                    continue
                copied.append(relative)
    finally:
        if apply:
            write_manifest(manifest, new)
    return copied, skipped, conflicts


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sync shared framework resources to a project")
    parser.add_argument("--framework", required=True, type=Path)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--apply", action="store_true", help="Write changes; default is dry-run")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite differing target files")
    args = parser.parse_args(argv)
    copied, skipped, conflicts = sync(args.framework, args.project, args.apply, args.overwrite)
    for title, items in (("COPIED" if args.apply else "TO COPY", copied),
                         ("SKIPPED", skipped), ("CONFLICTS", conflicts)):
        print(f"\n{title} ({len(items)})")
        for item in items:
            print(" -", item)
    print("\nSYNC APPLIED" if args.apply else "\nDRY RUN ONLY")
    return 2 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
