# Interview Notes

## Static Versus Dynamic Tradeoff

DS2 intentionally chooses static analysis for low-friction, pre-execution review. That keeps it safe, deterministic, and easy to run in early governance workflows, but it also means DS2 does not claim runtime reachability or exploitability.

## Why Deterministic Outputs Matter

Deterministic outputs make the artifact reviewable. If the same repo and inputs produce different reports, receipts, or hashes across repeated runs, trust in the tool collapses quickly. Stable output is part of the product, not just an implementation detail.

## Why Authority Classification Is Intentionally Bounded

Authority classification is deliberately heuristic and narrow. The goal is to surface likely runtime-expanding packages and route reviewer attention, not to invent a false precision layer that claims full behavioral certainty from static imports alone.

## Known Edge Cases

- Dynamic imports may evade top-level AST import scanning.
- Namespace packages can make import-to-distribution mapping ambiguous.
- Editable installs can distort installed-metadata expectations versus declared dependencies.
- Build backends and build-system hooks can introduce behavior outside the v1 source-import model.
