# Ödev: Tersten Doğrusal Arama (Reverse Linear Search)

## Ders
Veri Yapıları ve Algoritmalar

## Ödevin Amacı

Bu ödevde, bir liste içerisinde arama yapan algoritmayı **listenin sonundan başlayarak** yazmanız istenmektedir.

Amaç:

- Diziler üzerinde arama işlemleri yapmak
- Döngü kontrolünü geliştirmek
- İndeks kullanımı
- Algoritmanın adım adım çalışmasını anlamak

---

# Genel Tanım

Normal doğrusal aramada:

→ Liste baştan sona taranır

Bu ödevde ise:

👉 Liste **sondan başa doğru** taranacaktır

---

# Bölüm 1 – Fonksiyonu Yazınız (Zorunlu)

```python
def tersten_arama(liste, aranansayi):
    pass
```

Kurallar:

- Arama listenin **son elemanından başlamalıdır**
- Baştaki elemana kadar ilerlemelidir
- Eleman bulunursa index döndürülmelidir
- Bulunamazsa -1 döndürülmelidir

---

# Örnek

```
Liste: [5, 3, 8, 1, 3]

Aranan sayı: 3

Arama sırası:
3 (index 4) → bulundu

Sonuç: 4
```

NOT: İlk bulunan değil, **sondan ilk bulunan** döndürülür.

---

# Bölüm 2 – Adım Adım Çalışmayı Yazdırma (Zorunlu)

Algoritma çalışırken HER ADIM yazdırılmalıdır.

Örnek çıktı:

```
Liste: [5, 3, 8, 1, 3]

Aranan sayı: 3

1. adım: index 4 kontrol ediliyor → 3
Bulundu!

Sonuç: index = 4
```

---

# Bölüm 3 – Karşılaştırma Sayacı

Programa sayaç ekleyiniz:

- Kaç karşılaştırma yapıldı?

Örnek:

```
Toplam karşılaştırma sayısı: 1
```

---

# Bölüm 4 – Testler (Zorunlu)

Aşağıdaki testleri yapınız:

1. [5, 3, 8, 1, 3] → 3
2. [10, 20, 30, 40] → 10
3. [1, 2, 3, 4, 5] → 6
4. [7] → 7
5. [] → 5
6. [9, 9, 9, 9] → 9
7. [1, 5, 2, 5, 3] → 5

Her testte:

- Adımlar yazdırılmalı
- Sonuç doğru olmalı

---

# Bölüm 5 – Kullanıcıdan Girdi Alma

Programın sonunda:

- Kullanıcıdan liste elemanları alın
- Aranacak sayıyı alın
- Fonksiyonu çalıştırın

Örnek:

```
Kaç sayı gireceksiniz: 4
Sayı 1: 5
Sayı 2: 2
Sayı 3: 9
Sayı 4: 2

Aranacak sayı: 2

Sonuç: index = 3
```

---

# Bölüm 6 – Zaman Karmaşıklığı Analizi

Kodun altına yorum olarak yazınız:

1. Bu algoritmanın zaman karmaşıklığı nedir?
2. En iyi durum nedir?
3. En kötü durum nedir?
4. Baştan arama ile farkı var mıdır?

---

# Bonus (İsteğe Bağlı)

1. Baştan arama ile karşılaştırma yapın
2. Her iki yöntemde karşılaştırma sayısını yazdırın
3. En son bulunan değil, tüm bulunan indexleri listeleyin

---

# Değerlendirme Ölçütleri

- Doğru çalışması: %40
- Tersten arama mantığı: %20
- Adım adım çıktı: %20
- Sayaç kullanımı: %10
- Testler: %10

---

# Teslim

Dosya adı:

`odev_tersten_arama.py`

---

# Önemli Not

Bu ödevin amacı sadece arama yapmak değil,  
**algoritmanın başlangıç noktasının sonucu nasıl etkilediğini anlamaktır.**

Başarılar.
