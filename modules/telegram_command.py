import threading
import requests
from config import TG_TOKEN, TG_USER_ID
from modules import booster, detox, location, notifier

import os

BASE_URL = f"https://api.telegram.org/bot{TG_TOKEN}"
chat_id = TG_USER_ID

# Flag untuk sleep/resume
sleep_mode = False

COMMANDS_HELP = """
📖 *Daftar Perintah Telegram:*
/start - Menyapa user dan status awal
/help - Tampilkan semua perintah
/status - Cek status aktif & IP
/ip - Lihat IP publik
/ping - Ping ke Google
/boost - Jalankan booster manual
/detox - Detox random manual
/notifikasi - Lihat notifikasi order
/lokasi - Kirim lokasi GPS terkini
/lokasi network - Kirim lokasi berbasis Network
/sleep - Pause semua aktivitas
/resume - Lanjutkan aktivitas
/stop - Hentikan script OjolBoost sepenuhnya
"""

def send_message(text):
    requests.post(f"{BASE_URL}/sendMessage", data={"chat_id": chat_id, "text": text})

def handle_commands():
    def poll():
        global sleep_mode
        last_update_id = None
        while True:
            try:
                url = f"{BASE_URL}/getUpdates?timeout=30"
                if last_update_id:
                    url += f"&offset={last_update_id + 1}"
                res = requests.get(url).json()
                for update in res.get("result", []):
                    last_update_id = update["update_id"]
                    message = update.get("message", {})
                    text = message.get("text", "")
                    if not text:
                        continue
                    command = text.strip().lower()
                    print(f"[Telegram] Command diterima: {command}")
                    
                    if command == "/start":
                        send_message("👋 Selamat datang di OjolBoost!\nKetik /help untuk daftar perintah.")
                    elif command == "/help":
                        send_message(COMMANDS_HELP)
                    elif command == "/status":
                        ip = booster.get_ip()
                        ping = booster.ping_google()
                        send_message(f"📡 Status Aktif\nIP: {ip}\nPing: {ping}")
                    elif command == "/ip":
                        ip = booster.get_ip()
                        send_message(f"🌐 IP Publik: {ip}")
                    elif command == "/ping":
                        ping = booster.ping_google()
                        send_message(f"📶 Ping Google:\n{ping}")
                    elif command == "/boost":
                        send_message("🚀 Boosting koneksi...")
                        ping = booster.ping_google()
                        send_message(ping)
                    elif command == "/detox":
                        send_message("🧘 Detox dimulai...")
                        detox.random_detox()
                        send_message("✅ Detox selesai")
                    elif command == "/notifikasi":
                        notif = notifier.get_last_notifikasi()
                        send_message(f"🔔 Notifikasi terbaru:\n{notif}")
                    elif command == "/lokasi":
                        loc = location.get_location(provider="gps")
                        send_message(f"📍 Lokasi (GPS):\n{loc}")
                    elif command == "/lokasi network":
                        loc = location.get_location(provider="network")
                        send_message(f"📶 Lokasi (Network):\n{loc}")
                    elif command == "/sleep":
                        sleep_mode = True
                        send_message("😴 Mode sleep diaktifkan")
                    elif command == "/resume":
                        sleep_mode = False
                        send_message("✅ Mode sleep dimatikan, lanjut aktivitas")
                    elif command == "/stop":
                        send_message("🛑 Script dihentikan. Bye 👋")
                        os._exit(0)
                    else:
                        send_message("❓ Perintah tidak dikenali. Ketik /help untuk daftar.")
            except Exception as e:
                print(f"[Telegram Error] {e}")
    threading.Thread(target=poll, daemon=True).start()