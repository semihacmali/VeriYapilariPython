# Ödev: O(log n) Zaman Karmaşıklığında Kuvvet Hesaplama (Exponentiation by Squaring)

## Ders
Veri Yapıları ve Algoritmalar (Önlisans)

## Amaç
Bu ödevde, **taban^üs** (power) işlemini **O(log n)** zaman karmaşıklığında hesaplayan bir fonksiyon geliştireceksiniz.  
Klasik yöntem (üs kadar çarpma) **O(n)** iken, bu ödevde kullanılacak yöntem **Exponentiation by Squaring** ile **O(log n)** olacaktır.

---

## Kazanımlar
- Algoritma tasarlama ve uygulama
- İteratif ve/veya özyinelemeli (recursive) çözüm kurma
- Zaman karmaşıklığını analiz etme (Big-O)
- Kenar durumları (edge cases) yönetme
- Basit test senaryoları yazma

---

## Tanım
Aşağıdaki fonksiyonu yazınız:

### İstenen Fonksiyon
`fast_power(base, exp) -> int | float`

- `base`: int veya float olabilir
- `exp`: **0 veya pozitif** tamsayı (int) olacak
- Fonksiyon, `base ** exp` değerini döndürmeli
- **Zaman karmaşıklığı hedefi:** `O(log exp)`

> Not: Python’un hazır `**` operatörünü veya `pow(base, exp)` fonksiyonunu doğrudan sonucu hesaplamak için kullanmayın.

---

## Kullanmanız Gereken Yöntem (Özet)
Exponentiation by Squaring fikri:

- Eğer `exp` çift ise:  
  `base^exp = (base^(exp/2))^2`
- Eğer `exp` tek ise:  
  `base^exp = base * base^(exp-1)`  
  ve `(exp-1)` çift olacağı için yine hızlıca yarıya indirilebilir.

---

## Zorunlu Gereksinimler
1. `fast_power` fonksiyonunuz **O(log n)** olmalı.
2. `exp` için:
   - `exp == 0` durumunda sonuç **1** olmalı.
3. En az **10 adet test** çalıştırmalısınız (aşağıda örnekler var).
4. Kodunuzun içinde (yorum satırlarında) şu kısımlar bulunmalı:
   - Kullanılan algoritmanın kısa açıklaması
   - Zaman karmaşıklığı açıklaması
5. Kod tek dosyada çalışmalı: `odev_fast_power.py`

---

## Bölüm A — Temel Uygulama (Zorunlu)
Aşağıdaki fonksiyonu yazın:

```python
def fast_power(base, exp):
    """
    base^exp değerini O(log exp) zamanda hesaplar.
    Kural: ** veya pow kullanmak yasak.
    """
    # TODO: burayı doldurun
    pass
