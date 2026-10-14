# Benchmarking Turkish Native

The regression files in `evals/cases/` are a behavior specification, not a
complete automated benchmark. Use the held-out `evals/benchmark/cases.yaml`
corpus for the v0.4 cross-model comparison described in issue #1. It is kept
separate so examples used to develop the skill are not also presented as a
benchmark claim.

The benchmark schema keeps the input and task instruction visible, but stores
case-specific scoring notes instead of a single target rewrite. This preserves
room for more than one natural Turkish formulation while making factual drift
and over-editing reviewable.

## Recommended comparison

Run each benchmark case twice with the same model and settings:

1. without Turkish Native,
2. with Turkish Native.

Then randomize the A/B labels and compare the outputs blind. Keep the corpus
revision, prompt, model, date, runtime, and sampling settings with the result.

## Suggested dimensions

Score each output from 1 to 5 for:

- **Fidelity:** Does it preserve the source meaning and factual scope?
- **Native Turkish:** Would a careful native writer plausibly phrase it this way?
- **Pattern resolution:** Did it fix the targeted failure?
- **Register:** Does it fit the medium and audience?
- **Restraint:** Did it avoid unnecessary edits and preserve positive controls?

Report correction cases, adaptation cases, and preservation cases separately.
For correction cases, pattern resolution asks whether the named problem was
fixed. For adaptation cases, it asks whether the requested audience, medium,
or register change was made without inventing a problem. Preservation cases
are positive controls: unchanged output is the expected result and should be
reported as an over-editing check, not as a correction success.

Also check every `exact_invariants` entry in the case. A fluent rewrite that
changes a date, identifier, entity, count, or domain fact is a fidelity failure.

## Native-reader review

For serious benchmarking, use at least two native Turkish reviewers and hide
which output used the skill. Record disagreements rather than forcing
consensus. Randomize case order as well as output labels when practical.

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
- correction, adaptation, and preservation results separately.

For the v0.4 corpus, also include the corpus commit, positive-control
preservation rate, exact-invariant failures, and any per-pattern or per-group
failure concentration.
