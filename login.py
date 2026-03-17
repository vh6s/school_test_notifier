import requests
from config import BASE_URL, USERNAME, PASSWORD

def login(session: requests.Session):
    # globalni hlavicky pro cely seassion
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:148.0) Gecko/20100101 Firefox/148.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "cs,sk;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive"
    })
    
    session.get(f"{BASE_URL}/auth/?lang=cz")
    
    # sends data for authentization
    session.post(
        f"{BASE_URL}/system/ajax_handler.pl",
        data={
            "login": USERNAME,
            "password": PASSWORD,
            "lang": "cz"
        },
        headers={
            "X-Requested-With": "XMLHttpRequest",
            "Referer": f"{BASE_URL}/system/login.pl?lang=cz"
        }
    )
    
    # user login into site, should return cookie UISAuth
    response = session.post(
        f"{BASE_URL}/system/login.pl",
        data={
            "lang": "cz",
            "login_hidden": "1",
            "destination": "/auth/?lang=cz",
            "auth_id_hidden": "0",
            "auth_2fa_type": "no",
            "credential_0": USERNAME,
            "credential_1": PASSWORD
        },
        headers={
            "Referer": f"{BASE_URL}/auth/?lang=cz"
        },
        allow_redirects=True
    )

    cookies = session.cookies.get_dict()
    if "UISAuth" not in cookies:
        raise Exception("Login selhal – chybí UISAuth cookie")

    print("Přihlášení proběhlo úspěšně")