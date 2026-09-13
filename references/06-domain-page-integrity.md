# Turkish Native patterns — F. Domain and page integrity

### 52. Cross-sector template residue

A sentence can be grammatical and still belong to the wrong business. Reused templates often carry fields, CTAs, process steps, or labels from a neighboring sector.

**Bad, on an auto-repair page:** `Araç ihtiyacı: Şehir otomobili / Aile aracı / Performans odaklı araç.`

That belongs to vehicle selection or sales, not repair intake.

**Better:** `İşlem türü: Periyodik bakım / Arıza & motor / Fren & lastik / Kaporta & boya.`

**Bad, on a florist page:** `Buket & aranjman için randevu almak istiyorum.`

**Better:** `Buket veya aranjman siparişi vermek istiyorum.`

Perform a domain-consistency pass across the whole page. Ask whether each noun, field, button, and step belongs to the actual business and user task. Do not preserve a wrong template merely because the sentence itself is fluent.

A neighboring-sector term can be correct elsewhere: `Randevu alın` is natural on a dental clinic page.

### 53. Use the information and objects the real task needs

Generic forms and model-written flows often ask for abstract or adjacent information instead of what the business actually needs.

**Bad, for an auto service:** `Kullanım amacı ve öncelikler görüşmenin başlangıç noktasıdır.`

**Better:** `Marka, model, kilometre ve yaşadığınız sorunu paylaşın.` when those are the supported intake details.

**Bad, on a restaurant menu:** `Bu kartta fiyat ve stok bilgisi yoktur.`

`Stok` is inventory language. Diners usually need the current menu, price, availability, or what is being served that day.

**Better:** `Güncel menü ve fiyat bilgisi için işletmeyle iletişime geçin.`

Use domain-native objects and questions. Do not replace a vague field with invented details; use only information supported by the page or task.

### 54. Unsupported operational promises

Generated marketing copy often invents service levels because they sound helpful: response times, delivery windows, same-day service, immediate appointments, guaranteed availability, or fixed turnaround.

**Bad without a source:** `İstediğiniz saat ve adrese kısa sürede ulaştırırız.`

**Better:** `Teslimat koşulları ve uygun saatler için işletmeyle iletişime geçin.`

**Bad without a source:** `Mesajlarınıza çalışma saatleri içinde yanıt veriyoruz.`

**Better:** `WhatsApp'tan yazabilir veya telefonla arayabilirsiniz.`

**Bad without a source:** `Size uygun günü dakikalar içinde belirleriz.`

**Better:** `Uygun gün ve saat için klinikle iletişime geçin.`

If the business explicitly supplies a service promise, preserve its scope exactly. Do not weaken a verified fact merely because it is operational; do not invent one merely because the template has a slot for it.

### 55. High-stakes and regulated claims need narrower language

Health, finance, legal, safety, and other regulated or high-stakes sectors need extra restraint. Do not turn a service description into a promise of outcome, safety, permanence, speed, or suitability unless that claim is supported and appropriate.

**Bad, for a dental demo:** `Eksik dişler için kalıcı, doğal görünümlü implant çözümleri.`

**Better:** `Eksik dişlerin tedavisinde implant seçenekleri hakkında muayene sonrası bilgi alın.`

**Bad without support:** `Klinik ortamında güvenli, tek seansta fark edilen beyazlatma.`

**Better:** `Diş beyazlatma uygulamaları hakkında muayene sonrası bilgi alın.`

When the copy answers a medical question, prefer conditional language tied to examination, procedure, or individual circumstances rather than universal reassurance.

This rule is about factual scope, not making health copy cold. Plain, readable Turkish is still the goal.

### 56. Do not imply a source or provenance you do not have

Source labels are factual claims. Do not present synthetic, placeholder, rewritten, or generated material as if it came from Google, a customer, a review platform, a study, or another named source.

**Bad:** generated placeholder quotes under the heading `Google değerlendirmeleri`.

**Better:** label them `Örnek yorumlar`, make it clear that they are illustrative, or omit the section.

If genuine source text is supplied, preserve the quote. Do not rewrite a real review to make it more sector-specific or polished unless the task explicitly asks for an edited paraphrase rather than a quotation.

The same rule applies to ratings, dates, reviewer names, badges, statistics, certifications, and source attributions.

### 57. Do not manufacture a process section from obvious interactions

Templates often demand a `Nasıl ilerler?` section even when there is no meaningful process. Models then turn obvious navigation into a fake four-step journey.

**Bad, on a restaurant page:**

1. `Kategorilere bakın.`
2. `Telefonla sorun.`
3. `WhatsApp'tan yazın.`
4. `Konumu açın.`

These are interface actions, not a business process.

**Better:** remove the section, or condense it to the one useful instruction: `Menü, rezervasyon veya müsaitlik için işletmeyi arayabilir ya da WhatsApp'tan yazabilirsiniz.`

Keep a process section when it explains a real sequence that helps the user make a decision.

**Natural example, for auto repair:** `Randevu → araç kontrolü → yapılacak işlemlerin ve fiyatın paylaşılması → onay sonrası servis.`

Do not force three or four steps simply because the page template has numbered cards.
