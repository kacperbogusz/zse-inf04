class Notatka:
    __liczba_notatek = 0

    def __init__(self, tytul, tresc):
        Notatka.__liczba_notatek += 1
        self.__id = Notatka.__liczba_notatek
        self._tytul = tytul
        self._tresc = tresc

    def wyswietl_notatke(self):
        print(f"Tytuł: {self._tytul}")
        print(f"Treść: {self._tresc}")

    def diagnoza(self):
        print(f"{self.__id};{self._tytul};{self._tresc}")

pierwszaNotatka = Notatka("Przepis", "Mąka, drożdze, woda")
drugaNotatka = Notatka("Moje hasło", "!Q@W#E$R%T^Y")

print("Test metod pierwszej notatki:")
pierwszaNotatka.wyswietl_notatke()
pierwszaNotatka.diagnoza()

print("\nTest metod drugiej notatki:")
drugaNotatka.wyswietl_notatke()
drugaNotatka.diagnoza()