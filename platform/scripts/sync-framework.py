#!/usr/bin/env python3
import argparse, hashlib, json, shutil
from pathlib import Path

SYNC_DIRS=("templates","standards","governance")
def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def sync(framework,project,apply=False,overwrite=False):
    if not framework.is_dir(): raise FileNotFoundError(framework)
    if not project.is_dir(): raise FileNotFoundError(project)
    base=project/".ai-sdlc/framework-resources"
    manifest=project/".ai-sdlc/framework-sync.json"
    old=json.loads(manifest.read_text()) if manifest.exists() else {"files":{}}
    new={"framework_path":str(framework),"files":{}}
    copied=[]; skipped=[]; conflicts=[]
    for folder in SYNC_DIRS:
        src=framework/folder
        if not src.exists(): continue
        for item in sorted(src.rglob("*")):
            if not item.is_file() or ".git" in item.parts: continue
            rel=(Path(folder)/item.relative_to(src)).as_posix()
            target=base/rel; source_hash=sha(item); new["files"][rel]=source_hash
            if target.exists():
                target_hash=sha(target); prior=old.get("files",{}).get(rel)
                if not overwrite and prior and target_hash!=prior:
                    conflicts.append(rel); continue
                if not overwrite and not prior:
                    skipped.append(rel); continue
                if target_hash==source_hash:
                    skipped.append(rel); continue
            copied.append(rel)
            if apply:
                target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(item,target)
    if apply:
        base.mkdir(parents=True,exist_ok=True)
        manifest.write_text(json.dumps(new,indent=2),encoding="utf-8")
    return copied,skipped,conflicts

p=argparse.ArgumentParser(description="Sync shared framework resources to a project")
p.add_argument("--framework",required=True); p.add_argument("--project",required=True)
p.add_argument("--apply",action="store_true",help="Write changes; without this flag runs as dry-run")
p.add_argument("--overwrite",action="store_true",help="Overwrite project-modified files")
a=p.parse_args()
copied,skipped,conflicts=sync(Path(a.framework).resolve(),Path(a.project).resolve(),a.apply,a.overwrite)
for title,items in (("TO COPY",copied),("SKIPPED",skipped),("CONFLICTS",conflicts)):
    print(f"\n{title} ({len(items)})")
    for item in items: print(" -",item)
print("\nSYNC APPLIED" if a.apply else "\nDRY RUN ONLY")
raise SystemExit(2 if conflicts else 0)
