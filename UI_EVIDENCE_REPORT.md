# UI Evidence Report

Date: `2026-06-08`

Scope: final UI/demo evidence pass for the clean DS2 root. No upload, push, publish, scanner-scope expansion, or scanner-logic changes were performed.

## What UI/Demo Exists

- A minimal static demo/report viewer was added at `docs/demo-viewer.html`.
- It is a presentation layer over the existing committed demo artifacts and regenerated `artifacts/demo` outputs.
- It has:
  - no backend
  - no network calls beyond a local loopback file server used for browser rendering
  - no telemetry
  - no external assets
  - no scanner logic changes

The viewer shows:

- project name `DS2`
- dependency/exposure summary
- authority/exposure findings
- generated report/receipt references
- explicit demo-artifact labeling

## Screenshot Paths

- `docs/assets/ds2-demo-overview.png`
- `docs/assets/ds2-report-viewer.png`
- `docs/assets/ds2-receipt-evidence.png`

## PASS

- Static viewer exists and opens locally through a local loopback server at:
  - `http://127.0.0.1:8765/docs/demo-viewer.html`

- Viewer content verified:
  - `DS2` project name is visible
  - dependency/exposure summary is visible
  - authority/exposure findings are visible
  - report/graph/receipt references are visible
  - “static demo/report viewer” labeling is explicit

- Viewer links are relative:
  - `../artifacts/demo/DS2_REPORT.md`
  - `../artifacts/demo/ds2_graph.json`
  - `../artifacts/demo/ds2_receipt.json`
  - `../examples/fastapi_app/DS2_REPORT.md`

- No local `C:\` absolute paths were embedded in the viewer content.

- No external assets or tracking were found in the viewer.

- README now includes screenshot previews and accurately describes the UI as a static demo/report viewer.

- Final checks passed:
  - `python -m pytest` -> `13 passed`
  - `python -m ds2.cli scan examples/fastapi_app --out artifacts/demo` succeeded
  - `python -m ds2.cli version` -> `0.1.0`
  - demo JSON parses successfully
  - screenshot files exist

## WARN

- The clean repo root is still a fresh local git repo with no initial commit, so:
  - `git status --short` shows intentional files as untracked
  - `git diff --stat` is empty
  - `git diff --check` is empty

- Browser access to `file://` URLs was blocked by in-app browser policy, so screenshots were captured via a local loopback static server instead.
  - This did not change project code or add dependencies.

## FAIL

- No UI/demo release-blocking FAIL items were found.

## Commands Run

UI inspection:

```text
rg -n "<html|viewer|screenshot|demo image|preview|docs/assets|png|jpg|hero|report viewer" -S .
Get-Content docs/demo-viewer.html
```

Local viewer serving and browser validation:

```text
Start-Process -WindowStyle Hidden -FilePath '.\.preflight-venv\Scripts\python.exe' -ArgumentList '-m','http.server','8765','--bind','127.0.0.1' -WorkingDirectory '...\\ds2-clean-root'
http://127.0.0.1:8765/docs/demo-viewer.html
```

Screenshot generation:

```text
docs/assets/ds2-demo-overview.png
docs/assets/ds2-report-viewer.png
docs/assets/ds2-receipt-evidence.png
```

Final checks:

```text
python -m pytest
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
python -m ds2.cli version
python -c "import json, pathlib; files=['artifacts/demo/ds2_graph.json','artifacts/demo/ds2_receipt.json']; [json.loads(pathlib.Path(f).read_text(encoding='utf-8')) for f in files]; print('json-ok')"
Get-ChildItem docs\assets | Select-Object Name,Length
git status --short
git diff --stat
git diff --check
```

## Files Changed

- `README.md`
- `docs/demo-viewer.html`
- `docs/assets/ds2-demo-overview.png`
- `docs/assets/ds2-report-viewer.png`
- `docs/assets/ds2-receipt-evidence.png`
- `UI_EVIDENCE_REPORT.md`

## Scanner Logic Confirmation

- Scanner logic was unchanged.
- No changes were made to:
  - dependency collection rules
  - graph assembly behavior
  - exposure classification
  - authority classification
  - receipt generation semantics

## Publish Confirmation

- No upload happened.
- No push happened.
- No publish happened.
