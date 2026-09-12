# Turkish Native v0.3.0 — OSS preview

First public-ready preview of Turkish Native, an agent skill for writing Turkish from meaning instead of translated-English sentence structure.

## Highlights

- 48 Turkish-specific writing and localization patterns.
- 72 regression cases with full pattern coverage.
- Positive controls to prevent overcorrection of already-natural Turkish.
- English and Turkish documentation.
- Claude plugin packaging and OpenAI-compatible agent metadata.
- Package validation and GitHub Actions CI.
- Contribution guide, security policy, code of conduct, issue templates, and pull request template.

## What the skill targets

Turkish Native focuses on Turkish that is grammatically understandable but still sounds translated: imported clause structures, nominalization chains, wrong case or direction choices, unnatural verb–noun pairings, literal SaaS and sales calques, internal product jargon, forced slogans, repetitive model-written copy, and register mismatches.

It is deliberately conservative. Natural Turkish should stay natural, and supported facts, numbers, names, citations, product terminology, code, keys, URLs, and identifiers should not be invented or silently changed.

## Status

This is a pre-1.0 release. Pattern names, evaluation schema, packaging, and benchmark methodology may still change as the corpus grows and more native-reader feedback is collected.

## Installation

```bash
npx skills add oguzhankayan/turkish-native --global
```

Claude Code users can also install it as a plugin through the repository marketplace manifest.

## Feedback

Bug reports, pattern proposals, positive controls, cross-agent compatibility fixes, and benchmark contributions are welcome through GitHub Issues and pull requests.
