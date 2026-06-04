class Urzadzenie:
    def wyswietl_komunikat(self, tresc):
        print(tresc)

class Pralka(Urzadzenie):
    def __init__(self):
        self.__numer_programu = 0

    def ustaw_numer_programu(self, numer_programu):
        if 1 <= numer_programu <= 12:
            self.__numer_programu = numer_programu
            print("Program został ustawiony")
        else:
            self.__numer_programu = 0
            print("Podano niepoprawny numer programu")
        return self.__numer_programu

class Odkurzacz(Urzadzenie):
    def __init__(self):
        self.__stan = False

    def on(self):
        if not self.__stan:
            self.__stan = True
            self.wyswietl_komunikat("Odkurzacz włączono")

    def off(self):
        if self.__stan:
            self.__stan = False
            self.wyswietl_komunikat("Odkurzacz wyłączono")

moja_pralka = Pralka()
moj_odkurzacz = Odkurzacz()

input1 = int(input("Podaj numer prania:\n"))
moja_pralka.ustaw_numer_programu(input1)

input2 = int(input("Podaj numer prania:\n"))
moja_pralka.ustaw_numer_programu(input2)

moj_odkurzacz.on()
moj_odkurzacz.on()
moj_odkurzacz.on()
moj_odkurzacz.wyswietl_komunikat("Odkuracz wyładował się")
moj_odkurzacz.off()
