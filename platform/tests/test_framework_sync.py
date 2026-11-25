import contextlib
import errno
import io
import importlib.util, json, tempfile, unittest
import os
from pathlib import Path
from stat import S_IMODE
from struct import pack
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync-framework.py"
spec = importlib.util.spec_from_file_location("sync_framework", SCRIPT)
sf = importlib.util.module_from_spec(spec); spec.loader.exec_module(sf)

REL = "templates/a.md"


class FrameworkSyncTests(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory(); self.addCleanup(self._t.cleanup)
        root = Path(self._t.name)
        self.fw = root / "fw"; self.proj = root / "proj"
        (self.fw / "templates").mkdir(parents=True); self.proj.mkdir()
        self.src = self.fw / REL
        self.target = self.proj / ".ai-sdlc/framework-resources" / REL
        self.manifest = self.proj / ".ai-sdlc/framework-sync.json"

    def run_sync(self, **kw):
        return sf.sync(self.fw, self.proj, **kw)

    def files(self):
        return json.loads(self.manifest.read_text())["files"]

    def h(self, text):
        p = Path(self._t.name) / "h"; p.write_text(text); return sf.sha(p)

    def test_conflict_keeps_old_hash_and_restore_then_updates(self):
        self.src.write_text("v1"); self.run_sync(apply=True)
        self.target.write_text("local"); self.src.write_text("v2")
        _, _, conflicts = self.run_sync(apply=True)
        self.assertEqual(conflicts, [REL])
        self.assertEqual(self.files()[REL], self.h("v1"))
        self.assertEqual(self.target.read_text(), "local")
        self.target.write_text("v1")  # restore old copy
        copied, _, conflicts = self.run_sync(apply=True)
        self.assertEqual((copied, conflicts), ([REL], []))
        self.assertEqual(self.target.read_text(), "v2")
        self.assertEqual(self.files()[REL], self.h("v2"))

    def test_already_identical_records_hash(self):
        self.src.write_text("same")
        self.target.parent.mkdir(parents=True); self.target.write_text("same")
        _, skipped, _ = self.run_sync(apply=True)
        self.assertEqual(skipped, [REL])
        self.assertEqual(self.files()[REL], self.h("same"))

    def test_unmanaged_differing_not_adopted(self):
        self.src.write_text("src")
        self.target.parent.mkdir(parents=True); self.target.write_text("mine")
        _, skipped, conflicts = self.run_sync(apply=True)
        self.assertEqual((skipped, conflicts), ([REL], []))
        self.assertNotIn(REL, self.files())
        self.assertEqual(self.target.read_text(), "mine")

    def test_dry_run_is_non_mutating(self):
        self.src.write_text("v1")
        copied, _, _ = self.run_sync()
        self.assertEqual(copied, [REL])
        self.assertFalse((self.proj / ".ai-sdlc").exists())
        self.run_sync(apply=True); before = self.manifest.read_text()
        self.src.write_text("v2"); self.run_sync()
        self.assertEqual(self.target.read_text(), "v1")
        self.assertEqual(self.manifest.read_text(), before)

    def test_apply_preserves_existing_manifest_mode_and_uses_private_default(self):
        self.src.write_text("source")
        self.run_sync(apply=True)
        self.assertEqual(S_IMODE(self.manifest.stat().st_mode), 0o600)
        self.manifest.chmod(0o664)
        self.run_sync(apply=True)
        self.assertEqual(S_IMODE(self.manifest.stat().st_mode), 0o664)
        self.run_sync()

    def test_sync_preserves_existing_destination_mode_instead_of_using_source_mode(self):
        self.src.write_text("v1")
        self.src.chmod(0o644)
        self.run_sync(apply=True)
        self.assertEqual(S_IMODE(self.target.stat().st_mode), 0o644)
        self.target.chmod(0o600)
        self.src.write_text("v2")
        copied, _, conflicts = self.run_sync(apply=True)
        self.assertEqual((copied, conflicts), ([REL], []))
        self.assertEqual(self.target.read_text(), "v2")
        self.assertEqual(S_IMODE(self.target.stat().st_mode), 0o600)
        self.assertEqual(self.files()[REL], self.h("v2"))

    def set_test_acl(self, path, group=12345, *, default=False):
        if not hasattr(os, "setxattr"):
            self.skipTest("POSIX access ACL xattrs are unavailable")
        # Linux ACL xattr: owner rw, owning group none, named group read, mask read, other none.
        entries = ((1, 6, -1), (4, 0, -1), (8, 4, group), (16, 4, -1), (32, 0, -1))
        acl = pack("<I", 2) + b"".join(pack("<HHi", *entry) for entry in entries)
        try:
            attribute = "system.posix_acl_default" if default else sf.ACCESS_ACL
            os.setxattr(path, attribute, acl)
        except OSError as error:
            if error.errno == errno.ENOTSUP:
                self.skipTest("Temporary filesystem does not support POSIX ACLs")
            raise
        return acl

    def test_sync_preserves_source_acl_on_install_and_destination_acl_on_update(self):
        self.src.write_text("v1")
        source_acl = self.set_test_acl(self.src)
        self.assertEqual(self.run_sync(apply=True), ([REL], [], []))
        self.assertEqual(os.getxattr(self.target, sf.ACCESS_ACL), source_acl)
        target_acl = self.set_test_acl(self.target, group=12346)
        self.src.write_text("v2")
        self.assertEqual(self.run_sync(apply=True), ([REL], [], []))
        self.assertEqual(self.target.read_text(), "v2")
        self.assertEqual(os.getxattr(self.target, sf.ACCESS_ACL), target_acl)
        self.assertEqual(S_IMODE(self.target.stat().st_mode), 0o640)

    def test_sync_cannot_replace_file_if_acl_cannot_be_preserved(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        target_acl = self.set_test_acl(self.target)
        self.src.write_text("v2")
        with patch.object(sf.os, "setxattr", side_effect=OSError(errno.ENOTSUP, "ACL unsupported")):
            self.assertEqual(self.run_sync(apply=True), ([], [], [REL]))
        self.assertEqual(self.target.read_text(), "v1")
        self.assertEqual(os.getxattr(self.target, sf.ACCESS_ACL), target_acl)
        self.assertEqual(self.files()[REL], self.h("v1"))

    def test_manifest_keeps_its_acl_and_new_manifest_drops_inherited_acl(self):
        self.src.write_text("v1")
        self.target.parent.mkdir(parents=True)
        self.set_test_acl(self.manifest.parent, group=12346, default=True)
        self.run_sync(apply=True)
        self.assertEqual(S_IMODE(self.manifest.stat().st_mode), 0o600)
        with self.assertRaises(OSError) as no_acl:
            os.getxattr(self.manifest, sf.ACCESS_ACL)
        self.assertEqual(no_acl.exception.errno, errno.ENODATA)
        acl = self.set_test_acl(self.manifest, group=12345)
        self.src.write_text("v2")
        self.run_sync(apply=True)
        self.assertEqual(os.getxattr(self.manifest, sf.ACCESS_ACL), acl)
        self.assertEqual(self.files()[REL], self.h("v2"))

    def test_apply_does_not_replace_a_manifest_edited_during_sync(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        local_manifest = '{"files": {}, "local_edit": true}\n'
        original = sf.copy_atomic

        def copy_then_edit_manifest(*args, **kwargs):
            digest = original(*args, **kwargs)
            self.manifest.write_text(local_manifest)
            return digest

        with patch.object(sf, "copy_atomic", side_effect=copy_then_edit_manifest):
            with self.assertRaisesRegex(sf.SyncConflict, "Manifest changed during sync"):
                self.run_sync(apply=True)
        self.assertEqual(self.manifest.read_text(), local_manifest)

    def test_manifest_acl_preflight_failure_leaves_resources_untouched(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        acl = self.set_test_acl(self.manifest)
        self.src.write_text("v2")
        with patch.object(sf.os, "setxattr", side_effect=OSError(errno.ENOTSUP, "ACL unsupported")):
            with self.assertRaisesRegex(sf.SyncConflict, "Cannot preserve file access permissions"):
                self.run_sync(apply=True)
        self.assertEqual(self.target.read_text(), "v1")
        self.assertEqual(self.files()[REL], self.h("v1"))
        self.assertEqual(os.getxattr(self.manifest, sf.ACCESS_ACL), acl)
        self.assertFalse(self.manifest.with_name("framework-sync.pending.json").exists())

    def test_recovery_after_manifest_rename_failure_with_newer_upstream(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        replace = Path.replace

        def fail_manifest_rename(staged, destination):
            if destination == self.manifest:
                raise OSError("manifest rename failed")
            return replace(staged, destination)

        with patch.object(Path, "replace", fail_manifest_rename):
            with self.assertRaisesRegex(OSError, "manifest rename failed"):
                self.run_sync(apply=True)
        journal = self.manifest.with_name("framework-sync.pending.json")
        self.assertEqual(self.target.read_text(), "v2")
        self.assertEqual(self.files()[REL], self.h("v1"))
        pending = journal.read_bytes()
        self.assertEqual(S_IMODE(journal.stat().st_mode), 0o600)
        self.src.write_text("v3")
        self.assertEqual(self.run_sync(), ([REL], [], []))
        self.assertEqual(journal.read_bytes(), pending)
        self.assertEqual(self.files()[REL], self.h("v1"))
        self.assertEqual(self.run_sync(apply=True), ([REL], [], []))
        self.assertEqual(self.target.read_text(), "v3")
        self.assertEqual(self.files()[REL], self.h("v3"))
        self.assertFalse(journal.exists())

    def test_recovery_does_not_adopt_local_edit_after_partial_apply(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        original = sf.write_manifest

        def fail_final_write(stream, data):
            if "framework_path" in data:
                raise OSError("manifest write failed")
            return original(stream, data)

        with patch.object(sf, "write_manifest", side_effect=fail_final_write):
            with self.assertRaisesRegex(OSError, "manifest write failed"):
                self.run_sync(apply=True)
        self.assertEqual(self.target.read_text(), "v2")
        self.target.write_text("local edit")
        self.src.write_text("v3")
        self.assertEqual(self.run_sync(apply=True), ([], [], [REL]))
        self.assertEqual(self.target.read_text(), "local edit")
        self.assertEqual(self.files()[REL], self.h("v1"))

    def test_interruption_before_rename_does_not_adopt_matching_local_bytes(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        replace = Path.replace

        def interrupt(staged, target):
            if target == self.target:
                raise KeyboardInterrupt
            return replace(staged, target)

        with patch.object(Path, "replace", interrupt):
            with self.assertRaises(KeyboardInterrupt):
                self.run_sync(apply=True)
        self.target.write_text("v2")
        self.src.write_text("v3")
        self.assertEqual(self.run_sync(apply=True), ([], [], [REL]))
        self.assertEqual(self.target.read_text(), "v2")
        self.assertEqual(self.files()[REL], self.h("v1"))

    def test_failed_directory_flush_retains_journal_until_recovery_is_durable(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        journal = self.manifest.with_name("framework-sync.pending.json")
        original = sf.sync_directory

        def fail_flush(path):
            if path == self.target.parent and self.target.read_text() == "v2":
                raise OSError(errno.EIO, "resource directory flush failed")
            return original(path)

        with patch.object(sf, "sync_directory", side_effect=fail_flush):
            with self.assertRaisesRegex(OSError, "resource directory flush failed"):
                self.run_sync(apply=True)
            self.assertEqual(self.target.read_text(), "v2")
            self.assertEqual(self.files()[REL], self.h("v1"))
            self.assertTrue(journal.exists())
            self.src.write_text("v3")
            (self.fw / "standards").mkdir()
            (self.fw / "standards/b.md").write_text("unrelated")
            self.assertEqual(self.run_sync(apply=True), (["standards/b.md"], [], [REL]))
            self.assertTrue(journal.exists())
            self.assertEqual(self.files()[REL], self.h("v1"))
        self.assertEqual(self.run_sync(apply=True), ([REL], ["standards/b.md"], []))
        self.assertEqual(self.files()[REL], self.h("v3"))
        self.assertFalse(journal.exists())

    def test_staging_is_private_and_new_ancestor_directories_are_flushed(self):
        if os.name != "posix":
            self.skipTest("POSIX staging permissions and directory durability")
        relative = "templates/nested/a.md"
        source = self.fw / relative
        target = self.target.parent / "nested/a.md"
        source.parent.mkdir()
        source.write_text("resource")
        source.chmod(0o664)
        replace = Path.replace
        seen = []

        def inspect(staged, destination):
            self.assertEqual(S_IMODE(staged.parent.stat().st_mode), 0o700)
            seen.append(destination)
            return replace(staged, destination)

        with patch.object(Path, "replace", inspect), patch.object(sf, "sync_directory", wraps=sf.sync_directory) as flush:
            self.assertEqual(self.run_sync(apply=True), ([relative], [], []))
        self.assertIn(target, seen)
        self.assertIn(self.manifest, seen)
        flushed = {call.args[0] for call in flush.call_args_list}
        self.assertTrue({target.parent, target.parent.parent, self.manifest.parent, self.proj} <= flushed)

    @unittest.skipUnless(os.name == "posix", "POSIX filenames may contain a literal backslash")
    def test_recovery_accepts_literal_backslash_in_posix_filename(self):
        relative = r"templates/a\b.md"
        source = self.fw / relative
        source.write_text("v1")
        replace = Path.replace

        def fail_manifest(staged, target):
            if target == self.manifest:
                raise OSError("manifest rename failed")
            return replace(staged, target)

        with patch.object(Path, "replace", fail_manifest):
            with self.assertRaisesRegex(OSError, "manifest rename failed"):
                self.run_sync(apply=True)
        source.write_text("v2")
        self.assertEqual(self.run_sync(apply=True), ([relative], [], []))
        self.assertEqual(self.files()[relative], self.h("v2"))

    def test_unverifiable_recovery_proof_is_retained_as_conflict(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        replace = Path.replace

        def fail_manifest(staged, target):
            if target == self.manifest:
                raise OSError("manifest rename failed")
            return replace(staged, target)

        with patch.object(Path, "replace", fail_manifest):
            with self.assertRaisesRegex(OSError, "manifest rename failed"):
                self.run_sync(apply=True)
        journal = self.manifest.with_name("framework-sync.pending.json")
        entry = json.loads(journal.read_text())[REL]
        (journal.with_name("framework-sync.proofs") / entry["proof"] / "resource").unlink()
        self.src.write_text("v3")
        self.assertEqual(self.run_sync(apply=True), ([], [], [REL]))
        self.assertEqual(json.loads(journal.read_text())[REL], entry)
        self.assertEqual(self.files()[REL], self.h("v1"))
        self.assertEqual(self.target.read_text(), "v2")

    def interrupt_after_install(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        replace = Path.replace

        def fail_manifest(staged, target):
            if target == self.manifest:
                raise OSError("manifest rename failed")
            return replace(staged, target)

        with patch.object(Path, "replace", fail_manifest):
            with self.assertRaisesRegex(OSError, "manifest rename failed"):
                self.run_sync(apply=True)
        return self.manifest.with_name("framework-sync.pending.json")

    def test_recovery_io_error_is_reported_and_left_unresolved(self):
        journal = self.interrupt_after_install()
        pending = journal.read_bytes()
        with patch.object(sf, "target_hash", side_effect=OSError("disk exploded")), \
                contextlib.redirect_stderr(io.StringIO()) as stderr:
            self.assertEqual(self.run_sync(), ([], [], [REL]))
        self.assertIn(REL, stderr.getvalue())
        self.assertIn("disk exploded", stderr.getvalue())
        self.assertEqual(journal.read_bytes(), pending)

    def test_proof_cleanup_failure_does_not_fail_committed_sync(self):
        journal = self.interrupt_after_install()
        unlink = Path.unlink

        def fail_proof_unlink(path, *args, **kwargs):
            if path.name == "resource":
                raise OSError("cleanup denied")
            return unlink(path, *args, **kwargs)

        with patch.object(Path, "unlink", fail_proof_unlink), \
                contextlib.redirect_stderr(io.StringIO()) as stderr:
            self.run_sync(apply=True)
        self.assertIn("cleanup denied", stderr.getvalue())
        self.assertEqual(self.files()[REL], self.h("v2"))
        self.assertFalse(journal.exists())

    @unittest.skipUnless(os.name == "posix", "POSIX directory fsync")
    def test_update_does_not_flush_unchanged_project_root(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        with patch.object(sf, "sync_directory", wraps=sf.sync_directory) as flush:
            self.assertEqual(self.run_sync(apply=True), ([REL], [], []))
        self.assertNotIn(self.proj, {call.args[0] for call in flush.call_args_list})

    def test_invalid_manifest_checksum_prevents_overwrite_and_journaling(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        self.manifest.write_text(json.dumps({"files": {REL: "invalid"}}))
        with self.assertRaisesRegex(sf.SyncConflict, "SHA-256 checksums"):
            self.run_sync(apply=True, overwrite=True)
        self.assertEqual(self.target.read_text(), "v1")
        self.assertFalse(self.manifest.with_name("framework-sync.pending.json").exists())

    @unittest.skipUnless(os.name == "posix", "POSIX setgid inheritance")
    def test_staging_preserves_setgid_without_group_access(self):
        self.target.parent.mkdir(parents=True)
        self.target.parent.chmod(0o2770)
        with sf.replacement(self.target) as staged:
            self.assertEqual(S_IMODE(staged.parent.stat().st_mode), 0o2700)
            self.assertEqual(staged.stat().st_gid, self.target.parent.stat().st_gid)

    def test_unreadable_destination_does_not_block_other_resources(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        (self.fw / "templates/b.md").write_text("other")
        original = sf.sha

        def hash_readable_files(path):
            if path == self.target:
                raise PermissionError(errno.EACCES, "destination unreadable")
            return original(path)

        with patch.object(sf, "sha", side_effect=hash_readable_files):
            self.assertEqual(self.run_sync(apply=True), (["templates/b.md"], [], [REL]))
        self.assertEqual(self.target.read_text(), "v1")

    def test_sync_skips_optional_xattr_rejected_by_destination(self):
        if not hasattr(os, "setxattr"):
            self.skipTest("Extended attributes are unavailable")
        self.src.write_text("resource")
        original = os.setxattr
        get_attribute = os.getxattr

        def reject_user_attribute(path, name, value, **kwargs):
            if name == "user.optional":
                raise OSError(errno.EPERM, "optional attribute rejected")
            return original(path, name, value, **kwargs)

        with patch.object(sf.os, "listxattr", return_value=["user.optional"]), \
                patch.object(sf.os, "getxattr", side_effect=lambda path, name, **kw: (
                    b"value" if name == "user.optional" else get_attribute(path, name, **kw))), \
                patch.object(sf.os, "setxattr", side_effect=reject_user_attribute):
            self.assertEqual(self.run_sync(apply=True), ([REL], [], []))
        self.assertEqual(self.target.read_text(), "resource")

    def test_sync_copies_source_timestamp_and_user_xattrs(self):
        self.src.write_text("v1")
        self.src.chmod(0o644)
        if not hasattr(os, "setxattr"):
            self.skipTest("Extended attributes are unavailable")
        for version, timestamp in (("v1", 1_700_000_000), ("v2", 1_700_000_100)):
            with self.subTest(version=version):
                self.src.write_text(version)
                try:
                    os.setxattr(self.src, "user.framework-revision", version.encode())
                except OSError as error:
                    if error.errno == errno.ENOTSUP:
                        self.skipTest("Temporary filesystem does not support user xattrs")
                    raise
                os.utime(self.src, (timestamp, timestamp))
                self.assertEqual(self.run_sync(apply=True), ([REL], [], []))
                self.assertEqual(self.target.stat().st_mtime_ns, self.src.stat().st_mtime_ns)
                self.assertEqual(os.getxattr(self.target, "user.framework-revision"), version.encode())
                self.assertEqual(S_IMODE(self.target.stat().st_mode), 0o644 if version == "v1" else 0o600)
                self.target.chmod(0o600)

    def test_permission_change_during_final_checksum_is_not_overwritten(self):
        self.src.write_text("v1")
        self.src.chmod(0o644)
        self.run_sync(apply=True)
        self.src.write_text("v2")
        original_hash = sf.target_hash
        checksum_calls = 0

        def checksum_then_chmod(path):
            nonlocal checksum_calls
            digest = original_hash(path)
            checksum_calls += 1
            if checksum_calls == 3:
                path.chmod(0o600)
            return digest

        with patch.object(sf, "target_hash", side_effect=checksum_then_chmod):
            self.assertEqual(self.run_sync(apply=True), ([], [], [REL]))
        self.assertEqual(S_IMODE(self.target.stat().st_mode), 0o600)
        self.assertEqual(self.target.read_text(), "v1")
        self.assertEqual(self.files()[REL], self.h("v1"))

    def test_overwrite_replaces_and_records(self):
        self.src.write_text("src")
        self.target.parent.mkdir(parents=True); self.target.write_text("mine")
        self.run_sync(apply=True, overwrite=True)
        self.assertEqual(self.target.read_text(), "src")
        self.assertEqual(self.files()[REL], self.h("src"))

    def test_symlink_target_is_not_updated_even_with_overwrite(self):
        self.src.write_text("source")
        outside = self.proj.parent / "outside.md"
        outside.write_text("untouched")
        self.target.parent.mkdir(parents=True)
        self.target.symlink_to(outside)
        _, _, conflicts = self.run_sync(apply=True, overwrite=True)
        self.assertEqual(conflicts, [REL])
        self.assertEqual(outside.read_text(), "untouched")
        self.assertNotIn(REL, self.files())

    def test_edit_during_staging_is_preserved_and_keeps_old_baseline(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.src.write_text("v2")
        original = sf.shutil.copyfile

        def edit_during_copy(source, temporary):
            original(source, temporary)
            self.target.write_text("local save")

        with patch.object(sf.shutil, "copyfile", side_effect=edit_during_copy):
            copied, _, conflicts = self.run_sync(apply=True)
        self.assertEqual((copied, conflicts), ([], [REL]))
        self.assertEqual(self.target.read_text(), "local save")
        self.assertEqual(self.files()[REL], self.h("v1"))
        self.assertFalse(list(self.target.parent.glob(".sync-*")))

    def test_read_only_target_is_never_replaced_even_with_overwrite(self):
        self.src.write_text("v1")
        self.run_sync(apply=True)
        self.target.chmod(0o444)
        self.src.write_text("v2")
        for apply in (False, True):
            with self.subTest(apply=apply):
                copied, _, conflicts = self.run_sync(apply=apply, overwrite=True)
                self.assertEqual((copied, conflicts), ([], [REL]))
                self.assertEqual(self.target.read_text(), "v1")
                self.assertEqual(self.files()[REL], self.h("v1"))
                self.assertEqual(S_IMODE(self.target.stat().st_mode), 0o444)

    def test_failure_mid_run_preserves_progress(self):
        (self.fw / "templates/b.md").write_text("b"); self.src.write_text("a")
        orig = sf.copy_atomic
        def boom(item, target, **kwargs):
            if item.name == "b.md": raise OSError("x")
            return orig(item, target, **kwargs)
        sf.copy_atomic = boom
        try:
            with self.assertRaises(OSError): self.run_sync(apply=True)
        finally:
            sf.copy_atomic = orig
        self.assertEqual(list(self.files()), [REL])
        self.assertFalse(self.manifest.with_name(self.manifest.name + ".tmp").exists())


if __name__ == "__main__":
    unittest.main()
