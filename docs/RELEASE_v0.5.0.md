# Turkish Native v0.5.0

v0.5.0 is the first tagged release after v0.3.0. It includes the production work that landed on `main` as v0.4.0 plus a new **domain and page integrity** layer.

## Highlights

- 57 Turkish-specific patterns, up from 48 in v0.3.0.
- 105 regression cases, up from 72.
- Set-level tests for heading monotony and duplicate meaning.
- New page-integrity patterns for cross-sector template residue, domain-native fields and actions, unsupported operational promises, high-stakes claims, provenance/source labels, and process-section theater.
- Positive controls that preserve context-sensitive language when it is actually correct.
- A privacy regression case for unsupported absolute data-handling claims.

## Why this release exists

Recent production reviews surfaced several examples that were grammatically fine but contextually wrong: a florist CTA asked users to book an appointment, an auto-service form asked users to choose a vehicle segment, a restaurant used inventory language such as `stok`, a generated dental demo made unsupported outcome claims, synthetic placeholder reviews were presented as Google reviews, and obvious UI actions were expanded into artificial multi-step processes.

Turkish Native now treats **sector, task, provenance, and factual scope** as part of writing quality rather than as separate cleanup work.

## Installation

```bash
npx skills add oguzhankayan/turkish-native --global
```

The core principle has not changed: work from meaning and context, preserve supported facts, and do not replace one template-shaped failure with another.
