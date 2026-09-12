# Turkish Native

**Write Turkish as Turkish, not translated English.**

[Türkçe README](README.tr.md) · [Skill](SKILL.md) · [Examples](examples/before-after.md) · [Contributing](CONTRIBUTING.md) · [Roadmap](ROADMAP.md)

Turkish Native is an open-source agent skill for writing and editing natural Turkish. It targets a specific failure mode in AI-generated and localized copy: Turkish that is grammatically understandable but still carries foreign sentence structure, unnatural collocations, literal SaaS or sales calques, internal product jargon, or model-written marketing formulas.

A sentence can be grammatically correct and still sound translated.

## Why this exists

Spell checkers and grammar tools catch mechanical errors. Turkish Native works one layer above them: **native construction**. It asks an agent to rebuild the sentence from meaning instead of preserving the source-language skeleton.

That means checking syntax before vocabulary: subordinate clauses, nominalization, word order, case suffixes, possessives, verb–noun pairings, product language, register, and factual fidelity.

## Examples

| Artificial / translated | Natural Turkish |
|---|---|
| `Kim açtı, kim düzenledi gör.` | `Kimin açtığını, kimin düzenlediğini gör.` |
| `Sayfayı WhatsApp'ta gönder.` | `Sayfayı WhatsApp'tan gönder.` |
| `16 işletme bulundu, 12'si telefonlu.` | `16 işletme bulundu, 12 telefon numarası bulundu.` |
| `Aynı işletme için tekrar kayıt oluşturulmaz.` | `Aynı işletme ikinci kez eklenmez.` |
| `Kart istemiyoruz.` | `Kredi kartı gerekmez.` |

The skill also protects against overcorrection. Natural phrases such as `Sen satışa bak.`, `Bulamazsa uydurmaz.`, `Site kurmak`, or `Linki gönder.` should stay natural when the context supports them.

## Scope

Use Turkish Native for marketing, product/UI copy, SaaS, localization, documentation, support, legal/privacy/security prose, institutional communication, and reviews of AI-written Turkish.

It is not a spell checker, AI detector, loanword ban list, or replacement for professional legal review. It does not claim that Turkish has only one correct phrasing.

## Installation

### Skills CLI

```bash
npx skills add oguzhankayan/turkish-native --global
```

### Claude Code plugin

```text
/plugin marketplace add oguzhankayan/turkish-native
/plugin install turkish-native@turkish-native
```

### Manual

Copy `SKILL.md` and the bundled `references/` directory into the skill directory used by your agent.

## Usage

```text
Use $turkish-native to review this Turkish copy.
Flag translationese and unnatural collocations, then rewrite it naturally.
```

```text
Translate this into native Turkish with $turkish-native.
Preserve facts and product terminology, but do not preserve English sentence structure.
```

```text
Use $turkish-native to rewrite the prose in src/content/tr/home.ts.
Keep keys, variables, URLs, code, and route names unchanged.
```

## How it works

Turkish Native uses a meaning-first workflow: identify the audience and register, separate facts from wording, fix structural problems before isolated vocabulary, rebuild foreign sentence architecture, then check native flow, factual fidelity, and over-editing.

The taxonomy contains **48 patterns** in five groups:

- 1–10: sentence architecture,
- 11–20: verb choice and lexical fit,
- 21–30: product, UI, and localization,
- 31–40: marketing and model-written copy,
- 41–48: register, fidelity, and final checks.

Detailed rules, examples, and false-positive guards live in [`references/`](references/). The compact runtime instructions live in [`SKILL.md`](SKILL.md).

## Evaluation

The repository ships with **72 regression cases** across [`evals/cases/`](evals/cases/), including positive controls that should remain unchanged. Every numbered pattern has evaluation coverage.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-package.py
```

The validator checks package structure, continuous pattern numbering, version consistency, unique case IDs, positive-control count, and per-pattern eval coverage. For benchmark methodology, see [`docs/BENCHMARKING.md`](docs/BENCHMARKING.md).

## Project status

Current release: **v0.3.0, pre-1.0**. Pattern names and the evaluation schema may still change before 1.0.

See [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md) and [`ROADMAP.md`](ROADMAP.md) for design rationale and next steps.

## Relationship to Humanizer

[blader/humanizer](https://github.com/blader/humanizer) is a general-purpose skill for broad AI-writing patterns. Turkish Native solves a narrower Turkish-specific problem: translationese and non-native construction.

Turkish Native is not a fork and does not reuse Humanizer's pattern taxonomy. Humanizer inspired the packaging approach.

## Contributing

Contributions are welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a PR.

## License

MIT © 2026 Oğuzhan Kayan. See [`LICENSE`](LICENSE).
