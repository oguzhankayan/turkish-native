# Turkish Native

**Türkçeyi çevrilmiş İngilizce gibi değil, Türkçe gibi yaz.**

[![Paket doğrulama](https://github.com/oguzhankayan/turkish-native/actions/workflows/validate.yml/badge.svg)](https://github.com/oguzhankayan/turkish-native/actions/workflows/validate.yml) [![Sürüm](https://img.shields.io/github/v/release/oguzhankayan/turkish-native?display_name=tag)](https://github.com/oguzhankayan/turkish-native/releases/latest) [![Lisans: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[English README](README.md) · [Skill](SKILL.md) · [Örnekler](examples/before-after.md) · [Sürüm](https://github.com/oguzhankayan/turkish-native/releases/tag/v0.3.0) · [Katkı rehberi](CONTRIBUTING.md) · [Yol haritası](ROADMAP.md)

Turkish Native, doğal Türkçe yazmak ve mevcut metinleri düzenlemek için hazırlanmış açık kaynaklı bir agent skill'idir. Özellikle yapay zekâ ve lokalizasyon metinlerinde görülen bir soruna odaklanır: Dilbilgisi açısından anlaşılır olduğu hâlde cümle yapısı, fiil seçimi, ürün jargonu veya pazarlama kalıplarıyla hâlâ çevrilmiş İngilizce gibi duran Türkçe.

Bir cümle dilbilgisi açısından doğru olabilir ve yine de doğal Türkçe olmayabilir.

## Neden var?

Yazım ve dilbilgisi araçları mekanik hataları yakalar. Turkish Native başka bir katmana bakar: **cümlenin Türkçede doğal kurulup kurulmadığına**.

Agent'ın kaynak cümlenin iskeletini koruması yerine anlamdan hareket etmesini ister. Bu yüzden önce kelimelere değil yapıya bakar: yan cümleler, adlaştırma, sözcük dizimi, hâl ekleri, iyelik, fiil–isim birliktelikleri, ürün dili, ton ve bilgi sadakati.

## Örnekler

| Yapay / çeviri kokan | Doğal Türkçe |
|---|---|
| `Kim açtı, kim düzenledi gör.` | `Kimin açtığını, kimin düzenlediğini gör.` |
| `Sayfayı WhatsApp'ta gönder.` | `Sayfayı WhatsApp'tan gönder.` |
| `16 işletme bulundu, 12'si telefonlu.` | `16 işletme bulundu, 12 telefon numarası bulundu.` |
| `Aynı işletme için tekrar kayıt oluşturulmaz.` | `Aynı işletme ikinci kez eklenmez.` |
| `Kart istemiyoruz.` | `Kredi kartı gerekmez.` |

Skill ters hatayı da önlemeye çalışır. `Sen satışa bak.`, `Bulamazsa uydurmaz.`, `Site kurmak` veya `Linki gönder.` gibi doğal ifadeler bağlama uyuyorsa gereksiz yere değiştirilmez.

## Nerede kullanılır?

Pazarlama, ürün/UI metinleri, SaaS, lokalizasyon, dokümantasyon, destek içerikleri, hukuk/gizlilik/güvenlik metinleri, kurumsal iletişim ve AI tarafından yazılmış Türkçenin gözden geçirilmesinde kullanılabilir.

Genel yazım denetleyicisi, AI detector, İngilizce kelime yasak listesi veya profesyonel hukuk incelemesinin yerine geçen bir araç değildir.

## Kurulum

```bash
npx skills add oguzhankayan/turkish-native --global
```

Claude Code plugin desteği olan sürümlerde:

```text
/plugin marketplace add oguzhankayan/turkish-native
/plugin install turkish-native@turkish-native
```

Elle kurulumda `SKILL.md` ile `references/` klasörünü kullandığın agent'ın skill dizinine kopyala.

## Kullanım

```text
Use $turkish-native to review this Turkish copy.
Flag translationese and rewrite it naturally.
```

```text
Translate this into native Turkish with $turkish-native.
Preserve the facts, but do not preserve English sentence structure.
```

## Nasıl çalışır?

Skill önce hedef kitleyi ve tonu belirler, bilgiyi mevcut cümle yapısından ayırır, kelime seçiminden önce yapısal sorunları arar, yabancı cümle iskeletini yeniden kurar ve son olarak bilgi sadakati ile aşırı düzeltmeyi kontrol eder.

Toplam **48 Türkçeye özel kalıp** beş grupta toplanır:

- 1–10: cümle mimarisi,
- 11–20: fiil seçimi ve doğal kelime birliktelikleri,
- 21–30: ürün, UI ve lokalizasyon,
- 31–40: pazarlama ve model yazımı,
- 41–48: ton, bilgi sadakati ve son kontroller.

Ayrıntılı açıklamalar, örnekler ve false-positive korumaları [`references/`](references/) altında; çalışma talimatları [`SKILL.md`](SKILL.md) içinde.

## Eval seti

Repo [`evals/cases/`](evals/cases/) altında **72 regression vakası** içerir. Bunların arasında değiştirilmemesi gereken doğal Türkçe örnekleri de vardır. Numaralandırılmış 48 kalıbın tamamı eval setinde kapsanır.

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate-package.py
```

Benchmark yaklaşımı için [`docs/BENCHMARKING.md`](docs/BENCHMARKING.md), tasarım ilkeleri için [`docs/PHILOSOPHY.md`](docs/PHILOSOPHY.md) dosyasına bakabilirsin.

## Proje durumu

Güncel sürüm **v0.3.0, 1.0 öncesi**. Repo herkese açık test ve katkı için hazırlanmıştır. Kalıp adları ve eval şeması, daha fazla örnek ve native-reader geri bildirimi geldikçe değişebilir.

## Humanizer ile ilişkisi

[blader/humanizer](https://github.com/blader/humanizer) genel AI yazım kalıplarına odaklanır. Turkish Native ise daha dar bir problemi çözer: Türkçeye özgü translationese ve doğal olmayan cümle kuruluşu.

Turkish Native bir Humanizer fork'u değildir ve onun pattern taxonomy'sini kullanmaz. Repo paketleme yaklaşımı Humanizer'dan ilham almıştır.

## Katkı

Katkılar açıktır. PR açmadan önce [`CONTRIBUTING.md`](CONTRIBUTING.md) dosyasını oku.

## Lisans

MIT © 2026 Oğuzhan Kayan. Ayrıntılar için [`LICENSE`](LICENSE).
