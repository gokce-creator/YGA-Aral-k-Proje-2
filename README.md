Ön Koltukta Oturma Koşulu Kontrolü
1. Giriş
Bu proje, bir bireyin yaşına göre ön koltukta oturup oturamayacağını belirleyen basit bir Python programıdır. Kullanıcıdan yaş bilgisi alınarak, belirlenen yaş sınırına göre uygun bir mesaj görüntülenir.

2. Algoritmanın Çalışma Mantığı
Kullanıcıdan yaş bilgisi girişi alınır.
Girilen değer integer (tam sayı) olarak saklanır.
Eğer girilen yaş 12’den küçükse, ekrana "You can't front passenger seat" yazdırılır.
Eğer yaş 12 veya daha büyükse, ekrana "You can front passenger seat" yazdırılır.
Kodun akış şeması şu şekildedir:


Başla
↓
Yaş bilgisini al
↓
Eğer yaş < 12 ise:
   → "You can't front passenger seat"
Aksi halde:
   → "You can front passenger seat"
↓
Bitiş

3. Karşılaşılan Zorluklar ve Çözümler
🔹 Sorun 1: Kullanıcının Geçersiz Veri Girmesi
Hata: Kullanıcı harf veya boşluk girdiğinde program hata veriyordu.
Çözüm: try-except bloğu eklenerek hata kontrolü sağlandı.

try:
    passenger_age = int(input("Enter your age please: "))
except ValueError:
    print("Invalid input! Please enter a number.")
🔹 Sorun 2: VS Code Debugger’ın Girişte Takılması
Hata: Debug işlemi giriş satırında duraklıyor ve ilerlemiyordu.

Çözüm:
"Debug Console" yerine "Terminal" kullanıldı.
VS Code’un terminal ayarları düzenlendi.