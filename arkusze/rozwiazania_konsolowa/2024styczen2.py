class StringNarzedzia:
    @staticmethod
    def licz_samogloski(tekst):
        if not tekst:
            return 0
        else:
            licznik = 0
            for litera in tekst:
                if litera in 'aąeęiouóyAĄEĘIOUÓY':
                    licznik += 1
            return licznik

    @staticmethod
    def usun_powtorzenia(tekst):
        if not tekst:
            return ''

        czysty_tekst = tekst[0]

        for i in range(1, len(tekst)):
            if tekst[i] != tekst[i - 1]:
                czysty_tekst += tekst[i]
        return czysty_tekst


tekst_uzytkownika = input("Wpisz tekst: ")
print(f"Liczba samogłosek w tekście: {StringNarzedzia.licz_samogloski(tekst_uzytkownika)}")
print(f"Tekst po usunięciu sąsiednich powtórzeń: {StringNarzedzia.usun_powtorzenia(tekst_uzytkownika)}")