import importlib.util, json, tempfile, unittest
from pathlib import Path
from stat import S_IMODE
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
        original = sf.shutil.copy2

        def edit_during_copy(source, temporary):
            original(source, temporary)
            self.target.write_text("local save")

        with patch.object(sf.shutil, "copy2", side_effect=edit_during_copy):
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
