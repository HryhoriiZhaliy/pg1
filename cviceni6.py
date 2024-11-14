import sys
import requests

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
    response.content

    return nadpisy



if __name__ == "__main__":
    url = sys.argv[1]
    nadpisy = stahniurlavratnadpisy(url)
    print(nadpisy)