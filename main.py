import time
from datetime import datetime
from config import JADWAL
from modules import booster, detox, notifier, telegram_command

def cek_jam_aktif():
    now = datetime.now().strftime("%H:%M")
    for waktu in JADWAL.values():
        if waktu[0] <= now <= waktu[1]:
            return True
    return False

def main_loop():
    telegram_command.send_message("✅ OjolBoost aktif...")
    telegram_command.handle_commands()  # Jalankan polling command Telegram
    while True:
        if telegram_command.sleep_mode:
            print("[Bot] Mode sleep aktif. Tidur 30 detik...")
            time.sleep(30)
            continue

        if cek_jam_aktif():
            print("[Status] Dalam jam aktif")
            ip = booster.get_ip()
            print(f"[IP] {ip}")
            print("[Ping] " + booster.ping_google())
            detox.random_detox()
            notifier.monitor_notifikasi()
        else:
            print("[Status] Di luar jam aktif. Tidur 5 menit...")
            time.sleep(300)

if __name__ == "__main__":
    main_loop()