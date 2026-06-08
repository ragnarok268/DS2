# Contributing

Thanks for helping build DS2.

## Development

Use Python 3.11 or newer.

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -e .
python -m pip install pytest
python -m pytest
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install pytest
python -m pytest
```

## Principles

- Keep scans deterministic.
- Do not add network calls.
- Do not install packages during scans.
- Treat malformed input as a warning, not a crash.
- Prefer standard-library implementations first.

## Pull Requests

- Add tests for new collectors or exposure rules.
- Keep output ordering stable.
- Update docs when exposure classes or receipt fields change.
