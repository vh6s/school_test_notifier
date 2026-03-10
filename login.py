from bs4 import BeautifulSoup
import requests
from config import LOGIN_URL, TABLE_URL, USERNAME, PASSWORD

def login(session):

    r = session.get(LOGIN_URL)

    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    session.post(LOGIN_URL, data=payload)

# Testovací funkce pro ověření přihlášení
'''
def test_login():
    print("Zkousim prihlaseni")
    session = requests.Session()
    login(session)
    
    test_response = session.get(TABLE_URL)
    soup = BeautifulSoup(test_response.text, "html.parser")
    test_text = soup.find("td", id="prihlasen")
    
    if test_text:
        print("funguje")
    else:
        print("nefunguje")
        
if __name__ == "__main__":
    test_login()
'''