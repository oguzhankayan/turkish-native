# Roadmap

Turkish Native is pre-1.0. The rule set is usable today, but the evaluation corpus and benchmarking methodology will continue to evolve.

## Current baseline: v0.5

- 57 patterns covering sentence architecture, lexical fit, product/UI copy, model-written marketing, register/fidelity, and domain/page integrity.
- 105 regression cases with full pattern coverage and positive controls.
- Set-level cases for failures that only appear across a page, such as repetitive sentence shapes, duplicate meaning, wrong-sector template residue, false provenance, and process filler.

## v0.6

- Expand the regression corpus with independent examples outside the initial Klevia production set.
- Add a reproducible benchmark runner for comparing the same model with and without the skill.
- Publish a native-reader review rubric and anonymized score sheet.
- Add tagged eval subsets for product, legal, technical, institutional, local-business, and high-stakes copy.
- Measure unsupported-claim rate and provenance errors separately from style quality.

## v0.7

- Test the skill across multiple agent runtimes and model families.
- Measure positive-control preservation and over-edit rates.
- Document recurring disagreements and accepted variants rather than forcing one canonical rewrite.
- Add more full-page and multi-slot evaluations, not just isolated sentences.

## Toward 1.0

A 1.0 release should require:

- a stable pattern taxonomy,
- broad native-reader review,
- reproducible benchmarks,
- strong positive-control performance,
- strong factual-fidelity and source-label performance,
- installation tested on supported skill loaders,
- no known packaging or licensing issues.

The project will not chase a fixed number of patterns. New rules should be added only when they describe a recurring failure that is not already covered by an existing rule.
