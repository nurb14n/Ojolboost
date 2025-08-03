# OjolBoost 🚀

Toolkit Termux berbasis Python untuk membantu driver ojek online (ShopeeFood & Grab Driver) dalam meningkatkan performa jaringan dan memantau order secara otomatis.

---

## ✨ Fitur Utama

- **Auto Boost Koneksi** (ping & get IP)
- **Detox Otomatis** (pause acak)
- **Jadwal Aktif Dinamis** (pagi & sore)
- **Monitoring Notifikasi Order** (ShopeeFood / Grab)
- **Telegram Remote Control** (command bot)
- **Tracking Lokasi Realtime** (GPS/Network)
- **Auto Pause saat dapat order**
- **Log Order**
- **Command Telegram: /start /status /ping /lokasi /boost /detox /notifikasi /sleep /resume /stop**

---

## 🧰 Requirements (Pra-instalasi)

Pastikan hal berikut sudah disiapkan di Termux:

- Python 3.10+  
- Git (`pkg install git`)
- Termux:API (`pkg install termux-api`)
- Aplikasi **Termux:API** terinstal dari Play Store / F-Droid
- Token & Chat ID Telegram untuk command bot
- Izin lokasi & notifikasi telah diberikan ke Termux

---

## ⚙️ Langkah Instalasi

```bash
# 1. Clone proyek
git clone https://github.com/username/ojolboost.git
cd ojolboost

# 2. Jalankan installer otomatis
python installer.py