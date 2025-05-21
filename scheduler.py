import schedule
import threading
import time
from datetime import datetime
from tkinter import messagebox

def schedule_post(job_function, date, time_str):
    schedule_time = f"{date} {time_str}"
    target_time = datetime.strptime(schedule_time, "%Y-%m-%d %H:%M")

    if target_time < datetime.now():
        messagebox.showerror("Hata", "Girilen tarih ve saat geçersiz. Lütfen gelecekteki bir tarih ve saat girin.")
        return False

    schedule.every().day.at(target_time.strftime("%H:%M")).do(job_function)
    threading.Thread(target=run_schedule).start()
    return True

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)
