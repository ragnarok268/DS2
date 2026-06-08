# Limitations

Applies to release target: `v0.1.0`.

DS2 is intentionally honest about what static analysis can and cannot prove.

## What DS2 Can Say Reliably

- Which dependencies were declared in `requirements.txt` and `pyproject.toml`.
- Which top-level imports were observed in Python source files.
- Which common packages likely expand runtime authority into server, client, process, browser, database, cache, parser, plugin, or cloud surfaces.
- Which best-effort `Requires-Dist` edges were available from installed metadata.
- Whether repeated scans over unchanged inputs produce identical artifacts.

## What DS2 Cannot Prove

- That an imported package is reachable in production execution.
- That a declared dependency is actually used at runtime.
- That dynamic imports, plugin loading, or string-built imports were fully captured.
- That subprocess, network, database, browser, or cloud behavior will occur, only that the dependency surface suggests those authorities exist.
- That transitive dependency coverage is complete when installed metadata is unavailable or partial.
- That package-name heuristics always match real execution behavior.

## Static Analysis Boundaries

- Import scanning is based on Python `ast` and records top-level imports in `.py` files.
- Non-Python entrypoints, shell scripts, container files, CI workflows, and runtime configuration are out of scope for v1.
- Environment markers, optional extras, and conditional imports may shift real runtime surface beyond what the report shows.
- Vendored code, namespace packages, and local module shadowing can make import/package attribution imperfect.

## Reviewer Guidance

Treat DS2 as a dependency authority and exposure mapper, not as a verdict engine. It is best used to narrow review effort, document inherited authority, and create a reproducible baseline before deeper manual or dynamic investigation.
