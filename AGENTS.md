# Guide for agents and maintainers

This repository contains a portable agent skill for native Turkish writing.

## Source of truth

`SKILL.md` is the behavioral source of truth. Keep it portable across agents and tools. `README.md` and `README.tr.md` explain the product; they must not silently redefine behavior.

## Rules for changes

- Keep the pattern count and names in `SKILL.md`, `README.md`, and `README.tr.md` in sync.
- Prefer expanding an existing pattern over adding a near-duplicate rule.
- Examples must show a recurring Turkish distinction, not a personal preference presented as grammar.
- Every strong rule needs a false-positive guard when natural Turkish can legitimately use the flagged form.
- Never turn suspicious-word lists into banned-word lists.
- Keep legal and technical guidance focused on language and fidelity; do not invent legal or technical claims.
- Add regression cases to `evals/cases/` for every behavior change.
- Every numbered pattern must have at least one evaluation case.
- Keep positive controls that should remain unchanged; overcorrection is a regression.
- Keep version numbers aligned in `SKILL.md`, `.claude-plugin/plugin.json`, and `CHANGELOG.md`.
- Run `python3 scripts/validate-package.py` before committing.

## Adding or changing a pattern

A new pattern should meet all of these conditions:

1. It recurs across more than one sentence, text, or domain.
2. It is not already implied by an existing pattern.
3. A native Turkish reader can recognize the failure without seeing the English source.
4. It can be explained as a structural or contextual rule, not only as a phrase replacement.
5. It has at least one bad/better example and a false-positive guard where appropriate.
6. It has at least one regression case.

## Evaluation guidance

Exact string equality is appropriate only when one form is clearly required, such as preserving an identifier or fixing a deterministic grammar error. For open-ended rewriting, test properties instead: required meaning, forbidden calque, preserved terminology, maximum sentence count, or unchanged positive control.

## Writing style

Use direct Turkish or plain English in repository documentation. Keep technical identifiers exact. Keep examples short enough that the linguistic difference is obvious.
