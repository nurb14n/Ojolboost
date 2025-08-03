import time
import random

def random_detox():
    durasi = random.randint(30, 90)
    print(f"[Detox] Tidur {durasi} detik...")
    time.sleep(durasi)
