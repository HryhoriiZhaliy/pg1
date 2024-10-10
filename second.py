def cislo_text(cislo):
    cisla = {
        0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři",
        5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět",
        10: "deset", 11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct",
        15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct",
        20: "dvacet", 30: "třicet", 40: "čtyřicet", 50: "padesát",
        60: "šedesát", 70: "sedmdesát", 80: "osmdesát", 90: "devadesát", 100: "sto"}
    cislo = int(cislo)
    if cislo in cisla:
        return cisla[cislo]
    elif cislo < 100:
        desitky = cislo // 10 * 10
        jednotky = cislo % 10
        return f"{cisla[desitky]} {cisla[jednotky]}"
    else:
        return "Číslo je mimo rozsah"
    

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)

