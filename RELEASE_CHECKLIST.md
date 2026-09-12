# Release checklist

## Repository settings

Suggested GitHub description:

> Agent skill for writing native Turkish and removing translationese from AI and localized copy.

Suggested topics:

`turkish`, `agent-skill`, `localization`, `translation`, `translationese`, `writing`, `copywriting`, `llm`, `claude`, `codex`, `chatgpt`

## Before making the repository public

- [ ] Run `python scripts/validate-package.py`
- [ ] Confirm the repository is on `main`
- [ ] Confirm MIT license is detected by GitHub
- [ ] Confirm README links work
- [ ] Confirm issue templates render correctly
- [ ] Confirm the validation workflow passes
- [ ] Confirm no private/customer text exists in examples or git history
- [ ] Confirm author email shown publicly is intentional
- [ ] Set repository description and topics
- [ ] Enable Issues
- [ ] Optionally enable Discussions

## v0.3.0 release

Suggested title:

> Turkish Native v0.3.0 — OSS preview

Suggested release notes:

> First public-ready preview of Turkish Native, an agent skill for writing Turkish from meaning instead of translated-English sentence structure.
>
> Highlights:
> - 48 Turkish-specific writing and localization patterns
> - 72 regression cases with full pattern coverage
> - positive controls to prevent overcorrection
> - English and Turkish documentation
> - Claude plugin and OpenAI-compatible agent metadata
> - package validation and GitHub Actions CI
> - contribution, security, conduct, and issue templates
>
> The project is pre-1.0. Pattern names, evaluation schema, and packaging may still change as the corpus grows.

## After publishing

- [ ] Tag `v0.3.0`
- [ ] Create a GitHub release from the tag
- [ ] Test `npx skills add oguzhankayan/turkish-native --global`
- [ ] Test Claude plugin installation
- [ ] Open one tracking issue for benchmark automation
- [ ] Collect native-reader feedback before v0.4.0
