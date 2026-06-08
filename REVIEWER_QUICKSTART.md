# Reviewer Quickstart

Release target: `v0.1.0`.

## What DS2 Is

DS2 is a deterministic dependency authority and runtime exposure mapper for Python repositories. It combines declared dependencies, observed imports, and lightweight classification rules into a readable report plus machine-checkable artifacts.

## Expected Runtime

- Example scan: typically well under 30 seconds on a normal local machine.
- Test suite: typically under a minute for this repository.

## One-Command Review Flow

```bash
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
```

## Where Outputs Appear

- `artifacts/demo/DS2_REPORT.md`
- `artifacts/demo/ds2_graph.json`
- `artifacts/demo/ds2_receipt.json`

## Optional Static Viewer

Serve the repository locally:

```bash
python -m http.server 8765
```

Then open:

- `http://127.0.0.1:8765/docs/demo-viewer.html`

## What To Look At First

1. `README.md` for the project framing and evaluator pitch.
2. `artifacts/demo/DS2_REPORT.md` for the human-readable output.
3. `artifacts/demo/ds2_receipt.json` for stable hashes and generated-file metadata.
4. `LIMITATIONS.md` for the honest static-analysis boundaries.

## How To Verify Determinism

Run the same command twice:

```bash
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
```

Then confirm:

- `artifacts/demo/ds2_receipt.json` stays unchanged.
- `artifacts/demo/DS2_REPORT.md` stays unchanged.
- if testing from a fresh clone, install `pytest` first with `python -m pip install pytest`
- `python -m pytest` passes, including golden-output checks.
