# Ödev: Insertion Sort (Ekleme Sıralaması) Algoritması

## Ders
Veri Yapıları ve Algoritmalar

## Ödevin Amacı

Bu ödevde, bir diziyi sıralayan **Insertion Sort algoritmasını** adım adım yazarak algoritmanın nasıl çalıştığını anlamanız istenmektedir.

Amaç:

- Diziler üzerinde işlem yapabilme
- İç içe döngü kullanımı
- Karşılaştırma ve yer değiştirme işlemleri
- Algoritmanın adım adım nasıl çalıştığını kavrama

---

# Insertion Sort Nedir?

Insertion Sort, diziyi sıralarken:

- Her adımda bir elemanı alır
- Onu doğru konuma yerleştirir
- Sol taraf her zaman sıralı olur

---

# Örnek Mantık

```
Başlangıç: [5, 3, 8, 1]

Adım 1: [3, 5, 8, 1]
Adım 2: [3, 5, 8, 1]
Adım 3: [1, 3, 5, 8]
```

---

# Bölüm 1 – Insertion Sort Fonksiyonunu Yazınız (Zorunlu)

```python
def insertion_sort(dizi):
    pass
```

Kurallar:

- Algoritmayı kendiniz yazmalısınız
- Hazır `sort()` veya `sorted()` kullanmak yasaktır
- Diziyi küçükten büyüğe sıralamalıdır

---

# Bölüm 2 – Adım Adım Çıktı (Zorunlu)

Algoritma çalışırken HER ADIMI ekrana yazdırmalısınız.

Örnek çıktı:

```
Başlangıç: [5, 3, 8, 1]

Adım 1: [3, 5, 8, 1]
Adım 2: [3, 5, 8, 1]
Adım 3: [1, 3, 5, 8]
```

Kurallar:

- Her dış döngü adımından sonra dizi yazdırılmalıdır
- Adım numarası gösterilmelidir

---

# Bölüm 3 – Karşılaştırma ve Yer Değiştirme Sayacı

Programınıza sayaç ekleyiniz:

- Kaç tane karşılaştırma yapıldı?
- Kaç tane yer değiştirme yapıldı?

Örnek çıktı:

```
Toplam karşılaştırma sayısı: 7
Toplam yer değiştirme sayısı: 4
```

---

# Bölüm 4 – Testler (Zorunlu)

Aşağıdaki dizilerle test yapınız:

1. [5, 3, 8, 1]
2. [1, 2, 3, 4] (zaten sıralı)
3. [9, 7, 5, 3]
4. [4]
5. []
6. [5, 5, 5, 5]
7. [10, -2, 3, -1]
8. [100, 50, 25, 75]

Her testte:

- Adımlar yazdırılmalı
- Sonuç doğru olmalı

---

# Bölüm 5 – Kullanıcıdan Girdi Alma

Programın sonunda:

- Kullanıcıdan sayılar alın
- Listeye ekleyin
- Sıralayıp sonucu gösterin

Örnek:

```
Kaç sayı gireceksiniz: 4
Sayı 1: 5
Sayı 2: 2
Sayı 3: 9
Sayı 4: 1

Sıralı hali: [1, 2, 5, 9]
```

---

# Bölüm 6 – Zaman Karmaşıklığı Analizi

Kodun altına yorum olarak yazınız:

1. Insertion Sort’un zaman karmaşıklığı nedir?
2. En iyi durum nedir?
3. En kötü durum nedir?
4. Zaten sıralı bir dizide nasıl davranır?

---

# Bonus (İsteğe Bağlı)

1. Diziyi büyükten küçüğe sıralayın
2. String listesi üzerinde deneyin (["ali","veli","ayşe"])
3. Her adımda sadece değişen kısmı yazdırın

---

# Değerlendirme Ölçütleri

- Doğru çalışması: %40
- Adım adım çıktı: %25
- Sayaç kullanımı: %15
- Testler: %10
- Analiz kısmı: %10

---

# Teslim

Dosya adı:

`odev_insertion_sort.py`

---

# Önemli Not

Bu ödevin amacı sadece sıralama yapmak değil,  
algoritmanın nasıl çalıştığını **gözlemleyerek öğrenmektir.**

Başarılar.
