"""Development shim so `python -m ds2.cli` works from the repo root."""

from __future__ import annotations

from pathlib import Path

__version__ = "0.1.0"
__path__ = [str(Path(__file__).resolve().parent.parent / "src" / "ds2")]
