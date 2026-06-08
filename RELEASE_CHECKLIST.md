# Release Checklist

Target release: `v0.1.0`.

Use this checklist before publishing a DS2 OSS release.

## Environment

- Confirm Python 3.11+ is available.
- Confirm the repo is in a clean, reviewable state.
- Confirm committed example artifacts match the current scanner output.

## Clean Install

```bash
python -m pip install -e .
python -m ds2.cli version
```

Expected result:

- Editable install succeeds without fetching project-specific runtime extras.
- `python -m ds2.cli version` prints the release version.

## CLI Smoke Test

```bash
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
```

Expected result:

- `artifacts/demo/DS2_REPORT.md` is generated.
- `artifacts/demo/ds2_graph.json` is generated.
- `artifacts/demo/ds2_receipt.json` is generated.
- Terminal output explicitly confirms report and receipt generation.

## Pytest

Install the test runner in a fresh environment first:

```bash
python -m pip install pytest
```

Then run:

```bash
python -m pytest
```

Expected result:

- Full suite passes, including deterministic golden-output coverage.

## Example Scan Generation

Regenerate the public demo artifacts:

```bash
python -m ds2.cli scan examples/fastapi_app --out examples/fastapi_app
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
```

Expected result:

- `examples/fastapi_app` contains the committed report, graph, and receipt.
- `artifacts/demo` mirrors the same contents for low-friction reviewer evaluation.

## Artifact Verification

- Compare `examples/fastapi_app/DS2_REPORT.md` against `artifacts/demo/DS2_REPORT.md`.
- Compare `examples/fastapi_app/ds2_graph.json` against `artifacts/demo/ds2_graph.json`.
- Compare `examples/fastapi_app/ds2_receipt.json` against `artifacts/demo/ds2_receipt.json`.
- Confirm repeated scans keep hashes stable when inputs have not changed.

## Lint And Type Check Status

- Lint: intentionally omitted in v1 to keep evaluation friction low and avoid introducing extra toolchain requirements.
- Type check: intentionally omitted in v1 for the same reason.
- Release note should state this explicitly rather than implying those gates exist.
