import sys
import requests
from lxml import html

def stahniurlavratnadpisy(url):
    nadpisy = []
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f'nastala chyba, nepodarilo se pripojit na {url}')
        return []
    if response.status_code != 200:
        print(f'nastala chyba, http code: {response.status_code}')
        return []
    root = html.fromstring(response.content)
    for h in ("h1", "h2", "h3", "h4", "h5"):
        for h1 in root.xpath("//h1"):
            h1_text = h1.text_content().strip()
            if h1_text:
                nadpisy.appent(h1_text)

    

    return nadpisy



if __name__ == "__main__":
    url = sys.argv[1]
    nadpisy = stahniurlavratnadpisy(url)
    print(nadpisy)