# Turkish Native patterns — C. Product, UI, and localization

### 21. Internal product jargon leaking into user copy

**Watch for:** `run`, `orchestrator`, `candidate`, `pipeline`, internal status names, service names, table names.

**Bad:** `Orchestrator adayları pipeline'a taşır.`

**Better:** `Klevia uygun işletmeleri seçip listeye ekler.`

Keep internal terminology in developer documentation where it is actually the subject.

### 22. Database language in customer-facing text

**Bad:** `Aynı işletme için tekrar kayıt oluşturulmaz.`

**Better:** `Aynı işletme ikinci kez eklenmez.`

**Bad:** `Kayıt silindi.` for a customer account.

**Better:** `Hesap silindi.`

Name the user's object, not the database representation.

### 23. Literal SaaS calques

**Watch for:** `kart istemiyoruz`, `planı yükselt`, `kota tüketmek`, `workspace`, `seat`, `usage` translated mechanically.

**Bad:** `Kart istemiyoruz.`

**Better:** `Kredi kartı gerekmez.`

`Planını yükselt` can be natural in some products. Judge the product voice, not the English source alone.

### 24. Literal sales and growth calques

**Watch for:** `satışı kapat`, `aksiyon al`, `satışa çevir`, `lead'i nurture et`, `funnel'ın altına taşı` in general customer copy.

**Bad:** `Bildirim gelince aksiyon al.`

**Better:** Name the action: `Bildirim gelince müşteriye yaz.` when supported by context.

Do not replace specialist sales terminology if the intended audience genuinely uses it.

### 25. Microcopy that sounds like documentation

Buttons, notices, and status messages should usually say the action or state directly.

**Bad:** `İşlem başarıyla gerçekleştirilmiştir.`

**Better:** `Kaydedildi.`

**Bad:** `İlgili kayıt için düzenleme işlemi gerçekleştirilebilir.`

**Better:** `Düzenleyebilirsin.`

### 26. Noun-only labels where the user needs an action or result

**Bad:** `Telefon doğrulama` as a button that starts verification.

**Better:** `Telefonu doğrula.`

A noun label is fine for a navigation section or feature name. Match the UI role.

### 27. UI copy that narrates implementation

**Bad:** `Bu butona basıldığında sistem yeni bir kayıt oluşturur.`

**Better:** `Yeni işletme ekle.` or `İşletme eklendi.` depending on whether this is a button or a status.

Describe the user's action or result unless implementation details are relevant.

### 28. English-style labels, capitalization, and colon patterns

Avoid title-casing every Turkish heading and writing every bullet as `Label: explanation` when natural prose or sentence case is clearer.

**Bad:** `Hızlı Kurulum`, `Kolay Yönetim`, `Güvenli Veri` used mechanically as title-case feature labels.

**Better:** `Hızlı kurulum`, `Kolay yönetim`, `Veri güvenliği` when they are ordinary Turkish headings.

Brand style can override sentence case when deliberate and consistent.

### 29. Counts, plurals, units, and Turkish number formatting

Use Turkish conventions in ordinary prose and UI unless the field is machine-readable.

**Bad:** `12 yorum, 4.8 puan`

**Better:** `12 yorum, 4,8 puan`

Avoid unnecessary plural suffixes after numerals: `3 kullanıcı`, not `3 kullanıcılar`.

### 30. Overlocalizing natural technical loanwords

Do not replace a familiar technical term with a formal or obscure Turkish equivalent merely to make the text “more Turkish”.

**Natural:** `Linki müşteriye gönder.`

**Potentially worse in this product voice:** `Bağlantıyı müşteriye ilet.`

Choose terminology from the audience and existing product voice.
