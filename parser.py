from bs4 import BeautifulSoup

def parse_tests(html, target_name = "Formální jazyky a překladače"):
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.select("tbody tr.lbn")

    for row in rows:
        tds = row.find_all("td")
        if len(tds) > 1 and target_name in tds[1].text:
            return True

    return False