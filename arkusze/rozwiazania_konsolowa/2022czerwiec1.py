import random

def wypelnij_losowo(rozmiar, minimum, maksimum):
    return [random.randint(minimum, maksimum) for _ in range(rozmiar)]

def wyszukaj(tablica, szukana):
    n = len(tablica)
    tablica.append(szukana)

    i = 0
    while tablica[i] != szukana:
        i += 1
    tablica.pop()

    if i < n:
        return i
    else:
        return -1

losowa_tablica = wypelnij_losowo(100, 1, 100)

szukana_liczba = int(input("Podaj szukaną liczbę: "))
indeks_szukanej = wyszukaj(losowa_tablica, szukana_liczba)

print("\nTablica:")
print(*losowa_tablica, sep=", ")

if indeks_szukanej != -1:
    print(f"\nZnaleziono liczbę {szukana_liczba} na indeksie {indeks_szukanej}")
else:
    print(f"\nNie znaleziono liczby {szukana_liczba} w tablicy")