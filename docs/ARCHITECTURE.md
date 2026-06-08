# DS2 Architecture

DS2 is organized around a deterministic scan pipeline.

## Flow

1. Collect dependency declarations from `requirements.txt` and `pyproject.toml`.
2. Parse Python source with `ast` and collect observed imports.
3. Use installed distribution metadata as a fallback and best-effort transitive edge source.
4. Build a normalized graph of direct dependencies, observed imports, and `Requires-Dist` edges.
5. Classify exposure and authority state.
6. Emit stable JSON, markdown, and a receipt with content hashes.

## Modules

- `src/ds2/cli.py`: CLI entrypoints for `scan` and `explain`.
- `src/ds2/scan.py`: orchestration layer for the full scan.
- `src/ds2/collectors/`: manifest, import, and installed metadata collection.
- `src/ds2/graph/`: graph models, assembly, and explanation helpers.
- `src/ds2/classify/`: exposure and authority rules.
- `src/ds2/reports/`: deterministic markdown and JSON renderers.
- `src/ds2/receipts/`: stable receipt generation.
- `src/ds2/util/`: path and stable JSON helpers.

## Determinism Rules

- Stable sorting for dependencies, edges, imports, notes, and warnings.
- UTF-8 with LF line endings.
- No network calls.
- No installation during scans.
- Graceful degradation on malformed or missing input.
