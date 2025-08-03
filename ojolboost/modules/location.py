import subprocess
import json

def get_location(provider="gps"):
    """
    Ambil lokasi menggunakan termux-location tanpa opsi -r,
    pakai last known location agar lebih cepat & reliable.
    """
    for prov in (provider, "network" if provider=="gps" else "gps"):
        try:
            # Hapus -r, agar mengambil last known location
            result = subprocess.check_output(
                ["termux-location", "-p", prov],
                stderr=subprocess.DEVNULL
            ).decode().strip()

            if not result:
                continue  # coba provider selanjutnya

            data = json.loads(result)
            lat = data.get("latitude")
            lon = data.get("longitude")
            acc = data.get("accuracy")

            if lat is None or lon is None:
                continue

            return (
                f"Latitude : {lat:.6f}\n"
                f"Longitude: {lon:.6f}\n"
                f"Akurasi   : {acc:.2f} m\n"
                f"Provider  : {prov}"
            )
        except json.JSONDecodeError:
            continue
        except Exception:
            continue

    return "❌ Gagal ambil lokasi. Pastikan GPS/Network aktif & izin diberikan."