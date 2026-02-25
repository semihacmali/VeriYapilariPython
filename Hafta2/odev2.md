# Ödev: Verilen Metni Tersine Çeviren Fonksiyon

## Ders
Veri Yapıları ve Algoritmalar

## Ödevin Amacı

Bu ödevde, kullanıcıdan alınan bir metni tersine çeviren bir fonksiyon yazmanız istenmektedir.

Amaç:

- Döngü kullanımı
- String (metin) indeksleme
- Karakter bazlı işlem yapma
- Zaman karmaşıklığı analizi
- Farklı çözüm yolları geliştirme

Bu ödevde liste (array) kullanmak yasaktır.

---

# Genel Tanım

Aşağıdaki fonksiyonu yazınız:

```python
def ters_cevir(metin):
    pass
```

Fonksiyon:

- Parametre olarak bir string alacak.
- String’in ters halini döndürecek.
- Hazır `[::-1]` slicing yöntemi kullanılmayacak.
- `reversed()` fonksiyonu kullanılmayacak.

---

# Örnek

```
Girdi:  "merhaba"
Çıktı:  "abahrem"
```

```
Girdi:  "Python"
Çıktı:  "nohtyP"
```

---

# Bölüm A – Temel Çözüm (Zorunlu)

- Bir döngü kullanarak metni sondan başa doğru dolaşın.
- Yeni bir string değişken oluşturup karakterleri ekleyin.
- Sonucu return edin.

---

# Bölüm B – İndeks Kullanarak Çözüm (Zorunlu)

Aşağıdaki yapıyı kullanarak ikinci bir fonksiyon yazınız:

```python
def ters_cevir_index(metin):
    pass
```

- `range()` ile indeksleri tersten dolaşın.
- Her karakteri yeni string’e ekleyin.

---

# Bölüm C – While Döngüsü ile Çözüm (Zorunlu)

```python
def ters_cevir_while(metin):
    pass
```

- While döngüsü kullanın.
- İndeks değişkeni ile tersten ilerleyin.

---

# Bölüm D – Sayaç Ekleyin

Her fonksiyona:

- Kaç karakter işlendiğini sayan bir sayaç ekleyin.
- Sayaç değerini ekrana yazdırın.
- İşlenen karakter sayısının metin uzunluğuna eşit olduğunu gösterin.

---

# Bölüm E – Testler (En Az 15 Test)

Aşağıdaki testleri yapınız:

1. "a"
2. "ab"
3. "abc"
4. "12345"
5. "Python"
6. ""
7. " "
8. "Veri Yapıları"
9. "123abc"
10. "!!!"
11. Uzun bir cümle
12. Büyük harfli metin
13. Küçük harfli metin
14. Sayı ve harf karışık
15. 100 karakterlik bir metin

---

# Bölüm F – Kullanıcıdan Girdi Alma

Programın sonunda:

- Kullanıcıdan metin alın.
- Tersini ekrana yazdırın.

Örnek:

```
Metin giriniz: algoritma
Tersi: amtirogla
```

---

# Bölüm G – Zaman Karmaşıklığı Analizi

Kodun altına yorum olarak yazınız:

1. Bu algoritmanın zaman karmaşıklığı nedir?
2. Neden O(n) dir?
3. Bellek karmaşıklığı nedir?
4. Daha hızlı bir yöntem var mıdır?

---

# Teslim

Dosya adı:

`odev_metin_ters_cevir.py`

Dosyada bulunması gerekenler:

- 3 farklı ters çevirme fonksiyonu
- Sayaç çıktıları
- Testler
- Kullanıcıdan giriş alma
- Kısa analiz

---

# Önemli Not

Amaç sadece metni ters çevirmek değil,  
karakter bazlı algoritma mantığını kavramaktır.

Başarılar.
