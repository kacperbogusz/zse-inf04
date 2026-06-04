import random
class Kosc:
    liczba_istancji = 0

    nazwy_plikow = [
        "kosc0.png",
        "kosc1.png",
        "kosc2.png",
        "kosc3.png",
        "kosc4.png",
        "kosc5.png",
        "kosc6.png",
    ]

    liczby_tekstem = [
        "zero",
        "jeden",
        "dwa",
        "trzy",
        "cztery",
        "pięć",
        "sześć",
    ]

    def __init__(self, liczba_oczek=None):
        self.czy_dostepna = True
        Kosc.liczba_istancji += 1

        if liczba_oczek is not None:
            if 1 <= liczba_oczek <= 6:
                self.liczba_oczek = liczba_oczek
                self.id_pliku = liczba_oczek
            else:
                self.liczba_oczek = 0
                self.id_pliku = 0
        else:
            losowa_liczba = random.randint(1, 6)
            self.liczba_oczek = losowa_liczba
            self.id_pliku = losowa_liczba

    def rzut_koscia(self):
        if self.czy_dostepna:
            wyrzucona = random.randint(1, 6)
            self.liczba_oczek = wyrzucona
            self.id_pliku = wyrzucona

    def blokuj_kosc(self):
        self.czy_dostepna = False

    def postac_tekstowa(self):
        return Kosc.liczby_tekstem[self.liczba_oczek]

# Sprawdzanie działania klasy
print("Pierwsza kość")
wartosc_rzutu = int(input("Podaj wartość wyrzuconej ilości oczek dla pierwszej kości: "))
pierwsza_kosc = Kosc(wartosc_rzutu)
print(pierwsza_kosc.liczba_istancji)
print(pierwsza_kosc.liczba_oczek)
print(pierwsza_kosc.postac_tekstowa())

print("\nDruga kość")
druga_kosc = Kosc()
print(druga_kosc.liczba_istancji)
print(druga_kosc.liczba_oczek)
print(druga_kosc.postac_tekstowa())