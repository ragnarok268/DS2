# Artifact Summary

Release target: `v0.1.0`.

DS2 is a dependency authority and exposure mapper for AI/runtime governance.

Built as a static governance primitive for pre-execution review, not as a CVE scanner or malware detector.

It answers a narrow question: when a repo or coding agent introduces dependencies, what execution authority may have been inherited into the runtime surface? Instead of pretending to prove exploitability, DS2 builds a deterministic artifact that connects dependency declarations, observed imports, runtime exposure classes, and reviewer attention signals.

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
