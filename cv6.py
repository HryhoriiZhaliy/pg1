import json
import requests


url = "https://db.carnewschina.com/suggest?q="


def download_json_and_parse_brands(prefix):
    # stahneme url + prefix
    urlprefix = url + prefix
    response = requests.get(urlprefix)
    # stahneme json
    if  response.status != 200:
        print("chyba")
        return []
    json_data = response.json()
    # zkonvertujeme na data
    data = json.loads(json_data)
    print(data)

    brands = []

    # vytahneme nazvy brandu ["brans"]["name"]
    for brand in data["brands"]:
        brands.append(brand["name"])

    return brands


if __name__ == "__main__":

    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    for brand in brands:
        print(brand)

    