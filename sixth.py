import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    try:
        
        response = requests.get(url)
        
        
        if response.status_code == 200:
           
            soup = BeautifulSoup(response.content, "html.parser")
            
            
            for link in soup.find_all('a', href=True):
                hrefs.append(link['href'])
        else:
            print(f"nastala chyba, nepodarilo se pripojit na: {response.status_code}")
    
    except requests.RequestException as e:
        print(f"Nastala chyba: {e}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        print(all_hrefs)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")