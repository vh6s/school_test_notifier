import requests
from config import DISCORD_WEBHOOK

def send():
    data = {
        "content": "Test do jazyků je dostupný! 🟢 @everyone"
    }
    requests.post(DISCORD_WEBHOOK, json=data)