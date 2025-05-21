import tkinter as tk
from tkinter import filedialog, messagebox
from instagram import post_to_instagram
from scheduler import schedule_post
from datetime import datetime


def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.jpg;*.png")])
    entry_image_path.delete(0, tk.END)
    entry_image_path.insert(0, filename)

def submit():
    username = entry_username.get()
    password = entry_password.get()
    image_path = entry_image_path.get()
    caption = entry_caption.get("1.0", tk.END).strip()
    date = entry_date.get()
    time_str = entry_time.get()

    if not username or not password or not image_path or not caption or not date or not time_str:
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")
        return


    def job():
        post_to_instagram(username, password, image_path, caption)

    if schedule_post(job, date, time_str):
        messagebox.showinfo("Planlandı", f"Gönderi {date} {time_str} tarihinde paylaşılmak üzere planlandı.")




root = tk.Tk()
root.title("Instagram Post Planlayıcı")

# Pencereyi ekranın ortasında açmak için:
screen_width = root.winfo_screenwidth()  # Ekran genişliği
screen_height = root.winfo_screenheight()  # Ekran yüksekliği
window_width = 500  # Pencere genişliği
window_height = 500  # Pencere yüksekliği

# Ekranın ortasına pencereyi yerleştir
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Pencereyi tam görünür yapmak ve ortalamak
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)  # Pencereyi yeniden boyutlandırmayı engelle

# Arka plan rengi
root.config(bg="#002333")

# Kullanıcı Giriş Alanları
tk.Label(root, text="Kullanıcı Adı:", bg="#002333", fg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_username = tk.Entry(root, width=30)
entry_username.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Şifre:", bg="#002333", fg="#f0f0f0", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_password = tk.Entry(root, width=30, show="*")  # Şifre gizleme
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Gönderi Bilgileri
tk.Label(root, text="Resim Dosyası:", bg="#002333", fg="#f0f0f0", font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_image_path = tk.Entry(root, width=30)
entry_image_path.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Gözat", command=browse_file, bg="#159A9C", fg="white", font=("Arial", 10)).grid(row=2, column=2, padx=10, pady=10)

tk.Label(root, text="Açıklama:", bg="#002333", fg="#f0f0f0", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_caption = tk.Text(root, width=30, height=5)
entry_caption.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="w")

tk.Label(root, text="Tarih (YYYY-AA-GG):", bg="#002333", fg="#f0f0f0", font=("Arial", 10)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_date = tk.Entry(root, width=30)
entry_date.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Saat (SS:DD):", bg="#002333", fg="#f0f0f0", font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
entry_time = tk.Entry(root, width=30)
entry_time.grid(row=5, column=1, padx=10, pady=10)

# Planlama Butonu
planla_button = tk.Button(root, text="Planla", command=submit, bg="#159A9C", fg="white", font=("Arial", 12), height=2, width=10)
planla_button.grid(row=6, column=0, columnspan=3, pady=20)

root.mainloop()





