# Turkish Native patterns — E. Register, fidelity, and final checks

### 41. Match the register instead of flattening the voice

Marketing, support, legal, technical, municipal, and conversational Turkish need different levels of formality.

Do not rewrite `Sen satışa bak.` as `Satış faaliyetlerinize odaklanabilirsiniz.` unless the requested register requires it.

### 42. Legal and policy prose: precision before casualness

Legal text should be readable, but do not simplify away conditions, scope, exceptions, defined terms, or responsibility.

**Bad rewrite:** turning `Tüketici sıfatıyla hareket eden kullanıcılar bakımından...` into `Tüketiciler için...` when the qualification matters.

Avoid decorative brand language inside legal obligations.

### 43. Security and privacy prose: avoid unsupported absolutes

**Bad:** `Hiçbir bilgi açıkta kalmaz.`

**Better:** `Tarayıcı ile hizmet arasındaki bağlantı TLS ile şifrelenir.` when that is the supported fact.

Do not invent security controls. Prefer a verifiable control over a reassuring slogan.

### 44. Technical prose: preserve identifiers and exact behavior

Keep API routes, commands, package names, identifiers, schema fields, code, and exact technical terms unchanged unless the task explicitly asks to rename them.

**Keep:** `npm install -g klevia-mcp`

Do not “naturalize” code.

### 45. Factual fidelity before fluency

A smoother sentence is still wrong if it invents a feature, metric, legal claim, source, or guarantee.

If a natural rewrite needs a fact you do not have, ask for it or write a narrower sentence.

### 46. Do not overcorrect natural Turkish

A phrase that appears on a watch list can still be right.

**Keep when natural:**

- `Sen satışa bak.`
- `Bulamazsa uydurmaz.`
- `Site kurmak`
- `Linki gönder.`
- `API üzerinden bağlanır.`

The skill should reduce translationese, not erase the writer's voice.

### 47. Morphology, agreement, apostrophes, dates, and decimals

After structural editing, check ordinary Turkish mechanics:

- person and tense agreement
- case and possessive suffixes
- numeral/plural agreement
- decimal commas in ordinary Turkish text
- apostrophes on proper names and brand names according to Turkish usage
- date and time formatting appropriate to the context

**Bad:** `Sen sayfayı gönderir, satışı tamamlarsın.`

**Better:** `Sen sayfayı gönderirsin, satışı tamamlarsın.`

Do not alter machine-readable formats, code, or API payloads.

### 48. Native-read and source-free reconstruction test

Before finalizing, perform two checks:

1. **Native-read test:** Does this sound like something a careful Turkish writer would actually write for this audience?
2. **Source-free test:** If the source-language sentence disappeared and only the intended meaning remained, would you independently build the same Turkish sentence?

If either answer is no, rebuild the sentence.
