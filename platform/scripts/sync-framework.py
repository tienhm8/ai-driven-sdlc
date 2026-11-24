#!/usr/bin/env python3
import argparse
from contextlib import contextmanager, nullcontext
import errno
from hashlib import sha256
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
from stat import S_IMODE, S_ISGID, S_ISREG
from tempfile import TemporaryDirectory
from uuid import uuid4

SYNC_DIRS = ("templates", "standards", "governance")
ACCESS_ACL = "system.posix_acl_access"


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
    ensure_directory(target.parent)
    sync_directory(target.parent)  # Preflight the directory whose entry will change.
    with TemporaryDirectory(dir=target.parent, prefix=".sync-") as directory:
        staging = Path(directory)
        # Strip a parent's default POSIX ACL, including named entries that chmod
        # alone would merely mask. On Windows the directory inherits host ACLs.
        apply_access_permissions(staging, None, None, private_directory=True)
        temporary = staging / "staged"
        temporary.touch(mode=0o600, exist_ok=False)
        yield temporary
        temporary.replace(target)
        sync_directory(staging)


def file_revision(info):
    return ((info.st_dev, info.st_ino, info.st_ctime_ns, info.st_mtime_ns, info.st_size, info.st_mode)
            if info is not None else None)


@contextmanager
def prepared_manifest(manifest, expected_info, expected_digest):
    def unchanged():
        return ((sha(manifest) if manifest.is_file() else None) == expected_digest
                and file_revision(require_writable(manifest)) == file_revision(expected_info))
    with replacement(manifest) as temporary:
        # Keep an open descriptor: the preserved ACL may not allow reopening the stage.
        with temporary.open("w", encoding="utf-8") as stream:
            apply_access_permissions(temporary, manifest if expected_info is not None else None, expected_info)
            if not unchanged():
                raise SyncConflict("Manifest changed during sync preparation")
            yield stream
            if not unchanged():
                raise SyncConflict("Manifest changed during sync; recovery journal retained")


def write_manifest(stream, data):
    stream.write(json.dumps(data, indent=2) + "\n")
    stream.flush()
    os.fsync(stream.fileno())


def sync_directory(directory):
    if os.name == "posix":
        fd = os.open(directory, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)


def ensure_directory(directory):
    if directory.is_dir():
        return
    ensure_directory(directory.parent)
    sync_directory(directory.parent)
    directory.mkdir(exist_ok=True)
    sync_directory(directory.parent)


def file_identity(info):
    return info.st_dev, info.st_ino


def valid_relative(name):
    rel = PurePosixPath(name)
    return (len(rel.parts) >= 2 and rel.parts[0] in SYNC_DIRS and ".." not in rel.parts
            and rel.as_posix() == name and not (os.name == "nt" and "\\" in name) and "\0" not in name)


def valid_digest(value):
    return isinstance(value, str) and re.fullmatch(r"[a-f0-9]{64}", value) is not None


def manifest_data(manifest):
    try:
        content = manifest.read_bytes()
        data = json.loads(content.decode("utf-8"))
    except FileNotFoundError:
        return {}, None
    except (UnicodeError, ValueError) as error:
        raise SyncConflict("Sync manifest is invalid") from error
    if (not isinstance(data, dict) or not isinstance(data.get("files"), dict)
            or any(not valid_relative(name) or not valid_digest(value) for name, value in data["files"].items())):
        raise SyncConflict("Sync manifest must contain valid resource paths and SHA-256 checksums")
    return data, sha256(content).hexdigest()


class SyncJournal:
    """Persist the staged digest and identity before publishing each resource."""

    def __init__(self, path, manifest, manifest_info):
        self.path = path
        self.manifest = manifest
        self.manifest_info = manifest_info
        self.proofs = path.with_name("framework-sync.proofs")
        if self.proofs.resolve() != self.proofs:
            raise SyncConflict("Recovery proof directory must not use symlinks")
        self.entries = {}
        try:
            if not S_ISREG(path.lstat().st_mode):
                raise SyncConflict("Recovery journal is not a regular file")
            data = json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            return
        except PermissionError as error:
            raise SyncConflict("Cannot read recovery journal; run sync as its owner or restore maintainer access") from error
        except (UnicodeError, ValueError) as error:
            raise SyncConflict("Recovery journal is invalid") from error
        if not isinstance(data, dict):
            raise SyncConflict("Recovery journal is invalid")
        for name, entry in data.items():
            if (not valid_relative(name) or not isinstance(entry, dict)
                    or set(entry) != {"prior", "installed", "proof", "expected"}
                    or not isinstance(entry["proof"], str) or not re.fullmatch(r"[a-f0-9]{32}", entry["proof"])
                    or not valid_digest(entry["installed"])
                    or any(entry[key] is not None and not valid_digest(entry[key]) for key in ("prior", "expected"))):
                raise SyncConflict("Recovery journal contains an invalid entry; preserve it for manual reconciliation")
        self.entries = data

    def proof_path(self, entry):
        return self.proofs / entry["proof"] / "resource" if entry.get("proof") else None

    def recover(self, base, baseline, *, apply):
        unresolved = {}
        for relative, entry in self.entries.items():
            if baseline.get(relative) != entry["prior"]:
                continue
            target = base / relative
            proof = self.proof_path(entry)
            try:
                try:
                    info = target.lstat()
                except FileNotFoundError:
                    if entry["expected"] is not None:
                        unresolved[relative] = entry
                    continue
                actual = target_hash(target)
                if file_revision(target.lstat()) != file_revision(info):
                    unresolved[relative] = entry
                    continue
                proof_info = proof.lstat() if proof.resolve() == proof else None
                same_file = (proof_info is not None and S_ISREG(proof_info.st_mode)
                             and info.st_ino != 0 and file_identity(info) == file_identity(proof_info))
                if not same_file:
                    if actual != entry["expected"] or actual == entry["installed"]:
                        unresolved[relative] = entry
                    continue
                if actual != entry["installed"] or file_revision(target.lstat()) != file_revision(info):
                    unresolved[relative] = entry
                    continue
                if apply:
                    sync_directory(target.parent)
                    if file_revision(target.lstat()) != file_revision(info):
                        unresolved[relative] = entry
                        continue
            except (OSError, SyncConflict):
                unresolved[relative] = entry
                continue
            baseline[relative] = entry["installed"]
        return unresolved

    def save(self, entries):
        with replacement(self.path) as temporary:
            with temporary.open("w", encoding="utf-8") as stream:
                apply_access_permissions(temporary, self.manifest if self.manifest_info is not None else None,
                                         self.manifest_info)
                write_manifest(stream, entries)
        sync_directory(self.path.parent)
        self.entries = entries

    def record(self, relative, prior, installed, expected, staged):
        if not self.proofs.exists():
            self.proofs.mkdir(mode=0o700)
            apply_access_permissions(self.proofs, None, None, private_directory=True)
            sync_directory(self.proofs.parent)
        token = uuid4().hex
        folder = self.proofs / token
        folder.mkdir(mode=0o700)
        apply_access_permissions(folder, None, None, private_directory=True)
        proof = folder / "resource"
        try:
            os.link(staged, proof)
        except OSError as error:
            raise SyncConflict("Cannot retain recovery proof; hard links on the same filesystem are required") from error
        sync_directory(folder)
        sync_directory(self.proofs)
        self.save({**self.entries, relative: {"prior": prior, "installed": installed,
                                           "proof": token, "expected": expected}})

    def finalize(self, unresolved):
        retired = [entry for key, entry in self.entries.items() if key not in unresolved]
        if unresolved:
            if unresolved != self.entries:
                self.save(unresolved)
        elif self.entries:
            self.path.unlink(missing_ok=True)
            sync_directory(self.path.parent)
            self.entries = {}
        for entry in retired:
            proof = self.proof_path(entry)
            if proof.resolve() == proof and proof.parent.is_dir():
                proof.unlink(missing_ok=True)
                proof.parent.rmdir()
        if retired:
            sync_directory(self.proofs)


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
    except PermissionError as error:
        raise SyncConflict(f"Cannot read destination: {path}") from error


def require_writable(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return
    if not S_ISREG(info.st_mode) or not info.st_mode & 0o222 or not os.access(path, os.W_OK):
        raise SyncConflict("Destination is read-only or is not a regular file")
    return info


def read_access_acl(path):
    try:
        return os.getxattr(path, ACCESS_ACL, follow_symlinks=False)
    except OSError as error:
        if error.errno in (getattr(errno, "ENODATA", None), errno.ENOTSUP):
            return None
        raise SyncConflict("Cannot read POSIX access ACL") from error


def apply_access_permissions(temporary, reference, info, *, preserve_owner=True, private_directory=False):
    # Linux exposes POSIX ACLs through system.posix_acl_access. Other platforms
    # retain mode handling; no claim is made about their ACL formats.
    acl = read_access_acl(reference) if reference is not None and hasattr(os, "getxattr") else None
    mode = S_IMODE(info.st_mode) & 0o777 if info is not None else 0o600
    if private_directory:
        mode = 0o700 | (temporary.stat().st_mode & S_ISGID)
    try:
        if private_directory and hasattr(os, "removexattr"):
            try:
                os.removexattr(temporary, "system.posix_acl_default", follow_symlinks=False)
            except OSError as error:
                if error.errno not in (errno.ENOTSUP, getattr(errno, "ENODATA", None)):
                    raise
        if info is not None and preserve_owner and hasattr(os, "chown"):
            staged = temporary.stat()
            if (staged.st_uid, staged.st_gid) != (info.st_uid, info.st_gid):
                os.chown(temporary, info.st_uid, info.st_gid)
        if acl is not None:
            # Setting the ACL also sets all of the ordinary mode bits.
            os.setxattr(temporary, ACCESS_ACL, acl, follow_symlinks=False)
        else:
            # Remove any ACL inherited from the destination directory before
            # changing the mode, which could otherwise activate inherited grants.
            if hasattr(os, "getxattr") and read_access_acl(temporary) is not None:
                os.removexattr(temporary, ACCESS_ACL, follow_symlinks=False)
            temporary.chmod(mode)
        if hasattr(os, "getxattr") and read_access_acl(temporary) != acl:
            raise SyncConflict("Replacement access ACL differs from the original")
        mode_mask = 0o200 if os.name == "nt" else (0o777 | S_ISGID)
        if (S_IMODE(temporary.stat().st_mode) & mode_mask) != (mode & mode_mask):
            raise SyncConflict("Replacement file mode differs from the original")
    except OSError as error:
        raise SyncConflict("Cannot preserve file access permissions") from error


def copy_resource_metadata(source, temporary):
    """Copy source timestamps and user metadata without importing access controls."""
    info = source.stat()
    os.utime(temporary, ns=(info.st_atime_ns, info.st_mtime_ns))
    if not hasattr(os, "listxattr"):
        return
    optional_errors = (errno.ENOTSUP, errno.EPERM, errno.EACCES, errno.EINVAL, getattr(errno, "ENODATA", None))
    try:
        names = os.listxattr(source, follow_symlinks=False)
    except OSError as error:
        if error.errno in optional_errors:
            return
        raise
    for name in names:
        if name.startswith("user."):
            try:
                value = os.getxattr(source, name, follow_symlinks=False)
                os.setxattr(temporary, name, value, follow_symlinks=False)
            except OSError as error:
                if error.errno not in optional_errors:
                    raise


def copy_atomic(item, target, *, expected_hash, before_install):
    with replacement(target) as temporary:
        # Keep staged contents private until the destination's permissions are known.
        shutil.copyfile(item, temporary)
        installed_hash = sha(temporary)
        copy_resource_metadata(item, temporary)
        if target_hash(target) != expected_hash:
            raise SyncConflict("Destination changed while the replacement was prepared")
        target_info = require_writable(target)
        if (expected_hash is None) != (target_info is None):
            raise SyncConflict("Destination appeared or disappeared while the replacement was prepared")
        reference = target if target_info is not None else item
        with temporary.open("r+b") as staged:
            apply_access_permissions(temporary, reference, target_info or item.stat(),
                                     preserve_owner=target_info is not None)
            os.fsync(staged.fileno())
        before_install(installed_hash, temporary)
        if target_hash(target) != expected_hash or file_revision(require_writable(target)) != file_revision(target_info):
            raise SyncConflict("Destination changed while access permissions were prepared")
    sync_directory(target.parent)
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
    journal_path = manifest.with_name("framework-sync.pending.json")
    if journal_path.resolve() != journal_path:
        raise SyncConflict("Recovery journal path must not use symlinks")
    manifest_info = require_writable(manifest) if apply else None
    old, manifest_digest = manifest_data(manifest)
    prior_files = dict(old.get("files", {}))
    journal = SyncJournal(journal_path, manifest, manifest_info)
    unresolved = journal.recover(base, prior_files, apply=apply)
    if apply and journal.entries:
        # Publish recovered progress before reusing any journal slots.
        with prepared_manifest(manifest, manifest_info, manifest_digest) as stream:
            write_manifest(stream, {**old, "files": prior_files})
        sync_directory(manifest.parent)
        manifest_info = require_writable(manifest)
        manifest_digest = sha(manifest)
        journal.manifest_info = manifest_info
        journal.finalize(unresolved)
    new = {"framework_path": str(framework), "files": dict(prior_files)}
    copied, skipped, conflicts = [], [], sorted(unresolved)
    with (prepared_manifest(manifest, manifest_info, manifest_digest) if apply else nullcontext()) as stream:
        try:
            for folder in SYNC_DIRS:
                for item in sorted((framework / folder).rglob("*")):
                    if not item.is_file() or ".git" in item.relative_to(framework).parts:
                        continue
                    relative = item.relative_to(framework).as_posix()
                    if relative in unresolved:
                        continue
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
                            new["files"][relative] = copy_atomic(
                                item, target, expected_hash=expected_hash,
                                before_install=lambda digest, staged: journal.record(
                                    relative, prior_files.get(relative), digest, expected_hash, staged),
                            )
                    except SyncConflict:
                        conflicts.append(relative)
                        continue
                    copied.append(relative)
        except Exception as error:
            if not apply:
                raise
            unresolved = journal.recover(base, new["files"], apply=True)
            write_manifest(stream, new)
            # Re-raise after committing partial progress.
            failure = error
        else:
            failure = None
            if apply:
                write_manifest(stream, new)
    if apply:
        sync_directory(manifest.parent)
        journal.manifest_info = require_writable(manifest)
        journal.finalize(unresolved)
    if failure is not None:
        raise failure
    return copied, skipped, conflicts


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sync shared framework resources to a project")
    parser.add_argument("--framework", required=True, type=Path)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--apply", action="store_true", help="Write changes; default is dry-run")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite differing target files")
    args = parser.parse_args(argv)
    try:
        copied, skipped, conflicts = sync(args.framework, args.project, args.apply, args.overwrite)
    except SyncConflict as error:
        parser.exit(2, f"Sync conflict: {error}\n")
    for title, items in (("COPIED" if args.apply else "TO COPY", copied),
                         ("SKIPPED", skipped), ("CONFLICTS", conflicts)):
        print(f"\n{title} ({len(items)})")
        for item in items:
            print(" -", item)
    print("\nSYNC APPLIED" if args.apply else "\nDRY RUN ONLY")
    return 2 if conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
