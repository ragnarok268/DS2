# DS2

[![CI](https://github.com/ragnarok268/DS2/actions/workflows/ci.yml/badge.svg)](https://github.com/ragnarok268/DS2/actions/workflows/ci.yml)

DS2 is `ps + netstat + tree for dependency/runtime authority`.

Current release candidate: `v0.1.0`.

In one command, it turns a Python repo into a deterministic map of declared dependencies, observed imports, runtime exposure classes, and inherited execution authority. The goal is not vulnerability hype or static-analysis theater. The goal is a reviewer-trustworthy artifact that shows what code you pulled in, what runtime surface it appears to open, and where human attention should go next.

For evaluators: DS2 is a deliberately scoped governance artifact for AI-assisted software workflows. It emphasizes reproducibility, honest boundaries, and low-friction local evaluation over feature sprawl.

## In plain English

DS2 shows what capabilities enter your software through its dependencies.

It helps reviewers see when a project depends on packages that may introduce network access, process execution, cloud access, browser automation, database access, or other operational capabilities.

DS2 does not decide that a dependency is malicious. It gives reviewers a deterministic map of the dependency surface so they know what deserves attention before running, deploying, or accepting generated code.

What DS2 shows you:

- Which dependencies were declared by the project.
- Which packages were observed in the source imports.
- Which kinds of operational capability those packages may introduce.
- Which parts of the dependency surface deserve closer review.

Why you would care:

- It helps you spot runtime-relevant dependencies before you execute or deploy a project.
- It gives you a reviewer-friendly summary instead of making you inspect every dependency by hand.
- It makes generated or fast-moving codebases easier to sanity-check.

### Example Meanings

| What DS2 sees | What it means in plain English |
|---|---|
| Network client dependency | This project may make outbound network calls. |
| Network server dependency | This project may expose a service or API. |
| Process execution capability | This project may launch local programs or shell commands. |
| Cloud/API dependency | This project may interact with external cloud services. |
| Browser automation dependency | This project may control a browser or automate web interactions. |

### What DS2 Does Not Do

- Does not replace SBOM tools.
- Does not scan for CVEs.
- Does not prove code is safe.
- Does not perform dynamic runtime monitoring.
- Does not implement SLSA or provenance systems.

## One-Minute Evaluator Flow

```bash
python -m pip install -e .
python -m pip install pytest
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
python -m pytest
```

Expected review path:

- Open `artifacts/demo/DS2_REPORT.md` first.
- Check `artifacts/demo/ds2_receipt.json` for stable hashes.
- Compare with `examples/fastapi_app/` for committed reference artifacts.

## What It Is

- A local CLI for understanding direct dependencies and observed runtime surface.
- A deterministic report generator for dependency topology and authority expansion.
- A lightweight review aid for server, client, process, browser, database, cache, and cloud-adjacent packages.

## What It Is Not

- Not a generic CVE scanner.
- Not a secret collector.
- Not a package installer or resolver.
- Not a complete SBOM system.
- Not a guarantee of runtime reachability.

## How DS2 Relates To SBOM, SLSA, And Provenance

DS2 is not an SBOM generator. It does not try to replace CycloneDX, SPDX, provenance attestations, or build-integrity frameworks.

Instead, DS2 complements SBOM and provenance work by mapping dependency exposure and inherited authority surfaces: what a repo appears to import, what runtime classes those imports imply, and where reviewer attention should go before execution.

Future compatibility is intended around CycloneDX/SPDX-style export and in-toto/SLSA-style workflows, but that integration is explicitly future work rather than part of `v0.1.0`.

## Reviewer Demo

```bash
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
```

```text
$ python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
DS2 report generated: .../artifacts/demo/DS2_REPORT.md
DS2 receipt generated: .../artifacts/demo/ds2_receipt.json
```

Outputs appear in:

- `artifacts/demo/DS2_REPORT.md`
- `artifacts/demo/ds2_graph.json`
- `artifacts/demo/ds2_receipt.json`

Static demo/report viewer:

- `docs/demo-viewer.html`
- Local preview:

```bash
python -m http.server 8765
```

Then open:

- `http://127.0.0.1:8765/docs/demo-viewer.html`

Screenshot previews:

![DS2 demo overview](docs/assets/ds2-demo-overview.png)
![DS2 report viewer](docs/assets/ds2-report-viewer.png)
![DS2 receipt evidence](docs/assets/ds2-receipt-evidence.png)

## Install And Dev

```bash
python -m pip install -e .
python -m pip install pytest
python -m ds2.cli version
python -m ds2.cli scan examples/fastapi_app --out artifacts/demo
python -m pytest
```

## CLI

```bash
ds2 --version
ds2 version
ds2 scan .
ds2 scan . --out .ds2 --json
ds2 explain fastapi
```

## Evaluator Tour

- Sample app: `examples/fastapi_app`
- Sample report: `examples/fastapi_app/DS2_REPORT.md`
- Sample graph: `examples/fastapi_app/ds2_graph.json`
- Sample receipt: `examples/fastapi_app/ds2_receipt.json`
- Reviewer flow: `artifacts/demo`
- Static demo/report viewer: `docs/demo-viewer.html`
- Artifact framing: `ARTIFACT_SUMMARY.md`
- Static-analysis boundaries: `LIMITATIONS.md`
- Future integration direction: `docs/FUTURE_INTEGRATIONS.md`
- Quick evaluator path: `REVIEWER_QUICKSTART.md`
- Release gate: `RELEASE_CHECKLIST.md`

## Philosophy

Dependencies do not just add code. They expand inherited execution authority. A package that opens sockets, starts subprocesses, drives browsers, touches persistent storage, or reaches cloud APIs changes the effective authority surface of the repo that imports it.

DS2 focuses on that question first: what execution authority is now inside the graph, how was it observed, and where should a reviewer pay attention.

## V1 Limitations

- See `LIMITATIONS.md`.

## V2 Direction

DS2 v2 is aimed at generation-aware dependency governance for coding agents: tracking how generated code expands dependency authority, comparing intended versus introduced surface, and enforcing review gates around inherited execution power.
