# Contributing to Turkish Native

Thanks for helping improve Turkish Native.

The project is intentionally conservative: a new rule should describe a recurring native-Turkish problem, not one contributor's preferred wording.

## Good contributions

Useful contributions include:

- a recurring translationese pattern,
- a better explanation or false-positive guard for an existing pattern,
- a minimal bad → better example,
- a regression case,
- a positive control showing text that should stay unchanged,
- documentation or packaging fixes,
- cross-agent compatibility improvements.

## Before proposing a new pattern

Ask:

1. Does this happen repeatedly, or is it a one-off awkward sentence?
2. Can a native Turkish reader identify the problem without seeing the source language?
3. Is the issue already covered by an existing pattern?
4. Can the rule be stated without banning a normal Turkish word?
5. Is there a clear false-positive case?
6. Can we write at least one regression test for it?

If the answer to #3 is yes, expand the existing pattern instead.

## Example quality

Prefer small examples where one distinction is obvious.

Good:

```text
Bad:    Kim açtı gör.
Better: Kimin açtığını gör.
```

Less useful:

```text
Bad:    [entire 300-word landing page]
Better: [completely rewritten page]
```

Long examples are welcome in issues when context is necessary, but the skill itself should teach reusable rules with compact examples.

## Evaluation cases

Behavior changes should include a case in `evals/cases/`.

Use exact `expected` only when the output is deterministic. Otherwise prefer properties:

- `expected_contains`
- `expected_not_contains`
- `expected_max_sentences`
- `expected_property`

Positive controls should use `expected` equal to `input` when natural Turkish must remain unchanged.

Every numbered pattern must have coverage.

## Pull requests

Before opening a PR:

```bash
python3 -m pip install pyyaml
python3 scripts/validate-package.py
```

Keep the PR focused. If you change behavior:

- update `SKILL.md`,
- update README pattern summaries if needed,
- add or update eval cases,
- add an entry under `Unreleased` in `CHANGELOG.md`.

## Language

Issues and pull requests may be written in Turkish or English. Turkish examples should preserve Turkish characters.

## Attribution and data

Do not submit private customer text, personal data, confidential documents, or copyrighted material that you do not have permission to share. Reduce examples to the smallest form needed to demonstrate the pattern.

## Code of Conduct

By participating, you agree to follow [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
