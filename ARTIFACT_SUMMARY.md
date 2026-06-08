# Artifact Summary

Release target: `v0.1.0`.

DS2 is a dependency authority and exposure mapper for AI/runtime governance.

Built as a static governance primitive for pre-execution review, not as a CVE scanner or malware detector.

It answers a narrow question: when a repo or coding agent introduces dependencies, what execution authority may have been inherited into the runtime surface? Instead of pretending to prove exploitability, DS2 builds a deterministic artifact that connects dependency declarations, observed imports, runtime exposure classes, and reviewer attention signals.

## What It Is

DS2 is a local review tool for understanding what capabilities may enter a Python project through its dependencies.

## What It Does

- Scans a Python repo for declared dependencies and observed imports.
- Maps common packages to plain runtime capability categories such as network access, database access, process execution, browser automation, and cloud access.
- Produces deterministic report artifacts that a reviewer can inspect, compare, and rerun.

## Why It Matters

- Dependencies can change what software is able to do before a reviewer ever runs it.
- AI-assisted code generation can introduce runtime-relevant packages faster than humans notice.
- Reviewers need a simple artifact that helps them decide what deserves closer attention before execution or deployment.

## Evidence

- Tests: `python -m pytest`
- Demo: `python -m ds2.cli scan examples/fastapi_app --out artifacts/demo`
- Reports: `artifacts/demo/DS2_REPORT.md`, `artifacts/demo/ds2_graph.json`, `artifacts/demo/ds2_receipt.json`
- Screenshots: `docs/assets/ds2-demo-overview.png`, `docs/assets/ds2-report-viewer.png`, `docs/assets/ds2-receipt-evidence.png`
- CI: GitHub Actions workflow in `.github/workflows/ci.yml`

## Why This Artifact Exists

- AI-assisted development can expand dependency surface faster than humans notice.
- Runtime authority often arrives indirectly through frameworks, clients, storage libraries, job systems, browser drivers, and cloud SDKs.
- Reviewers need an artifact they can re-run, diff, and trust.

## What Makes It Resume-Grade

- Minimal, readable architecture with a standard-library-first approach.
- Reproducible outputs backed by receipt hashes and golden tests.
- Honest boundaries documented in `LIMITATIONS.md`.
- Operational framing that fits dependency governance, runtime review, and agent-era software controls.

## Reviewer Checklist

- Run `python -m ds2.cli scan examples/fastapi_app --out artifacts/demo`.
- Open `artifacts/demo/DS2_REPORT.md`.
- Check `artifacts/demo/ds2_receipt.json`.
- Run `python -m pytest`.
- Compare the generated outputs with the committed example artifacts.
- Read the report as a map of inherited execution authority, not a claim of complete runtime proof.
