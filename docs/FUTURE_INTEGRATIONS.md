# Future Integrations

This file documents likely integration directions for DS2 beyond `v0.1.0`. These are intentionally future work, not current capabilities.

## CycloneDX And SPDX Export

Future work may include exporting DS2 observations into CycloneDX or SPDX-adjacent formats so dependency exposure findings can travel alongside traditional component inventories.

## in-toto And SLSA-Style Attestations

Future work may include compatibility with in-toto or SLSA-style attestation workflows, where DS2 receipts or summary claims can be attached to broader provenance and build-integrity pipelines.

## CI Gate Usage

Future work may include CI usage patterns where DS2 acts as a pre-merge or pre-release review gate for newly introduced dependency authority surface.

## Graph Visualization

Future work may include simple graph visualization so reviewers can inspect direct dependencies, observed imports, and best-effort edges visually without changing the underlying scan model.

## Large-Repo Performance And Caching

Future work may include caching and incremental scan strategies for larger repositories where repeated full-tree parsing would otherwise dominate review time.
