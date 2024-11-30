def obvod_ctverce(delka_strany):
    # funkce vypocita obvod ctverce z delky jeho strany
    return 4 * delka_strany

def obsah_ctverce(delka_strany):
    # funkce vypocita obsah ctverce z delky jeho strany
    return delka_strany ** 2

def pocet_pismen(text, pismeno):
    pocet = 0
    for p in text:
        if p == pismeno:
            pocet +=1
        
    return pocet


def index_pismene(text, pismeno):
    indexy = []
    i = 0
    while i < len(text):
        if text[i] == pismeno:
            indexy.append(i)
        i += 1
    return indexy

def fibonachi(maximum):
    fib = [1, 1]
    soucet = fib[-2] = fib[-1]
    while soucet <= maximum:
        fib.append(soucet)
        soucet = fib[-2] = fib[-1]
    return fib

if __name__ == "__main__":
    print(obsah_ctverce(5))
    print(obsah_ctverce(5))