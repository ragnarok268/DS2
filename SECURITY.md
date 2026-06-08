# Security Policy

## Scope

DS2 is a static-analysis tool. It does not execute target code, does not perform dynamic exploit validation, and does not claim to prove runtime reachability or vulnerability presence.

## Reporting Issues

If you find a security issue in DS2 itself, please report it privately to the project maintainer before public disclosure. Include:

- affected version, such as `v0.1.0`
- operating system and Python version
- reproduction steps
- expected behavior
- actual behavior
- whether the issue affects scan integrity, output correctness, or local safety

## Good-Faith Expectations

- Do not treat DS2 output as a vulnerability verdict.
- Do not rely on DS2 alone for exploitability or production-runtime claims.
- Prefer coordinated disclosure for issues that could mislead users about local safety, artifact integrity, or deterministic reporting.
