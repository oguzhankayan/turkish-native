# Design philosophy

Turkish Native is built around one claim: **grammatical Turkish is not automatically native Turkish**.

## Meaning before source shape

Translationese often survives because the editor preserves the source sentence and replaces its words one by one. Turkish Native does the opposite: it separates meaning from wording, then rebuilds the sentence in Turkish.

This is why syntax comes before vocabulary. A sentence with ordinary Turkish words can still feel foreign if its subordinate clauses, word order, case relations, or verb-noun pairings come from English.

## Patterns, not bans

The project avoids blanket rules such as "never use `sunmak`" or "always replace `link` with `bağlantı`". Those rules create a different kind of bad Turkish.

Each pattern should have a false-positive guard. If a flagged form can be natural in the right context, the skill must say so.

## Restraint is a feature

Overcorrection is a regression. The evaluation set therefore includes positive controls such as:

- `Sen satışa bak.`
- `Bulamazsa uydurmaz.`
- `Linki müşteriye gönder.`
- `API üzerinden bağlanır.`

A good language skill must know when not to edit.

## Register matters

There is no single correct level of Turkish. Product copy, legal text, technical documentation, support messages, institutional communication, and conversation need different registers.

The skill should preserve the intended register while removing structures that sound translated or mechanically generated.

## Fidelity beats fluency

A fluent rewrite that invents a feature, legal rule, security control, metric, source, or guarantee is worse than an awkward but accurate sentence.

When natural Turkish requires information the source does not provide, the agent should ask for it or write a narrower sentence.

## Why evaluation is property-based

Many Turkish sentences have more than one natural rewrite. Exact-string tests work for deterministic grammar fixes, but open-ended cases need properties: a calque must disappear, a technical identifier must stay, a factual claim must not be added, or a natural sentence must remain unchanged.

The benchmark should measure native-reader preference and fidelity, not only string equality.
