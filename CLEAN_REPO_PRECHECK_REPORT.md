# Clean Repo Precheck Report

Date: `2026-06-08`

Scope: DS2-only clean release directory preflight. No upload, push, or publish actions were performed.

Clean root checked:

- `C:\Users\Brandon Caylor\Documents\New project\ds2-clean-root`

## PASS

- The clean root contains only intentional DS2 project material.
  - Source: `ds2/`, `src/ds2/`
  - Tests: DS2-only `tests/`
  - Example: `examples/fastapi_app/`
  - Intentional demo artifacts: `artifacts/demo/`
  - Release and reviewer docs:
    - `README.md`
    - `LICENSE`
    - `SECURITY.md`
    - `CONTRIBUTING.md`
    - `CHANGELOG.md`
    - `ARTIFACT_SUMMARY.md`
    - `INTERVIEW_NOTES.md`
    - `REVIEWER_QUICKSTART.md`
    - `RELEASE_CHECKLIST.md`
    - `LIMITATIONS.md`
    - `docs/ARCHITECTURE.md`
    - `docs/EXPOSURE_CLASSES.md`
    - `docs/FUTURE_INTEGRATIONS.md`
    - `docs/ROADMAP.md`

- No `.env` files were found in the clean root.

- No files over 5 MB were found in the clean root.

- `.gitignore` covers the expected hygiene cases.
  - `__pycache__/`
  - `.pytest_cache/`
  - `.venv/`
  - `.preflight-venv/`
  - `build/`
  - `dist/`
  - `*.egg-info/`
  - `.env`
  - `artifacts/*` with explicit allowlist for `artifacts/demo/DS2_REPORT.md`, `artifacts/demo/ds2_graph.json`, and `artifacts/demo/ds2_receipt.json`

- `pyproject.toml` parses successfully.
  - Project name: `ds2`
  - Version: `0.1.0`
  - Python requirement: `>=3.11`
  - CLI entry point: `ds2 = "ds2.cli:main"`

- README opening is evaluator-friendly and explains DS2 quickly.
  - The first section states what DS2 is, what it produces, and how to run the reviewer flow in under 30 seconds.

- Public docs and links are portable.
  - No `C:/Users/...` or `/C:/Users/...` markdown links were found.
  - Demo artifact names in docs match actual outputs:
    - `DS2_REPORT.md`
    - `ds2_graph.json`
    - `ds2_receipt.json`
  - Future integrations remain clearly marked as future work.

- Fresh-venv install simulation succeeded.
  - `.preflight-venv` created successfully
  - `pip` upgraded successfully
  - Editable install succeeded
  - Version command worked in the fresh venv

- Test verification succeeded in the clean root.
  - `.\\.preflight-venv\\Scripts\\python.exe -m pip install pytest`
  - `.\\.preflight-venv\\Scripts\\python.exe -m pytest`
  - Result: `13 passed`

- Reproducible demo simulation succeeded.
  - `artifacts/demo/DS2_REPORT.md` exists
  - `artifacts/demo/ds2_graph.json` exists
  - `artifacts/demo/ds2_receipt.json` exists
  - JSON parses successfully
  - `DS2_REPORT.md` uses portable relative project path `examples/fastapi_app`

## WARN

- `git status --short` shows all files as untracked because this clean root was initialized as a fresh local git repository with no initial commit yet.
  - This is expected for a new clean repo root.
  - It is not a content-hygiene problem, but it does mean `git diff --stat` and `git diff --check` are empty until files are added and committed.

- `python -m pytest` is not available immediately after `python -m pip install -e .` alone.
  - The documented fix is explicit and now reflected in the copied docs:
    - `python -m pip install pytest`
  - This is acceptable for preflight, but a future dev extra could make the test bootstrap smoother.

- Optional quality tools are not configured in this clean root.
  - No DS2-specific `ruff`, `black`, `mypy`, or `pre-commit` configuration was found.

## FAIL

- No release-blocking FAIL items were found inside the clean DS2 root.

## Commands Run

Repository state:

```text
git init
git status --short
git diff --stat
git diff --check
Get-Content .gitignore
Get-ChildItem -Recurse -Force -File -Filter .env -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
Get-ChildItem -Recurse -Force -File -ErrorAction SilentlyContinue | Where-Object { $_.Length -gt 5MB } | Sort-Object Length -Descending | Select-Object -First 20 FullName,Length
```

Metadata and docs:

```text
python -c "import tomllib, pathlib; data=tomllib.loads(pathlib.Path('pyproject.toml').read_text(encoding='utf-8')); print(data['project']['name']); print(data['project']['version']); print(data['project']['requires-python']); print(data['project']['scripts'])"
rg -n "C:/Users|/C:/Users|file://|vscode://|artifacts/demo|examples/fastapi_app|0\.1\.0|DS2_REPORT\.md|ds2_graph\.json|ds2_receipt\.json|CycloneDX|SPDX|in-toto|SLSA" README.md REVIEWER_QUICKSTART.md ARTIFACT_SUMMARY.md LIMITATIONS.md RELEASE_CHECKLIST.md SECURITY.md CONTRIBUTING.md CHANGELOG.md INTERVIEW_NOTES.md docs examples src tests
python -m ds2.cli version
```

Fresh install simulation:

```text
python -m venv .preflight-venv
.\.preflight-venv\Scripts\python.exe -m pip install -U pip
.\.preflight-venv\Scripts\python.exe -m pip install -e .
.\.preflight-venv\Scripts\python.exe -m pip install pytest
.\.preflight-venv\Scripts\python.exe -m ds2.cli version
.\.preflight-venv\Scripts\python.exe -m pytest
```

Demo reproducibility:

```text
if (Test-Path 'artifacts\demo') { Remove-Item 'artifacts\demo' -Recurse -Force }; New-Item -ItemType Directory -Path 'artifacts\demo' | Out-Null
.\.preflight-venv\Scripts\python.exe -m ds2.cli scan examples/fastapi_app --out artifacts/demo
Get-ChildItem artifacts\demo | Select-Object Name,Length
python -c "import json, pathlib; files=['artifacts/demo/ds2_graph.json','artifacts/demo/ds2_receipt.json']; [json.loads(pathlib.Path(f).read_text(encoding='utf-8')) for f in files]; print('json-ok')"
Get-Content artifacts\demo\DS2_REPORT.md
Get-Content artifacts\demo\ds2_receipt.json
```

## Exact Results

- `git status --short`
  - Shows only intentional DS2 files and directories as untracked in the fresh repo root

- `git diff --stat`
  - No output

- `git diff --check`
  - No output

- `python -c "... tomllib ..."`
  - Output:
    - `ds2`
    - `0.1.0`
    - `>=3.11`
    - `{'ds2': 'ds2.cli:main'}`

- `python -m ds2.cli version`
  - Output: `0.1.0`

- `.\\.preflight-venv\\Scripts\\python.exe -m pip install -U pip`
  - Succeeded
  - Upgraded `pip` to `26.1.2`

- `.\\.preflight-venv\\Scripts\\python.exe -m pip install -e .`
  - Succeeded
  - Installed editable package `ds2-0.1.0`

- `.\\.preflight-venv\\Scripts\\python.exe -m pip install pytest`
  - Succeeded

- `.\\.preflight-venv\\Scripts\\python.exe -m ds2.cli version`
  - Output: `0.1.0`

- `.\\.preflight-venv\\Scripts\\python.exe -m pytest`
  - Succeeded
  - Result: `13 passed`

- `.\\.preflight-venv\\Scripts\\python.exe -m ds2.cli scan examples/fastapi_app --out artifacts/demo`
  - Output:
    - `DS2 report generated: C:/Users/Brandon Caylor/Documents/New project/ds2-clean-root/artifacts/demo/DS2_REPORT.md`
    - `DS2 receipt generated: C:/Users/Brandon Caylor/Documents/New project/ds2-clean-root/artifacts/demo/ds2_receipt.json`

- `python -c "... json loads ..."`
  - Output: `json-ok`

## Files Changed

- `CLEAN_REPO_PRECHECK_REPORT.md`
- `artifacts/demo/DS2_REPORT.md`
- `artifacts/demo/ds2_graph.json`
- `artifacts/demo/ds2_receipt.json`

## Recommended Fixes

1. Make the initial git commit in `ds2-clean-root` so repo-state checks become more informative than “all files untracked.”

2. Keep the current docs that explicitly install `pytest` before running tests from a fresh clone.

3. If you want a smoother contributor bootstrap later, consider a dev/test extra such as `pip install -e .[dev]`.
   - This is optional and was not required to validate the clean release root.
