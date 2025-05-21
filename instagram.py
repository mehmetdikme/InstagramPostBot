from instagrapi import Client
from tkinter import messagebox



def post_to_instagram(username, password, image_path, caption):
    try:
        cl = Client()
        cl.login(username, password)
        cl.photo_upload(image_path, caption)
        messagebox.showinfo("Başarılı", "Gönderi başarıyla paylaşıldı!")
    except Exception as e:
        messagebox.showerror("Hata", f"Gönderi paylaşımı başarısız oldu: {e}")




