import time
import requests
from config import TABLE_URL, CHECK_INTERVAL
from login import login
from notifier import send
from parser import parse_tests

session = requests.Session()
login(session)

start = time.time()

while time.time() - start < 7200:
    try:
        response = session.get(TABLE_URL, timeout=10)
        
        # check jestli session expirovala, pokud ano -> znovu se prihlasi
        if response.status_code == 403:
            print(f"[{time.strftime('%H:%M:%S')}] Session expirovala, login znovu...")
            login(session)
            continue
        
        response.raise_for_status()

        if parse_tests(response.text):
            print("Test je tam! Posílám Discord zprávu.")
            send()
            break
        
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Zatím nic, čekám {CHECK_INTERVAL}s...")

    # exception co hlida problemy se spojenim a serverem, tak aby skript nespadnul
    except requests.exceptions.RequestException as req_err:
        print(f"[{time.strftime('%H:%M:%S')}] Problém se spojením/serverem: {req_err}")
    
    # obecny expection aby skript bezel dal
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] Chyba v kódu: {e}")

    time.sleep(CHECK_INTERVAL)

print("----- Skript skončil. -----")