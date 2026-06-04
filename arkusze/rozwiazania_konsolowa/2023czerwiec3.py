class Film:
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0

    def set_tytul(self, nowy_tytul):
        self._tytul = nowy_tytul

    def get_tytul(self):
        return self._tytul

    def get_liczba_wypozyczen(self):
        return self._liczba_wypozyczen

    def inkrementuj(self):
        self._liczba_wypozyczen += 1

mojFilm = Film()
print("Zawartość pól po utworzeniu obiektu:")
print(f"Tytuł: {mojFilm._tytul}")
print(f"Liczba wypożyczeń: {mojFilm._liczba_wypozyczen}\n")

mojFilm.set_tytul("Interstellar")
print(mojFilm.get_tytul())

print(f"\nLiczba wypożyczeń przed inkrementacją: {mojFilm._liczba_wypozyczen}")
mojFilm.inkrementuj()
print(f"Liczba wypożyczeń po inkrementacji: {mojFilm._liczba_wypozyczen}")
