# Reviewer Experience Report

Date: `2026-06-08`

Perspective: first-time external reviewer starting only from `README.md`.

## Summary

- DS2 purpose understood within 60 seconds: `YES`
- Screenshots improve understanding: `YES, moderately`
- Demo artifacts support README claims: `YES`
- Could explain DS2 to another engineer after 5 minutes: `YES`

## What I Followed

From `README.md`:

```bash
python -m pip install -e .
python -m pip install pytest
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
python -m pytest
```

Then I followed the stated review path:

- opened `artifacts/demo/DS2_REPORT.md`
- checked `artifacts/demo/ds2_receipt.json`
- compared against `examples/fastapi_app/`
- inspected the static demo/report viewer and screenshots

## Findings

### MAJOR

- Fixed: the README said a static demo/report viewer existed at `docs/demo-viewer.html`, but it did not explain how a first-time reviewer should actually open it locally.
  - Why it mattered:
    - on GitHub, an `.html` file is not automatically the same as a rendered local demo experience
    - the presence of screenshots implied a viewer mattered, but the reviewer path to it was missing
  - Fix applied:
    - added a minimal local-view instruction to `README.md`
    - added the same instruction to `REVIEWER_QUICKSTART.md`
    - local command:
      - `python -m http.server 8765`
      - open `http://127.0.0.1:8765/docs/demo-viewer.html`

### MINOR

- Terminology: `dependency/runtime authority` is memorable, but slightly jargon-heavy on first read.
  - The next paragraph clarifies it enough, so this did not block understanding.

- Terminology: `inherited execution authority` is useful but abstract.
  - A reviewer can infer the meaning from the examples, though the phrase is more governance-oriented than mainstream packaging language.

- Expected output vs actual output:
  - README demo output uses `.../artifacts/demo/...` as a placeholder.
  - Actual CLI output prints a full absolute path.
  - This is acceptable, but it is a visible difference from the snippet.

- Screenshot presentation:
  - The screenshots help reinforce that a demo/viewer exists.
  - They do not replace the report itself; the report is still the strongest artifact.

### NIT

- The `ps + netstat + tree` phrase is a good hook, but it is more evocative than precise.

- `Current release candidate: v0.1.0` is fine, though a casual reviewer may not care unless they are checking release maturity.

## Confusion Log

- Initial confusion:
  - What exactly does `authority` mean in DS2?
  - Resolved by the README explanation and the generated report sections.

- Initial confusion:
  - Is this an SBOM/provenance tool?
  - Resolved by the explicit “not an SBOM generator” section.

- Initial confusion:
  - How do I open the static viewer?
  - Severity before fix: `MAJOR`
  - Resolved by the docs patch described above.

## Expected Output Versus Actual Output

- `python -m pip install -e .`
  - Expected: install succeeds
  - Actual: install succeeds

- `python -m pip install pytest`
  - Expected: pytest available for README flow
  - Actual: succeeds

- `python -m ds2.cli scan examples/fastapi_app --out artifacts/demo`
  - Expected from README:
    - `DS2 report generated: .../artifacts/demo/DS2_REPORT.md`
    - `DS2 receipt generated: .../artifacts/demo/ds2_receipt.json`
  - Actual:
    - `DS2 report generated: C:/Users/Brandon Caylor/Documents/New project/ds2-clean-root/artifacts/demo/DS2_REPORT.md`
    - `DS2 receipt generated: C:/Users/Brandon Caylor/Documents/New project/ds2-clean-root/artifacts/demo/ds2_receipt.json`

- `python -m pytest`
  - Expected: tests pass
  - Actual: `13 passed`

## Purpose Comprehension Within 60 Seconds

`YES`

After about a minute, DS2 reads as:

- a Python-focused static review tool
- not a CVE scanner
- not an SBOM generator
- a way to map declared dependencies, observed imports, and likely runtime exposure/authority surface

That is enough to form a credible first mental model quickly.

## Whether The Screenshots Improve Understanding

`YES`

Why:

- they make the project feel more concrete
- they show that the demo/viewer is static and artifact-driven
- they visually reinforce the dependency/exposure summary and receipt evidence

Limit:

- screenshots are supportive, not primary evidence
- the markdown report and receipt are still the core reviewer artifacts

## Whether The Demo Artifacts Support The README Claims

`YES`

Evidence:

- `artifacts/demo/DS2_REPORT.md` matches the README’s claim of a deterministic, readable report
- `artifacts/demo/ds2_receipt.json` gives concrete hashes and generated-file metadata
- `artifacts/demo/ds2_graph.json` provides machine-readable structure
- `examples/fastapi_app/` matches the demo output story and supports reproducibility claims

## Whether A Reviewer Could Explain DS2 After 5 Minutes

`YES`

A plausible explanation after 5 minutes:

> DS2 is a static Python dependency review tool. It reads manifest files and source imports, classifies likely runtime exposure such as server, client, database, or async behavior, and emits deterministic report/graph/receipt artifacts so a reviewer can reason about inherited execution surface before running code.

## Commands Run

```text
python -m pip install -e .
python -m pip install pytest
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
python -m pytest
python -m http.server 8765
```

## Files Changed

- `README.md`
- `REVIEWER_QUICKSTART.md`
- `REVIEWER_EXPERIENCE_REPORT.md`

## Patch Scope Confirmation

- Only documentation issues were patched.
- No scanner functionality was expanded.
- No scanner behavior was changed.
