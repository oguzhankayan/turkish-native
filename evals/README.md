# Evaluation set

`cases/*.yaml` is a regression corpus for Turkish Native.

It is intentionally not limited to exact-string rewrites. Natural Turkish can have multiple valid formulations, so cases may specify behavioral properties instead.

## Fields

- `id`: stable unique case ID
- `pattern`: pattern number in `SKILL.md`
- `input`: source text
- `instruction`: optional context needed to disambiguate the task
- `expected`: exact expected output when deterministic
- `expected_contains`: strings that must survive / appear
- `expected_not_contains`: known calques or failures that must disappear
- `expected_max_sentences`: structural constraint
- `expected_property`: qualitative requirement that needs model or human judgment

## Positive controls

A positive control is already-natural Turkish that should remain unchanged. These cases are critical because a language skill can fail by over-editing just as easily as by missing translationese.

## Benchmarking

For model comparisons, run the same case set with and without the skill. Score at least:

1. factual fidelity,
2. native-reader preference,
3. pattern resolution,
4. register fit,
5. positive-control preservation.

Do not treat exact string equality as the only metric for open-ended cases.
