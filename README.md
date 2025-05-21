Belirlenen Tarih ve Saate Otomatik Instagram Gönderisi Paylaşma Aracı
Bu proje, kullanıcıların belirledikleri tarih ve saatte Instagram hesaplarından otomatik olarak gönderi paylaşmalarını sağlayan bir masaüstü otomasyon uygulamasıdır. 
Python programlama dili ile geliştirilmiş olup, görsel arayüzü sayesinde kullanım kolaylığı sunar.

🛠 Kullanılan Teknolojiler ve Kütüphaneler
Python 3.x
Tkinter – Masaüstü arayüzü için
instagrapi – Instagram API işlemleri için
schedule – Görev zamanlama
threading – Arka plan işlemleri için
datetime, time – Zaman işlemleri için
tkinter.messagebox, filedialog – Bilgi ve dosya seçimi için

🔧 Modül Yapısı ve Fonksiyonlar
📁 instagram.py
post_to_instagram(username, password, image_path, caption):
Kullanıcı adı ve şifre ile Instagram hesabına giriş yapar, belirtilen görseli ve açıklamayı paylaşır.
Hata durumunda kullanıcıya bilgi mesajı gösterir.
Client(): instagrapi kütüphanesinden gelen, Instagram API ile iletişim sağlayan istemcidir.

📁 scheduler.py
schedule_post(date, time, job_function):
Kullanıcının belirlediği tarih ve saatte, gönderi paylaşım fonksiyonunu zamanlar.
Geçmiş tarih kontrolü yapılır, threading ile görev arka planda başlatılır.
run_schedule():
Planlanan görevleri sürekli kontrol eder ve zamanı geleni çalıştırır.
threading.Thread: Arayüzün donmaması ve planlanan görevlerin arka planda yürütülmesi için kullanılmıştır.

📁 main.py
Tkinter tabanlı kullanıcı arayüzüdür.
Fonksiyonlar:
browse_file(): Kullanıcının bilgisayarından görsel seçmesini sağlar.
submit(): Giriş alanlarındaki bilgileri okur ve doğrular.
job(): Gönderi işlemini bir görev olarak tanımlar.
root.mainloop(): Arayüzü başlatır.

💡 Özellikler
✅ Görsel kullanıcı arayüzü (GUI)
✅ Belirlenen tarih ve saatte otomatik gönderi paylaşımı
✅ Gönderiye açıklama ekleyebilme
✅ Zamanlanmış görevlerin arka planda çalışması
✅ Hatalara karşı kullanıcı bilgilendirmesi

⚙️ Kullanım
Uygulamayı başlatın:

Arayüzden:
Kullanıcı adınızı ve şifrenizi girin
Gönderilecek resmi seçin
Açıklamayı yazın
Tarih ve saat girin
“Planla” butonuna tıklayın

⚠️ Dikkat Edilmesi Gerekenler
Instagram, üçüncü parti araçlar için zaman zaman API erişim kurallarını değiştirebilir.
Bu bot, eğitim amaçlı geliştirilmiştir.
Çok faktörlü doğrulama (2FA) aktifse, giriş işlemi başarısız olabilir.
Hesap güvenliğiniz için, test sırasında yeni bir Instagram hesabı kullanmanız önerilir.
