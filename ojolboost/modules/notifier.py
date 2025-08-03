import subprocess
import json
from config import LOG_FILE, TG_TOKEN, TG_USER_ID
import requests

def monitor_notifikasi():
    try:
        output = subprocess.check_output(["termux-notification-list"])
        notif_list = json.loads(output)

        for notif in notif_list:
            app = notif.get("packageName", "").strip()
            title = notif.get("title", "").strip()
            content = notif.get("content", "").strip()
            waktu = notif.get("when", "").strip()

            # Hanya proses jika title adalah "Pesanan Baru"
            if title.lower() != "pesanan baru":
                print(f"[Skip] Judul bukan 'Pesanan Baru': {title}")
                continue

            # Hanya proses aplikasi ShopeeFood & Grab Driver
            if app in ["com.shopee.foody.driver.id", "com.grabtaxi.driver2"]:
                log_entry = f"[{waktu}] {app} | {title} | {content}"
                print(f"[Notif] {log_entry}")

                with open(LOG_FILE, "a") as f:
                    f.write(log_entry + "\n")

                message = f"📲 Order Masuk!\n📱 App: {app}\n🕒 {waktu}\n📌 {title}\n{content}"
                requests.post(
                    f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
                    data={"chat_id": TG_USER_ID, "text": message}
                )

    except Exception as e:
        print(f"[Error] Gagal ambil notifikasi: {e}")