# CI Hardening Report

## Files Changed

- `.gitattributes`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/ARCHITECTURE.md`

## Repo-Layout Findings

- `src/ds2/` is the actual package source tree.
- Top-level `ds2/` is not a duplicate implementation.
- `ds2/__init__.py` is a small development shim that points module resolution at `src/ds2` so `python -m ds2.cli` works from the repo root during local evaluation.
- The shim was kept intentionally and documented instead of removed.
- Local-only directories such as `.preflight-venv/` and `_runtime_tmp/` are ignored and not tracked.

## Commands Run

```powershell
git status --short
git diff --check
git diff --stat
python -m pytest
python -m ds2.cli version
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
@'
import json
from pathlib import Path
for p in [
    Path("artifacts/demo/ds2_graph.json"),
    Path("artifacts/demo/ds2_receipt.json"),
]:
    json.loads(p.read_text(encoding="utf-8"))
print("json-ok")
'@ | python -
git diff --check
git add .
git diff --cached --check
git commit -m "Add CI verification workflow"
git push
```

## Local Results

- `python -m pytest`: passed, `13 passed in 3.87s`
- `python -m ds2.cli version`: returned `0.1.0`
- `python -m ds2.cli scan examples/fastapi_app --out artifacts/demo`: succeeded and regenerated demo artifacts
- Demo JSON parse: passed, `json-ok`
- `git diff --check`: passed with working-copy LF/CRLF warnings before adding `.gitattributes`

## GitHub Actions Result

- Workflow file: `.github/workflows/ci.yml`
- Badge URL responded successfully.
- Repository page includes the CI badge in the rendered README.
- Repository page includes the screenshot references used in the README.
- GitHub detected the MIT license.
- Actions workflow page loaded successfully and exposed success markers for the CI run.
- Pushed commit: `510ac96` with message `Add CI verification workflow`

## Scanner Behavior

No scanner behavior was changed. This pass adds repository automation and documentation only.

## Release Safety

- No package publication was performed.
- No GitHub release was created.
- No optional local verification script was added because the workflow and existing commands were already sufficient.
