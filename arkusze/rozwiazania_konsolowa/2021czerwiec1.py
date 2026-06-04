class Narzedzia:
    def __init__(self):
        self.tablica = []

        for i in range(10):
            wartosc = int(input(f"Podaj wartość {i + 1}: "))
            self.tablica.append(wartosc)

    def __znajdz_indeks_najwyzszej_wartosci(self, start):
        indeks_max = start

        for i in range(start + 1, len(self.tablica)):
            if self.tablica[i] > self.tablica[indeks_max]:
                indeks_max = i

        return indeks_max

    def sortowanie_przez_wybieranie(self):
        n = len(self.tablica)

        for i in range(n - 1):
            indeks_max = self.__znajdz_indeks_najwyzszej_wartosci(i)

            pomocnicza = self.tablica[i]
            self.tablica[i] = self.tablica[indeks_max]
            self.tablica[indeks_max] = pomocnicza

    def wyswietl_tablice(self):
        print(*self.tablica, sep=", ")


mojaTablica = Narzedzia()

print("\nTablica przed sortowaniem:")
mojaTablica.wyswietl_tablice()

mojaTablica.sortowanie_przez_wybieranie()

print("\nTablica po sortowaniu malejąco:")
mojaTablica.wyswietl_tablice()