# Roadmap

Turkish Native is pre-1.0. The rule set is usable today, but the evaluation corpus and benchmarking methodology will continue to evolve.

## v0.4

- Expand the regression corpus beyond 100 cases.
- Add more localization-specific cases from UI, support, and documentation.
- Add independent examples that did not originate from the initial product-copy review set.
- Add a reproducible benchmark runner for comparing the same model with and without the skill.
- Publish a native-reader review rubric and anonymized score sheet.

## v0.5

- Test the skill across multiple agent runtimes and model families.
- Measure positive-control preservation and over-edit rates.
- Add domain packs or tagged eval subsets for product, legal, technical, institutional, and marketing Turkish.
- Document recurring disagreements and accepted variants rather than forcing one canonical rewrite.

## Toward 1.0

A 1.0 release should require:

- a stable pattern taxonomy,
- broad native-reader review,
- reproducible benchmarks,
- strong positive-control performance,
- installation tested on supported skill loaders,
- no known packaging or licensing issues.

The project will not chase a fixed number of patterns. New rules should be added only when they describe a recurring failure that is not already covered by an existing rule.
