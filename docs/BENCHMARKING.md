# Benchmarking Turkish Native

The regression file in `evals/cases/` is a behavior specification, not a complete automated benchmark.

## Recommended comparison

Run each case twice with the same model and settings:

1. without Turkish Native,
2. with Turkish Native.

Then compare the outputs blind.

## Suggested dimensions

Score each output from 1 to 5 for:

- **Fidelity:** Does it preserve the source meaning and factual scope?
- **Native Turkish:** Would a careful native writer plausibly phrase it this way?
- **Pattern resolution:** Did it fix the targeted failure?
- **Register:** Does it fit the medium and audience?
- **Restraint:** Did it avoid unnecessary edits and preserve positive controls?

## Native-reader review

For serious benchmarking, use at least two native Turkish reviewers and hide which output used the skill. Record disagreements rather than forcing consensus.

## Exact vs. open-ended cases

Use exact matching only for deterministic cases such as person agreement, number formatting, or identifier preservation. For copywriting and structural rewrites, evaluate properties and human preference.

## Reporting results

A useful report includes:

- model and version,
- date,
- runtime / agent,
- prompt used to invoke the skill,
- temperature or equivalent sampling settings when available,
- total cases,
- positive-control preservation rate,
- per-pattern failures,
- native-reader preference rate.
