#!/usr/bin/env python3
import argparse, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from ai_sdlc_platform.validators.project import validate_project

p=argparse.ArgumentParser(description="Validate project structure and configuration")
p.add_argument("--project",required=True)
p.add_argument("--framework")
a=p.parse_args()
issues=validate_project(Path(a.project).resolve(),Path(a.framework).resolve() if a.framework else None)
for x in issues: print(f"[{x['severity'].upper()}] {x['code']}: {x['message']}")
print(f"\n{sum(x['severity']=='error' for x in issues)} error(s), {sum(x['severity']=='warning' for x in issues)} warning(s)")
sys.exit(1 if any(x["severity"]=="error" for x in issues) else 0)
