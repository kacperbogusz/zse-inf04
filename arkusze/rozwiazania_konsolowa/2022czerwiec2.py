class Osoba:
    liczba_instancji = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    def kopiuj(self, inna_osoba):
        self.__id = inna_osoba.__id
        self.__imie = inna_osoba.__imie

    def przedstaw_sie(self, inne_imie):
        if self.__imie == "":
            print("Brak danych")
        else:
            print(f"Cześć {inne_imie}, mam na imię {self.__imie}")


# Program główny

osoba1 = Osoba()
osoba2 = Osoba(1, "Anna")

osoba3 = Osoba()
osoba3.kopiuj(osoba2)

print("Test osoby 1:")
osoba1.przedstaw_sie("Jan")

print("\nTest osoby 2:")
osoba2.przedstaw_sie("Jan")

print("\nTest osoby 3 po kopiowaniu z osoby 2:")
osoba3.przedstaw_sie("Jan")

print(f"\nLiczba instancji klasy Osoba: {Osoba.liczba_instancji}")