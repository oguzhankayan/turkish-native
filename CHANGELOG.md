# Changelog

All notable project changes are documented here.

The project is pre-1.0. Minor releases may still refine pattern names, evaluation schema, and packaging.

## Unreleased

- No unreleased changes yet.

## 0.4.0 - 2026-09-13

### Added

- Three patterns (49-51) drawn from a 93-page production run of the skill:
  collapsing every sentence into one shape, the same sentence living in two
  slots of a page, and section labels that repeat the navigation.
- Evaluation cases for the new patterns, including set-level cases: the input
  is several headings from one page, because shape monotony and self-repetition
  cannot be seen one sentence at a time.
- Regression cases for mistranslations caught in production: `kalıp oranı` for
  a pass rate (it reads as the FAILURE rate), `sır` glaze written as `sırrını`,
  a bicycle wheel described with the car word `rot`, `gezdir` for `gezdirir`,
  `palamuta kadar` closing a list, a literal "walk in", and a `sen` heading on
  a `siz` page.

### Changed

- `SKILL.md` non-negotiable checks now ask whether one repaired shape has been
  copied onto every sentence, and whether a line repeats what another line on
  the same page already said. Both are page-level questions; every check before
  them could be answered one sentence at a time.

## 0.3.0 - 2026-09-12

### Added

- Expanded the taxonomy from 20 to 48 Turkish-specific patterns.
- Added full English and Turkish READMEs.
- Added contributing, code-of-conduct, security, changelog, issue-template, and pull-request documentation.
- Added evaluation documentation and per-pattern coverage validation.
- Added more positive controls to protect natural Turkish from overcorrection.

### Changed

- Reorganized the skill into sentence architecture, lexical fit, product/UI, marketing, and fidelity sections.
- Strengthened guidance for localization, legal prose, security claims, technical identifiers, and factual fidelity.
- Clarified that word lists are diagnostic, not bans.

## 0.2.0 - 2026-09-12

- Expanded the regression set to 50 cases.
- Added positive controls.
- Strengthened translation/localization guidance.
- Tightened the distinction between structural errors and suspicious vocabulary.

## 0.1.0 - 2026-09-12

- Initial 20-pattern skill and cross-agent packaging.
