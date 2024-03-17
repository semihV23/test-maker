## Nedir

Soru fotoğrafları ile küçük testler hazırlayan bir araç.

Çözdüğüm denemelerde yaptığım yanlış soruları daha sonra tekrardan çözebilmek için bir araya getirmek istedim. Bunu yapmak için önzcelikle soruların fotoğraflarına ihtiyacımız var. Fotoğraflar çekildiği sıra ile teste yerleşecek. (Dosya ismi baz alınıyor.) Bu fotoğrafları sıra ile çekmek önemli. Fotoğrafları çektikten sonra bunları `questions` dizinine atıyoruz. Ardından `Header.txt` dosyasını düzenliyoruz. Dosya formatı şu şekilde olmalı;

```
Doküman Adı
[[NewLine]]
Tarih
[[NewLine]]
Doküman ile ilgili açıklama metni.
```

Dosyayı bu formatta düzenledikten sonra yapmamız gereken Python kodunu çalıştırmak. Bunun için aşağıdaki kod ile gereki kütüphaneleri kurmamız gerekiyor.

```
pip install -r requirements.txt
```

Şimdi kodu çalıştıralım;

```
python main.py
```

Çıktı dosyası `doküman_adı_tarih.pdf` ismiyle ana dizine kaydedilecektir.

## Yardımcı Araçlar

### Exif Remover

Fotoğrafların metadata bilgisini silmek için Python ile yazılmış bir araç.

Kullanmak için temizlemek istediğiniz fotoğrafları `exif_remove` dizinine koyun. Ardından aşağıdaki komutu çalıştırın.

```
python exif_remove_tool.py
```

Temiz fotoğraflar `exif_remove/safe` dizinine kaydedilecek.

### IMGTools Crop Images

Site: https://www.imgtools.co/crop-image

Bu site soru fotoğraflarını doğru ölçüde kırpmaya yarıyor. Siteye fotoğrafların metadata bilgilerini vermek istemezseniz Exif Remover aracını kullanabilirsiniz.
