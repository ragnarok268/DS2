# Changelog

## v0.1.0

Initial public release candidate for DS2.

### Highlights

- Python-focused dependency authority and runtime exposure mapping.
- Deterministic `scan` and `explain` CLI workflows.
- Support for `requirements.txt`, `pyproject.toml`, source import scanning, and installed-metadata fallback.
- Exposure classification for common server, client, process, browser, database, cache, queue, parser, plugin, and cloud-adjacent packages.
- Stable markdown, graph JSON, and receipt outputs.
- Committed example artifacts in `examples/fastapi_app`.
- Golden-output and determinism tests for reviewer trust and reproducibility.

### Non-Goals In v0.1.0

- No CVE scanning.
- No network access during scans.
- No package installation during scans.
- No dynamic runtime tracing.
- No lint or type-check gate in the default review flow.
