# Design philosophy

Turkish Native is built around one claim: **grammatical Turkish is not automatically native Turkish**.

A second claim follows from production use: **a natural sentence can still be wrong for the page it appears on**.

## Meaning before source shape

Translationese often survives because the editor preserves the source sentence and replaces its words one by one. Turkish Native does the opposite: it separates meaning from wording, then rebuilds the sentence in Turkish.

This is why syntax comes before vocabulary. A sentence with ordinary Turkish words can still feel foreign if its subordinate clauses, word order, case relations, or verb-noun pairings come from English.

## Context before template

Generated pages introduce another failure mode: a template slot is filled fluently even when the slot, CTA, field, or process belongs to another sector.

A florist does not normally ask a customer to book an appointment for a bouquet. An auto-repair intake does not need vehicle-sales categories. A restaurant should not inherit inventory vocabulary merely because a generic card schema has a `stock` field.

The skill therefore judges copy at three levels:

1. **sentence:** is the Turkish natural?
2. **page:** does this line add something and fit the surrounding sections?
3. **task/domain:** does this action, object, promise, or label belong to the actual business and user goal?

## Patterns, not bans

The project avoids blanket rules such as "never use `sunmak`" or "always replace `link` with `bağlantı`". Those rules create a different kind of bad Turkish.

Each pattern should have a false-positive guard. If a flagged form can be natural in the right context, the skill must say so. `Randevu alın` is wrong for a florist order CTA and completely normal for a clinic.

## Restraint is a feature

Overcorrection is a regression. The evaluation set therefore includes positive controls such as:

- `Sen satışa bak.`
- `Bulamazsa uydurmaz.`
- `Linki müşteriye gönder.`
- `API üzerinden bağlanır.`
- verified operational claims whose scope should not be weakened.

A good language skill must know when not to edit.

## Register matters

There is no single correct level of Turkish. Product copy, legal text, technical documentation, support messages, institutional communication, local-business pages, and conversation need different registers.

The skill should preserve the intended register while removing structures that sound translated or mechanically generated.

## Fidelity beats fluency

A fluent rewrite that invents a feature, legal rule, security control, medical outcome, service level, metric, source, or guarantee is worse than an awkward but accurate sentence.

Source labels are facts too. Synthetic reviews must not be presented as Google reviews; placeholder ratings must not be made to look verified; a real quotation must not be silently polished into a different quotation.

When natural Turkish requires information the source does not provide, the agent should ask for it or write a narrower sentence.

## Whole-page review matters

Some failures do not exist at sentence level. Four individually good headings can become a tic when all end in the same person marker. Two different sentences can repeat the same meaning. A numbered process can be pure filler even if every step is grammatical.

For page work, Turkish Native therefore reviews the set, not only each line in isolation.

## Why evaluation is property-based

Many Turkish sentences have more than one natural rewrite. Exact-string tests work for deterministic grammar fixes, but open-ended cases need properties: a calque must disappear, a technical identifier must stay, a factual claim must not be added, a sector action must fit its context, or a natural sentence must remain unchanged.

The benchmark should measure native-reader preference, fidelity, provenance, domain fit, and restraint, not only string equality.
