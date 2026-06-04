import random

class Tablica:
    def __init__(self, rozmiar):
        self.__tablica = []
        self.__liczba_elementow = rozmiar

        for _ in range(rozmiar):
            self.__tablica.append(random.randint(1,1000))

    def wyswietl_elementy(self):
        for i, wartosc in enumerate(self.__tablica):
            print(f"{i}: {wartosc}")

    def wyszukaj_wartosc(self, szukana_wartosc):
        for i, wartosc in enumerate(self.__tablica):
            if wartosc == szukana_wartosc:
                return i
            else:
                return -1

    def zlicz_nieparzyste(self):
        licznik_nieparzystych = 0
        for wartosc in self.__tablica:
            if wartosc % 2 == 1:
                licznik_nieparzystych += 1
        print(f"Razem nieparzystych: {licznik_nieparzystych}")

    def policz_srednia(self):
        return sum(self.__tablica) / len(self.__tablica)

moja_tablica = Tablica(30)
moja_tablica.wyswietl_elementy()
indeks_szukanej = moja_tablica.wyszukaj_wartosc(2)
if indeks_szukanej != -1:
    print(indeks_szukanej)
moja_tablica.zlicz_nieparzyste()
print(f"Średnia wszystkich elementów: {moja_tablica.policz_srednia()}")
