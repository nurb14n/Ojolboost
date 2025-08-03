import subprocess
import requests

def get_ip():
    try:
        return requests.get("https://api64.ipify.org").text
    except:
        return "Tidak dapat IP"

def ping_google():
    try:
        result = subprocess.check_output(["ping", "-c", "3", "8.8.8.8"])
        return result.decode()
    except:
        return "Ping gagal"
