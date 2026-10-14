# Held-out benchmark corpus

`cases.yaml` is the v0.4 benchmark corpus requested in issue #1. It is
deliberately separate from `evals/cases/`, which is the package's regression
and behavior-specification set. The benchmark cases are not intended to be
loaded as runtime examples or copied into training prompts.

## Case schema

Each case contains:

- `id`: stable identifier for result tables
- `pattern` and `group`: the primary taxonomy area under test
- `input`: the text shown to the compared systems
- `instruction`: the same task context given to both systems
- `case_type`: whether the case is a `correction`, `adaptation`, or
  `preservation` task
- `positive_control`: whether the text is expected to remain unchanged
- `dimensions`: case-specific notes for fidelity, native Turkish, pattern
  resolution, register, and restraint
- `exact_invariants`: facts, identifiers, or entities that must survive

The corpus intentionally does not include a target rewrite. For open-ended
Turkish, a single reference string would turn a reader-preference study into
an exact-match test.

## Case types and scoring

- A **correction** case starts with a targeted pattern problem. Pattern
  resolution measures whether the output fixes that problem without changing
  the facts.
- An **adaptation** case starts with valid source text and asks for a change of
  audience, medium, or register. Pattern resolution measures whether the
  requested adaptation is completed without inventing a correction.
- A **preservation** case is a positive control. The expected result is the
  unchanged input unless a concrete problem is found; it is counted in
  preservation/over-editing results, not as a successful correction.

`positive_control` must be `true` only for preservation cases. This keeps
pattern-resolution results separate from the cost of unnecessary edits.

## Reproducible protocol

1. Freeze the corpus revision, model versions, prompts, temperature, and date.
2. Run every case with the skill disabled and enabled using identical settings.
3. Randomize the A/B labels before showing outputs to native Turkish readers.
4. Have at least two independent readers score fidelity, native Turkish,
   pattern resolution, register, and restraint from 1 to 5. Record ties and
   disagreements instead of forcing a consensus.
5. Report aggregate scores, native-reader preference, correction and adaptation
   results separately, positive-control preservation, exact-invariant failures,
   and per-pattern failures.

Do not mix these cases with `evals/cases/` when measuring a model. Keeping the
benchmark held out makes cross-model comparisons less vulnerable to regression
examples that were already visible during development.
