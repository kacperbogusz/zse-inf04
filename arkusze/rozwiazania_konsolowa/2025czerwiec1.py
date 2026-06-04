import random

def wypelnij_tablice(tablica_losowan):
    ilosc_zestawow = int(input("Ile wygenerować losowań:\n"))
    for i in range(ilosc_zestawow):
        zestaw = random.sample(range(1, 50), 6)
        tablica_losowan.append(zestaw)
    return tablica_losowan

def wyswietl_wyniki(tablica_losowan):
    for i, zestaw in enumerate(tablica_losowan):
        print(f"Losowanie {i+1}: {' '.join(map(str, zestaw))}")

    liczba_wystapien = [0] * 50
    for zestaw in tablica_losowan:
        for liczba in zestaw:
            liczba_wystapien[liczba-1] += 1

    for i, liczba in enumerate(liczba_wystapien):
        print(f"Wystąpienia liczby {i+1}: {liczba}")

tablica_losowan = []
wypelnij_tablice(tablica_losowan)
wyswietl_wyniki(tablica_losowan)