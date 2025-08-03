import os
import subprocess
import sys

def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[!] Gagal menjalankan perintah: {cmd}")

def install_termux_api():
    print("📦 Memeriksa termux-api...")
    result = subprocess.run("command -v termux-notification-list", shell=True, stdout=subprocess.DEVNULL)
    if result.returncode != 0:
        print("🛠 Menginstal termux-api...")
        run_cmd("pkg update -y && pkg install termux-api -y")
    else:
        print("✅ termux-api sudah terinstal.")

def install_pip_requirements():
    print("📦 Menginstal dependency Python...")
    if not os.path.exists("requirements.txt"):
        print("❌ File requirements.txt tidak ditemukan!")
        return
    run_cmd("pip install --upgrade pip")
    run_cmd("pip install -r requirements.txt")

def buat_file_log():
    if not os.path.exists("notifikasi.log"):
        print("📄 Membuat file log notifikasi.log...")
        with open("notifikasi.log", "w") as f:
            f.write("")
    else:
        print("✅ notifikasi.log sudah ada.")

def cek_config():
    if not os.path.exists("config.py"):
        print("❌ config.py belum ada. Silakan salin atau buat dulu file konfigurasi.")
    else:
        print("✅ config.py ditemukan.")

def main():
    print("🚀 Menjalankan installer OjolBoost...\n")
    install_termux_api()
    install_pip_requirements()
    cek_config()
    buat_file_log()
    print("\n✅ Instalasi selesai! Jalankan dengan: python main.py")

if __name__ == "__main__":
    main()